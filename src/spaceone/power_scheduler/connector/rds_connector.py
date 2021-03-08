__all__ = ["RDSConnector"]

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

class RDSConnector(BaseConnector):

    def __init__(self, transaction=None, config=None):
        self.session = None
        self.rds_client = None

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
        self.rds_client = self.session.client('rds')

    def start_rds_instance(self, rds_instance_id):
        try:
            res = self.rds_client.start_db_instance(DBInstanceIdentifier=rds_instance_id)
            _LOGGER.info(f'[RDSConnector] Start RDS instance : {res}')
            return res
        except Exception as e:
            _LOGGER.error(f'[RDSConnector] start_rds_instance error: {e}')
            raise e

    def start_rds_cluster(self, rds_cluster_id):
        try:
            res = self.rds_client.start_db_cluster(DBClusterIdentifier=rds_cluster_id)
            _LOGGER.info(f'[RDSConnector] Start RDS cluster : {res}')
            return res
        except Exception as e:
            _LOGGER.error(f'[RDSConnector] start_rds_cluster error: {e}')
            raise e

    def stop_rds_instance(self, rds_instance_id):
        try:
            res = self.rds_client.stop_db_instance(DBInstanceIdentifier=rds_instance_id)
            _LOGGER.info(f'[RDSConnector] Stop RDS instance : {res}')
            return res
        except Exception as e:
            _LOGGER.error(f'[RDSConnector] stop_rds_instance error: {e}')
            raise e

    def stop_rds_cluster(self, rds_cluster_id):
        try:
            res = self.rds_client.stop_db_cluster(DBClusterIdentifier=rds_cluster_id)
            _LOGGER.info(f'[RDSConnector] Stop RDS cluster : {res}')
            return res
        except Exception as e:
            _LOGGER.error(f'[RDSConnector] stop_rds_cluster error: {e}')
            raise e

    def get_rds_instance(self, db_instance_id):
        try:
            response = self.rds_client.describe_db_instances(DBInstanceIdentifier=db_instance_id)
            _LOGGER.debug(f'[RDSConnector] get_rds_instance response : {response}')
            return response['DBInstances'][0]
        except Exception as e:
            _LOGGER.error(f'[RDSConnector] get_rds_instance error: {e}')
            raise e

    def get_rds_cluster(self, db_cluster_id):
        try:
            response = self.rds_client.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
            _LOGGER.debug(f'[RDSConnector] get_rds_cluster response : {response}')
            return response['DBClusters'][0]
        except Exception as e:
            _LOGGER.error(f'[RDSConnector] get_rds_cluster error: {e}')
            raise e
