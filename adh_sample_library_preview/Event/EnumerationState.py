from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState


class EnumerationState(object):

    def __init__(self, name: str = None, graph_q_l_name: str = None, code: int = None, state: LifeCycleState = None, description: str = None):
        """
        :param str name: 
        :param str graph_q_l_name: 
        :param int code: 
        :param LifeCycleState state: 
        :param str description: 
        """

        self.__name = name
        self.__graph_q_l_name = graph_q_l_name
        self.__code = code
        self.__state = state
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def graph_q_l_name(self) -> str:
        return self.__graph_q_l_name

    @graph_q_l_name.setter
    def graph_q_l_name(self, value: str):
        self.__graph_q_l_name = value

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, value: int):
        self.__code = value

    @property
    def state(self) -> LifeCycleState:
        return self.__state

    @state.setter
    def state(self, value: LifeCycleState):
        self.__state = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        self.__description = value

    def to_json(self) -> str:
        return json.dumps(self.to_dictionary())

    def to_dictionary(self) -> dict[str, Any]:
        result = {}

        if self.name is not None:
            result['Name'] = self.name

        if self.graph_q_l_name is not None:
            result['GraphQLName'] = self.graph_q_l_name

        if self.code is not None:
            result['Code'] = self.code

        if self.state is not None:
            result['State'] = self.state.value

        if self.description is not None:
            result['Description'] = self.description

        return result

    @staticmethod
    def from_json(content: dict[str, Any]) -> EnumerationState:
        result = EnumerationState()

        if not content:
            return result

        if 'Name' in content:
            result.name = content['Name']

        if 'GraphQLName' in content:
            result.graph_q_l_name = content['GraphQLName']

        if 'Code' in content:
            result.code = content['Code']

        if 'State' in content:
            result.state = LifeCycleState(content['State'])

        if 'Description' in content:
            result.description = content['Description']

        return result