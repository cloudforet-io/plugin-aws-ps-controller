import logging

from spaceone.core.service import *
from spaceone.power_scheduler.manager.controller_manager import ControllerManager

_LOGGER = logging.getLogger(__name__)
DEFAULT_REGION = 'us-east-1'
SUPPORTED_RESOURCE_TYPE = ['power_scheduler.Server']
FILTER_FORMAT = []

@authentication_handler
class ControllerService(BaseService):
    def __init__(self, metadata):
        super().__init__(metadata)
        self.collector_manager: ControllerManager = self.locator.get_manager('ControllerManager')

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
        manager = self.locator.get_manager('ControllerManager')
        secret_data = params['secret_data']
        region_name = params.get('region_name', DEFAULT_REGION)
        active = manager.verify(secret_data, region_name)

        return {}

    @transaction
    @check_required(['options','secret_data','resources'])
    def start(self, params):
        """ verify options capability
        Args:
            params
              - options : dict
              - secret_data: dict
              - resources: list

        Returns:

        Raises:
             ERROR_VERIFY_FAILED:
        """
        manager = self.locator.get_manager('ControllerManager')
        resource_list = params['resources']
        secret_data = params['secret_data']
        region_name = params.get('region_name', DEFAULT_REGION)

        _LOGGER.debug(f'[start] resources: {params["resources"]}')
        _LOGGER.debug(f'[start] secret_data: {params["secret_data"]}')

        manager.start(secret_data, region_name, resource_list)

        return {}
