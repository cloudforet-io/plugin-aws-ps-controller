# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/cost_saving/v1/cost_saving.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/cost_saving/v1/cost_saving.proto',
  package='spaceone.api.cost_saving.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-spaceone/api/cost_saving/v1/cost_saving.proto\x12\x1bspaceone.api.cost_saving.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xfa\x01\n\x17\x43reateCostSavingRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x11\n\tsaving_by\x18\x03 \x01(\t\x12\x31\n\x05state\x18\x04 \x01(\x0e\x32\".spaceone.api.cost_saving.v1.State\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x10\n\x08provider\x18\x07 \x01(\t\x12)\n\x08resource\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\"\xcf\x01\n\x17UpdateCostSavingRequest\x12\x16\n\x0e\x63ost_saving_id\x18\x01 \x01(\t\x12\x11\n\tsaving_by\x18\x02 \x01(\t\x12\x31\n\x05state\x18\x03 \x01(\x0e\x32\".spaceone.api.cost_saving.v1.State\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12/\n\x0esaving_details\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x16 \x01(\t\">\n\x11\x43ostSavingRequest\x12\x16\n\x0e\x63ost_saving_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"O\n\x14GetCostSavingRequest\x12\x16\n\x0e\x63ost_saving_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xc2\x01\n\x0f\x43ostSavingQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x16\n\x0e\x63ost_saving_id\x18\x02 \x01(\t\x12\x31\n\x05state\x18\x03 \x01(\x0e\x32\".spaceone.api.cost_saving.v1.State\x12\x11\n\tsaving_by\x18\x05 \x01(\t\x12\x12\n\nproject_id\x18\x06 \x01(\t\x12\x11\n\tdomain_id\x18\x07 \x01(\t\"^\n\x13\x43ostSavingStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\x85\x03\n\x0e\x43ostSavingInfo\x12\x16\n\x0e\x63ost_saving_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x11\n\tsaving_by\x18\x04 \x01(\t\x12\x31\n\x05state\x18\x05 \x01(\x0e\x32\".spaceone.api.cost_saving.v1.State\x12\x10\n\x08provider\x18\x0b \x01(\t\x12\x0e\n\x06region\x18\x0c \x01(\t\x12\x15\n\rresource_type\x18\r \x01(\t\x12%\n\x04\x64\x61ta\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12.\n\ncreated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpired_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"d\n\x0f\x43ostSavingsInfo\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.spaceone.api.cost_saving.v1.CostSavingInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05*+\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0b\n\x07STOPPED\x10\x02\x32\x9a\x07\n\nCostSaving\x12\x90\x01\n\x06\x63reate\x12\x34.spaceone.api.cost_saving.v1.CreateCostSavingRequest\x1a+.spaceone.api.cost_saving.v1.CostSavingInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/cost-saving/v1/cost-saving\x12\xa1\x01\n\x06update\x12\x34.spaceone.api.cost_saving.v1.UpdateCostSavingRequest\x1a+.spaceone.api.cost_saving.v1.CostSavingInfo\"4\x82\xd3\xe4\x93\x02.\x1a,/cost-saving/v1/cost-saving/{cost_saving_id}\x12\x86\x01\n\x06\x64\x65lete\x12..spaceone.api.cost_saving.v1.CostSavingRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.*,/cost-saving/v1/cost-saving/{cost_saving_id}\x12\x9b\x01\n\x03get\x12\x31.spaceone.api.cost_saving.v1.GetCostSavingRequest\x1a+.spaceone.api.cost_saving.v1.CostSavingInfo\"4\x82\xd3\xe4\x93\x02.\x12,/cost-saving/v1/cost-saving/{cost_saving_id}\x12\xaf\x01\n\x04list\x12,.spaceone.api.cost_saving.v1.CostSavingQuery\x1a,.spaceone.api.cost_saving.v1.CostSavingsInfo\"K\x82\xd3\xe4\x93\x02\x45\x12\x1c/cost-saving/v1/cost-savingsZ%\"#/cost-saving/v1/cost-savings/search\x12|\n\x04stat\x12\x30.spaceone.api.cost_saving.v1.CostSavingStatQuery\x1a\x17.google.protobuf.Struct\")\x82\xd3\xe4\x93\x02#\"!/cost-saving/v1/cost-savings/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,])

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='spaceone.api.cost_saving.v1.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1629,
  serialized_end=1672,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
NONE = 0
RUNNING = 1
STOPPED = 2



_CREATECOSTSAVINGREQUEST = _descriptor.Descriptor(
  name='CreateCostSavingRequest',
  full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.project_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saving_by', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.saving_by', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.tags', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.region', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.provider', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='spaceone.api.cost_saving.v1.CreateCostSavingRequest.resource', index=7,
      number=11, type=11, cpp_type=10, label=1,
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
  serialized_start=235,
  serialized_end=485,
)


