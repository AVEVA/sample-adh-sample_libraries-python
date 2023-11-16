from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState


class EnumerationState(object):

    def __init__(self, name: str = None, graph_ql_name: str = None, code: int = None, state: LifeCycleState = None, description: str = None):
        """
        :param str name: 
        :param str graph_ql_name: 
        :param int code: 
        :param LifeCycleState state: 
        :param str description: 
        """

        self.__name = name
        self.__graph_ql_name = graph_ql_name
        self.__code = code
        self.__state = state
        self.__description = description

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
    def Code(self) -> int:
        return self.__code

    @Code.setter
    def Code(self, value: int):
        self.__code = value

    @property
    def State(self) -> LifeCycleState:
        return self.__state

    @State.setter
    def State(self, value: LifeCycleState):
        self.__state = value

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
    def fromJson(content: dict[str, Any]) -> EnumerationState:
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