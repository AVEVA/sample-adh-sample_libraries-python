from __future__ import annotations
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
    def fromJson(content: dict[str, Any]) -> AuthorizationTag:
        result = AuthorizationTag()

        if not content:
            return result

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