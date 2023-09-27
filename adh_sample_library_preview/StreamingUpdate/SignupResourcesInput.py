from __future__ import annotations
import json
from typing import Any



class SignupResourcesInput(object):
    """
    The SignupResourcesInput object.
    """

    def __init__(self, resources_to_add: list[str] = None, resources_to_remove: list[str] = None):
        """
        :param list[str] resources_to_add: Signup resources to be added.
        :param list[str] resources_to_remove: Signup resources to be removed.
        """

        self.__resources_to_add = resources_to_add
        self.__resources_to_remove = resources_to_remove

    @property
    def ResourcesToAdd(self) -> list[str]:
        return self.__resources_to_add

    @ResourcesToAdd.setter
    def ResourcesToAdd(self, value: list[str]):
        self.__resources_to_add = value

    @property
    def ResourcesToRemove(self) -> list[str]:
        return self.__resources_to_remove

    @ResourcesToRemove.setter
    def ResourcesToRemove(self, value: list[str]):
        self.__resources_to_remove = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.ResourcesToAdd is not None:
            result['ResourcesToAdd'] = []
            for value in self.ResourcesToAdd:
                result['ResourcesToAdd'].append(value)

        if self.ResourcesToRemove is not None:
            result['ResourcesToRemove'] = []
            for value in self.ResourcesToRemove:
                result['ResourcesToRemove'].append(value)

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> SignupResourcesInput:
        result = SignupResourcesInput()

        if not content:
            return result

        if 'ResourcesToAdd' in content:
            values = content['ResourcesToAdd']
            if values is not None:
                result.ResourcesToAdd = []
                for value in values:
                    result.ResourcesToAdd.append(value)

        if 'ResourcesToRemove' in content:
            values = content['ResourcesToRemove']
            if values is not None:
                result.ResourcesToRemove = []
                for value in values:
                    result.ResourcesToRemove.append(value)

        return result