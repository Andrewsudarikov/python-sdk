# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/kafka.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2
from doublecloud.transfer.v1.endpoint import parsers_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_parsers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,doublecloud/transfer/v1/endpoint/kafka.proto\x12 doublecloud.transfer.v1.endpoint\x1a-doublecloud/transfer/v1/endpoint/common.proto\x1a.doublecloud/transfer/v1/endpoint/parsers.proto\"\x9a\x01\n\x16KafkaConnectionOptions\x12\x1f\n\ncluster_id\x18\x01 \x01(\tH\x00R\tclusterId\x12Q\n\non_premise\x18\x02 \x01(\x0b\x32\x30.doublecloud.transfer.v1.endpoint.OnPremiseKafkaH\x00R\tonPremiseB\x0c\n\nconnection\"w\n\x0eOnPremiseKafka\x12\x1f\n\x0b\x62roker_urls\x18\x01 \x03(\tR\nbrokerUrls\x12\x44\n\x08tls_mode\x18\x05 \x01(\x0b\x32).doublecloud.transfer.v1.endpoint.TLSModeR\x07tlsMode\"\xa7\x01\n\tKafkaAuth\x12I\n\x04sasl\x18\x01 \x01(\x0b\x32\x33.doublecloud.transfer.v1.endpoint.KafkaSaslSecurityH\x00R\x04sasl\x12\x43\n\x07no_auth\x18\x02 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.NoAuthH\x00R\x06noAuthB\n\n\x08security\"\xbd\x01\n\x11KafkaSaslSecurity\x12\x12\n\x04user\x18\x01 \x01(\tR\x04user\x12\x44\n\x08password\x18\x04 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.SecretR\x08password\x12N\n\tmechanism\x18\x03 \x01(\x0e\x32\x30.doublecloud.transfer.v1.endpoint.KafkaMechanismR\tmechanism\"\x89\x02\n\x0bKafkaSource\x12X\n\nconnection\x18\x01 \x01(\x0b\x32\x38.doublecloud.transfer.v1.endpoint.KafkaConnectionOptionsR\nconnection\x12?\n\x04\x61uth\x18\x02 \x01(\x0b\x32+.doublecloud.transfer.v1.endpoint.KafkaAuthR\x04\x61uth\x12\x1d\n\ntopic_name\x18\x04 \x01(\tR\ttopicName\x12@\n\x06parser\x18\x07 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.ParserR\x06parser\"\x8b\x02\n\x0bKafkaTarget\x12X\n\nconnection\x18\x01 \x01(\x0b\x32\x38.doublecloud.transfer.v1.endpoint.KafkaConnectionOptionsR\nconnection\x12?\n\x04\x61uth\x18\x02 \x01(\x0b\x32+.doublecloud.transfer.v1.endpoint.KafkaAuthR\x04\x61uth\x12\x61\n\x0etopic_settings\x18\x07 \x01(\x0b\x32:.doublecloud.transfer.v1.endpoint.KafkaTargetTopicSettingsR\rtopicSettings\"\x9d\x01\n\x18KafkaTargetTopicSettings\x12J\n\x05topic\x18\x01 \x01(\x0b\x32\x32.doublecloud.transfer.v1.endpoint.KafkaTargetTopicH\x00R\x05topic\x12#\n\x0ctopic_prefix\x18\x02 \x01(\tH\x00R\x0btopicPrefixB\x10\n\x0etopic_settings\"U\n\x10KafkaTargetTopic\x12\x1d\n\ntopic_name\x18\x01 \x01(\tR\ttopicName\x12\"\n\rsave_tx_order\x18\x02 \x01(\x08R\x0bsaveTxOrder*i\n\x0eKafkaMechanism\x12\x1f\n\x1bKAFKA_MECHANISM_UNSPECIFIED\x10\x00\x12\x1a\n\x16KAFKA_MECHANISM_SHA256\x10\x01\x12\x1a\n\x16KAFKA_MECHANISM_SHA512\x10\x02\x42\x46ZDgithub.com/doublecloud/api/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.kafka_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/doublecloud/api/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_KAFKAMECHANISM']._serialized_start=1602
  _globals['_KAFKAMECHANISM']._serialized_end=1707
  _globals['_KAFKACONNECTIONOPTIONS']._serialized_start=178
  _globals['_KAFKACONNECTIONOPTIONS']._serialized_end=332
  _globals['_ONPREMISEKAFKA']._serialized_start=334
  _globals['_ONPREMISEKAFKA']._serialized_end=453
  _globals['_KAFKAAUTH']._serialized_start=456
  _globals['_KAFKAAUTH']._serialized_end=623
  _globals['_KAFKASASLSECURITY']._serialized_start=626
  _globals['_KAFKASASLSECURITY']._serialized_end=815
  _globals['_KAFKASOURCE']._serialized_start=818
  _globals['_KAFKASOURCE']._serialized_end=1083
  _globals['_KAFKATARGET']._serialized_start=1086
  _globals['_KAFKATARGET']._serialized_end=1353
  _globals['_KAFKATARGETTOPICSETTINGS']._serialized_start=1356
  _globals['_KAFKATARGETTOPICSETTINGS']._serialized_end=1513
  _globals['_KAFKATARGETTOPIC']._serialized_start=1515
  _globals['_KAFKATARGETTOPIC']._serialized_end=1600
# @@protoc_insertion_point(module_scope)
