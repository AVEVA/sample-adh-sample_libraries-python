from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from dateutil.parser import isoparse
from typing import Any

from ..Asset import Asset
from .EventState import EventState

interval_regex = re.compile(
    r'^(?P<days>\d+)?[.]?(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>(\d\d|\d\d[.]\d+))$'
)


def _pascalToCamelCase(dictionary: dict[str, Any]):
    camel_case_dictionary = {}
    for k, v in dictionary.items():
        if isinstance(v, list):
            l = []
            for i in v:
                l.append(_pascalToCamelCase(i))
            camel_case_dictionary.update({k[:1].lower() + k[1:]: l})
        elif isinstance(v, dict):
            camel_case_dictionary.update({k[:1].lower() + k[1:]: _pascalToCamelCase(v)})
        else:
            camel_case_dictionary.update({k[:1].lower() + k[1:]: v})
    return camel_case_dictionary


def _camelToPascalCase(dictionary: dict[str, Any]):
    pascal_case_dictionary = {}
    for k, v in dictionary.items():
        if isinstance(v, list):
            l = []
            for i in v:
                l.append(_camelToPascalCase(i))
            pascal_case_dictionary.update({k[:1].upper() + k[1:]: l})
        elif isinstance(v, dict):
            pascal_case_dictionary.update(
                {k[:1].upper() + k[1:]: _camelToPascalCase(v)}
            )
        else:
            pascal_case_dictionary.update({k[:1].upper() + k[1:]: v})
    return pascal_case_dictionary


@dataclass
class BaseEvent(object):
    Id: str = None
    Name: str = None
    Description: str = None
    StartTime: datetime = None
    EndTime: datetime = None
    Duration: timedelta = None
    State: EventState = None
    Asset: Asset = None
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
            result['startTime'] = datetime.isoformat(
                self.StartTime.astimezone(tz=timezone.utc)
            ).replace('+00:00', 'Z')

        if self.EndTime is not None:
            result['endTime'] = datetime.isoformat(
                self.EndTime.astimezone(tz=timezone.utc)
            ).replace('+00:00', 'Z')

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
            result['asset'] = _pascalToCamelCase(self.Asset.toDictionary())

        if self.CreatedDate is not None:
            result['createdDate'] = datetime.isoformat(
                self.CreatedDate.astimezone(tz=timezone.utc)
            ).replace('+00:00', 'Z')

        if self.ModifiedDate is not None:
            result['modifiedDate'] = datetime.isoformat(
                self.ModifiedDate.astimezone(tz=timezone.utc)
            ).replace('+00:00', 'Z')

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
            result.StartTime = isoparse(content['startTime'])

        if 'endTime' in content and content['endTime']:
            result.EndTime = isoparse(content['endTime'])

        if 'duration' in content and content['duration']:
            groups = interval_regex.match(content['duration']).groupdict()
            time_delta_params = {k: (float(v) if v else 0) for k, v in groups.items()}
            result.Duration = timedelta(**time_delta_params)

        if 'state' in content:
            result.State = EventState(content['state'])

        if 'asset' in content and content['asset']:
            result.Asset = Asset.fromJson(_camelToPascalCase(content['asset']))

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

        return result
