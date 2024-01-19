from __future__ import annotations
import json
from typing import Any
from .SignupResource import SignupResource

class SignupResources(object):
    """
    A model that holds lists of resources retrieved from signup
    """

    def __init__(self, resources: list[SignupResource] = None):
        """
        :param Resources[SignupResource]: Collection of resources from a signup.
        """
        self.__resources = resources

    @property
    def Resources(self) -> list[SignupResource]:
        return self.__resources

    @Resources.setter
    def Resources(self, value: list[SignupResource]):
        self.__resources = value


    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}
        if self.Resources is not None:
            result['resources'] = []
            for resource in self.Resources:
                result['resources'].append(resource.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> SignupResources:
        result = SignupResources()

        if not content:
            return result

        if 'resources' in content:
            result.Resources = []
            for resource in content['resources']:
                result.Resources.append(SignupResource.fromJson(resource))

        return result