﻿from __future__ import annotations
import json
from typing import Any



class CreateSignupInput(object):
    """
    The CreateSignupInput object.
    """

    def __init__(self, name: str = None, resource_type: Any = None, resource_ids: list[str] = None):
        """
        :param str name: Signup Name.
        :param Any resource_type: Resource type of the resource identifiers.
        :param list[str] resource_ids: Collection of resource identifiers.
        """

        self.__name = name
        self.__resource_type = resource_type
        self.__resource_ids = resource_ids

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def ResourceType(self) -> Any:
        return self.__resource_type

    @ResourceType.setter
    def ResourceType(self, value: Any):
        self.__resource_type = value

    @property
    def ResourceIds(self) -> list[str]:
        return self.__resource_ids

    @ResourceIds.setter
    def ResourceIds(self, value: list[str]):
        self.__resource_ids = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.Name is not None:
            result['Name'] = self.Name

        if self.ResourceType is not None:
            result['ResourceType'] = self.ResourceType

        if self.ResourceIds is not None:
            result['ResourceIds'] = []
            for value in self.ResourceIds:
                result['ResourceIds'].append(value)

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> CreateSignupInput:
        result = CreateSignupInput()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'ResourceType' in content:
            result.ResourceType = content['ResourceType']

        if 'ResourceIds' in content:
            values = content['ResourceIds']
            if values is not None:
                result.ResourceIds = []
                for value in values:
                    result.ResourceIds.append(value)

        return result