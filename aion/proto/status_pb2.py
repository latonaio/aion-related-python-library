# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/kanbanpb/status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/kanbanpb/status.proto',
  package='kanbanpb',
  syntax='proto3',
  serialized_options=b'Z/bitbucket.org/latonaio/aion-core/proto/kanbanpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bproto/kanbanpb/status.proto\x12\x08kanbanpb\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19google/protobuf/any.proto\"\xdc\x01\n\x0cStatusKanban\x12\x0f\n\x07startAt\x18\x01 \x01(\t\x12\x10\n\x08\x66inishAt\x18\x02 \x01(\t\x12\x16\n\x0enextDeviceName\x18\x03 \x01(\t\x12\x15\n\rconnectionKey\x18\x04 \x01(\t\x12\x15\n\rprocessNumber\x18\x05 \x01(\x05\x12\x14\n\x0cpriorSuccess\x18\x06 \x01(\x08\x12\x10\n\x08\x64\x61taPath\x18\x07 \x01(\t\x12\x10\n\x08\x66ileList\x18\x08 \x03(\t\x12)\n\x08metadata\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\"\x8a\x01\n\nSendKanban\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\x12\n\ndeviceAddr\x18\x02 \x01(\t\x12\x13\n\x0bnextService\x18\x03 \x01(\t\x12\x12\n\nnextNumber\x18\x04 \x01(\x05\x12+\n\x0b\x61\x66terKanban\x18\x05 \x01(\x0b\x32\x16.kanbanpb.StatusKanban\"&\n\x05\x43hunk\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\"_\n\x0bSendContext\x12)\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1b.kanbanpb.UploadRequestCode\x12%\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"O\n\x0cUploadStatus\x12\x0f\n\x07Message\x18\x01 \x01(\t\x12.\n\nstatusCode\x18\x02 \x01(\x0e\x32\x1a.kanbanpb.UploadStatusCode\"p\n\x11InitializeService\x12*\n\x08initType\x18\x01 \x01(\x0e\x32\x18.kanbanpb.InitializeType\x12\x18\n\x10microserviceName\x18\x02 \x01(\t\x12\x15\n\rprocessNumber\x18\x03 \x01(\x05\"L\n\x07Request\x12\x18\n\x10microserviceName\x18\x01 \x01(\t\x12\'\n\x07message\x18\x02 \x01(\x0b\x32\x16.kanbanpb.StatusKanban\"C\n\x08Response\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.kanbanpb.ResponseStatus\x12\r\n\x05\x65rror\x18\x02 \x01(\t*r\n\x11UploadRequestCode\x12\x11\n\rSendingKanban\x10\x00\x12\x14\n\x10SendingFile_CONT\x10\x01\x12\x13\n\x0fSendingFile_EOF\x10\x02\x12\x16\n\x12SendingFile_FAILED\x10\x03\x12\x07\n\x03\x45OS\x10\x04*3\n\x10UploadStatusCode\x12\x0b\n\x07Unknown\x10\x00\x12\n\n\x06\x46\x61iled\x10\x01\x12\x06\n\x02OK\x10\x02*E\n\x0eInitializeType\x12\x11\n\rSTART_SERVICE\x10\x00\x12 \n\x1cSTART_SERVICE_WITHOUT_KANBAN\x10\x01*)\n\x0eResponseStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\x85\x01\n\x06Kanban\x12\x46\n\rReceiveKanban\x12\x1b.kanbanpb.InitializeService\x1a\x16.kanbanpb.StatusKanban0\x01\x12\x33\n\nSendKanban\x12\x11.kanbanpb.Request\x1a\x12.kanbanpb.Response2\x9a\x01\n\x0cSendAnything\x12\x43\n\x11ServiceBrokerConn\x12\x14.kanbanpb.SendKanban\x1a\x14.kanbanpb.SendKanban(\x01\x30\x01\x12\x45\n\x12SendToOtherDevices\x12\x15.kanbanpb.SendContext\x1a\x16.kanbanpb.UploadStatus(\x01\x42\x31Z/bitbucket.org/latonaio/aion-core/proto/kanbanpbb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_UPLOADREQUESTCODE = _descriptor.EnumDescriptor(
  name='UploadRequestCode',
  full_name='kanbanpb.UploadRequestCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SendingKanban', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SendingFile_CONT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SendingFile_EOF', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SendingFile_FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EOS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=941,
  serialized_end=1055,
)
_sym_db.RegisterEnumDescriptor(_UPLOADREQUESTCODE)

