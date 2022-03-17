from __future__ import annotations
import json

from .AccessControlEntry import AccessControlEntry


class AccessControlList(object):
    """ADH access control list definition"""

    def __init__(self, role_trustee_access_control_entries: list[AccessControlEntry] = None):
        self.RoleTrusteeAccessControlEntries = role_trustee_access_control_entries

    @property
    def RoleTrusteeAccessControlEntries(self) -> list[AccessControlEntry]:
        return self.__role_trustee_access_control_entries

    @RoleTrusteeAccessControlEntries.setter
    def RoleTrusteeAccessControlEntries(self, value: list[AccessControlEntry]):
        self.__role_trustee_access_control_entries = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'RoleTrusteeAccessControlEntries': []}

        if self.RoleTrusteeAccessControlEntries is not None:
            for value in self.RoleTrusteeAccessControlEntries:
                result['RoleTrusteeAccessControlEntries'].append(
                    value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = AccessControlList()

        if not content:
            return result

        if 'RoleTrusteeAccessControlEntries' in content:
            entries = content['RoleTrusteeAccessControlEntries']
            if entries is not None and len(entries) > 0:
                result.RoleTrusteeAccessControlEntries = []
                for value in entries:
                    result.RoleTrusteeAccessControlEntries.append(
                        AccessControlEntry.fromJson(value))

        return result
