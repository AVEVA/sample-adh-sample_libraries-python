from __future__ import annotations

from .LifeCycleState import LifeCycleState
from .PropertyTypeCode import PropertyTypeCode
from .PropertyTypeFlags import PropertyTypeFlags
from .ReferenceDataType import ReferenceDataType
from .ReferenceDataCategory import ReferenceDataCategory
from .TypeProperty import TypeProperty


class BaseReferenceDataType(ReferenceDataType):
    """ADH Asset definition"""

    def __init__(self):
        """ """
        properties = [
            TypeProperty(
                PropertyTypeCode.String,
                'id',
                'id',
                'id',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='Unique identifier for the resource',
            ),
            TypeProperty(
                PropertyTypeCode.DateTime,
                'modifiedDate',
                'modifiedDate',
                'modifiedDate',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='When the resource was last modified',
            ),
            TypeProperty(
                PropertyTypeCode.DateTime,
                'createdDate',
                'createdDate',
                'createdDate',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='Timestamp of when the resource was created',
            ),
            TypeProperty(
                PropertyTypeCode.String,
                'createdByUser',
                'createdByUser',
                'createdByUser',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='Id of user/identity that created the resource',
            ),
            TypeProperty(
                PropertyTypeCode.String,
                'authorizationTags',
                'authorizationTags',
                'authorizationTags',
                PropertyTypeFlags.IsCollection,
                LifeCycleState.Active,
                description='Tags that are descriptive of the resource and are used when determining what roles should have access',
            ),
            TypeProperty(
                PropertyTypeCode.String,
                'name',
                'name',
                'name',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='User friendly name for the resource',
            ),
            TypeProperty(
                PropertyTypeCode.String,
                'description',
                'description',
                'description',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='Description of what the resource means',
            ),
        ]
        super().__init__(
            ReferenceDataCategory.ReferenceData,
            properties,
            'BaseAuthorizationTag',
            'BaseReferenceData',
            'BaseReferenceData',
            1,
            'BaseReferenceData',
            LifeCycleState.Active,
        )
