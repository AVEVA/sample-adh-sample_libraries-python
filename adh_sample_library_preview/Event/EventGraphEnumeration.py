from __future__ import annotations
import json
from typing import Any

from .EnumerationState import EnumerationState
from .LifeCycleState import LifeCycleState


class EventGraphEnumeration(object):

    def __init__(self, Members: list[EnumerationState] = None, Name: str = None, GraphQLName: str = None, Version: int = None, Id: str = None, State: LifeCycleState = None, CreatedDate: str = None, ModifiedDate: str = None, Description: str = None):
        """
        :param list[EnumerationState] Members: 
        :param str Name: 
        :param str GraphQLName: 
        :param int Version: 
        :param str Id: 
        :param LifeCycleState State: 
        :param str CreatedDate: 
        :param str ModifiedDate: 
        :param str Description: 
        """

        self.__Members = Members
        self.__Name = Name
        self.__GraphQLName = GraphQLName
        self.__Version = Version
        self.__Id = Id
        self.__State = State
        self.__CreatedDate = CreatedDate
        self.__ModifiedDate = ModifiedDate
        self.__Description = Description

    @property
    def Members(self) -> list[EnumerationState]:
        return self.__Members

    @Members.setter
    def Members(self, value: list[EnumerationState]):
        self.__Members = value

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
    def Version(self) -> int:
        return self.__Version

    @Version.setter
    def Version(self, value: int):
        self.__Version = value

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, value: str):
        self.__Id = value

    @property
    def State(self) -> LifeCycleState:
        return self.__State

    @State.setter
    def State(self, value: LifeCycleState):
        self.__State = value

    @property
    def CreatedDate(self) -> str:
        return self.__CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, value: str):
        self.__CreatedDate = value

    @property
    def ModifiedDate(self) -> str:
        return self.__ModifiedDate

    @ModifiedDate.setter
    def ModifiedDate(self, value: str):
        self.__ModifiedDate = value

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

        if self.Members is not None:
            result['Members'] = []
            for value in self.Members:
                result['Members'].append(value.to_dictionary())

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
    def from_json(content: dict[str, Any]) -> EventGraphEnumeration:
        result = EventGraphEnumeration()

        if not content:
            return result

        if 'Members' in content:
            values = content['Members']
            if values is not None:
                result.Members = []
                for value in values:
                    result.Members.append(EnumerationState.from_json(value))

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