UploadRequestCode = enum_type_wrapper.EnumTypeWrapper(_UPLOADREQUESTCODE)
_UPLOADSTATUSCODE = _descriptor.EnumDescriptor(
  name='UploadStatusCode',
  full_name='kanbanpb.UploadStatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1057,
  serialized_end=1108,
)
_sym_db.RegisterEnumDescriptor(_UPLOADSTATUSCODE)

UploadStatusCode = enum_type_wrapper.EnumTypeWrapper(_UPLOADSTATUSCODE)
_INITIALIZETYPE = _descriptor.EnumDescriptor(
  name='InitializeType',
  full_name='kanbanpb.InitializeType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START_SERVICE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='START_SERVICE_WITHOUT_KANBAN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1110,
  serialized_end=1179,
)
_sym_db.RegisterEnumDescriptor(_INITIALIZETYPE)

InitializeType = enum_type_wrapper.EnumTypeWrapper(_INITIALIZETYPE)
_RESPONSESTATUS = _descriptor.EnumDescriptor(
  name='ResponseStatus',
  full_name='kanbanpb.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1181,
  serialized_end=1222,
)
_sym_db.RegisterEnumDescriptor(_RESPONSESTATUS)

ResponseStatus = enum_type_wrapper.EnumTypeWrapper(_RESPONSESTATUS)
SendingKanban = 0
SendingFile_CONT = 1
SendingFile_EOF = 2
SendingFile_FAILED = 3
EOS = 4
Unknown = 0
Failed = 1
OK = 2
START_SERVICE = 0
START_SERVICE_WITHOUT_KANBAN = 1
SUCCESS = 0
FAILED = 1



_STATUSKANBAN = _descriptor.Descriptor(
  name='StatusKanban',
  full_name='kanbanpb.StatusKanban',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='startAt', full_name='kanbanpb.StatusKanban.startAt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finishAt', full_name='kanbanpb.StatusKanban.finishAt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nextDeviceName', full_name='kanbanpb.StatusKanban.nextDeviceName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connectionKey', full_name='kanbanpb.StatusKanban.connectionKey', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processNumber', full_name='kanbanpb.StatusKanban.processNumber', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priorSuccess', full_name='kanbanpb.StatusKanban.priorSuccess', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataPath', full_name='kanbanpb.StatusKanban.dataPath', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileList', full_name='kanbanpb.StatusKanban.fileList', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='kanbanpb.StatusKanban.metadata', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=319,
)


_SENDKANBAN = _descriptor.Descriptor(
  name='SendKanban',
  full_name='kanbanpb.SendKanban',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceName', full_name='kanbanpb.SendKanban.deviceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceAddr', full_name='kanbanpb.SendKanban.deviceAddr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nextService', full_name='kanbanpb.SendKanban.nextService', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nextNumber', full_name='kanbanpb.SendKanban.nextNumber', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='afterKanban', full_name='kanbanpb.SendKanban.afterKanban', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=322,
  serialized_end=460,
)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='kanbanpb.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='kanbanpb.Chunk.context', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='kanbanpb.Chunk.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=462,
  serialized_end=500,
)


_SENDCONTEXT = _descriptor.Descriptor(
  name='SendContext',
  full_name='kanbanpb.SendContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='kanbanpb.SendContext.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='kanbanpb.SendContext.context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=597,
)


_UPLOADSTATUS = _descriptor.Descriptor(
  name='UploadStatus',
  full_name='kanbanpb.UploadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Message', full_name='kanbanpb.UploadStatus.Message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statusCode', full_name='kanbanpb.UploadStatus.statusCode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=678,
)


_INITIALIZESERVICE = _descriptor.Descriptor(
  name='InitializeService',
  full_name='kanbanpb.InitializeService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='initType', full_name='kanbanpb.InitializeService.initType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='microserviceName', full_name='kanbanpb.InitializeService.microserviceName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processNumber', full_name='kanbanpb.InitializeService.processNumber', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=792,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='kanbanpb.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='microserviceName', full_name='kanbanpb.Request.microserviceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='kanbanpb.Request.message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=794,
  serialized_end=870,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='kanbanpb.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='kanbanpb.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='kanbanpb.Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=939,
)

