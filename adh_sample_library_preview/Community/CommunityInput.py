from __future__ import annotations
import json


class CommunityInput(object):
    """ADH community input definition"""

    def __init__(self, name: str = None, description: str = None):
        self.Name = name
        self.Description = description

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}

        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = CommunityInput()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        return result
