from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState
from .PropertyTypeCode import PropertyTypeCode
from .PropertyTypeFlags import PropertyTypeFlags


class TypeProperty(object):

    def __init__(self, PropertyTypeCode: PropertyTypeCode = None, Id: str = None, Name: str = None, GraphQLName: str = None, Flags: PropertyTypeFlags = None, State: LifeCycleState = None, PropertyTypeId: str = None, RemoteReferenceName: str = None, Description: str = None):
        """
        :param PropertyTypeCode PropertyTypeCode: 
        :param str Id: 
        :param str Name: 
        :param str GraphQLName: 
        :param PropertyTypeFlags Flags: 
        :param LifeCycleState State: 
        :param str PropertyTypeId: 
        :param str RemoteReferenceName: 
        :param str Description: 
        """

        self.__PropertyTypeCode = PropertyTypeCode
        self.__Id = Id
        self.__Name = Name
        self.__GraphQLName = GraphQLName
        self.__Flags = Flags
        self.__State = State
        self.__PropertyTypeId = PropertyTypeId
        self.__RemoteReferenceName = RemoteReferenceName
        self.__Description = Description

    @property
    def PropertyTypeCode(self) -> PropertyTypeCode:
        return self.__PropertyTypeCode

    @PropertyTypeCode.setter
    def PropertyTypeCode(self, value: PropertyTypeCode):
        self.__PropertyTypeCode = value

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, value: str):
        self.__Id = value

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, value: str):
        self.__Name = value

    @property
    def GraphQLName(self) -> str:
        return self.__GraphQLName

    @GraphQLName.setter
    def GraphQLName(self, value: str):
        self.__GraphQLName = value

    @property
    def Flags(self) -> PropertyTypeFlags:
        return self.__Flags

    @Flags.setter
    def Flags(self, value: PropertyTypeFlags):
        self.__Flags = value

    @property
    def State(self) -> LifeCycleState:
        return self.__State

    @State.setter
    def State(self, value: LifeCycleState):
        self.__State = value

    @property
    def PropertyTypeId(self) -> str:
        return self.__PropertyTypeId

    @PropertyTypeId.setter
    def PropertyTypeId(self, value: str):
        self.__PropertyTypeId = value

    @property
    def RemoteReferenceName(self) -> str:
        return self.__RemoteReferenceName

    @RemoteReferenceName.setter
    def RemoteReferenceName(self, value: str):
        self.__RemoteReferenceName = value

    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, value: str):
        self.__Description = value

    def to_json(self) -> str:
        return json.dumps(self.to_dictionary())

    def to_dictionary(self) -> dict[str, Any]:
        result = {}

        if self.PropertyTypeCode is not None:
            result['PropertyTypeCode'] = self.PropertyTypeCode.value

        if self.Id is not None:
            result['Id'] = self.Id

        if self.Name is not None:
            result['Name'] = self.Name

        if self.GraphQLName is not None:
            result['GraphQLName'] = self.GraphQLName

        if self.Flags is not None:
            result['Flags'] = self.Flags.value

        if self.State is not None:
            result['State'] = self.State.value

        if self.PropertyTypeId is not None:
            result['PropertyTypeId'] = self.PropertyTypeId

        if self.RemoteReferenceName is not None:
            result['RemoteReferenceName'] = self.RemoteReferenceName

        if self.Description is not None:
            result['Description'] = self.Description

        return result

    @staticmethod
    def from_json(content: dict[str, Any]) -> TypeProperty:
        result = TypeProperty()

        if not content:
            return result

        if 'PropertyTypeCode' in content:
            result.PropertyTypeCode = PropertyTypeCode(content['PropertyTypeCode'])

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'GraphQLName' in content:
            result.GraphQLName = content['GraphQLName']

        if 'Flags' in content:
            result.Flags = PropertyTypeFlags(content['Flags'])

        if 'State' in content:
            result.State = LifeCycleState(content['State'])

        if 'PropertyTypeId' in content:
            result.PropertyTypeId = content['PropertyTypeId']

        if 'RemoteReferenceName' in content:
            result.RemoteReferenceName = content['RemoteReferenceName']

        if 'Description' in content:
            result.Description = content['Description']

        return result