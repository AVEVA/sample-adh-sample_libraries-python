from __future__ import annotations
import json

from .ResolvedProperty import ResolvedProperty


class ResolvedStream(object):
    def __init__(self, name: str = None, properties: list[ResolvedProperty] = None):
        self.Name = name
        self.Properties = properties

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Properties(self) -> list[ResolvedProperty]:
        return self.__properties

    @Properties.setter
    def Properties(self, value: list[ResolvedProperty]):
        self.__properties = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Name': self.Name, 'Properties': []}

        if self.Properties is not None:
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedStream()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Properties = []
                for value in properties:
                    result.Properties.append(
                        ResolvedProperty.fromJson(value))

        return result
