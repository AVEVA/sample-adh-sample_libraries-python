from __future__ import annotations
import json

from .StatusDefinitionType import StatusDefinitionType
from .StatusMapping import StatusMapping


class StatusConfiguration(object):
    """ADH Asset Status Configuration definition"""

    def __init__(self, definition_type: StatusDefinitionType = None, definition: StatusMapping = None):
        """
        :param definition_type: required
        :param definition: required
        """
        self.DefinitionType = definition_type
        self.Definition = definition

    @property
    def DefinitionType(self) -> StatusDefinitionType:
        """
        required
        :return:
        """
        return self.__definition_type

    @DefinitionType.setter
    def DefinitionType(self, value: StatusDefinitionType):
        """"
        required
        :param value:
        :return:
        """
        self.__definition_type = value

    @property
    def Definition(self) -> StatusMapping:
        """
        required
        :return:
        """
        return self.__definition

    @Definition.setter
    def Definition(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__definition = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        return {'DefinitionType': self.DefinitionType.value, 'Definition': self.Definition.toDictionary()}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = StatusConfiguration()

        if not content:
            return result

        if 'DefinitionType' in content:
            result.DefinitionType = StatusDefinitionType[content['DefinitionType']]

        if 'Definition' in content:
            result.Definition = StatusMapping.fromJson(content['Definition'])

        return result
