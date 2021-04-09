# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

import grpc
from threading import Thread, Condition
from queue import Queue, Empty
from dateutil import parser
from typing import Iterator
from retry import retry

from google.protobuf.any_pb2 import Any
from google.protobuf.struct_pb2 import Struct
from google.protobuf.json_format import MessageToDict

from aion.logger import lprint
from aion.proto import status_pb2_grpc as rpc
from aion.proto import status_pb2 as message


class Kanban:
    def __init__(self, kanban):
        self.kanban = kanban

    def get_start_at(self):
        if self.kanban.startAt:
            return parser.parse(self.kanban.startAt)
        return None

    def get_finish_at(self):
        if self.kanban.startAt:
            return parser.parse(self.kanban.finishAt)
        return None

    def get_services(self):
        return self.kanban.services

    def get_connection_key(self):
        return self.kanban.connectionKey

    def get_process_number(self):
        return self.kanban.processNumber

    def get_result(self):
        return self.kanban.priorSuccess

    def get_data_path(self):
        return self.kanban.dataPath

    def get_file_list(self):
        return self.kanban.fileList

    def get_metadata(self):
        return MessageToDict(self.kanban.metadata)


class KanbanServerNotFoundError(Exception):
    def __init__(self, addr):
        self.addr = addr

    def __str__(self):
        return f"cant connect to kanban server: {self.addr}"


class KanbanNotFoundError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f"cant get kanban from server"


class _Callback(object):
    def __init__(self):
        self._condition = Condition()
        self._connectivity = None

    def update(self, connectivity):
        with self._condition:
            self._connectivity = connectivity
            self._condition.notify()

    def connectivity(self):
        with self._condition:
            return self._connectivity

    def block_until_connectivities_satisfy(self, predicate):
        with self._condition:
            while True:
                connectivity = self._connectivity
                if predicate(connectivity):
                    return connectivity
                else:
                    self._condition.wait()


class KanbanConnection:

    def __init__(self, addr, init_type, service_name, process_number):
        self.addr = addr
        self.init_type = init_type
        self.service_name = service_name
        self.process_number = process_number
        self.recv_kanban_queue = Queue()
        self.run()

    def run(self):
        try:
            callback = _Callback()
            self.recv_channel = grpc.insecure_channel(self.addr, options=[('grpc.keepalive_time_ms', 20000), ('grpc.keepalive_timeout_ms', 60000), ('grpc.min_time_between_pings_ms', 120000), ('grpc.max_pings_without_data', 0)])
            self.recv_channel.subscribe(callback.update, try_to_connect=True)
            self.connectivity = callback.block_until_connectivities_satisfy(
                lambda c:
                c == grpc.ChannelConnectivity.READY or
                c == grpc.ChannelConnectivity.TRANSIENT_FAILURE
            )
            self.recv_conn = rpc.KanbanStub(self.recv_channel)
            self.responses = self.recv_conn.ReceiveKanban(message.InitializeService(
                initType=self.init_type,
                microserviceName=self.service_name,
                processNumber=self.process_number
            ))

            self.send_channel = grpc.insecure_channel(self.addr, options=[('grpc.keepalive_time_ms', 20000), ('grpc.keepalive_timeout_ms', 60000), ('grpc.min_time_between_pings_ms', 120000), ('grpc.max_pings_without_data', 0)])
            self.send_conn = rpc.KanbanStub(self.recv_channel)

            self.check_connectivity()
            self.is_thread_stop = False
            self.response_thread = Thread(target=self._receive_function, args=())
            self.response_thread.start()
            lprint("start watch kanban")
        except Exception as e:
            raise e

    @retry(exceptions=Exception, tries=5, delay=1, backoff=2, max_delay=4)
    def reconnect(self):
        try:
            lprint("[gRPC] reconnect connection")
            self.run()
        except Exception as e:
            raise e

    def check_connectivity(self):
        lprint(self.connectivity)
        if grpc.ChannelConnectivity.READY != self.connectivity:
            raise KanbanServerNotFoundError(self.addr)

    def close(self, complete=False):
        self.is_thread_stop = True
        self.recv_kanban_queue.put(None)
        connection_key = ''
        if complete:
            connection_key = 'service-broker'
        self.output_kanban(
                process_number = self.process_number,
                connection_key = connection_key,
                result = complete,
                metadata = {
                    "type": "terminate",
                    "name": self.service_name,
                    "number": self.process_number
                }
        )
        if self.response_thread is not None:
            self.response_thread.join()
        lprint("[gRPC] stop microservice")

    def _receive_function(self):
        try:
            for res in self.responses:
                lprint("[gRPC] get cache kanban")
                self.recv_kanban_queue.put(res.message)
        except Exception as e:
            self.response.cancel()
            self.recv_channel.close()
            self.send_channel.close()
            lprint(f'[gRPC] exception caused: {e}')
            if self.is_thread_stop:
                lprint("[gRPC] closed connection is successful")
            else:
                self.reconnect()

    def get_one_kanban(self, service_name, number) -> Kanban:
        try:
            k = self.recv_kanban_queue.get()
            if k is None:
                raise KanbanNotFoundError
        except Empty:
            lprint("[gRPC] cant connect to status kanban server, exit service")

        return Kanban(k)

    def get_kanban_itr(self, service_name: str, number: int) -> Iterator[Kanban]:
        try:
            while True:
                k = self.recv_kanban_queue.get()
                if k is None:
                    break
                yield Kanban(k)
        except Empty:
            lprint("[gRPC] kanban queue is empty")

    def output_kanban(
            self, result=True, connection_key="default", output_data_path="",
            process_number=1, file_list=None, metadata=None, device_name="") -> None:
        m = message.StatusKanban()

        if metadata is None:
            metadata = {}

        if not file_list:
            file_list = []
        elif not isinstance(file_list, list):
            file_list = [file_list]

        s = Struct()
        s.update(metadata)

        m.priorSuccess = result
        m.dataPath = output_data_path
        m.connectionKey = connection_key
        m.processNumber = int(process_number)
        m.fileList.extend(file_list)
        m.metadata.CopyFrom(s)
        m.nextDeviceName = device_name

        self.send_conn.SendKanban(message.Request(
            microserviceName=self.srevice_name,
            message=m
        ))

