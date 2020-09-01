__all__ = ["AutoScalingConnector"]

import boto3
import botocore
from boto3.session import Session
import logging

from spaceone.core.error import *
from spaceone.core import utils
from spaceone.core import pygrpc 
from spaceone.core.utils import parse_endpoint
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)

class AutoScalingConnector(BaseConnector):

    def __init__(self, transaction=None, config=None):
        self.session = None
        self.asg_client = None

    def get_session(self, secret_data, region_name):
        params = {
            'aws_access_key_id': secret_data['aws_access_key_id'],
            'aws_secret_access_key': secret_data['aws_secret_access_key'],
            'region_name': region_name
        }

        session = Session(**params)

        # ASSUME ROLE
        if role_arn := secret_data.get('role_arn'):
            sts = session.client('sts')
            assume_role_object = sts.assume_role(RoleArn=role_arn,
                                                 RoleSessionName=utils.generate_id('AssumeRoleSession'))
            credentials = assume_role_object['Credentials']

            assume_role_params = {
                'aws_access_key_id': credentials['AccessKeyId'],
                'aws_secret_access_key': credentials['SecretAccessKey'],
                'region_name': region_name,
                'aws_session_token': credentials['SessionToken']
            }
            session = Session(**assume_role_params)

        return session

    def set_client(self, secret_data, region_name):
        self.session = self.get_session(secret_data, region_name)
        self.asg_client = self.session.client('autoscaling')

    def start_auto_scaling(self, asg_list, min_size, desired_capacity, **query):
        return self.set_asg_desired_capacity_with_min_size(asg_list, min_size, desired_capacity)

    def stop_auto_scaling(self, asg_list, **query):
        desired_capacity = {}
        min_size = {}
        for asg_name in asg_list:
            # initialize dictionaries with zero, {'A': 0, 'B': 0}
            desired_capacity[asg_name] = 0
            min_size[asg_name] = 0

        return self.set_asg_desired_capacity_with_min_size(asg_list, min_size, desired_capacity)

    def set_asg_desired_capacity_with_min_size(self, asg_list, min_size, desired_capacity):
        response_list = []

        for asg_name in asg_list:
            if asg_name in min_size and asg_name in desired_capacity:
                try:
                    res = self.asg_client.update_auto_scaling_group(
                        AutoScalingGroupName=asg_name,
                        MinSize=int(min_size[asg_name]),
                        DesiredCapacity=int(desired_capacity[asg_name]),
                    )
                    print('Set asg_desired_capacity :' + str(asg_name) + ', capacity: ' + str(desired_capacity[asg_name]))
                except botocore.exceptions.ClientError as e:
                    print (e)

                    e_arr = str(e).split(':')[1].split(',')
                    
                    # An error occurred (ValidationError) when calling the UpdateAutoScalingGroup operation: Max bound, 3, must be greater than or equal to min bound, 5
                    if ' Max bound' == e_arr[0] and ' must be greater than or equal to min bound' == e_arr[2]:
                        max_capacity = int(e_arr[1].strip())

                        res = self.asg_client.update_auto_scaling_group(
                            AutoScalingGroupName=asg_name,
                            MinSize=max_capacity,
                            DesiredCapacity=max_capacity,
                        )
                        print('Set asg_desired_capacity(max capacity may be changed by user) :' + str(asg_name) + ', capacity: ' + e_arr[1])
                response_list.append(res)

        return response_list
      