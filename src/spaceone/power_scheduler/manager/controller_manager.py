__all__ = ['ControllerManager']

import time
import logging
import json

from spaceone.core.manager import BaseManager


_LOGGER = logging.getLogger(__name__)

RESOURCE_TYPE_SERVER = 'inventory.Server'
RESOURCE_TYPE_ASG = 'inventory.CloudService.aws.AutoScaling.AutoScalingGroup'
RESOURCE_TYPE_RDS_DB = 'inventory.CloudService.aws.RDS.Database'

DEFAULT_REGION = 'us-east-1'

class ControllerManager(BaseManager):

    def __init__(self, transaction):
        super().__init__(transaction)

    def verify(self, secret_data, region_name):
        """ Check connection
        """
        ec2_connector = self.locator.get_connector('EC2Connector')
        r = ec2_connector.verify(secret_data, region_name)
        # ACTIVE/UNKNOWN
        return r

    def start(self, secret_data, region_name, resource_id, resource_type, resource_data):
        """ Check connection
        """
        if resource_type == RESOURCE_TYPE_SERVER:
            ec2_connector = self.locator.get_connector('EC2Connector')
            ec2_connector.set_client(secret_data, region_name)
            # Step 1 : Get instance from requested input params
            instance = ec2_connector.get_ec2_instance(resource_id)

            # Step 2 : Start instance by status
            instance_status = instance['State']['Name']
            if instance_status == 'stopped':
                res = ec2_connector.start_instances(resource_id)
                _LOGGER.debug(f'[start] instance res: {res}')
        if resource_type == RESOURCE_TYPE_ASG:
            auto_scaling_connector = self.locator.get_connector('AutoScalingConnector')
            auto_scaling_connector.set_client(secret_data, region_name)

            # Step 1 : Get ASG from requested input params
            autoScalingGroup = auto_scaling_connector.get_asg(resource_id)

            # Step 2 : Start ASG by status
            asg_status = self._get_asg_status(asg)
            if asg_status == 'stopped':
                res = auto_scaling_connector.start_auto_scaling(resource_id, resource_data['min_size'], resource_data['desired_capacity'])
                _LOGGER.debug(f'[start] autoScalingGroup res: {res}')

    def stop(self, secret_data, region_name, resource_id, resource_type, resource_data):
        """ Check connection
        """
        if resource_type == RESOURCE_TYPE_SERVER:
            ec2_connector = self.locator.get_connector('EC2Connector')
            ec2_connector.set_client(secret_data, region_name)
            # Step 1 : Get instance from requested input params
            instance = ec2_connector.get_ec2_instance(resource_id)

            # Step 2 : Stop instance by status
            instance_status = instance['State']['Name']
            if instance_status == 'running':
                res = ec2_connector.stop_instances(resource_id)
                _LOGGER.debug(f'[stop] instance res: {res}')
        if resource_type == RESOURCE_TYPE_ASG:
            auto_scaling_connector = self.locator.get_connector('AutoScalingConnector')
            auto_scaling_connector.set_client(secret_data, region_name)

            # Step 1 : Get ASG from requested input params
            autoScalingGroup = auto_scaling_connector.get_asg(resource_id)

            # Step 2 : Stop ASG by status
            asg_status = self._get_asg_status(autoScalingGroup)
            if asg_status == 'running':
                res = auto_scaling_connector.stop_auto_scaling(resource_id)
                _LOGGER.debug(f'[stop] autoScalingGroup res: {res}')

    def _get_asg_status(self, asg) -> str:
        inservice_count = 0
        desired_capacity = asg['DesiredCapacity']

        if desired_capacity == 0:
            return 'stopped'

        for instance in asg['Instances']:
            if instance['LifecycleState'] == 'InService':
                inservice_count += 1

        if desired_capacity == inservice_count:
            return 'running'

        return 'stopped'