_UPDATECOSTSAVINGREQUEST = _descriptor.Descriptor(
  name='UpdateCostSavingRequest',
  full_name='spaceone.api.cost_saving.v1.UpdateCostSavingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost_saving_id', full_name='spaceone.api.cost_saving.v1.UpdateCostSavingRequest.cost_saving_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saving_by', full_name='spaceone.api.cost_saving.v1.UpdateCostSavingRequest.saving_by', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.cost_saving.v1.UpdateCostSavingRequest.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.cost_saving.v1.UpdateCostSavingRequest.project_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saving_details', full_name='spaceone.api.cost_saving.v1.UpdateCostSavingRequest.saving_details', index=4,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.UpdateCostSavingRequest.domain_id', index=5,
      number=22, type=9, cpp_type=9, label=1,
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
  serialized_start=488,
  serialized_end=695,
)


_COSTSAVINGREQUEST = _descriptor.Descriptor(
  name='CostSavingRequest',
  full_name='spaceone.api.cost_saving.v1.CostSavingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost_saving_id', full_name='spaceone.api.cost_saving.v1.CostSavingRequest.cost_saving_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.CostSavingRequest.domain_id', index=1,
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
  serialized_start=697,
  serialized_end=759,
)


_GETCOSTSAVINGREQUEST = _descriptor.Descriptor(
  name='GetCostSavingRequest',
  full_name='spaceone.api.cost_saving.v1.GetCostSavingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost_saving_id', full_name='spaceone.api.cost_saving.v1.GetCostSavingRequest.cost_saving_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.GetCostSavingRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only', full_name='spaceone.api.cost_saving.v1.GetCostSavingRequest.only', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=761,
  serialized_end=840,
)


_COSTSAVINGQUERY = _descriptor.Descriptor(
  name='CostSavingQuery',
  full_name='spaceone.api.cost_saving.v1.CostSavingQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.cost_saving.v1.CostSavingQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_saving_id', full_name='spaceone.api.cost_saving.v1.CostSavingQuery.cost_saving_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.cost_saving.v1.CostSavingQuery.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saving_by', full_name='spaceone.api.cost_saving.v1.CostSavingQuery.saving_by', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.cost_saving.v1.CostSavingQuery.project_id', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.CostSavingQuery.domain_id', index=5,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=843,
  serialized_end=1037,
)


_COSTSAVINGSTATQUERY = _descriptor.Descriptor(
  name='CostSavingStatQuery',
  full_name='spaceone.api.cost_saving.v1.CostSavingStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.cost_saving.v1.CostSavingStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.CostSavingStatQuery.domain_id', index=1,
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
  serialized_start=1039,
  serialized_end=1133,
)


_COSTSAVINGINFO = _descriptor.Descriptor(
  name='CostSavingInfo',
  full_name='spaceone.api.cost_saving.v1.CostSavingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost_saving_id', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.cost_saving_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.project_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saving_by', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.saving_by', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.state', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.provider', index=5,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.region', index=6,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.resource_type', index=7,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.data', index=8,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.created_at', index=9,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.updated_at', index=10,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expired_at', full_name='spaceone.api.cost_saving.v1.CostSavingInfo.expired_at', index=11,
      number=23, type=11, cpp_type=10, label=1,
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
  serialized_start=1136,
  serialized_end=1525,
)


_COSTSAVINGSINFO = _descriptor.Descriptor(
  name='CostSavingsInfo',
  full_name='spaceone.api.cost_saving.v1.CostSavingsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.cost_saving.v1.CostSavingsInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.cost_saving.v1.CostSavingsInfo.total_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1527,
  serialized_end=1627,
)

