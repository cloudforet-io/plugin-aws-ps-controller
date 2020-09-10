import logging

from spaceone.api.power_scheduler.plugin import controller_pb2, controller_pb2_grpc
from spaceone.core.pygrpc import BaseAPI
from spaceone.core.pygrpc.message_type import *

_LOGGER = logging.getLogger(__name__)

class Controller(BaseAPI, controller_pb2_grpc.ControllerServicer):

    pb2 = controller_pb2
    pb2_grpc = controller_pb2_grpc

    def init(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('ControllerService', metadata) as controller_svc:
            data = controller_svc.init(params)
            return self.locator.get_info('PluginInfo', data)

    def verify(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('ControllerService', metadata) as controller_svc:
            controller_svc.verify(params)
            return self.locator.get_info('EmptyInfo')

    def start(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('ControllerService', metadata) as controller_svc:
            for resource in controller_svc.start(params):
                _LOGGER.debug(f'[start] response resource: {resource}')
                res = {
                    'state': 'SUCCESS',
                    'message': '',
                    'resource_type': '',
                    'resource': change_struct_type(resource)
                }
                _LOGGER.debug(f'[start] response res (struct type): {res}')
                # TODO(check) : Need to check if there is a way for API test(spacectl) with yield like below
                #yield self.locator.get_info('ResourceInfo', res)
            return self.locator.get_info('EmptyInfo')

    def stop(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('ControllerService', metadata) as controller_svc:
            for resource in controller_svc.stop(params):
                _LOGGER.debug(f'[stop] response resource: {resource}')
                res = {
                    'state': 'SUCCESS',
                    'message': '',
                    'resource_type': '',
                    'resource': change_struct_type(resource)
                }
                _LOGGER.debug(f'[stop] response res (struct type): {res}')

                #yield self.locator.get_info('ResourceInfo', res)
            return self.locator.get_info('EmptyInfo')

    def getRetryResourceStatus(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('ControllerService', metadata) as controller_svc:
            resources, schedule_status = controller_svc.getRetryResourceStatus(params)
            res = {
                'requested_schedule_status': schedule_status,
                'resources': resources
            }
            return self.locator.get_info('RetryResourceStatusInfo', res)