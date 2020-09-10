import time
import logging
import concurrent.futures

from spaceone.core.service import *
from spaceone.power_scheduler.manager.controller_manager import ControllerManager

_LOGGER = logging.getLogger(__name__)
SUPPORTED_RESOURCE_TYPE = ['power_scheduler.Server']
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
    @check_required(['resources_params'])
    def start(self, params):
        """ verify options capability
        Args:
            params
              - resources_params: list

        Returns:

        Raises:
             ERROR_VERIFY_FAILED:
        """
        start_time = time.time()

        resources_params = params['resources_params']

        _LOGGER.debug(f'[start] resources_params: {params["resources_params"]}')

        with concurrent.futures.ThreadPoolExecutor(max_workers=NUMBER_OF_CONCURRENT) as executor:
            future_executors = []
            for resource_param in resources_params:
                future_executors.append(executor.submit(self.controller_manager.start, resource_param))

            for future in concurrent.futures.as_completed(future_executors):
                for result in future.result():
                    _LOGGER.debug(f'[start] result: {result}')

                    yield result

        print(f'############## TOTAL START FINISHED {time.time() - start_time} Sec ##################')

        return {}

    @transaction
    @check_required(['resources_params'])
    def stop(self, params):
        """ verify options capability
        Args:
            params
              - resources_params: list

        Returns:

        Raises:
             ERROR_VERIFY_FAILED:
        """
        start_time = time.time()

        resources_params = params['resources_params']

        _LOGGER.debug(f'[stop] resources_params: {params["resources_params"]}')

        with concurrent.futures.ThreadPoolExecutor(max_workers=NUMBER_OF_CONCURRENT) as executor:
            future_executors = []
            for resource_param in resources_params:
                future_executors.append(executor.submit(self.controller_manager.stop, resource_param))

            for future in concurrent.futures.as_completed(future_executors):
                for result in future.result():
                    _LOGGER.debug(f'[stop] result: {result}')

                    yield result
        print(f'############## TOTAL STOP FINISHED {time.time() - start_time} Sec ##################')

        return {}

    @transaction
    @check_required(['schedule_status','target_resources_params'])
    def getRetryResourceStatus(self, params):
        """ verify options capability
        Args::q:q:
            params
              - schedule_status: string
              - target_resources_params: list

        Returns:

        Raises:
             ERROR_VERIFY_FAILED:
        """
        start_time = time.time()
        schedule_status = params['schedule_status']
        target_resources_params = params['target_resources_params']
        res = []

        _LOGGER.debug(f'[getRetryResourceStatus] target_resources: {params["target_resources_params"]}')

        with concurrent.futures.ThreadPoolExecutor(max_workers=NUMBER_OF_CONCURRENT) as executor:
            future_executors = []
            for resource_param in target_resources_params:
                future_executors.append(executor.submit(self.controller_manager.getRetryResourceStatus, resource_param))

            for future in concurrent.futures.as_completed(future_executors):
                for result in future.result():
                    _LOGGER.debug(f'[getRetryResourceStatus] result: {result}')
                    res.append(result)

        print(f'############## TOTAL START FINISHED {time.time() - start_time} Sec ##################')

        return res, schedule_status