_STATUSKANBAN.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SENDKANBAN.fields_by_name['afterKanban'].message_type = _STATUSKANBAN
_SENDCONTEXT.fields_by_name['code'].enum_type = _UPLOADREQUESTCODE
_SENDCONTEXT.fields_by_name['context'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_UPLOADSTATUS.fields_by_name['statusCode'].enum_type = _UPLOADSTATUSCODE
_INITIALIZESERVICE.fields_by_name['initType'].enum_type = _INITIALIZETYPE
_REQUEST.fields_by_name['message'].message_type = _STATUSKANBAN
_RESPONSE.fields_by_name['status'].enum_type = _RESPONSESTATUS
DESCRIPTOR.message_types_by_name['StatusKanban'] = _STATUSKANBAN
DESCRIPTOR.message_types_by_name['SendKanban'] = _SENDKANBAN
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['SendContext'] = _SENDCONTEXT
DESCRIPTOR.message_types_by_name['UploadStatus'] = _UPLOADSTATUS
DESCRIPTOR.message_types_by_name['InitializeService'] = _INITIALIZESERVICE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['UploadRequestCode'] = _UPLOADREQUESTCODE
DESCRIPTOR.enum_types_by_name['UploadStatusCode'] = _UPLOADSTATUSCODE
DESCRIPTOR.enum_types_by_name['InitializeType'] = _INITIALIZETYPE
DESCRIPTOR.enum_types_by_name['ResponseStatus'] = _RESPONSESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusKanban = _reflection.GeneratedProtocolMessageType('StatusKanban', (_message.Message,), {
  'DESCRIPTOR' : _STATUSKANBAN,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.StatusKanban)
  })
_sym_db.RegisterMessage(StatusKanban)

SendKanban = _reflection.GeneratedProtocolMessageType('SendKanban', (_message.Message,), {
  'DESCRIPTOR' : _SENDKANBAN,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.SendKanban)
  })
_sym_db.RegisterMessage(SendKanban)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.Chunk)
  })
_sym_db.RegisterMessage(Chunk)

SendContext = _reflection.GeneratedProtocolMessageType('SendContext', (_message.Message,), {
  'DESCRIPTOR' : _SENDCONTEXT,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.SendContext)
  })
_sym_db.RegisterMessage(SendContext)

UploadStatus = _reflection.GeneratedProtocolMessageType('UploadStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADSTATUS,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.UploadStatus)
  })
_sym_db.RegisterMessage(UploadStatus)

InitializeService = _reflection.GeneratedProtocolMessageType('InitializeService', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZESERVICE,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.InitializeService)
  })
_sym_db.RegisterMessage(InitializeService)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'proto.kanbanpb.status_pb2'
  # @@protoc_insertion_point(class_scope:kanbanpb.Response)
  })
_sym_db.RegisterMessage(Response)


DESCRIPTOR._options = None

_KANBAN = _descriptor.ServiceDescriptor(
  name='Kanban',
  full_name='kanbanpb.Kanban',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1225,
  serialized_end=1358,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReceiveKanban',
    full_name='kanbanpb.Kanban.ReceiveKanban',
    index=0,
    containing_service=None,
    input_type=_INITIALIZESERVICE,
    output_type=_STATUSKANBAN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendKanban',
    full_name='kanbanpb.Kanban.SendKanban',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KANBAN)

DESCRIPTOR.services_by_name['Kanban'] = _KANBAN


_SENDANYTHING = _descriptor.ServiceDescriptor(
  name='SendAnything',
  full_name='kanbanpb.SendAnything',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1361,
  serialized_end=1515,
  methods=[
  _descriptor.MethodDescriptor(
    name='ServiceBrokerConn',
    full_name='kanbanpb.SendAnything.ServiceBrokerConn',
    index=0,
    containing_service=None,
    input_type=_SENDKANBAN,
    output_type=_SENDKANBAN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendToOtherDevices',
    full_name='kanbanpb.SendAnything.SendToOtherDevices',
    index=1,
    containing_service=None,
    input_type=_SENDCONTEXT,
    output_type=_UPLOADSTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDANYTHING)

DESCRIPTOR.services_by_name['SendAnything'] = _SENDANYTHING

# @@protoc_insertion_point(module_scope)
