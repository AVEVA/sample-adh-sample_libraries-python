from __future__ import annotations
import json
from typing import Any



class SignupResource(object):
    """
    A model that holds a signup resource
    """

    def __init__(self, resource_id: str = None, is_accessible: bool = None):
        """
        :param ResourceId[str]: Resource Identifier.
        :param IsAccessible[bool]: Boolean indicating if resource is accessible or inaccessible.
        """
        self.__resource_id = resource_id
        self.__is_accessible = is_accessible

    @property
    def ResourceId(self) -> str:
        return self.__resource_id

    @ResourceId.setter
    def ResourceId(self, value: str):
        self.__resource_id = value

    @property
    def IsAccessible(self) -> bool:
        return self.__is_accessible

    @IsAccessible.setter
    def IsAccessible(self, value: bool):
        self.__is_accessible = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.ResourceId is not None:
            result['resourceId'] = self.ResourceId

        if self.IsAccessible is not None:
            result['isAccessible'] = self.IsAccessible

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> SignupResource:
        result = SignupResource()

        if not content:
            return result

        if 'resourceId' in content:
            result.ResourceId = content['resourceId']

        if 'isAccessible' in content:
            result.IsAccessible = content['isAccessible']

        return result