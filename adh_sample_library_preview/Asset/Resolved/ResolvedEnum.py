from __future__ import annotations
import json
from typing import Any


class ResolvedEnum(object):
    def __init__(self, id: str = None, value: Any = None):
        self.Id = id
        self.Value = value

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Value(self) -> Any:
        return self.__value

    @Value.setter
    def Value(self, value: Any):
        self.__value = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Id': self.Id, 'Value': self.Value}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedEnum()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Value' in content:
            result.Value = content['Value']

        return result
