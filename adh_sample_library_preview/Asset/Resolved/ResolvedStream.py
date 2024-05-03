from __future__ import annotations
import json

from .ResolvedProperty import ResolvedProperty


class ResolvedStream(object):
    def __init__(self, name: str = None, properties: list[ResolvedProperty] = None, streamId: str = None, streamReferenceName: str = None):
        self.Name = name
        self.Properties = properties
        self.StreamId = streamId
        self.StreamReferenceName = streamReferenceName

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

    @property
    def StreamId(self) -> str:
        return self.__streamId

    @StreamId.setter
    def StreamId(self, value: str):
        self.__streamId = value

    @property
    def StreamReferenceName(self) -> str:
        return self.__streamReferenceName

    @StreamReferenceName.setter
    def StreamReferenceName(self, value: str):
        self.__streamReferenceName = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Name': self.Name, 'Properties': [], 'StreamId': self.StreamId, 'StreamReferenceName': self.StreamReferenceName}

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
        
        if 'StreamId' in content:
            result.StreamId = content['StreamId']
        
        if 'StreamReferenceName' in content:
            result.StreamReferenceName = content['StreamReferenceName']

        return result
