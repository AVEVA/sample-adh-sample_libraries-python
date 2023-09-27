from __future__ import annotations
import json
from typing import Any



class SignupResourceIds(object):
    """
    A model that holds lists of accessible and inaccessible recources retrieved from memory.
    """

    def __init__(self, accessible_resources: list[str] = None, inaccessible_resources: list[str] = None):
        """
        :param list[str] accessible_resources: Public accessor for accessible resources list
        :param list[str] inaccessible_resources: Public accessor for inaccessible resources list
        """

        self.__accessible_resources = accessible_resources
        self.__inaccessible_resources = inaccessible_resources

    @property
    def AccessibleResources(self) -> list[str]:
        return self.__accessible_resources

    @AccessibleResources.setter
    def AccessibleResources(self, value: list[str]):
        self.__accessible_resources = value

    @property
    def InaccessibleResources(self) -> list[str]:
        return self.__inaccessible_resources

    @InaccessibleResources.setter
    def InaccessibleResources(self, value: list[str]):
        self.__inaccessible_resources = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.AccessibleResources is not None:
            result['AccessibleResources'] = []
            for value in self.AccessibleResources:
                result['AccessibleResources'].append(value)

        if self.InaccessibleResources is not None:
            result['InaccessibleResources'] = []
            for value in self.InaccessibleResources:
                result['InaccessibleResources'].append(value)

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> SignupResourceIds:
        result = SignupResourceIds()

        if not content:
            return result

        if 'AccessibleResources' in content:
            values = content['AccessibleResources']
            if values is not None:
                result.AccessibleResources = []
                for value in values:
                    result.AccessibleResources.append(value)

        if 'InaccessibleResources' in content:
            values = content['InaccessibleResources']
            if values is not None:
                result.InaccessibleResources = []
                for value in values:
                    result.InaccessibleResources.append(value)

        return result