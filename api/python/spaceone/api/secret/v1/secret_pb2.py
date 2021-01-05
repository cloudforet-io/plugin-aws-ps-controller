# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/secret/v1/secret.proto

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
  name='spaceone/api/secret/v1/secret.proto',
  package='spaceone.api.secret.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#spaceone/api/secret/v1/secret.proto\x12\x16spaceone.api.secret.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xfd\x01\n\x13\x43reateSecretRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x37\n\x0bsecret_type\x18\x03 \x01(\x0e\x32\".spaceone.api.secret.v1.SecretType\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06schema\x18\x05 \x01(\t\x12\x1a\n\x12service_account_id\x18\x06 \x01(\t\x12\x12\n\nproject_id\x18\x07 \x01(\t\x12\x11\n\tdomain_id\x18\x08 \x01(\t\"\x9d\x01\n\x13UpdateSecretRequest\x12\x11\n\tsecret_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\x12\x17\n\x0frelease_project\x18\x06 \x01(\x08\"5\n\rSecretRequest\x12\x11\n\tsecret_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"F\n\x10GetSecretRequest\x12\x11\n\tsecret_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\x9b\x02\n\x0bSecretQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x11\n\tsecret_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x37\n\x0bsecret_type\x18\x04 \x01(\x0e\x32\".spaceone.api.secret.v1.SecretType\x12\x17\n\x0fsecret_group_id\x18\x05 \x01(\t\x12\x0e\n\x06schema\x18\x06 \x01(\t\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x1a\n\x12service_account_id\x18\x08 \x01(\t\x12\x1c\n\x14include_secret_group\x18\t \x01(\x08\x12\x11\n\tdomain_id\x18\n \x01(\t\"7\n\x0eSecretDataInfo\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xd5\x02\n\nSecretInfo\x12\x11\n\tsecret_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x37\n\x0bsecret_type\x18\x03 \x01(\x0e\x32\".spaceone.api.secret.v1.SecretType\x12\x31\n\rsecret_groups\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06schema\x18\x06 \x01(\t\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x1a\n\x12service_account_id\x18\x08 \x01(\t\x12\x12\n\nproject_id\x18\t \x01(\t\x12\x11\n\tdomain_id\x18\n \x01(\t\x12.\n\ncreated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"W\n\x0bSecretsInfo\x12\x33\n\x07results\x18\x01 \x03(\x0b\x32\".spaceone.api.secret.v1.SecretInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"Z\n\x0fSecretStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t*\'\n\nSecretType\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0b\x43REDENTIALS\x10\x01\x32\xf1\x06\n\x06Secret\x12u\n\x06\x63reate\x12+.spaceone.api.secret.v1.CreateSecretRequest\x1a\".spaceone.api.secret.v1.SecretInfo\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x12/secret/v1/secrets\x12\x80\x01\n\x06update\x12+.spaceone.api.secret.v1.UpdateSecretRequest\x1a\".spaceone.api.secret.v1.SecretInfo\"%\x82\xd3\xe4\x93\x02\x1f\x1a\x1d/secret/v1/secret/{secret_id}\x12n\n\x06\x64\x65lete\x12%.spaceone.api.secret.v1.SecretRequest\x1a\x16.google.protobuf.Empty\"%\x82\xd3\xe4\x93\x02\x1f*\x1d/secret/v1/secret/{secret_id}\x12\x89\x01\n\x08get_data\x12%.spaceone.api.secret.v1.SecretRequest\x1a&.spaceone.api.secret.v1.SecretDataInfo\".\x82\xd3\xe4\x93\x02(\x12&/secret/v1/secret/{secret_id}/get-data\x12z\n\x03get\x12(.spaceone.api.secret.v1.GetSecretRequest\x1a\".spaceone.api.secret.v1.SecretInfo\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/secret/v1/secret/{secret_id}\x12\x89\x01\n\x04list\x12#.spaceone.api.secret.v1.SecretQuery\x1a#.spaceone.api.secret.v1.SecretsInfo\"7\x82\xd3\xe4\x93\x02\x31\x12\x12/secret/v1/secretsZ\x1b\"\x19/secret/v1/secrets/search\x12i\n\x04stat\x12\'.spaceone.api.secret.v1.SecretStatQuery\x1a\x17.google.protobuf.Struct\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/secret/v1/secrets/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,])

_SECRETTYPE = _descriptor.EnumDescriptor(
  name='SecretType',
  full_name='spaceone.api.secret.v1.SecretType',
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
      name='CREDENTIALS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1630,
  serialized_end=1669,
)
_sym_db.RegisterEnumDescriptor(_SECRETTYPE)

SecretType = enum_type_wrapper.EnumTypeWrapper(_SECRETTYPE)
NONE = 0
CREDENTIALS = 1



