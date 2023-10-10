from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState
from .TypeProperty import TypeProperty


class EventGraphEventType(object):

    def __init__(self, properties: list[TypeProperty] = None, default_authorization_tag: str = None, name: str = None, graph_ql_name: str = None, version: int = None, id: str = None, state: LifeCycleState = None, created_date: str = None, modified_date: str = None, description: str = None):
        """
        :param list[TypeProperty] properties: 
        :param str default_authorization_tag: 
        :param str name: 
        :param str graph_ql_name: 
        :param int version: 
        :param str id: 
        :param LifeCycleState state: 
        :param str created_date: 
        :param str modified_date: 
        :param str description: 
        """

        self.__properties = properties
        self.__default_authorization_tag = default_authorization_tag
        self.__name = name
        self.__graph_ql_name = graph_ql_name
        self.__version = version
        self.__id = id
        self.__state = state
        self.__created_date = created_date
        self.__modified_date = modified_date
        self.__description = description

    @property
    def Properties(self) -> list[TypeProperty]:
        return self.__properties

    @Properties.setter
    def Properties(self, value: list[TypeProperty]):
        self.__properties = value

    @property
    def DefaultAuthorizationTag(self) -> str:
        return self.__default_authorization_tag

    @DefaultAuthorizationTag.setter
    def DefaultAuthorizationTag(self, value: str):
        self.__default_authorization_tag = value

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
    def Version(self) -> int:
        return self.__version

    @Version.setter
    def Version(self, value: int):
        self.__version = value

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def State(self) -> LifeCycleState:
        return self.__state

    @State.setter
    def State(self, value: LifeCycleState):
        self.__state = value

    @property
    def CreatedDate(self) -> str:
        return self.__created_date

    @CreatedDate.setter
    def CreatedDate(self, value: str):
        self.__created_date = value

    @property
    def ModifiedDate(self) -> str:
        return self.__modified_date

    @ModifiedDate.setter
    def ModifiedDate(self, value: str):
        self.__modified_date = value

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

        if self.Properties is not None:
            result['Properties'] = []
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        if self.DefaultAuthorizationTag is not None:
            result['DefaultAuthorizationTag'] = self.DefaultAuthorizationTag

        if self.Name is not None:
            result['Name'] = self.Name

        if self.GraphQLName is not None:
            result['GraphQLName'] = self.GraphQLName

        if self.Version is not None:
            result['Version'] = self.Version

        if self.Id is not None:
            result['Id'] = self.Id

        if self.State is not None:
            result['State'] = self.State.value

        if self.CreatedDate is not None:
            result['CreatedDate'] = self.CreatedDate

        if self.ModifiedDate is not None:
            result['ModifiedDate'] = self.ModifiedDate

        if self.Description is not None:
            result['Description'] = self.Description

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> EventGraphEventType:
        result = EventGraphEventType()

        if not content:
            return result

        if 'Properties' in content:
            values = content['Properties']
            if values is not None:
                result.Properties = []
                for value in values:
                    result.Properties.append(TypeProperty.fromJson(value))

        if 'DefaultAuthorizationTag' in content:
            result.DefaultAuthorizationTag = content['DefaultAuthorizationTag']

        if 'Name' in content:
            result.Name = content['Name']

        if 'GraphQLName' in content:
            result.GraphQLName = content['GraphQLName']

        if 'Version' in content:
            result.Version = content['Version']

        if 'Id' in content:
            result.Id = content['Id']

        if 'State' in content:
            result.State = LifeCycleState(content['State'])

        if 'CreatedDate' in content:
            result.CreatedDate = content['CreatedDate']

        if 'ModifiedDate' in content:
            result.ModifiedDate = content['ModifiedDate']

        if 'Description' in content:
            result.Description = content['Description']

        return result