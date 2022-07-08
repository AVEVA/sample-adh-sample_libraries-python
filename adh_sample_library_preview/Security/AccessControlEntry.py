from __future__ import annotations
from enum import IntEnum
import json

from .AccessType import AccessType
from .CommonAccessRightsEnum import CommonAccessRightsEnum
from .Trustee import Trustee


class AccessControlEntry(object):
    """ADH access control entry definition"""

    def __init__(self, trustee: 'Trustee' = None, access_type: 'AccessType' = None,
                 access_rights: CommonAccessRightsEnum = None):
        self.Trustee = trustee
        self.AccessType = access_type
        self.AccessRights = access_rights

    @property
    def Trustee(self) -> 'Trustee':
        return self.__trustee

    @Trustee.setter
    def Trustee(self, value: 'Trustee'):
        self.__trustee = value

    @property
    def AccessType(self) -> 'AccessType':
        return self.__access_type

    @AccessType.setter
    def AccessType(self, value: 'AccessType'):
        self.__access_type = value

    @property
    def AccessRights(self) -> CommonAccessRightsEnum:
        return self.__access_rights

    @AccessRights.setter
    def AccessRights(self, value: CommonAccessRightsEnum):
        self.__access_rights = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Trustee': self.Trustee.toDictionary(), 'AccessType': self.AccessType.value,
                'AccessRights': self.AccessRights.value}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = AccessControlEntry()

        if not content:
            return result

        if 'Trustee' in content:
            result.Trustee = Trustee.fromJson(content['Trustee'])

        if 'AccessType' in content:
            if type(content['AccessType']) == int:
                result.AccessType = AccessType(content['AccessType'])
            elif type(content['AccessType']) == str:
                result.AccessType = AccessType[content['AccessType']]
        else:
            result.AccessType = AccessType.Allowed

        if 'AccessRights' in content:
            result.AccessRights = CommonAccessRightsEnum(
                content['AccessRights'])
        else:
            result.AccessRights = CommonAccessRightsEnum.none

        return result
