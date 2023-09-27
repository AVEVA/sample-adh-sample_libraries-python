from __future__ import annotations
import json
from typing import Any

from .EnumerationState import EnumerationState
from .LifeCycleState import LifeCycleState


class EventGraphEnumeration(object):

    def __init__(self, members: list[EnumerationState] = None, name: str = None, graph_ql_name: str = None, version: int = None, id: str = None, state: LifeCycleState = None, created_date: str = None, modified_date: str = None, description: str = None):
        """
        :param list[EnumerationState] members: 
        :param str name: 
        :param str graph_ql_name: 
        :param int version: 
        :param str id: 
        :param LifeCycleState state: 
        :param str created_date: 
        :param str modified_date: 
        :param str description: 
        """

        self.__members = members
        self.__name = name
        self.__graph_ql_name = graph_ql_name
        self.__version = version
        self.__id = id
        self.__state = state
        self.__created_date = created_date
        self.__modified_date = modified_date
        self.__description = description

    @property
    def Members(self) -> list[EnumerationState]:
        return self.__members

    @Members.setter
    def Members(self, value: list[EnumerationState]):
        self.__members = value

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

        if self.Members is not None:
            result['Members'] = []
            for value in self.Members:
                result['Members'].append(value.toDictionary())

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
    def fromJson(content: dict[str, Any]) -> EventGraphEnumeration:
        result = EventGraphEnumeration()

        if not content:
            return result

        if 'Members' in content:
            values = content['Members']
            if values is not None:
                result.Members = []
                for value in values:
                    result.Members.append(EnumerationState.fromJson(value))

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