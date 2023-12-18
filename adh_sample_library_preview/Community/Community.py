from __future__ import annotations
import json

from .CommunityTenant import CommunityTenant
from ..Security import Role


class Community(object):
    """ADH community definition"""

    def __init__(
        self,
        id: str = None,
        member_role_id: str = None,
        name: str = None,
        display_name: str = None,
        description: str = None,
        tenants: list[CommunityTenant] = None,
        date_created: str = None,
        preferred_region_id: str = None,
        community_roles: list[Role] = None,
    ):
        self.Id = id
        self.MemberRoleId = member_role_id
        self.Name = name
        self.DisplayName = display_name
        self.Description = description
        self.Tenants = tenants
        self.DateCreated = date_created
        self.PreferredRegionId = preferred_region_id
        self.CommunityRoles = community_roles

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def MemberRoleId(self) -> str:
        return self.__member_role_id

    @MemberRoleId.setter
    def MemberRoleId(self, value: str):
        self.__member_role_id = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def DisplayName(self) -> str:
        return self.__display_name

    @DisplayName.setter
    def DisplayName(self, value: str):
        self.__display_name = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def Tenants(self) -> list[CommunityTenant]:
        return self.__tenants

    @Tenants.setter
    def Tenants(self, value: list[CommunityTenant]):
        self.__tenants = value

    @property
    def DateCreated(self) -> str:
        return self.__date_created

    @DateCreated.setter
    def DateCreated(self, value: str):
        self.__date_created = value

    @property
    def PreferredRegionId(self) -> str:
        return self.__preferred_region_id

    @PreferredRegionId.setter
    def PreferredRegionId(self, value: str):
        self.__preferred_region_id = value

    @property
    def CommunityRoles(self) -> list[Role]:
        return self.__community_roles

    @CommunityRoles.setter
    def CommunityRoles(self, value: list[Role]):
        self.__community_roles = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {
            'Id': self.Id,
            'MemberRoleId': self.MemberRoleId,
            'Name': self.Name,
            'DisplayName': self.DisplayName,
            'Description': self.Description,
            'Tenants': [],
            'DateCreated': self.DateCreated,
            'PreferredRegionId': self.PreferredRegionId,
            'CommunityRoles': [],
        }

        if self.Tenants is not None:
            for value in self.Tenants:
                result['Tenants'].append(value.toDictionary())

        if self.CommunityRoles is not None:
            for value in self.CommunityRoles:
                result['CommunityRoles'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Community()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'MemberRoleId' in content:
            result.MemberRoleId = content['MemberRoleId']

        if 'Name' in content:
            result.Name = content['Name']

        if 'DisplayName' in content:
            result.DisplayName = content['DisplayName']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Tenants' in content:
            tenants = content['Tenants']
            if tenants is not None and len(tenants) > 0:
                result.Tenants = []
                for value in tenants:
                    result.Tenants.append(CommunityTenant.fromJson(value))

        if 'DateCreated' in content:
            result.DateCreated = content['DateCreated']

        if 'PreferredRegionId' in content:
            result.PreferredRegionId = content['PreferredRegionId']

        if 'CommunityRoles' in content:
            community_roles = content['CommunityRoles']
            if community_roles is not None and len(community_roles) > 0:
                result.CommunityRoles = []
                for value in community_roles:
                    result.CommunityRoles.append(Role.fromJson(value))

        return result
