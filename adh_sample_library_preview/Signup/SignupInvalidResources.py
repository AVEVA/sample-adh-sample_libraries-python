from __future__ import annotations
import json
from typing import Any


class SignupInvalidResources(object):
    """
    The SignupInvalidResources object.
    """

    def __init__(self, invalid_resources_to_remove: list[str] = None, failed_resource_ids: list[str] = None):
        """
        :param list[str] invalid_resources_to_remove: Invalid resources that could not be deleted.
        :param list[str] failed_resource_ids: Failed resources that could not be added or removed.
        """

        self.__invalid_resources_to_remove = invalid_resources_to_remove
        self.__failed_resource_ids = failed_resource_ids

    @property
    def InvalidResourcesToRemove(self) -> list[str]:
        return self.__invalid_resources_to_remove

    @InvalidResourcesToRemove.setter
    def InvalidResourcesToRemove(self, value: list[str]):
        self.__invalid_resources_to_remove = value

    @property
    def FailedResourceIds(self) -> list[str]:
        return self.__failed_resource_ids

    @FailedResourceIds.setter
    def FailedResourceIds(self, value: list[str]):
        self.__failed_resource_ids = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.InvalidResourcesToRemove is not None:
            result['invalidresourcestoRemove'] = []
            for value in self.InvalidResourcesToRemove:
                result['invalidresourcestoRemove'].append(value)

        if self.FailedResourceIds is not None:
            result['failedresourceIds'] = []
            for value in self.FailedResourceIds:
                result['failedresourceIds'].append(value)

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> SignupInvalidResources:
        result = SignupInvalidResources()

        if not content:
            return result

        if 'invalidresourcestoRemove' in content:
            values = content['invalidresourcestoRemove']
            if values is not None:
                result.InvalidResourcesToRemove = []
                for value in values:
                    result.InvalidResourcesToRemove.append(value)

        if 'failedresourceIds' in content:
            values = content['failedresourceIds']
            if values is not None:
                result.FailedResourceIds = []
                for value in values:
                    result.FailedResourceIds.append(value)

        return result
