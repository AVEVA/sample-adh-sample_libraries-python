from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import isoparse
from typing import Any

from .EventState import EventState


@dataclass
class BaseReferenceData(object):
    Id: str = None
    Name: str = None
    Description: str = None
    State: EventState = None
    CreatedDate: datetime = None
    ModifiedDate: datetime = None
    CreatedByUser: str = None
    ModifiedByUser: str = None
    AuthorizationTags: list[str] = None
    SourceId: str = None
    ResourceId: str = None

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.Id is not None:
            result['id'] = self.Id

        if self.Name is not None:
            result['name'] = self.Name

        if self.Description is not None:
            result['description'] = self.Description

        if self.State is not None:
            result['state'] = self.State.value

        if self.CreatedDate is not None:
            result['createdDate'] = datetime.isoformat(self.CreatedDate)

        if self.ModifiedDate is not None:
            result['modifiedDate'] = datetime.isoformat(self.ModifiedDate)

        if self.CreatedByUser is not None:
            result['createdByUser'] = self.CreatedByUser

        if self.ModifiedByUser is not None:
            result['modifiedByUser'] = self.ModifiedByUser

        if self.AuthorizationTags is not None:
            result['authorizationTags'] = self.AuthorizationTags

        if self.SourceId is not None:
            result['sourceId'] = self.SourceId

        if self.ResourceId is not None:
            result['resourceId'] = self.ResourceId

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> BaseReferenceData:
        result = BaseReferenceData()

        if not content:
            return result

        if 'id' in content:
            result.Id = content['id']

        if 'name' in content:
            result.Name = content['name']

        if 'description' in content:
            result.Description = content['description']

        if 'state' in content:
            result.State = EventState(content['state'])

        if 'createdDate' in content:
            result.CreatedDate = isoparse(content['createdDate'])

        if 'modifiedDate' in content:
            result.ModifiedDate = isoparse(content['modifiedDate'])

        if 'createdByUser' in content:
            result.CreatedByUser = content['createdByUser']

        if 'modifiedByUser' in content:
            result.ModifiedByUser = content['modifiedByUser']

        if 'authorizationTags' in content:
            result.AuthorizationTags = content['authorizationTags']

        if 'sourceId' in content:
            result.SourceId = content['sourceId']

        if 'resourceId' in content:
            result.ResourceId = content['resourceId']

        return result
