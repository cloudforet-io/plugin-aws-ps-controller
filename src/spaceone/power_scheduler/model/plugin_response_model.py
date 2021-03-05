from schematics.models import Model
from schematics.types import ListType, DictType, StringType
from schematics.types.compound import ModelType

__all__ = ['PluginInitResponse']

_SUPPORTED_RESOURCE_TYPE = [
    'inventory.Server?provider=aws&cloud_service_group=EC2&cloud_service_type=Instance',
    'inventory.CloudService?provider=aws&cloud_service_group=RDS&cloud_service_type=Database',
    'inventory.CloudService?provider=aws&cloud_service_group=EC2&cloud_service_type=AutoScalingGroup'
]

_REFERENCE_KEYS = [
    {
        'resource_type': 'inventory.Server?provider=aws&cloud_service_group=EC2&cloud_service_type=Instance',
        'required_keys': [
            'reference.resource_id',
            'cloud_service_type'
        ]
    }, {
        'resource_type': 'inventory.CloudService?provider=aws&cloud_service_group=RDS&cloud_service_type=Database',
        'required_keys': [
            'reference.resource_id',
            'cloud_service_type',
            'data.status',
            'data.role'
        ]
    }, {
        'resource_type': 'inventory.CloudService?provider=aws&cloud_service_group=EC2&cloud_service_type=AutoScalingGroup',
        'required_keys': [
            'reference.resource_id',
            'cloud_service_type',
            'data.desired_capacity',
            'data.min_size',
            'data.instances',
            'data.power_scheduler.original_desired_capacity',
            'data.power_scheduler.original_min_size'
        ]
    }
]

class ReferenceKeyModel(Model):
    resource_type = StringType(required=True, choices=_SUPPORTED_RESOURCE_TYPE)
    required_keys = ListType(StringType)


class PluginMetadata(Model):
    supported_resource_type = ListType(StringType, default=_SUPPORTED_RESOURCE_TYPE)
    reference_keys = ListType(ModelType(ReferenceKeyModel), default=_REFERENCE_KEYS)


class PluginInitResponse(Model):
    _metadata = ModelType(PluginMetadata, default=PluginMetadata, serialized_name='metadata')