_CREATESECRETREQUEST = _descriptor.Descriptor(
  name='CreateSecretRequest',
  full_name='spaceone.api.secret.v1.CreateSecretRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.CreateSecretRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='spaceone.api.secret.v1.CreateSecretRequest.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_type', full_name='spaceone.api.secret.v1.CreateSecretRequest.secret_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.secret.v1.CreateSecretRequest.tags', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='spaceone.api.secret.v1.CreateSecretRequest.schema', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='spaceone.api.secret.v1.CreateSecretRequest.service_account_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.secret.v1.CreateSecretRequest.project_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.CreateSecretRequest.domain_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=220,
  serialized_end=473,
)


_UPDATESECRETREQUEST = _descriptor.Descriptor(
  name='UpdateSecretRequest',
  full_name='spaceone.api.secret.v1.UpdateSecretRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.secret.v1.UpdateSecretRequest.secret_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.UpdateSecretRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.secret.v1.UpdateSecretRequest.tags', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.secret.v1.UpdateSecretRequest.project_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.UpdateSecretRequest.domain_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='release_project', full_name='spaceone.api.secret.v1.UpdateSecretRequest.release_project', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=476,
  serialized_end=633,
)


_SECRETREQUEST = _descriptor.Descriptor(
  name='SecretRequest',
  full_name='spaceone.api.secret.v1.SecretRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.secret.v1.SecretRequest.secret_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretRequest.domain_id', index=1,
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
  serialized_start=635,
  serialized_end=688,
)


_GETSECRETREQUEST = _descriptor.Descriptor(
  name='GetSecretRequest',
  full_name='spaceone.api.secret.v1.GetSecretRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.secret.v1.GetSecretRequest.secret_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.GetSecretRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only', full_name='spaceone.api.secret.v1.GetSecretRequest.only', index=2,
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
  serialized_start=690,
  serialized_end=760,
)


_SECRETQUERY = _descriptor.Descriptor(
  name='SecretQuery',
  full_name='spaceone.api.secret.v1.SecretQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.secret.v1.SecretQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.secret.v1.SecretQuery.secret_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.SecretQuery.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_type', full_name='spaceone.api.secret.v1.SecretQuery.secret_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_group_id', full_name='spaceone.api.secret.v1.SecretQuery.secret_group_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='spaceone.api.secret.v1.SecretQuery.schema', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.secret.v1.SecretQuery.provider', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='spaceone.api.secret.v1.SecretQuery.service_account_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_secret_group', full_name='spaceone.api.secret.v1.SecretQuery.include_secret_group', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretQuery.domain_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=763,
  serialized_end=1046,
)


_SECRETDATAINFO = _descriptor.Descriptor(
  name='SecretDataInfo',
  full_name='spaceone.api.secret.v1.SecretDataInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='spaceone.api.secret.v1.SecretDataInfo.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1048,
  serialized_end=1103,
)


_SECRETINFO = _descriptor.Descriptor(
  name='SecretInfo',
  full_name='spaceone.api.secret.v1.SecretInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.secret.v1.SecretInfo.secret_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.SecretInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_type', full_name='spaceone.api.secret.v1.SecretInfo.secret_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_groups', full_name='spaceone.api.secret.v1.SecretInfo.secret_groups', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.secret.v1.SecretInfo.tags', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='spaceone.api.secret.v1.SecretInfo.schema', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.secret.v1.SecretInfo.provider', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='spaceone.api.secret.v1.SecretInfo.service_account_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.secret.v1.SecretInfo.project_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretInfo.domain_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.secret.v1.SecretInfo.created_at', index=10,
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
  serialized_start=1106,
  serialized_end=1447,
)


_SECRETSINFO = _descriptor.Descriptor(
  name='SecretsInfo',
  full_name='spaceone.api.secret.v1.SecretsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.secret.v1.SecretsInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.secret.v1.SecretsInfo.total_count', index=1,
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
  serialized_start=1449,
  serialized_end=1536,
)


_SECRETSTATQUERY = _descriptor.Descriptor(
  name='SecretStatQuery',
  full_name='spaceone.api.secret.v1.SecretStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.secret.v1.SecretStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretStatQuery.domain_id', index=1,
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
  serialized_start=1538,
  serialized_end=1628,
)

