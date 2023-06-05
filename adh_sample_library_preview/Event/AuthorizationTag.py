from __future__ import annotations
import json

from .EventProperty import EventProperty


class AuthorizationTag(object):
    """ADH Asset definition"""

    def __init__(self, id: str = None, state: str = None, createdDate: str = None,
                 modifiedDate: str = None, description: str = None):
        """
        """
        self.Id = id
        self.State = state
        self.CreationDate = createdDate
        self.ModifiedDate = modifiedDate
        self.Description = description

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self.__id = value

    @property
    def State(self) -> str:
        """
        not required
        :return:
        """
        return self.__state

    @State.setter
    def State(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__state = value

    @property
    def CreationDate(self) -> str:
        """
        not required
        :return:
        """
        return self._creationDate

    @CreationDate.setter
    def CreationDate(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._creationDate = value

    @property
    def ModifiedDate(self) -> str:
        """
        not required
        :return:
        """
        return self.__modifiedDate

    @ModifiedDate.setter
    def ModifiedDate(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__modifiedDate = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self.__description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__description = value        

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id}

        # optional properties
        if self.State is not None:
            result['State'] = self.State

        if self.CreationDate is not None:
            result['CreationDate'] = self.CreationDate

        if self.ModifiedDate is not None:
            result['ModifiedDate'] = self.ModifiedDate

        if self.Description is not None:
            result['Description'] = self.Description            

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = AuthorizationTag()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'State' in content:
            result.State = content['State']

        if 'CreationDate' in content:
            result.CreationDate = content['CreationDate']

        if 'ModifiedDate' in content:
            result.ModifiedDate = content['ModifiedDate']

        if 'Description' in content:
            result.Description = content['Description']

        return result
