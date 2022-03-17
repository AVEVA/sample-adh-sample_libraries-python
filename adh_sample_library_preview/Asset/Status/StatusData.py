from __future__ import annotations
import json
from typing import Any

from .StatusEnum import StatusEnum


class StatusData(object):
    def __init__(self, asset_id: str = None, status: StatusEnum = None, value: Any = None,
                 display_name: str = None, data_retrieval_time: str = None):
        self.AssetId = asset_id
        self.Status = status
        self.Value = value
        self.DisplayName = display_name
        self.DataRetrievalTime = data_retrieval_time

    @property
    def AssetId(self) -> str:
        return self.__asset_id

    @AssetId.setter
    def AssetId(self, value: str):
        self.__asset_id = value

    @property
    def Status(self) -> StatusEnum:
        return self.__status

    @Status.setter
    def Status(self, value: StatusEnum):
        self.__status = value

    @property
    def Value(self) -> Any:
        return self.__value

    @Value.setter
    def Value(self, value: Any):
        self.__value = value

    @property
    def DisplayName(self) -> str:
        return self.__display_name

    @DisplayName.setter
    def DisplayName(self, value: str):
        self.__display_name = value

    @property
    def DataRetrievalTime(self) -> str:
        return self.__data_retrieval_time

    @DataRetrievalTime.setter
    def DataRetrievalTime(self, value: str):
        self.__data_retrieval_time = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'AssetId': self.AssetId, 'Status': self.Status.name, 'Value': self.Value,
                'DisplayName': self.DisplayName, 'DataRetrievalTime': self.DataRetrievalTime}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = StatusData()

        if not content:
            return result

        if 'AssetId' in content:
            result.AssetId = content['AssetId']

        if 'Status' in content:
            result.Status = StatusEnum[content['Status']]

        if 'Value' in content:
            result.Value = content['Value']

        if 'DisplayName' in content:
            result.DisplayName = content['DisplayName']

        if 'DataRetrievalTime' in content:
            result.DataRetrievalTime = content['DataRetrievalTime']

        return result
