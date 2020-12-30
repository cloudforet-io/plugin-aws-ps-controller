from schematics.models import Model
from schematics.types import ListType, DictType, StringType
from schematics.types.compound import ModelType

__all__ = ['PluginInitResponse']

_SUPPORTED_RESOURCE_TYPE = [
    'inventory.Server',
    'inventory.CloudService'
]

_REFERENCE_KEYS = [
    {
        'resource_type': 'inventory.Server',
        'required_keys': [
            'collection_info.secrets',
            'region_code',
            'reference.resource_id',
            'provider',
            'cloud_service_type',
            'data.power_state'
        ]
    }, {
        'resource_type': 'inventory.CloudService',
        'required_keys': [
            'region_code',
            'collection_info.secrets',
            'reference.resource_id',
            'cloud_service_type',
            'cloud_service_group',
            'provider',
            'cloud_service_id',
            'data.auto_scaling_group_name',
            'data.db_identifier',
            'data.role',
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
