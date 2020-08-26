__all__ = ['ControllerManager']

import time
import logging
import json

from spaceone.core.manager import BaseManager


_LOGGER = logging.getLogger(__name__)

class ControllerManager(BaseManager):

    def __init__(self, transaction):
        super().__init__(transaction)
        self._instanceIds = []

    def verify(self, secret_data, region_name):
        """ Check connection
        """
        ec2_connector = self.locator.get_connector('EC2Connector')
        r = ec2_connector.verify(secret_data, region_name)
        # ACTIVE/UNKNOWN
        return r

    def start(self, secret_data, region_name, resource_list):
        """ Check connection
        """
        # TODO: Try to start resources by resource_list
        ec2_connector = self.locator.get_connector('EC2Connector')
        ec2_connector.set_client(secret_data, region_name)

        self._set_resources_by_resource_type(resource_list)

        ec2_connector.start_instances(self._get_resources('inventory.Server'))

        return {}

    def _set_resources_by_resource_type(self, resource_list):
        for resource in resource_list:
            _LOGGER.debug(f'[_set_resources_by_resource_type] resource: {resource}')
            if resource['resource_type'] == 'inventory.Server':
                instanceId = resource['resource']
                self._instanceIds.append(instanceId)
                _LOGGER.debug(f'[_set_resources_by_resource_type] instanceId: {instanceId}')

    def _get_resources(self, resource_type):
        # TODO: Try to add other resources by resource_type
        _LOGGER.debug(f'[_get_resources] instanceId: {self._instanceIds}')
        return self._instanceIds