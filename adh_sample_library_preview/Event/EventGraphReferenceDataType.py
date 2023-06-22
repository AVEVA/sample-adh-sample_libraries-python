from __future__ import annotations
import json
from typing import Any

from .EventGraphReferenceDataCategory import EventGraphReferenceDataCategory
from .LifeCycleState import LifeCycleState
from .TypeProperty import TypeProperty


class EventGraphReferenceDataType(object):

    def __init__(self, category: EventGraphReferenceDataCategory = None, properties: list[TypeProperty] = None, default_authorization_tag: str = None, name: str = None, graph_q_l_name: str = None, version: int = None, id: str = None, state: LifeCycleState = None, created_date: str = None, modified_date: str = None, description: str = None):
        """
        :param EventGraphReferenceDataCategory category: 
        :param list[TypeProperty] properties: 
        :param str default_authorization_tag: 
        :param str name: 
        :param str graph_q_l_name: 
        :param int version: 
        :param str id: 
        :param LifeCycleState state: 
        :param str created_date: 
        :param str modified_date: 
        :param str description: 
        """

        self.__category = category
        self.__properties = properties
        self.__default_authorization_tag = default_authorization_tag
        self.__name = name
        self.__graph_q_l_name = graph_q_l_name
        self.__version = version
        self.__id = id
        self.__state = state
        self.__created_date = created_date
        self.__modified_date = modified_date
        self.__description = description

    @property
    def category(self) -> EventGraphReferenceDataCategory:
        return self.__category

    @category.setter
    def category(self, value: EventGraphReferenceDataCategory):
        self.__category = value

    @property
    def properties(self) -> list[TypeProperty]:
        return self.__properties

    @properties.setter
    def properties(self, value: list[TypeProperty]):
        self.__properties = value

    @property
    def default_authorization_tag(self) -> str:
        return self.__default_authorization_tag

    @default_authorization_tag.setter
    def default_authorization_tag(self, value: str):
        self.__default_authorization_tag = value

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

        if self.category is not None:
            result['Category'] = self.category.value

        if self.properties is not None:
            result['Properties'] = []
            for value in self.properties:
                result['Properties'].append(value.to_dictionary())

        if self.default_authorization_tag is not None:
            result['DefaultAuthorizationTag'] = self.default_authorization_tag

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
    def from_json(content: dict[str, Any]) -> EventGraphReferenceDataType:
        result = EventGraphReferenceDataType()

        if not content:
            return result

        if 'Category' in content:
            result.category = EventGraphReferenceDataCategory(content['Category'])

        if 'Properties' in content:
            values = content['Properties']
            if values is not None:
                result.properties = []
                for value in values:
                    result.properties.append(TypeProperty.from_json(value))

        if 'DefaultAuthorizationTag' in content:
            result.default_authorization_tag = content['DefaultAuthorizationTag']

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