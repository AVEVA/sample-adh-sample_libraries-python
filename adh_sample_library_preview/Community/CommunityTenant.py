from __future__ import annotations
import json

from .CommunityTenantStatus import CommunityTenantStatus


class CommunityTenant(object):
    """ADH community tenant definition"""

    def __init__(
        self,
        id: str = None,
        name: str = None,
        status: CommunityTenantStatus = None,
        is_owner: bool = None,
        user_count: int = None,
        client_count: int = None,
        preferred_region_id: str = None,
        contact_email: str = None,
        community_alias: str = None,
    ):
        self.Id = id
        self.Name = name
        self.Status = status
        self.IsOwner = is_owner
        self.UserCount = user_count
        self.ClientCount = client_count
        self.PreferredRegionId = preferred_region_id
        self.ContactEmail = contact_email
        self.CommunityAlias = community_alias

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
    def Status(self) -> CommunityTenantStatus:
        return self.__status

    @Status.setter
    def Status(self, value: CommunityTenantStatus):
        self.__status = value

    @property
    def IsOwner(self) -> bool:
        return self.__is_owner

    @IsOwner.setter
    def IsOwner(self, value: bool):
        self.__is_owner = value

    @property
    def UserCount(self) -> int:
        return self.__user_count

    @UserCount.setter
    def UserCount(self, value: int):
        self.__user_count = value

    @property
    def ClientCount(self) -> int:
        return self.__client_count

    @ClientCount.setter
    def ClientCount(self, value: int):
        self.__client_count = value

    @property
    def PreferredRegionId(self) -> str:
        return self.__preferred_region_id

    @PreferredRegionId.setter
    def PreferredRegionId(self, value: str):
        self.__preferred_region_id = value

    @property
    def ContactEmail(self) -> str:
        return self.__contact_email

    @ContactEmail.setter
    def ContactEmail(self, value: str):
        self.__contact_email = value

    @property
    def CommunityAlias(self) -> str:
        return self.__community_alias

    @CommunityAlias.setter
    def CommunityAlias(self, value: str):
        self.__community_alias = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {
            'Id': self.Id,
            'Name': self.Name,
            'Status': self.Status.value,
            'IsOwner': self.IsOwner,
            'UserCount': self.UserCount,
            'ClientCount': self.ClientCount,
            'PreferredRegionId': self.PreferredRegionId,
            'ContactEmail': self.ContactEmail,
            'CommunityAlias': self.CommunityAlias,
        }

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = CommunityTenant()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Status' in content:
            result.Status = CommunityTenantStatus[content['Status']]

        if 'UserCount' in content:
            result.UserCount = content['UserCount']

        if 'ClientCount' in content:
            result.ClientCount = content['ClientCount']

        if 'PreferredRegionId' in content:
            result.PreferredRegionId = content['PreferredRegionId']

        if 'ContactEmail' in content:
            result.ContactEmail = content['ContactEmail']

        if 'CommunityAlias' in content:
            result.CommunityAlias = content['CommunityAlias']

        return result
