from __future__ import annotations
import json
from typing import Any


class UpdateSignupInput(object):
    """
    The UpdateSignupInput object.
    """

    def __init__(self, name: str = None):
        """
        :param str name: Signup name to be updated.
        """

        self.__name = name

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.Name is not None:
            result['name'] = self.Name

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> UpdateSignupInput:
        result = UpdateSignupInput()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['name']

        return result
