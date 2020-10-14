__all__ = ["EC2Connector"]

import boto3
from boto3.session import Session
import logging

from spaceone.core.error import *
from spaceone.core import utils
from spaceone.core import pygrpc 
from spaceone.core.utils import parse_endpoint
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)
DEFAULT_REGION = 'us-east-1'
PAGINATOR_MAX_ITEMS = 10000
PAGINATOR_PAGE_SIZE = 50
RESOURCES = ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']

class EC2Connector(BaseConnector):

    def __init__(self, transaction=None, config=None):
        self.session = None
        self.ec2_client = None

    def verify(self, secret_data, region_name):
        self.set_connect(secret_data, region_name)
        return "ACTIVE"

    def set_connect(self, secret_data, region_name, service="ec2"):
        session = self.get_session(secret_data, region_name)
        aws_conf = {}
        aws_conf['region_name'] = region_name

        if service in RESOURCES:
            resource = session.resource(service, **aws_conf)
            client = resource.meta.client
        else:
            resource = None
            client = session.client(service, region_name=region_name)
        return client, resource

    def get_session(self, secret_data, region_name):
        params = {
            'aws_access_key_id': secret_data['aws_access_key_id'],
            'aws_secret_access_key': secret_data['aws_secret_access_key'],
            'region_name': region_name
        }
        _LOGGER.debug(f'[EC2Connector] get_session params : {params}')

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
        self.ec2_client = self.session.client('ec2')

    def start_instances(self, instance_id, **query):
        try:
            response = self.ec2_client.start_instances(InstanceIds=[instance_id], **query)
            _LOGGER.info(f'[EC2Connector] Start instances : {response}')
            return response
        except Exception as e:
            _LOGGER.error(f'[EC2Connector] start_instances error: {e}')

    def stop_instances(self, instance_id, **query):
        try:
            response = self.ec2_client.stop_instances(InstanceIds=[instance_id], Force=True, **query)
            _LOGGER.info(f'[EC2Connector] Stop instances : {response}')
            return response
        except Exception as e:
            _LOGGER.error(f'[EC2Connector] stop_instances error: {e}')

    def reboot_instance(self, instance_id, **query):
        try:
            response = self.ec2_client.reboot_instances(InstanceIds=[instance_id], **query)
            _LOGGER.info(f'[EC2Connector] Reboot instances : {response}')
            return response
        except Exception as e:
            _LOGGER.error(f'[EC2Connector] Reboot_instances error: {e}')

    def get_ec2_instance(self, instance_id):
        try:
            response = self.ec2_client.describe_instances(InstanceIds=[instance_id])
            _LOGGER.debug(f'[EC2Connector] get_ec2_instance response : {response}')
            return response['Reservations'][0]['Instances'][0]
        except Exception as e:
            _LOGGER.error(f'[EC2Connector] get_ec2_instance error: {e}')