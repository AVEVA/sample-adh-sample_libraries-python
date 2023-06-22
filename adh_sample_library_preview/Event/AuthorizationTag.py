﻿from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState


class AuthorizationTag(object):

    def __init__(self, id: str = None, state: LifeCycleState = None, created_date: str = None, modified_date: str = None, description: str = None):
        """
        :param str id: 
        :param LifeCycleState state: 
        :param str created_date: 
        :param str modified_date: 
        :param str description: 
        """

        self.__id = id
        self.__state = state
        self.__created_date = created_date
        self.__modified_date = modified_date
        self.__description = description

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
    def from_json(content: dict[str, Any]) -> AuthorizationTag:
        result = AuthorizationTag()

        if not content:
            return result

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