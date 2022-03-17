from __future__ import annotations
import json
from typing import Any

from .DataErrors import DataErrors


class DataResults(object):
    def __init__(self, results: dict[str, list[Any]] = None, errors: DataErrors = None):
        self.Results = results
        self.Errors = errors

    @property
    def Results(self) -> dict[str, list[Any]]:
        return self.__results

    @Results.setter
    def Results(self, value: dict[str, list[Any]]):
        self.__results = value

    @property
    def Errors(self) -> DataErrors:
        return self.__errors

    @Errors.setter
    def Errors(self, value: DataErrors):
        self.__errors = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Results': self.Results}

        if self.Errors is not None:
            result['Errors'] = self.Errors.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataResults()

        if not content:
            return result

        if 'Results' in content:
            results = content['Results']
            if results is not None and len(results) > 0:
                result.Results = {}
                for key in results:
                    result.Results[key] = results[key]

        if 'Errors' in content:
            result.Errors = DataErrors.fromJson(content['Errors'])

        return result
