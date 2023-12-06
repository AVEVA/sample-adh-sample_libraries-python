from __future__ import annotations

from adh_sample_library_preview import Asset

from .EventType import EventType
from .TypeProperty import TypeProperty
from .PropertyTypeCode import PropertyTypeCode
from .PropertyTypeFlags import PropertyTypeFlags
from .LifeCycleState import LifeCycleState


class BaseEventType(EventType):
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
            TypeProperty(
                PropertyTypeCode.DateTime,
                'eventStartTime',
                'startTime',
                'startTime',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='Timestamp of when the event started',
            ),
            TypeProperty(
                PropertyTypeCode.DateTime,
                'eventEndTime',
                'endTime',
                'endTime',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='Timestamp of when the event ended',
            ),
            TypeProperty(
                PropertyTypeCode.TimeSpan,
                'eventDuration',
                'duration',
                'duration',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='Total duration of the event',
            ),
            TypeProperty(
                PropertyTypeCode.String,
                'eventType',
                'eventType',
                'eventType',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='A reference to another EventType that exists in the system',
            ),
            TypeProperty(
                PropertyTypeCode.Enumeration,
                'eventState',
                'state',
                'state',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                'state',
                description='Current state of the event',
            ),
            TypeProperty(
                PropertyTypeCode.Asset,
                'asset',
                'asset',
                'asset',
                PropertyTypeFlags.none,
                LifeCycleState.Active,
                description='The asset associated with the resource',
            ),
        ]
        super().__init__(
            properties,
            'BaseAuthorizationTag',
            'BaseEvent',
            'BaseEvent',
            1,
            'BaseEvent',
            LifeCycleState.Active,
        )
