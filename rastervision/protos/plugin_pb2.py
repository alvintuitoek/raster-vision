# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/plugin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/plugin.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n rastervision/protos/plugin.proto\x12\trv.protos\";\n\x0cPluginConfig\x12\x13\n\x0bplugin_uris\x18\x01 \x03(\t\x12\x16\n\x0eplugin_modules\x18\x02 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLUGINCONFIG = _descriptor.Descriptor(
  name='PluginConfig',
  full_name='rv.protos.PluginConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_uris', full_name='rv.protos.PluginConfig.plugin_uris', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plugin_modules', full_name='rv.protos.PluginConfig.plugin_modules', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['PluginConfig'] = _PLUGINCONFIG

PluginConfig = _reflection.GeneratedProtocolMessageType('PluginConfig', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINCONFIG,
  __module__ = 'rastervision.protos.plugin_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.PluginConfig)
  ))
_sym_db.RegisterMessage(PluginConfig)


# @@protoc_insertion_point(module_scope)