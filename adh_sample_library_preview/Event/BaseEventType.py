from __future__ import annotations

from .EventGraphEventType import EventGraphEventType
from .TypeProperty import TypeProperty
from .PropertyTypeCode import PropertyTypeCode
from .PropertyTypeFlags import PropertyTypeFlags
from .LifeCycleState import LifeCycleState


class BaseEvent(EventGraphEventType):
    """ADH Asset definition"""

    def __init__(self):
        """
        """
        properties = [
            TypeProperty(PropertyTypeCode.STRING, 'id', 'id', 'id',
                         PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.DATE_TIME, 'modifiedDate', 'modifiedDate',
                         'modifiedDate', PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.DATE_TIME, 'createdDate', 'createdDate',
                         'createdDate', PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.STRING, 'createdByUser', 'createdByUser',
                         'createdByUser', PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.DATE_TIME, 'eventStartTime', 'eventStartTime',
                         'eventStartTime', PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.DATE_TIME, 'eventEndTime', 'eventEndTime',
                         'eventEndTime', PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.TIME_SPAN, 'eventDuration', 'eventDuration',
                         'eventDuration', PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.STRING, 'eventType', 'eventType',
                         'eventType', PropertyTypeFlags.NONE, LifeCycleState.ACTIVE),
            TypeProperty(PropertyTypeCode.ENUMERATION, 'eventState', 'eventState', 'eventState',
                         PropertyTypeFlags.NONE, LifeCycleState.ACTIVE, 'EventState', 'EventState'),
            TypeProperty(PropertyTypeCode.STRING, 'authorizationTags', 'authorizationTags', 'authorizationTags',
                         PropertyTypeFlags.IS_COLLECTION, LifeCycleState.ACTIVE),
        ]
        super().__init__(properties, 'BaseAuthorizationTag', 'BaseEvent', 'BaseEvent', 2,
                         'BaseEvent', LifeCycleState.ACTIVE)
