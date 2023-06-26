from __future__ import annotations
import json
from typing import Any

from .LifeCycleState import LifeCycleState


class AuthorizationTag(object):

    def __init__(self, Id: str = None, State: LifeCycleState = None, CreatedDate: str = None, ModifiedDate: str = None, Description: str = None):
        """
        :param str Id: 
        :param LifeCycleState State: 
        :param str CreatedDate: 
        :param str ModifiedDate: 
        :param str Description: 
        """

        self.__Id = Id
        self.__State = State
        self.__CreatedDate = CreatedDate
        self.__ModifiedDate = ModifiedDate
        self.__Description = Description

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
    def from_json(content: dict[str, Any]) -> AuthorizationTag:
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