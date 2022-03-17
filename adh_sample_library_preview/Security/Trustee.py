from __future__ import annotations
import json

from .TrusteeType import TrusteeType


class Trustee(object):
    """ADH trustee definition"""

    def __init__(self, type: TrusteeType = None, tenant_id: str = None, object_id: str = None):
        self.Type = type
        self.TenantId = tenant_id
        self.ObjectId = object_id

    @property
    def Type(self) -> TrusteeType:
        return self.__type

    @Type.setter
    def Type(self, value: TrusteeType):
        self.__type = value

    @property
    def TenantId(self) -> str:
        return self.__tenant_id

    @TenantId.setter
    def TenantId(self, value: str):
        self.__tenant_id = value

    @property
    def ObjectId(self) -> str:
        return self.__object_id

    @ObjectId.setter
    def ObjectId(self, value: str):
        self.__object_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Type': self.Type.value}

        if self.TenantId is not None:
            result['TenantId'] = self.TenantId

        if self.ObjectId is not None:
            result['ObjectId'] = self.ObjectId

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Trustee()

        if not content:
            return result

        if 'Type' in content:
          if (type(content['Type']) is str):
            result.Type = TrusteeType[content['Type']]
          else:
            result.Type = TrusteeType(content['Type'])

        if 'TenantId' in content:
            result.TenantId = content['TenantId']

        if 'ObjectId' in content:
            result.ObjectId = content['ObjectId']

        return result
