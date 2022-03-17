from __future__ import annotations
import json
from typing import Any


class SdsResultPage(object):
    """
    definition of SdsResultPage
    """

    def __init__(self, results: list[Any] = None, continuation_token: str = None):
        self.Results = results
        self.ContinuationToken = continuation_token

    @property
    def Results(self) -> list[Any]:
        return self.__results

    @Results.setter
    def Results(self, value: list[Any]):
        self.__results = value

    @property
    def ContinuationToken(self) -> str:
        return self.__continuation_token

    @ContinuationToken.setter
    def ContinuationToken(self, value: str):
        self.__continuation_token = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Results': self.Results,
                  'ContinuationToken': self.ContinuationToken}

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsResultPage()

        if not content:
            return result

        if 'Results' in content:
            result.Results = content['Results']

        if 'ContinuationToken' in content:
            result.ContinuationToken = content['ContinuationToken']

        return result

    def end(self) -> bool:
        return self.ContinuationToken == None
