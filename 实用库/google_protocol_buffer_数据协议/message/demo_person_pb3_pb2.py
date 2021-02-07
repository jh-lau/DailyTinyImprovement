# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo_person_pb3.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo_person_pb3.proto',
  package='infos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x64\x65mo_person_pb3.proto\x12\x05infos\"\x85\x03\n\x06Person\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\"\n\x05score\x18\x04 \x03(\x0b\x32\x13.infos.Person.Score\x12)\n\x06number\x18\x05 \x01(\x0b\x32\x19.infos.Person.PhoneNumber\x12\x30\n\ndict_score\x18\x06 \x03(\x0b\x32\x1c.infos.Person.DictScoreEntry\x1a&\n\x05Score\x12\x0e\n\x06object\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\x1a\x43\n\x0bPhoneNumber\x12\r\n\x05phone\x18\x01 \x01(\x05\x12%\n\x04type\x18\x02 \x01(\x0e\x32\x17.infos.Person.PhoneType\x1a\x45\n\x0e\x44ictScoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.infos.Person.Score:\x02\x38\x01\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04WORK\x10\x01\x12\x08\n\x04HOME\x10\x02\"0\n\x03one\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\x06people\x18\x02 \x01(\x0b\x32\r.infos.Person**\n\x08RaceType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04WORK\x10\x01\x12\x08\n\x04HOME\x10\x02\x62\x06proto3'
)

_RACETYPE = _descriptor.EnumDescriptor(
  name='RaceType',
  full_name='infos.RaceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=474,
  serialized_end=516,
)
_sym_db.RegisterEnumDescriptor(_RACETYPE)

RaceType = enum_type_wrapper.EnumTypeWrapper(_RACETYPE)
MOBILE = 0
WORK = 1
HOME = 2


_PERSON_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='infos.Person.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=379,
  serialized_end=422,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONETYPE)


_PERSON_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='infos.Person.Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='infos.Person.Score.object', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='infos.Person.Score.score', index=1,
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
  serialized_start=199,
  serialized_end=237,
)

_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='infos.Person.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='infos.Person.PhoneNumber.phone', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='infos.Person.PhoneNumber.type', index=1,
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
  serialized_start=239,
  serialized_end=306,
)

_PERSON_DICTSCOREENTRY = _descriptor.Descriptor(
  name='DictScoreEntry',
  full_name='infos.Person.DictScoreEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='infos.Person.DictScoreEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='infos.Person.DictScoreEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=377,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='infos.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='infos.Person.age', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='infos.Person.name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='infos.Person.score', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='infos.Person.number', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dict_score', full_name='infos.Person.dict_score', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_SCORE, _PERSON_PHONENUMBER, _PERSON_DICTSCOREENTRY, ],
  enum_types=[
    _PERSON_PHONETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=422,
)


_ONE = _descriptor.Descriptor(
  name='one',
  full_name='infos.one',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='infos.one.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='people', full_name='infos.one.people', index=1,
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
  serialized_start=424,
  serialized_end=472,
)

_PERSON_SCORE.containing_type = _PERSON
_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONETYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON_DICTSCOREENTRY.fields_by_name['value'].message_type = _PERSON_SCORE
_PERSON_DICTSCOREENTRY.containing_type = _PERSON
_PERSON.fields_by_name['score'].message_type = _PERSON_SCORE
_PERSON.fields_by_name['number'].message_type = _PERSON_PHONENUMBER
_PERSON.fields_by_name['dict_score'].message_type = _PERSON_DICTSCOREENTRY
_PERSON_PHONETYPE.containing_type = _PERSON
_ONE.fields_by_name['people'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['one'] = _ONE
DESCRIPTOR.enum_types_by_name['RaceType'] = _RACETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {

  'Score' : _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_SCORE,
    '__module__' : 'demo_person_pb3_pb2'
    # @@protoc_insertion_point(class_scope:infos.Person.Score)
    })
  ,

  'PhoneNumber' : _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_PHONENUMBER,
    '__module__' : 'demo_person_pb3_pb2'
    # @@protoc_insertion_point(class_scope:infos.Person.PhoneNumber)
    })
  ,

  'DictScoreEntry' : _reflection.GeneratedProtocolMessageType('DictScoreEntry', (_message.Message,), {
    'DESCRIPTOR' : _PERSON_DICTSCOREENTRY,
    '__module__' : 'demo_person_pb3_pb2'
    # @@protoc_insertion_point(class_scope:infos.Person.DictScoreEntry)
    })
  ,
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'demo_person_pb3_pb2'
  # @@protoc_insertion_point(class_scope:infos.Person)
  })
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.Score)
_sym_db.RegisterMessage(Person.PhoneNumber)
_sym_db.RegisterMessage(Person.DictScoreEntry)

one = _reflection.GeneratedProtocolMessageType('one', (_message.Message,), {
  'DESCRIPTOR' : _ONE,
  '__module__' : 'demo_person_pb3_pb2'
  # @@protoc_insertion_point(class_scope:infos.one)
  })
_sym_db.RegisterMessage(one)


_PERSON_DICTSCOREENTRY._options = None
# @@protoc_insertion_point(module_scope)
