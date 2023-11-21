from __future__ import annotations
import json
from typing import Any

from .ResourceType import ResourceType
from .SignupState import SignupState


class Signup(object):
    """
    Represents a signup base model.
    """

    def __init__(self, id: str = None, bookmark: str = None ,name: str = None, owner: Any = None, community_id: str = None, type: Any = None, created_date: str = None, last_accessed_date: str = None, modified_date: str = None, expired_date: str = None, resources_deleted: bool = None, signup_state: Any = None):
        """
        :param str id: Signup Identifier.
        :param str name: Signup Name.
        :param Any owner: Signup Owner.
        :param str community_id: Community Identifier Associated with Signup.
        :param Any type: Signup Resource Type.
        :param str created_date: Date Signup was Created.
        :param str last_accessed_date: Date Signup was Last Accessed.
        :param str modified_date: Date Signup was Last Modified.
        :param str expired_date: Date Signup is set to expire.
        :param bool resources_deleted: Flag to indicate if all the partitions have successfully deleted the associated resources after expiring the signup.
        :param Any signup_state: Signup Status.
        """

        self.__id = id
        self.__bookmark = bookmark
        self.__name = name
        self.__owner = owner
        self.__community_id = community_id
        self.__type = type
        self.__created_date = created_date
        self.__last_accessed_date = last_accessed_date
        self.__modified_date = modified_date
        self.__expired_date = expired_date
        self.__resources_deleted = resources_deleted
        self.__signup_state = signup_state

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Bookmark(self) -> str:
        return self.__bookmark

    @Bookmark.setter
    def Bookmark(self, value: str):
        self.__bookmark = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Owner(self) -> Any:
        return self.__owner

    @Owner.setter
    def Owner(self, value: Any):
        self.__owner = value

    @property
    def CommunityId(self) -> str:
        return self.__community_id

    @CommunityId.setter
    def CommunityId(self, value: str):
        self.__community_id = value

    @property
    def Type(self) -> ResourceType:
        return self.__type

    @Type.setter
    def Type(self, value: ResourceType):
        self.__type = value

    @property
    def CreatedDate(self) -> str:
        return self.__created_date

    @CreatedDate.setter
    def CreatedDate(self, value: str):
        self.__created_date = value

    @property
    def LastAccessedDate(self) -> str:
        return self.__last_accessed_date

    @LastAccessedDate.setter
    def LastAccessedDate(self, value: str):
        self.__last_accessed_date = value

    @property
    def ModifiedDate(self) -> str:
        return self.__modified_date

    @ModifiedDate.setter
    def ModifiedDate(self, value: str):
        self.__modified_date = value

    @property
    def ExpiredDate(self) -> str:
        return self.__expired_date

    @ExpiredDate.setter
    def ExpiredDate(self, value: str):
        self.__expired_date = value

    @property
    def ResourcesDeleted(self) -> bool:
        return self.__resources_deleted

    @ResourcesDeleted.setter
    def ResourcesDeleted(self, value: bool):
        self.__resources_deleted = value

    @property
    def SignupState(self) -> SignupState:
        return self.__signup_state

    @SignupState.setter
    def SignupState(self, value: SignupState):
        self.__signup_state = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.Id is not None:
            result['Id'] = self.Id

        if self.Id is not None:
            result['Bookmark'] = self.Bookmark

        if self.Name is not None:
            result['Name'] = self.Name

        if self.Owner is not None:
            result['Owner'] = self.Owner

        if self.CommunityId is not None:
            result['CommunityId'] = self.CommunityId

        if self.Type is not None:
            result['Type'] = self.Type.name

        if self.CreatedDate is not None:
            result['CreatedDate'] = self.CreatedDate

        if self.LastAccessedDate is not None:
            result['LastAccessedDate'] = self.LastAccessedDate

        if self.ModifiedDate is not None:
            result['ModifiedDate'] = self.ModifiedDate

        if self.ExpiredDate is not None:
            result['ExpiredDate'] = self.ExpiredDate

        if self.ResourcesDeleted is not None:
            result['ResourcesDeleted'] = self.ResourcesDeleted

        if self.SignupState is not None:
            result['SignupState'] = self.SignupState.name

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> Signup:
        result = Signup()

        if not content:
            return result

        if 'Id'.casefold() in content:
            result.Id = content['Id'.casefold()]

        if 'Bookmark'.casefold() in content:
            result.Id = content['Bookmark'.casefold()]

        if 'Name'.casefold() in content:
            result.Name = content['Name'.casefold()]

        if 'Owner'.casefold() in content:
            result.Owner = content['Owner'.casefold()]

        if 'CommunityId'.casefold() in content:
            result.CommunityId = content['CommunityId'.casefold()]

        if 'Type'.casefold() in content:
            result.Type = ResourceType(content['Type'.casefold()])

        if 'CreatedDate'.casefold() in content:
            result.CreatedDate = content['CreatedDate'.casefold()]

        if 'LastAccessedDate'.casefold() in content:
            result.LastAccessedDate = content['LastAccessedDate'.casefold()]

        if 'ModifiedDate'.casefold() in content:
            result.ModifiedDate = content['ModifiedDate'.casefold()]

        if 'ExpiredDate'.casefold() in content:
            result.ExpiredDate = content['ExpiredDate'.casefold()]

        if 'ResourcesDeleted'.casefold() in content:
            result.ResourcesDeleted = content['ResourcesDeleted'].casefold()

        if 'SignupState'.casefold() in content:
            result.SignupState = SignupState(content['SignupState'.casefold()])

        return result
