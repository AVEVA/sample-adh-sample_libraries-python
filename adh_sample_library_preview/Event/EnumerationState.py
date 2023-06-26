from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState


class EnumerationState(object):

    def __init__(self, Name: str = None, GraphQLName: str = None, Code: int = None, State: LifeCycleState = None, Description: str = None):
        """
        :param str Name: 
        :param str GraphQLName: 
        :param int Code: 
        :param LifeCycleState State: 
        :param str Description: 
        """

        self.__Name = Name
        self.__GraphQLName = GraphQLName
        self.__Code = Code
        self.__State = State
        self.__Description = Description

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
    def Code(self) -> int:
        return self.__Code

    @Code.setter
    def Code(self, value: int):
        self.__Code = value

    @property
    def State(self) -> LifeCycleState:
        return self.__State

    @State.setter
    def State(self, value: LifeCycleState):
        self.__State = value

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

        if self.Name is not None:
            result['Name'] = self.Name

        if self.GraphQLName is not None:
            result['GraphQLName'] = self.GraphQLName

        if self.Code is not None:
            result['Code'] = self.Code

        if self.State is not None:
            result['State'] = self.State.value

        if self.Description is not None:
            result['Description'] = self.Description

        return result

    @staticmethod
    def from_json(content: dict[str, Any]) -> EnumerationState:
        result = EnumerationState()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'GraphQLName' in content:
            result.GraphQLName = content['GraphQLName']

        if 'Code' in content:
            result.Code = content['Code']

        if 'State' in content:
            result.State = LifeCycleState(content['State'])

        if 'Description' in content:
            result.Description = content['Description']

        return result