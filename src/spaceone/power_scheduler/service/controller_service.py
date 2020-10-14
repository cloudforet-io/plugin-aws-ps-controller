import time
import logging
import concurrent.futures

from spaceone.core.service import *
from spaceone.power_scheduler.manager.controller_manager import ControllerManager

_LOGGER = logging.getLogger(__name__)
SUPPORTED_RESOURCE_TYPE = ['inventory.CloudService', 'inventory.Server']
DEFAULT_REGION = 'us-east-1'
NUMBER_OF_CONCURRENT = 20
FILTER_FORMAT = []

@authentication_handler
class ControllerService(BaseService):
    def __init__(self, metadata):
        super().__init__(metadata)
        self.controller_manager: ControllerManager = self.locator.get_manager('ControllerManager')

    @check_required(['options'])
    def init(self, params):
        """ init plugin by options
        """
        capability = {
            'filter_format': FILTER_FORMAT,
            'supported_resource_type': SUPPORTED_RESOURCE_TYPE
        }
        _LOGGER.debug(f'[init] name: {params["options"]}')
        return {'metadata': capability}

    @transaction
    @check_required(['options'])
    def init(self, params):
        """ init plugin by options
        """
        capability = {
            'filter_format':FILTER_FORMAT,
            'supported_resource_type' : SUPPORTED_RESOURCE_TYPE
        }
        _LOGGER.debug(f'[init_transaction] name: {params["options"]}')
        return {'metadata': capability}

    @transaction
    @check_required(['options','secret_data'])
    @append_query_filter(['schema'])
    def verify(self, params):
        """ verify options capability
        Args:
            params
              - options
              - secret_data: may be empty dictionary

        Returns:

        Raises:
             ERROR_VERIFY_FAILED:
        """
        secret_data = params['secret_data']
        region_name = params.get('region_name', DEFAULT_REGION)
        active = self.controller_manager.verify(secret_data, region_name)

        return {}

    @transaction
    @check_required(['options','secret_data','resource_id','resource_type'])
    @append_query_filter(['schema', 'resource_data'])
    def start(self, params):
        """ verify options capability
        Args:
            params
              - options: list
              - secret_data: dict
              - resource_id: string
              - resource_type: string
              - resource_data: dict
              - schema: string

        Returns:
        """
        secret_data = params['secret_data']
        resource_id = params['resource_id']
        resource_type = params['resource_type']
        region_name = DEFAULT_REGION
        if 'region_name' in secret_data:
            region_name = secret_data['region_name']
        resource_data = None
        if 'resource_data' in params:
            resource_data = params['resource_data']

        self.controller_manager.start(secret_data, region_name, resource_id, resource_type, resource_data)

        return {}

    @transaction
    @check_required(['options','secret_data','resource_id','resource_type'])
    @append_query_filter(['schema', 'resource_data'])
    def stop(self, params):
        """ verify options capability
        Args:
            params
              - options: list
              - secret_data: dict
              - resource_id: string
              - resource_type: string
              - resource_data: dict
              - schema: string

        Returns:
        """
        secret_data = params['secret_data']
        resource_id = params['resource_id']
        resource_type = params['resource_type']
        region_name = DEFAULT_REGION
        if 'region_name' in secret_data:
            region_name = secret_data['region_name']
        resource_data = None
        if 'resource_data' in params:
            resource_data = params['resource_data']

        self.controller_manager.stop(secret_data, region_name, resource_id, resource_type, resource_data)

        return {}

    @transaction
    @check_required(['options','secret_data','resource_id','resource_type'])
    @append_query_filter(['schema', 'resource_data'])
    def reboot(self, params):
        """ verify options capability
        Args:
            params
              - options: list
              - secret_data: dict
              - resource_id: string
              - resource_type: string
              - resource_data: dict
              - schema: string

        Returns:
        """
        secret_data = params['secret_data']
        resource_id = params['resource_id']
        resource_type = params['resource_type']
        region_name = DEFAULT_REGION
        if 'region_name' in secret_data:
            region_name = secret_data['region_name']
        resource_data = None
        if 'resource_data' in params:
            resource_data = params['resource_data']

        self.controller_manager.reboot(secret_data, region_name, resource_id, resource_type, resource_data)

        return {}