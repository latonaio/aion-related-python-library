# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

from aion.logger import initialize_logger, lprint_exception, lprint
from aion.kanban import KanbanConnection, KanbanConnectionAsync, KanbanServerNotFoundError
from aion.proto import status_pb2 as message
from logging import DEBUG
import os
from retry import retry

NORMAL_CONNECTION_MODE = "normal"
DIRECT_CONNECTION_MODE = "direct"

WITH_KANBAN = True
WITHOUT_KANBAN = False


class Options:
    conn: KanbanConnection
    ms_number: int
    docker: bool

    def __init__(self, conn: KanbanConnection, ms_number: int, is_docker: bool):
        self.conn = conn
        self.ms_number = ms_number
        self.docker = is_docker

    def get_conn(self) -> KanbanConnection:
        return self.conn

    def get_number(self) -> int:
        return self.ms_number

    def is_docker(self) -> bool:
        return self.docker


def main_decorator(service_name, init_type, level=DEBUG, async_kanban=False):
    initialize_logger(service_name, level)

    def _main_decorator(func):

        @retry(exceptions=Exception, tries=5, delay=1, backoff=2, max_delay=4)
        def _wrapper(*args, **kwargs):
            conn = None
            try:
                addr = os.environ.get("KANBAN_ADDR")
                n = os.environ.get("MS_NUMBER")
                n = int(n) if n else 1

                connection_mode = os.environ.get("CONNECTION_MODE", NORMAL_CONNECTION_MODE)
                if connection_mode == DIRECT_CONNECTION_MODE:
                    addr = "aion-statuskanban:10000"

                if init_type == WITH_KANBAN:
                    init_msg_type = message.START_SERVICE
                else:
                    init_msg_type = message.START_SERVICE_WITHOUT_KANBAN

                if async_kanban:
                    conn = KanbanConnectionAsync(addr) if addr else KanbanConnectionAsync()
                else:
                    conn = KanbanConnection(addr, init_msg_type, service_name, n) if addr else KanbanConnection("aion-statuskanban:11010", init_msg_type, service_name, n)

                docker = os.environ.get("IS_DOCKER")
                is_docker = True if docker else False

                options = Options(
                    conn=conn,
                    ms_number=n,
                    is_docker=is_docker,
                )
                func(*args, **kwargs, opt=options)
                if conn is not None:
                    conn.close(complete=True)
            except Exception as e:
                lprint_exception(e)
                if conn is not None:
                    conn.close()
                raise
            return
        return _wrapper
    return _main_decorator
