__all__ = ['ControllerManager']

import time
import logging
import json

from spaceone.core.manager import BaseManager


_LOGGER = logging.getLogger(__name__)

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

    def start(self, secret_data, region_name, resource_id, cloud_service_type, resource_data):
        if cloud_service_type == "Instance":
            ec2_connector = self.locator.get_connector('EC2Connector')
            ec2_connector.set_client(secret_data, region_name)
            # Step 1 : Get instance from requested input params
            instance = ec2_connector.get_ec2_instance(resource_id)

            # Step 2 : Start instance by status
            instance_status = instance['State']['Name']
            if instance_status == 'stopped':
                res = ec2_connector.start_instances(resource_id)
                _LOGGER.debug(f'[start] instance res: {res}')
        if cloud_service_type == "AutoScalingGroup":
            auto_scaling_connector = self.locator.get_connector('AutoScalingConnector')
            auto_scaling_connector.set_client(secret_data, region_name)

            # Step 1 : Get ASG from requested input params
            autoScalingGroup = auto_scaling_connector.get_asg(resource_id)

            # Step 2 : Start ASG by status
            asg_status = self._get_asg_status(autoScalingGroup)
            if asg_status == 'stopped':
                if 'min_size' not in resource_data or 'desired_capacity' not in resource_data:
                    raise AttributeError('There is no desired_capacity or min_size in resource_data')
                res = auto_scaling_connector.start_auto_scaling(resource_id, resource_data['min_size'], resource_data['desired_capacity'])
                _LOGGER.debug(f'[start] autoScalingGroup res: {res}')
        if cloud_service_type == "Database":
            rds_connector = self.locator.get_connector('RDSConnector')
            rds_connector.set_client(secret_data, region_name)

            #if 'service_type' not in resource_data:
            #    raise AttributeError('There is no service_type(instance/cluster) for RDS in resource_data')

            service_type = resource_data['data']['role']
            if service_type == 'instance':
                # Step 1 : Get RDS instance from requested input params
                rds_instance = rds_connector.get_rds_instance(resource_id)

                # Step 2 : Start RDS instance by status
                rds_instance_status = rds_instance['DBInstanceStatus']
                if rds_instance_status == 'stopped':
                    res = rds_connector.start_rds_instance(resource_id)
                    _LOGGER.debug(f'[start] RDS instance res: {res}')
            if service_type == 'cluster':
                # Step 1 : Get RDS cluster from requested input params
                rds_cluster = rds_connector.get_rds_cluster(resource_id)

                # Step 2 : Start RDS cluster by status
                rds_cluster_status = rds_cluster['Status']
                if rds_cluster_status == 'stopped':
                    res = rds_connector.start_rds_cluster(resource_id)
                    _LOGGER.debug(f'[start] RDS cluster res: {res}')

    def stop(self, secret_data, region_name, resource_id, cloud_service_type, resource_data):
        if cloud_service_type == "Instance":
            ec2_connector = self.locator.get_connector('EC2Connector')
            ec2_connector.set_client(secret_data, region_name)
            # Step 1 : Get instance from requested input params
            instance = ec2_connector.get_ec2_instance(resource_id)

            # Step 2 : Stop instance by status
            instance_status = instance['State']['Name']
            if instance_status == 'running':
                res = ec2_connector.stop_instances(resource_id)
                _LOGGER.debug(f'[stop] instance res: {res}')
        if cloud_service_type == "AutoScalingGroup":
            auto_scaling_connector = self.locator.get_connector('AutoScalingConnector')
            auto_scaling_connector.set_client(secret_data, region_name)

            # Step 1 : Get ASG from requested input params
            autoScalingGroup = auto_scaling_connector.get_asg(resource_id)

            # Step 2 : Stop ASG by status
            asg_status = self._get_asg_status(autoScalingGroup)
            if asg_status == 'running':
                res = auto_scaling_connector.stop_auto_scaling(resource_id)
                _LOGGER.debug(f'[stop] autoScalingGroup res: {res}')
        if cloud_service_type == "Database":
            rds_connector = self.locator.get_connector('RDSConnector')
            rds_connector.set_client(secret_data, region_name)

            #if 'service_type' not in resource_data:
            #    raise AttributeError('There is no service_type(instance/cluster) for RDS in resource_data')

            service_type = resource_data['data']['role']
            if service_type == 'instance':
                # Step 1 : Get RDS instance from requested input params
                rds_instance = rds_connector.get_rds_instance(resource_id)

                # Step 2 : Stop RDS instance by status
                rds_instance_status = rds_instance['DBInstanceStatus']
                if rds_instance_status == 'available':
                    res = rds_connector.stop_rds_instance(resource_id)
                    _LOGGER.debug(f'[stop] RDS instance res: {res}')
            if service_type == 'cluster':
                # Step 1 : Get RDS cluster from requested input params
                rds_cluster = rds_connector.get_rds_cluster(resource_id)

                # Step 2 : Start RDS cluster by status
                rds_cluster_status = rds_cluster['Status']
                if rds_cluster_status == 'available':
                    res = rds_connector.stop_rds_cluster(resource_id)
                    _LOGGER.debug(f'[stop] RDS cluster res: {res}')

    def reboot(self, secret_data, region_name, resource_id, cloud_service_type, resource_data):
        # reboot case is only occured on server-type resource
        if cloud_service_type == "Instance":
            ec2_connector = self.locator.get_connector('EC2Connector')
            ec2_connector.set_client(secret_data, region_name)

            res = ec2_connector.reboot_instance(resource_id)
            _LOGGER.debug(f'[reboot] instance res: {res}')

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