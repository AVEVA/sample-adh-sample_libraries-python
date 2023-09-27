from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState
from .PropertyTypeCode import PropertyTypeCode
from .PropertyTypeFlags import PropertyTypeFlags


class TypeProperty(object):

    def __init__(self, property_type_code: PropertyTypeCode = None, id: str = None, name: str = None, graph_ql_name: str = None, flags: PropertyTypeFlags = None, state: LifeCycleState = None, property_type_id: str = None, remote_reference_name: str = None, description: str = None):
        """
        :param PropertyTypeCode property_type_code: 
        :param str id: 
        :param str name: 
        :param str graph_ql_name: 
        :param PropertyTypeFlags flags: 
        :param LifeCycleState state: 
        :param str property_type_id: 
        :param str remote_reference_name: 
        :param str description: 
        """

        self.__property_type_code = property_type_code
        self.__id = id
        self.__name = name
        self.__graph_ql_name = graph_ql_name
        self.__flags = flags
        self.__state = state
        self.__property_type_id = property_type_id
        self.__remote_reference_name = remote_reference_name
        self.__description = description

    @property
    def PropertyTypeCode(self) -> PropertyTypeCode:
        return self.__property_type_code

    @PropertyTypeCode.setter
    def PropertyTypeCode(self, value: PropertyTypeCode):
        self.__property_type_code = value

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
    def GraphQLName(self) -> str:
        return self.__graph_ql_name

    @GraphQLName.setter
    def GraphQLName(self, value: str):
        self.__graph_ql_name = value

    @property
    def Flags(self) -> PropertyTypeFlags:
        return self.__flags

    @Flags.setter
    def Flags(self, value: PropertyTypeFlags):
        self.__flags = value

    @property
    def State(self) -> LifeCycleState:
        return self.__state

    @State.setter
    def State(self, value: LifeCycleState):
        self.__state = value

    @property
    def PropertyTypeId(self) -> str:
        return self.__property_type_id

    @PropertyTypeId.setter
    def PropertyTypeId(self, value: str):
        self.__property_type_id = value

    @property
    def RemoteReferenceName(self) -> str:
        return self.__remote_reference_name

    @RemoteReferenceName.setter
    def RemoteReferenceName(self, value: str):
        self.__remote_reference_name = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
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
    def fromJson(content: dict[str, Any]) -> TypeProperty:
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