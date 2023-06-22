from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState
from .PropertyTypeCode import PropertyTypeCode
from .PropertyTypeFlags import PropertyTypeFlags


class TypeProperty(object):

    def __init__(self, property_type_code: PropertyTypeCode = None,
                 id: str = None, name: str = None, graph_q_l_name: str = None, flags: PropertyTypeFlags = None,
                 state: LifeCycleState = None, property_type_id: str = None, remote_reference_name: str = None,
                 description: str = None):
        """
        :param PropertyTypeCode property_type_code: 
        :param str id: 
        :param str name: 
        :param str graph_q_l_name: 
        :param PropertyTypeFlags flags: 
        :param LifeCycleState state: 
        :param str property_type_id: 
        :param str remote_reference_name: 
        :param str description: 
        """

        self.__property_type_code = property_type_code
        self.__id = id
        self.__name = name
        self.__graph_q_l_name = graph_q_l_name
        self.__flags = flags
        self.__state = state
        self.__property_type_id = property_type_id
        self.__remote_reference_name = remote_reference_name
        self.__description = description

    @property
    def property_type_code(self) -> PropertyTypeCode:
        return self.__property_type_code

    @property_type_code.setter
    def property_type_code(self, value: PropertyTypeCode):
        self.__property_type_code = value

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

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
    def flags(self) -> PropertyTypeFlags:
        return self.__flags

    @flags.setter
    def flags(self, value: PropertyTypeFlags):
        self.__flags = value

    @property
    def state(self) -> LifeCycleState:
        return self.__state

    @state.setter
    def state(self, value: LifeCycleState):
        self.__state = value

    @property
    def property_type_id(self) -> str:
        return self.__property_type_id

    @property_type_id.setter
    def property_type_id(self, value: str):
        self.__property_type_id = value

    @property
    def remote_reference_name(self) -> str:
        return self.__remote_reference_name

    @remote_reference_name.setter
    def remote_reference_name(self, value: str):
        self.__remote_reference_name = value

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

        if self.property_type_code is not None:
            result['PropertyTypeCode'] = self.property_type_code.value

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.graph_q_l_name is not None:
            result['GraphQLName'] = self.graph_q_l_name

        if self.flags is not None:
            result['Flags'] = self.flags.value

        if self.state is not None:
            result['State'] = self.state.value

        if self.property_type_id is not None:
            result['PropertyTypeId'] = self.property_type_id

        if self.remote_reference_name is not None:
            result['RemoteReferenceName'] = self.remote_reference_name

        if self.description is not None:
            result['Description'] = self.description

        return result

    @staticmethod
    def from_json(content: dict[str, Any]) -> TypeProperty:
        result = TypeProperty()

        if not content:
            return result

        if 'PropertyTypeCode' in content:
            result.property_type_code = PropertyTypeCode(
                content['PropertyTypeCode'])

        if 'Id' in content:
            result.id = content['Id']

        if 'Name' in content:
            result.name = content['Name']

        if 'GraphQLName' in content:
            result.graph_q_l_name = content['GraphQLName']

        if 'Flags' in content:
            result.flags = PropertyTypeFlags(content['Flags'])

        if 'State' in content:
            result.state = LifeCycleState(content['State'])

        if 'PropertyTypeId' in content:
            result.property_type_id = content['PropertyTypeId']

        if 'RemoteReferenceName' in content:
            result.remote_reference_name = content['RemoteReferenceName']

        if 'Description' in content:
            result.description = content['Description']

        return result
