from __future__ import annotations
import json


class ResolvedStatus(object):
    def __init__(self, name: str = None, stream_name: str = None, stream_property_id: str = None):
        self.Name = name
        self.StreamName = stream_name
        self.StreamPropertyId = stream_property_id

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def StreamName(self) -> str:
        return self.__stream_name

    @StreamName.setter
    def StreamName(self, value: str):
        self.__stream_name = value

    @property
    def StreamPropertyId(self) -> str:
        return self.__stream_property_id

    @StreamPropertyId.setter
    def StreamPropertyId(self, value: str):
        self.__stream_property_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Name': self.Name, 'StreamName': self.StreamName,
                'StreamPropertyId': self.StreamPropertyId}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedStatus()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'StreamName' in content:
            result.StreamName = content['StreamName']

        if 'StreamPropertyId' in content:
            result.StreamPropertyId = content['StreamPropertyId']

        return result
