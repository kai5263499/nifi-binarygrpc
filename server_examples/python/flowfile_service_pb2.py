# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flowfile_service.proto

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
  name='flowfile_service.proto',
  package='org.apache.nifi.processors.grpc',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x66lowfile_service.proto\x12\x1forg.apache.nifi.processors.grpc\"\xb7\x01\n\x0f\x46lowFileRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12T\n\nattributes\x18\x0f \x03(\x0b\x32@.org.apache.nifi.processors.grpc.FlowFileRequest.AttributesEntry\x12\x0f\n\x07\x63ontent\x18\x10 \x01(\x0c\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb9\x02\n\rFlowFileReply\x12\n\n\x02id\x18\x01 \x01(\x03\x12Q\n\x0cresponseCode\x18\x02 \x01(\x0e\x32;.org.apache.nifi.processors.grpc.FlowFileReply.ResponseCode\x12R\n\nattributes\x18\x0f \x03(\x0b\x32>.org.apache.nifi.processors.grpc.FlowFileReply.AttributesEntry\x12\x0f\n\x07\x63ontent\x18\x10 \x01(\x0c\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x0cResponseCode\x12\t\n\x05\x45RROR\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05RETRY\x10\x02\x32}\n\x0f\x46lowFileService\x12j\n\x04Send\x12\x30.org.apache.nifi.processors.grpc.FlowFileRequest\x1a..org.apache.nifi.processors.grpc.FlowFileReply\"\x00\x42\x32\n\x1e\x63om.manwe.binarygrpc.generatedB\x08\x46\x46SProtoP\x01\xa2\x02\x03\x46\x46Sb\x06proto3')
)



_FLOWFILEREPLY_RESPONSECODE = _descriptor.EnumDescriptor(
  name='ResponseCode',
  full_name='org.apache.nifi.processors.grpc.FlowFileReply.ResponseCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETRY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=510,
  serialized_end=559,
)
_sym_db.RegisterEnumDescriptor(_FLOWFILEREPLY_RESPONSECODE)


_FLOWFILEREQUEST_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='org.apache.nifi.processors.grpc.FlowFileRequest.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='org.apache.nifi.processors.grpc.FlowFileRequest.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='org.apache.nifi.processors.grpc.FlowFileRequest.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=243,
)

_FLOWFILEREQUEST = _descriptor.Descriptor(
  name='FlowFileRequest',
  full_name='org.apache.nifi.processors.grpc.FlowFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='org.apache.nifi.processors.grpc.FlowFileRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='org.apache.nifi.processors.grpc.FlowFileRequest.attributes', index=1,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='org.apache.nifi.processors.grpc.FlowFileRequest.content', index=2,
      number=16, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOWFILEREQUEST_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=243,
)


_FLOWFILEREPLY_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='org.apache.nifi.processors.grpc.FlowFileReply.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='org.apache.nifi.processors.grpc.FlowFileReply.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='org.apache.nifi.processors.grpc.FlowFileReply.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=243,
)

_FLOWFILEREPLY = _descriptor.Descriptor(
  name='FlowFileReply',
  full_name='org.apache.nifi.processors.grpc.FlowFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='org.apache.nifi.processors.grpc.FlowFileReply.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responseCode', full_name='org.apache.nifi.processors.grpc.FlowFileReply.responseCode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='org.apache.nifi.processors.grpc.FlowFileReply.attributes', index=2,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='org.apache.nifi.processors.grpc.FlowFileReply.content', index=3,
      number=16, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOWFILEREPLY_ATTRIBUTESENTRY, ],
  enum_types=[
    _FLOWFILEREPLY_RESPONSECODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=559,
)

_FLOWFILEREQUEST_ATTRIBUTESENTRY.containing_type = _FLOWFILEREQUEST
_FLOWFILEREQUEST.fields_by_name['attributes'].message_type = _FLOWFILEREQUEST_ATTRIBUTESENTRY
_FLOWFILEREPLY_ATTRIBUTESENTRY.containing_type = _FLOWFILEREPLY
_FLOWFILEREPLY.fields_by_name['responseCode'].enum_type = _FLOWFILEREPLY_RESPONSECODE
_FLOWFILEREPLY.fields_by_name['attributes'].message_type = _FLOWFILEREPLY_ATTRIBUTESENTRY
_FLOWFILEREPLY_RESPONSECODE.containing_type = _FLOWFILEREPLY
DESCRIPTOR.message_types_by_name['FlowFileRequest'] = _FLOWFILEREQUEST
DESCRIPTOR.message_types_by_name['FlowFileReply'] = _FLOWFILEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowFileRequest = _reflection.GeneratedProtocolMessageType('FlowFileRequest', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _FLOWFILEREQUEST_ATTRIBUTESENTRY,
    __module__ = 'flowfile_service_pb2'
    # @@protoc_insertion_point(class_scope:org.apache.nifi.processors.grpc.FlowFileRequest.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _FLOWFILEREQUEST,
  __module__ = 'flowfile_service_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.nifi.processors.grpc.FlowFileRequest)
  ))
_sym_db.RegisterMessage(FlowFileRequest)
_sym_db.RegisterMessage(FlowFileRequest.AttributesEntry)

FlowFileReply = _reflection.GeneratedProtocolMessageType('FlowFileReply', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _FLOWFILEREPLY_ATTRIBUTESENTRY,
    __module__ = 'flowfile_service_pb2'
    # @@protoc_insertion_point(class_scope:org.apache.nifi.processors.grpc.FlowFileReply.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _FLOWFILEREPLY,
  __module__ = 'flowfile_service_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.nifi.processors.grpc.FlowFileReply)
  ))
_sym_db.RegisterMessage(FlowFileReply)
_sym_db.RegisterMessage(FlowFileReply.AttributesEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.manwe.binarygrpc.generatedB\010FFSProtoP\001\242\002\003FFS'))
_FLOWFILEREQUEST_ATTRIBUTESENTRY.has_options = True
_FLOWFILEREQUEST_ATTRIBUTESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_FLOWFILEREPLY_ATTRIBUTESENTRY.has_options = True
_FLOWFILEREPLY_ATTRIBUTESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_FLOWFILESERVICE = _descriptor.ServiceDescriptor(
  name='FlowFileService',
  full_name='org.apache.nifi.processors.grpc.FlowFileService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=561,
  serialized_end=686,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='org.apache.nifi.processors.grpc.FlowFileService.Send',
    index=0,
    containing_service=None,
    input_type=_FLOWFILEREQUEST,
    output_type=_FLOWFILEREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FLOWFILESERVICE)

DESCRIPTOR.services_by_name['FlowFileService'] = _FLOWFILESERVICE

# @@protoc_insertion_point(module_scope)
