from __future__ import annotations
import json


class ResolvedSource(object):
    def __init__(self, stream_id: str = None, property_id: str = None):
        self.StreamId = stream_id
        self.PropertyId = property_id

    @property
    def StreamId(self) -> str:
        return self.__stream_id

    @StreamId.setter
    def StreamId(self, value: str):
        self.__stream_id = value

    @property
    def PropertyId(self) -> str:
        return self.__property_id

    @PropertyId.setter
    def PropertyId(self, value: str):
        self.__property_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'StreamId': self.StreamId, 'PropertyId': self.PropertyId}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedSource()

        if not content:
            return result

        if 'StreamId' in content:
            result.StreamId = content['StreamId']

        if 'PropertyId' in content:
            result.PropertyId = content['PropertyId']

        return result
