from __future__ import annotations
import json
from typing import Any

from .EnumerationState import EnumerationState
from .LifeCycleState import LifeCycleState


class EventGraphEnumeration(object):

    def __init__(self, members: list[EnumerationState] = None, name: str = None, graph_q_l_name: str = None, version: int = None, id: str = None, state: LifeCycleState = None, created_date: str = None, modified_date: str = None, description: str = None):
        """
        :param list[EnumerationState] members: 
        :param str name: 
        :param str graph_q_l_name: 
        :param int version: 
        :param str id: 
        :param LifeCycleState state: 
        :param str created_date: 
        :param str modified_date: 
        :param str description: 
        """

        self.__members = members
        self.__name = name
        self.__graph_q_l_name = graph_q_l_name
        self.__version = version
        self.__id = id
        self.__state = state
        self.__created_date = created_date
        self.__modified_date = modified_date
        self.__description = description

    @property
    def members(self) -> list[EnumerationState]:
        return self.__members

    @members.setter
    def members(self, value: list[EnumerationState]):
        self.__members = value

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
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, value: int):
        self.__version = value

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def state(self) -> LifeCycleState:
        return self.__state

    @state.setter
    def state(self, value: LifeCycleState):
        self.__state = value

    @property
    def created_date(self) -> str:
        return self.__created_date

    @created_date.setter
    def created_date(self, value: str):
        self.__created_date = value

    @property
    def modified_date(self) -> str:
        return self.__modified_date

    @modified_date.setter
    def modified_date(self, value: str):
        self.__modified_date = value

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

        if self.members is not None:
            result['Members'] = []
            for value in self.members:
                result['Members'].append(value.to_dictionary())

        if self.name is not None:
            result['Name'] = self.name

        if self.graph_q_l_name is not None:
            result['GraphQLName'] = self.graph_q_l_name

        if self.version is not None:
            result['Version'] = self.version

        if self.id is not None:
            result['Id'] = self.id

        if self.state is not None:
            result['State'] = self.state.value

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date

        if self.description is not None:
            result['Description'] = self.description

        return result

    @staticmethod
    def from_json(content: dict[str, Any]) -> EventGraphEnumeration:
        result = EventGraphEnumeration()

        if not content:
            return result

        if 'Members' in content:
            values = content['Members']
            if values is not None:
                result.members = []
                for value in values:
                    result.members.append(EnumerationState.from_json(value))

        if 'Name' in content:
            result.name = content['Name']

        if 'GraphQLName' in content:
            result.graph_q_l_name = content['GraphQLName']

        if 'Version' in content:
            result.version = content['Version']

        if 'Id' in content:
            result.id = content['Id']

        if 'State' in content:
            result.state = LifeCycleState(content['State'])

        if 'CreatedDate' in content:
            result.created_date = content['CreatedDate']

        if 'ModifiedDate' in content:
            result.modified_date = content['ModifiedDate']

        if 'Description' in content:
            result.description = content['Description']

        return result