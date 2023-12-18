from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any


from .EventState import EventState

interval_regex = re.compile(
    r'^(?P<days>\d+)?[.]?(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>(\d\d|\d\d[.]\d+))$'
)


@dataclass
class BaseEvent(object):
    Id: str = None
    Name: str = None
    Description: str = None
    StartTime: datetime = None
    EndTime: datetime = None
    Duration: timedelta = None
    State: EventState = None
    Asset: str = None
    CreatedDate: datetime = None
    ModifiedDate: datetime = None
    CreatedByUser: str = None
    ModifiedByUser: str = None
    AuthorizationTags: list[str] = None

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

        if self.StartTime is not None:
            result['startTime'] = datetime.isoformat(self.StartTime)

        if self.EndTime is not None:
            result['endTime'] = datetime.isoformat(self.EndTime)

        if self.Duration is not None:
            result['duration'] = (
                str(self.Duration)
                .replace(' 0:', ' 00:')
                .replace('days', 'day')
                .replace(' day, ', '.')
            )

        if self.State is not None:
            result['state'] = self.State.value

        if self.Asset is not None:
            result['asset'] = self.Asset

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

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> BaseEvent:
        result = BaseEvent()

        if not content:
            return result

        if 'id' in content:
            result.Id = content['id']

        if 'name' in content:
            result.Name = content['name']

        if 'description' in content:
            result.Description = content['description']

        if 'startTime' in content:
            result.StartTime = datetime.fromisoformat(content['startTime'])

        if 'endTime' in content and content['endTime']:
            result.EndTime = datetime.fromisoformat(content['endTime'])

        if 'duration' in content:
            groups = interval_regex.match(content['duration']).groupdict()
            time_delta_params = {k: (float(v) if v else 0) for k, v in groups.items()}
            result.Duration = timedelta(**time_delta_params)

        if 'state' in content:
            result.State = EventState(content['state'])

        if 'asset' in content:
            result.Asset = content['asset']

        if 'createdDate' in content:
            result.CreatedDate = datetime.fromisoformat(content['createdDate'])

        if 'modifiedDate' in content:
            result.ModifiedDate = datetime.fromisoformat(content['modifiedDate'])

        if 'createdByUser' in content:
            result.CreatedByUser = content['createdByUser']

        if 'modifiedByUser' in content:
            result.ModifiedByUser = content['modifiedByUser']

        if 'authorizationTags' in content:
            result.AuthorizationTags = content['authorizationTags']

        return result