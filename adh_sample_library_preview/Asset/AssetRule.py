from __future__ import annotations
import json
import datetime


class AssetRule(object):
    """ADH Asset Rule definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                created_date: datetime = None, modified_date: datetime = None ):
        """
        :param id: required
        :param name: required
        :param description: not required
        :param created_date: not required
        :param modified_date: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.CreatedDate = created_date
        self.ModifiedDate = modified_date

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
    def Name(self) -> str:
        """
        required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__name = value

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

    @property
    def CreatedDate(self) -> datetime:
        """
        not required
        :return:
        """
        return self.__created_date

    @CreatedDate.setter
    def CreatedDate(self, value: datetime):
        """
        not required
        :param value:
        :return:
        """
        self.__created_date = value

    @property
    def ModifiedDate(self) -> datetime:
        """
        not required
        :return:
        """
        return self.__modified_date

    @ModifiedDate.setter
    def ModifiedDate(self, value: datetime):
        """
        not required
        :param value:
        :return:
        """
        self.__modified_date = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id, 'Name': self.Name}

        # optional properties
        if self.Description is not None:
            result['Description'] = self.Description

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = AssetRule()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'CreatedDate' in content:
            result.CreatedDate = content['CreatedDate']

        if 'ModifiedDate' in content:
            result.ModifiedDate = content['ModifiedDate']

        return result