_CREATECOSTSAVINGREQUEST.fields_by_name['state'].enum_type = _STATE
_CREATECOSTSAVINGREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CREATECOSTSAVINGREQUEST.fields_by_name['resource'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATECOSTSAVINGREQUEST.fields_by_name['state'].enum_type = _STATE
_UPDATECOSTSAVINGREQUEST.fields_by_name['saving_details'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_COSTSAVINGQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_COSTSAVINGQUERY.fields_by_name['state'].enum_type = _STATE
_COSTSAVINGSTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
_COSTSAVINGINFO.fields_by_name['state'].enum_type = _STATE
_COSTSAVINGINFO.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_COSTSAVINGINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_COSTSAVINGINFO.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_COSTSAVINGINFO.fields_by_name['expired_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_COSTSAVINGSINFO.fields_by_name['results'].message_type = _COSTSAVINGINFO
DESCRIPTOR.message_types_by_name['CreateCostSavingRequest'] = _CREATECOSTSAVINGREQUEST
DESCRIPTOR.message_types_by_name['UpdateCostSavingRequest'] = _UPDATECOSTSAVINGREQUEST
DESCRIPTOR.message_types_by_name['CostSavingRequest'] = _COSTSAVINGREQUEST
DESCRIPTOR.message_types_by_name['GetCostSavingRequest'] = _GETCOSTSAVINGREQUEST
DESCRIPTOR.message_types_by_name['CostSavingQuery'] = _COSTSAVINGQUERY
DESCRIPTOR.message_types_by_name['CostSavingStatQuery'] = _COSTSAVINGSTATQUERY
DESCRIPTOR.message_types_by_name['CostSavingInfo'] = _COSTSAVINGINFO
DESCRIPTOR.message_types_by_name['CostSavingsInfo'] = _COSTSAVINGSINFO
DESCRIPTOR.enum_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateCostSavingRequest = _reflection.GeneratedProtocolMessageType('CreateCostSavingRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOSTSAVINGREQUEST,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CreateCostSavingRequest)
  })
_sym_db.RegisterMessage(CreateCostSavingRequest)

UpdateCostSavingRequest = _reflection.GeneratedProtocolMessageType('UpdateCostSavingRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOSTSAVINGREQUEST,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.UpdateCostSavingRequest)
  })
_sym_db.RegisterMessage(UpdateCostSavingRequest)

CostSavingRequest = _reflection.GeneratedProtocolMessageType('CostSavingRequest', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGREQUEST,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingRequest)
  })
_sym_db.RegisterMessage(CostSavingRequest)

GetCostSavingRequest = _reflection.GeneratedProtocolMessageType('GetCostSavingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOSTSAVINGREQUEST,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.GetCostSavingRequest)
  })
_sym_db.RegisterMessage(GetCostSavingRequest)

CostSavingQuery = _reflection.GeneratedProtocolMessageType('CostSavingQuery', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGQUERY,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingQuery)
  })
_sym_db.RegisterMessage(CostSavingQuery)

CostSavingStatQuery = _reflection.GeneratedProtocolMessageType('CostSavingStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGSTATQUERY,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingStatQuery)
  })
_sym_db.RegisterMessage(CostSavingStatQuery)

CostSavingInfo = _reflection.GeneratedProtocolMessageType('CostSavingInfo', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGINFO,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingInfo)
  })
_sym_db.RegisterMessage(CostSavingInfo)

CostSavingsInfo = _reflection.GeneratedProtocolMessageType('CostSavingsInfo', (_message.Message,), {
  'DESCRIPTOR' : _COSTSAVINGSINFO,
  '__module__' : 'spaceone.api.cost_saving.v1.cost_saving_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.CostSavingsInfo)
  })
_sym_db.RegisterMessage(CostSavingsInfo)



_COSTSAVING = _descriptor.ServiceDescriptor(
  name='CostSaving',
  full_name='spaceone.api.cost_saving.v1.CostSaving',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1675,
  serialized_end=2597,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.cost_saving.v1.CostSaving.create',
    index=0,
    containing_service=None,
    input_type=_CREATECOSTSAVINGREQUEST,
    output_type=_COSTSAVINGINFO,
    serialized_options=b'\202\323\344\223\002\035\"\033/cost-saving/v1/cost-saving',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.cost_saving.v1.CostSaving.update',
    index=1,
    containing_service=None,
    input_type=_UPDATECOSTSAVINGREQUEST,
    output_type=_COSTSAVINGINFO,
    serialized_options=b'\202\323\344\223\002.\032,/cost-saving/v1/cost-saving/{cost_saving_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.cost_saving.v1.CostSaving.delete',
    index=2,
    containing_service=None,
    input_type=_COSTSAVINGREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002.*,/cost-saving/v1/cost-saving/{cost_saving_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.cost_saving.v1.CostSaving.get',
    index=3,
    containing_service=None,
    input_type=_GETCOSTSAVINGREQUEST,
    output_type=_COSTSAVINGINFO,
    serialized_options=b'\202\323\344\223\002.\022,/cost-saving/v1/cost-saving/{cost_saving_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.cost_saving.v1.CostSaving.list',
    index=4,
    containing_service=None,
    input_type=_COSTSAVINGQUERY,
    output_type=_COSTSAVINGSINFO,
    serialized_options=b'\202\323\344\223\002E\022\034/cost-saving/v1/cost-savingsZ%\"#/cost-saving/v1/cost-savings/search',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.cost_saving.v1.CostSaving.stat',
    index=5,
    containing_service=None,
    input_type=_COSTSAVINGSTATQUERY,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002#\"!/cost-saving/v1/cost-savings/stat',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COSTSAVING)

DESCRIPTOR.services_by_name['CostSaving'] = _COSTSAVING

# @@protoc_insertion_point(module_scope)
