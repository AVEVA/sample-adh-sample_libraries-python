from __future__ import annotations
from dataclasses import dataclass
import json
from typing import Any


@dataclass
class BaseEvent(object):
    CreatedByUser: str = None
    CreatedDate: str = None
    EventDuration: str = None
    EventEndTime: str = None
    EventStartTime: str = None
    EventState: str = None
    EventId: str = None
    EventModifiedByUser: str = None
    EventModifiedDate: str = None
    AuthorizationTags: list[str] = None

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.CreatedByUser is not None:
            result['createdByUser'] = self.CreatedByUser

        if self.CreatedDate is not None:
            result['createdDate'] = self.CreatedDate

        if self.EventDuration is not None:
            result['eventDuration'] = self.EventDuration

        if self.EventEndTime is not None:
            result['eventEndTime'] = self.EventEndTime

        if self.EventStartTime is not None:
            result['eventStartTime'] = self.EventStartTime

        if self.EventState is not None:
            result['eventState'] = self.EventState

        if self.EventId is not None:
            result['eventId'] = self.EventId

        if self.EventModifiedByUser is not None:
            result['eventModifiedByUser'] = self.EventModifiedByUser

        if self.EventModifiedDate is not None:
            result['eventModifiedDate'] = self.EventModifiedDate

        if self.AuthorizationTags is not None:
            result['authorizationTags'] = self.AuthorizationTags

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> BaseEvent:
        result = BaseEvent()

        if not content:
            return result

        if 'createdByUser' in content:
            result.CreatedByUser = content['createdByUser']

        if 'createdDate' in content:
            result.CreatedDate = content['createdDate']

        if 'eventDuration' in content:
            result.EventDuration = content['eventDuration']

        if 'eventEndTime' in content:
            result.EventEndTime = content['eventEndTime']

        if 'eventStartTime' in content:
            result.EventStartTime = content['eventStartTime']

        if 'eventState' in content:
            result.EventState = content['eventState']

        if 'eventId' in content:
            result.EventId = content['eventId']

        if 'eventModifiedByUser' in content:
            result.EventModifiedByUser = content['eventModifiedByUser']

        if 'eventModifiedDate' in content:
            result.EventModifiedDate = content['eventModifiedDate']

        if 'authorizationTags' in content:
            result.AuthorizationTags = content['authorizationTags']

        return result
