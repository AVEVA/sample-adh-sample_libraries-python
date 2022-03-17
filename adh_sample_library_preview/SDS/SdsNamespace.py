from __future__ import annotations
import json


class SdsNamespace(object):
    """
    definition of SdsNamespace
    """

    def __init__(self, id: str = None):
        self.Id = id

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    def toString(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Id': self.Id}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsNamespace()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        return result
