# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import mii.legacy.grpc_related.proto.legacymodelresponse_pb2 as legacymodelresponse__pb2


class ModelResponseStub(object):
    """Missing associated documentation comment in .proto file."""
    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Terminate = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/Terminate',
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.
            SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.CreateSession = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/CreateSession',
            request_serializer=legacymodelresponse__pb2.SessionID.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.DestroySession = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/DestroySession',
            request_serializer=legacymodelresponse__pb2.SessionID.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.GeneratorReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/GeneratorReply',
            request_serializer=legacymodelresponse__pb2.MultiStringRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.MultiStringReply.FromString,
        )
        self.ClassificationReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/ClassificationReply',
            request_serializer=legacymodelresponse__pb2.SingleStringRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.SingleStringReply.FromString,
        )
        self.QuestionAndAnswerReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/QuestionAndAnswerReply',
            request_serializer=legacymodelresponse__pb2.QARequest.SerializeToString,
            response_deserializer=legacymodelresponse__pb2.SingleStringReply.FromString,
        )
        self.FillMaskReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/FillMaskReply',
            request_serializer=legacymodelresponse__pb2.SingleStringRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.SingleStringReply.FromString,
        )
        self.TokenClassificationReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/TokenClassificationReply',
            request_serializer=legacymodelresponse__pb2.SingleStringRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.SingleStringReply.FromString,
        )
        self.ConversationalReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/ConversationalReply',
            request_serializer=legacymodelresponse__pb2.ConversationRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.ConversationReply.FromString,
        )
        self.Txt2ImgReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/Txt2ImgReply',
            request_serializer=legacymodelresponse__pb2.MultiStringRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.ImageReply.FromString,
        )
        self.ZeroShotImgClassificationReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/ZeroShotImgClassificationReply',
            request_serializer=legacymodelresponse__pb2.ZeroShotImgClassificationRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.SingleStringReply.FromString,
        )
        self.InpaintingReply = channel.unary_unary(
            '/legacymodelresponse.ModelResponse/InpaintingReply',
            request_serializer=legacymodelresponse__pb2.InpaintingRequest.
            SerializeToString,
            response_deserializer=legacymodelresponse__pb2.ImageReply.FromString,
        )


class ModelResponseServicer(object):
    """Missing associated documentation comment in .proto file."""
    def Terminate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroySession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeneratorReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClassificationReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuestionAndAnswerReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FillMaskReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenClassificationReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConversationalReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Txt2ImgReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ZeroShotImgClassificationReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InpaintingReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelResponseServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Terminate':
        grpc.unary_unary_rpc_method_handler(
            servicer.Terminate,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.
            SerializeToString,
        ),
        'CreateSession':
        grpc.unary_unary_rpc_method_handler(
            servicer.CreateSession,
            request_deserializer=legacymodelresponse__pb2.SessionID.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.
            SerializeToString,
        ),
        'DestroySession':
        grpc.unary_unary_rpc_method_handler(
            servicer.DestroySession,
            request_deserializer=legacymodelresponse__pb2.SessionID.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.
            SerializeToString,
        ),
        'GeneratorReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.GeneratorReply,
            request_deserializer=legacymodelresponse__pb2.MultiStringRequest.FromString,
            response_serializer=legacymodelresponse__pb2.MultiStringReply.
            SerializeToString,
        ),
        'ClassificationReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.ClassificationReply,
            request_deserializer=legacymodelresponse__pb2.SingleStringRequest.FromString,
            response_serializer=legacymodelresponse__pb2.SingleStringReply.
            SerializeToString,
        ),
        'QuestionAndAnswerReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.QuestionAndAnswerReply,
            request_deserializer=legacymodelresponse__pb2.QARequest.FromString,
            response_serializer=legacymodelresponse__pb2.SingleStringReply.
            SerializeToString,
        ),
        'FillMaskReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.FillMaskReply,
            request_deserializer=legacymodelresponse__pb2.SingleStringRequest.FromString,
            response_serializer=legacymodelresponse__pb2.SingleStringReply.
            SerializeToString,
        ),
        'TokenClassificationReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.TokenClassificationReply,
            request_deserializer=legacymodelresponse__pb2.SingleStringRequest.FromString,
            response_serializer=legacymodelresponse__pb2.SingleStringReply.
            SerializeToString,
        ),
        'ConversationalReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.ConversationalReply,
            request_deserializer=legacymodelresponse__pb2.ConversationRequest.FromString,
            response_serializer=legacymodelresponse__pb2.ConversationReply.
            SerializeToString,
        ),
        'Txt2ImgReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.Txt2ImgReply,
            request_deserializer=legacymodelresponse__pb2.MultiStringRequest.FromString,
            response_serializer=legacymodelresponse__pb2.ImageReply.SerializeToString,
        ),
        'ZeroShotImgClassificationReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.ZeroShotImgClassificationReply,
            request_deserializer=legacymodelresponse__pb2.
            ZeroShotImgClassificationRequest.FromString,
            response_serializer=legacymodelresponse__pb2.SingleStringReply.
            SerializeToString,
        ),
        'InpaintingReply':
        grpc.unary_unary_rpc_method_handler(
            servicer.InpaintingReply,
            request_deserializer=legacymodelresponse__pb2.InpaintingRequest.FromString,
            response_serializer=legacymodelresponse__pb2.ImageReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'legacymodelresponse.ModelResponse',
        rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))


