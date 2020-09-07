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
        # Server
        self._instanceIds = []

        # AutoScalingGroup
        self._autoScalingGroups = []
        self._asg_desired_capacity = {}
        self._asg_min_size = {}

        # RDS
        self._rdsInstances = []
        self._rdsClusters = []

    def verify(self, secret_data, region_name):
        """ Check connection
        """
        ec2_connector = self.locator.get_connector('EC2Connector')
        r = ec2_connector.verify(secret_data, region_name)
        # ACTIVE/UNKNOWN
        return r

    def start(self, resource_param):
        """ Check connection
        """

        secret_data = resource_param['secret_data']
        resource_list = resource_param['resources']
        region_name = DEFAULT_REGION
        if 'region_name' in secret_data:
            region_name = secret_data['region_name']

        self._set_resources_by_resource_type(resource_list)
        result_list = []

        if len(self._instanceIds) > 0:
            ec2_connector = self.locator.get_connector('EC2Connector')
            ec2_connector.set_client(secret_data, region_name)
            # Step 1 : Get instances from requested input params
            instances = ec2_connector.get_ec2_instance_list(self._get_resources(RESOURCE_TYPE_SERVER))

            # Step 2 : Filtered resources by status
            stopped_instances = self._get_ec2_instance_list_by_status(instances, 'stopped')

            # Step 3 : Request to start resources to provider
            stopped_instances_ids = self._get_ec2_instance_ids(stopped_instances)
            ec2_result = ec2_connector.start_instances(stopped_instances_ids)
            result_list.append(ec2_result)

        if len(self._autoScalingGroups) > 0:
            auto_scaling_connector = self.locator.get_connector('AutoScalingConnector')
            auto_scaling_connector.set_client(secret_data, region_name)
            # Step 1 : Get ASGs from requested input params
            autoScalingGroups = auto_scaling_connector.get_asg_list(self._get_resources(RESOURCE_TYPE_ASG))

            # Step 2 : Filtered resources by status
            stopped_ASGs = self._get_asg_list_by_status(autoScalingGroups, 'stopped')

            # Step 3 : Request to start resources to provider
            stopped_asg_names = self._get_asg_names(stopped_ASGs)
            asg_result = auto_scaling_connector.start_auto_scaling(stopped_asg_names, self._get_min_size(), self._get_desired_capacity())
            result_list.append(asg_result)

        return result_list

    def stop(self, resource_param):
        """ Check connection
        """
        secret_data = resource_param['secret_data']
        resource_list = resource_param['resources']
        region_name = DEFAULT_REGION
        if 'region_name' in secret_data:
            region_name = secret_data['region_name']

        self._set_resources_by_resource_type(resource_list)
        result_list = []

        if len(self._instanceIds) > 0:
            ec2_connector = self.locator.get_connector('EC2Connector')
            ec2_connector.set_client(secret_data, region_name)
            # Step 1 : Get instances from requested input params
            instances = ec2_connector.get_ec2_instance_list(self._get_resources(RESOURCE_TYPE_SERVER))

            # Step 2 : Filtered resources by status
            running_instances = self._get_ec2_instance_list_by_status(instances, 'running')

            # Step 3 : Request to stop resources to provider
            running_instances_ids = self._get_ec2_instance_ids(running_instances)
            ec2_result = ec2_connector.stop_instances(running_instances_ids)
            result_list.append(ec2_result)

        if len(self._autoScalingGroups) > 0:
            auto_scaling_connector = self.locator.get_connector('AutoScalingConnector')
            auto_scaling_connector.set_client(secret_data, region_name)
            # Step 1 : Get ASGs from requested input params
            autoScalingGroups = auto_scaling_connector.get_asg_list(self._get_resources(RESOURCE_TYPE_ASG))

            # Step 2 : Filtered resources by status
            running_ASGs = self._get_asg_list_by_status(autoScalingGroups, 'running')

            # Step 3 : Request to stop resources to provider
            running_asg_names = self._get_asg_names(running_ASGs)
            asg_result = auto_scaling_connector.stop_auto_scaling(running_asg_names)
            result_list.append(asg_result)

        return result_list

    def _set_resources_by_resource_type(self, resource_list):
        for r in resource_list:
            _LOGGER.debug(f'[_set_resources_by_resource_type] resource: {r}')
            if r['resource_type'] == RESOURCE_TYPE_SERVER:
                instanceId = r['resource']['id']
                self._instanceIds.append(instanceId)
                _LOGGER.debug(f'[_set_resources_by_resource_type] instanceId: {instanceId}')
            if r['resource_type'] == RESOURCE_TYPE_ASG:
                asg_name = r['resource']['id']
                if 'desired_capacity' in r['resource'] and 'min_size' in r['resource']:
                    self._asg_desired_capacity[asg_name] = r['resource']['desired_capacity']
                    self._asg_min_size[asg_name] = r['resource']['min_size']
                self._autoScalingGroups.append(asg_name)
                _LOGGER.debug(f'[_set_resources_by_resource_type] asg_name: {asg_name}')

    def _get_resources(self, resource_type):
        # TODO: Try to add other resources by resource_type
        if resource_type == RESOURCE_TYPE_SERVER:
            _LOGGER.debug(f'[_get_resources] instanceId: {self._instanceIds}')
            return self._instanceIds

        if resource_type == RESOURCE_TYPE_ASG:
            _LOGGER.debug(f'[_get_resources] ASGs: {self._autoScalingGroups}')
            return self._autoScalingGroups

        return None

    def _get_desired_capacity(self):
        return self._asg_desired_capacity

    def _get_min_size(self):
        return self._asg_min_size

    def _get_asg_list_by_status(self, asg_list, status) -> list:
        filtered_asg_list = []

        for asg in asg_list:
            if self._get_asg_status(asg) == status:
                filtered_asg_list.append(asg)

        return filtered_asg_list

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

    def _get_asg_names(self, asg_list) -> list:
        asg_names = []

        for asg in asg_list:
            asg_names.append(asg['AutoScalingGroupName'])

        return asg_names

    def _get_ec2_instance_list_by_status(self, ec2_instance_list, status) -> list:
        filtered_ec2_instance_list = []

        for ec2_instance in ec2_instance_list:
            if self._get_ec2_instance_status(ec2_instance) == status:
                filtered_ec2_instance_list.append(ec2_instance)

        return filtered_ec2_instance_list

    def _get_ec2_instance_status(self, ec2_instance) -> str:
        return ec2_instance['State']['Name']

    def _get_ec2_instance_ids(self, ec2_instance_list) -> list:
        ec2_instance_ids = []

        for ec2_instance in ec2_instance_list:
            ec2_instance_ids.append(ec2_instance['InstanceId'])

        return ec2_instance_ids