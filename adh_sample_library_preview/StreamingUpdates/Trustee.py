from __future__ import annotations
import json
from typing import Any

from .TrusteeType import TrusteeType


class Trustee(object):

    def __init__(self, type: TrusteeType = None, object_id: str = None, __tenant_id: str = None):
        """
        :param TrusteeType type: 
        :param str object_id: 
        :param str __tenant_id: 
        """

        self.__type = type
        self.__object_id = object_id
        self.__tenant_id = __tenant_id

    @property
    def Type(self) -> TrusteeType:
        return self.__type

    @Type.setter
    def Type(self, value: TrusteeType):
        self.__type = value

    @property
    def ObjectId(self) -> str:
        return self.__object_id

    @ObjectId.setter
    def ObjectId(self, value: str):
        self.__object_id = value

    @property
    def TenantId(self) -> str:
        return self.__tenant_id

    @TenantId.setter
    def TenantId(self, value: str):
        self.__tenant_id = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.Type is not None:
            result['Type'] = self.Type.value

        if self.ObjectId is not None:
            result['ObjectId'] = self.ObjectId

        if self.TenantId is not None:
            result['TenantId'] = self.TenantId

        return result

    @staticmethod
    def from_json(content: dict[str, Any]) -> Trustee:
        result = Trustee()

        if not content:
            return result

        if 'Type' in content:
            result.Type = TrusteeType(content['Type'])

        if 'ObjectId' in content:
            result.ObjectId = content['ObjectId']

        if 'TenantId' in content:
            result.TenantId = content['TenantId']

        return result