_CREATESECRETREQUEST.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CREATESECRETREQUEST.fields_by_name['secret_type'].enum_type = _SECRETTYPE
_CREATESECRETREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATESECRETREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SECRETQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_SECRETQUERY.fields_by_name['secret_type'].enum_type = _SECRETTYPE
_SECRETDATAINFO.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SECRETINFO.fields_by_name['secret_type'].enum_type = _SECRETTYPE
_SECRETINFO.fields_by_name['secret_groups'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_SECRETINFO.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SECRETINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SECRETSINFO.fields_by_name['results'].message_type = _SECRETINFO
_SECRETSTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
DESCRIPTOR.message_types_by_name['CreateSecretRequest'] = _CREATESECRETREQUEST
DESCRIPTOR.message_types_by_name['UpdateSecretRequest'] = _UPDATESECRETREQUEST
DESCRIPTOR.message_types_by_name['SecretRequest'] = _SECRETREQUEST
DESCRIPTOR.message_types_by_name['GetSecretRequest'] = _GETSECRETREQUEST
DESCRIPTOR.message_types_by_name['SecretQuery'] = _SECRETQUERY
DESCRIPTOR.message_types_by_name['SecretDataInfo'] = _SECRETDATAINFO
DESCRIPTOR.message_types_by_name['SecretInfo'] = _SECRETINFO
DESCRIPTOR.message_types_by_name['SecretsInfo'] = _SECRETSINFO
DESCRIPTOR.message_types_by_name['SecretStatQuery'] = _SECRETSTATQUERY
DESCRIPTOR.enum_types_by_name['SecretType'] = _SECRETTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateSecretRequest = _reflection.GeneratedProtocolMessageType('CreateSecretRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESECRETREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.CreateSecretRequest)
  })
_sym_db.RegisterMessage(CreateSecretRequest)

UpdateSecretRequest = _reflection.GeneratedProtocolMessageType('UpdateSecretRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESECRETREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.UpdateSecretRequest)
  })
_sym_db.RegisterMessage(UpdateSecretRequest)

SecretRequest = _reflection.GeneratedProtocolMessageType('SecretRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretRequest)
  })
_sym_db.RegisterMessage(SecretRequest)

GetSecretRequest = _reflection.GeneratedProtocolMessageType('GetSecretRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSECRETREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.GetSecretRequest)
  })
_sym_db.RegisterMessage(GetSecretRequest)

SecretQuery = _reflection.GeneratedProtocolMessageType('SecretQuery', (_message.Message,), {
  'DESCRIPTOR' : _SECRETQUERY,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretQuery)
  })
_sym_db.RegisterMessage(SecretQuery)

SecretDataInfo = _reflection.GeneratedProtocolMessageType('SecretDataInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETDATAINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretDataInfo)
  })
_sym_db.RegisterMessage(SecretDataInfo)

SecretInfo = _reflection.GeneratedProtocolMessageType('SecretInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretInfo)
  })
_sym_db.RegisterMessage(SecretInfo)

SecretsInfo = _reflection.GeneratedProtocolMessageType('SecretsInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETSINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretsInfo)
  })
_sym_db.RegisterMessage(SecretsInfo)

SecretStatQuery = _reflection.GeneratedProtocolMessageType('SecretStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _SECRETSTATQUERY,
  '__module__' : 'spaceone.api.secret.v1.secret_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretStatQuery)
  })
_sym_db.RegisterMessage(SecretStatQuery)



_SECRET = _descriptor.ServiceDescriptor(
  name='Secret',
  full_name='spaceone.api.secret.v1.Secret',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1672,
  serialized_end=2553,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.secret.v1.Secret.create',
    index=0,
    containing_service=None,
    input_type=_CREATESECRETREQUEST,
    output_type=_SECRETINFO,
    serialized_options=b'\202\323\344\223\002\024\"\022/secret/v1/secrets',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.secret.v1.Secret.update',
    index=1,
    containing_service=None,
    input_type=_UPDATESECRETREQUEST,
    output_type=_SECRETINFO,
    serialized_options=b'\202\323\344\223\002\037\032\035/secret/v1/secret/{secret_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.secret.v1.Secret.delete',
    index=2,
    containing_service=None,
    input_type=_SECRETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\037*\035/secret/v1/secret/{secret_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_data',
    full_name='spaceone.api.secret.v1.Secret.get_data',
    index=3,
    containing_service=None,
    input_type=_SECRETREQUEST,
    output_type=_SECRETDATAINFO,
    serialized_options=b'\202\323\344\223\002(\022&/secret/v1/secret/{secret_id}/get-data',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.secret.v1.Secret.get',
    index=4,
    containing_service=None,
    input_type=_GETSECRETREQUEST,
    output_type=_SECRETINFO,
    serialized_options=b'\202\323\344\223\002\037\022\035/secret/v1/secret/{secret_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.secret.v1.Secret.list',
    index=5,
    containing_service=None,
    input_type=_SECRETQUERY,
    output_type=_SECRETSINFO,
    serialized_options=b'\202\323\344\223\0021\022\022/secret/v1/secretsZ\033\"\031/secret/v1/secrets/search',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.secret.v1.Secret.stat',
    index=6,
    containing_service=None,
    input_type=_SECRETSTATQUERY,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002\031\"\027/secret/v1/secrets/stat',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SECRET)

DESCRIPTOR.services_by_name['Secret'] = _SECRET

# @@protoc_insertion_point(module_scope)
