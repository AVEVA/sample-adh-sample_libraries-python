from __future__ import annotations
import json


class AssetLink(object):
    """ADH Asset definition"""

    def __init__(self, id: str = None, state: str = None, createdDate: str = None,
                 modifiedDate: str = None, description: str = None):
        """
        """
        self.Id = id

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

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id}       

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = AssetLink()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        return result
