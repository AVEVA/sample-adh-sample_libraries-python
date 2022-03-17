from __future__ import annotations
import json

from .RoleScope import RoleScope


class Role(object):
    """ADH role definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 role_scope: 'RoleScope' = None, tenant_id: str = None, community_id: str = None,
                 role_type_id: str = None):
        self.Id = id
        self.Name = name
        self.Description = description
        self.RoleScope = role_scope
        self.TenantId = tenant_id
        self.CommunityId = community_id
        self.RoleTypeId = role_type_id

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def RoleScope(self) -> 'RoleScope':
        return self.__role_scope

    @RoleScope.setter
    def RoleScope(self, value: 'RoleScope'):
        self.__role_scope = value

    @property
    def TenantId(self) -> str:
        return self.__tenant_id

    @TenantId.setter
    def TenantId(self, value: str):
        self.__tenant_id = value

    @property
    def CommunityId(self) -> str:
        return self.__community_id

    @CommunityId.setter
    def CommunityId(self, value: str):
        self.__community_id = value

    @property
    def RoleTypeId(self) -> str:
        return self.__role_type_id

    @RoleTypeId.setter
    def RoleTypeId(self, value: str):
        self.__role_type_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Id': self.Id, 'Name': self.Name,
                  'Description': self.Description, 'RoleScope': self.RoleScope.value}

        if self.TenantId is not None:
            result['TenantId'] = self.TenantId

        if self.CommunityId is not None:
            result['CommunityId'] = self.CommunityId

        if self.RoleTypeId is not None:
            result['RoleTypeId'] = self.RoleTypeId

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Role()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'RoleScope' in content:
            result.RoleScope = RoleScope(content['RoleScope'])

        if 'TenantId' in content:
            result.TenantId = content['TenantId']

        if 'CommunityId' in content:
            result.CommunityId = content['CommunityId']

        if 'RoleTypeId' in content:
            result.RoleTypeId = content['RoleTypeId']

        return result