# This class is part of an EXPERIMENTAL API.
class ModelResponse(object):
    """Missing associated documentation comment in .proto file."""
    @staticmethod
    def Terminate(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/Terminate',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def CreateSession(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/CreateSession',
            legacymodelresponse__pb2.SessionID.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def DestroySession(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/DestroySession',
            legacymodelresponse__pb2.SessionID.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def GeneratorReply(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/GeneratorReply',
            legacymodelresponse__pb2.MultiStringRequest.SerializeToString,
            legacymodelresponse__pb2.MultiStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def ClassificationReply(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/ClassificationReply',
            legacymodelresponse__pb2.SingleStringRequest.SerializeToString,
            legacymodelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def QuestionAndAnswerReply(request,
                               target,
                               options=(),
                               channel_credentials=None,
                               call_credentials=None,
                               insecure=False,
                               compression=None,
                               wait_for_ready=None,
                               timeout=None,
                               metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/QuestionAndAnswerReply',
            legacymodelresponse__pb2.QARequest.SerializeToString,
            legacymodelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def FillMaskReply(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/FillMaskReply',
            legacymodelresponse__pb2.SingleStringRequest.SerializeToString,
            legacymodelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def TokenClassificationReply(request,
                                 target,
                                 options=(),
                                 channel_credentials=None,
                                 call_credentials=None,
                                 insecure=False,
                                 compression=None,
                                 wait_for_ready=None,
                                 timeout=None,
                                 metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/TokenClassificationReply',
            legacymodelresponse__pb2.SingleStringRequest.SerializeToString,
            legacymodelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def ConversationalReply(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/ConversationalReply',
            legacymodelresponse__pb2.ConversationRequest.SerializeToString,
            legacymodelresponse__pb2.ConversationReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def Txt2ImgReply(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/Txt2ImgReply',
            legacymodelresponse__pb2.MultiStringRequest.SerializeToString,
            legacymodelresponse__pb2.ImageReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def ZeroShotImgClassificationReply(request,
                                       target,
                                       options=(),
                                       channel_credentials=None,
                                       call_credentials=None,
                                       insecure=False,
                                       compression=None,
                                       wait_for_ready=None,
                                       timeout=None,
                                       metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/ZeroShotImgClassificationReply',
            legacymodelresponse__pb2.ZeroShotImgClassificationRequest.SerializeToString,
            legacymodelresponse__pb2.SingleStringReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def InpaintingReply(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/legacymodelresponse.ModelResponse/InpaintingReply',
            legacymodelresponse__pb2.InpaintingRequest.SerializeToString,
            legacymodelresponse__pb2.ImageReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)
