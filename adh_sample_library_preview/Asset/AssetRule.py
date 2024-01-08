from __future__ import annotations
from datetime import datetime
from dateutil.parser import isoparse
import json


class AssetRule(object):
    """ADH Asset Rule definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                creation_time: datetime = None, modified_time: datetime = None ):
        """
        :param id: required
        :param name: required
        :param description: not required
        :param creation_time: not required
        :param modified_time: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.CreationTime = creation_time
        self.ModifiedTime = modified_time

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
    def CreationTime(self) -> datetime:
        """
        not required
        :return:
        """
        return self.__creation_time

    @CreationTime.setter
    def CreationTime(self, value: datetime):
        """
        not required
        :param value:
        :return:
        """
        self.__creation_time = value

    @property
    def ModifiedTime(self) -> datetime:
        """
        not required
        :return:
        """
        return self.__modified_time

    @ModifiedTime.setter
    def ModifiedTime(self, value: datetime):
        """
        not required
        :param value:
        :return:
        """
        self.__modified_time = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id, 'Name': self.Name}

        # optional properties
        if self.Description is not None:
            result['Description'] = self.Description

        if self.CreationTime is not None:
            result['CreationTime'] = datetime.isoformat(self.CreationTime)

        if self.ModifiedTime is not None:
            result['ModifiedTime'] = datetime.isoformat(self.ModifiedTime)

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

        if 'CreationTime' in content:
            result.CreationTime = isoparse(content['CreationTime'])

        if 'ModifiedTime' in content:
            result.ModifiedTime = isoparse(content['ModifiedTime'])

        return result
