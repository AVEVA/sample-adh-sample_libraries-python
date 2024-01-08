from __future__ import annotations
from datetime import datetime
from dateutil.parser import isoparse
import json

from .Status.StatusConfiguration import StatusConfiguration
from .MetadataItem import MetadataItem
from .StreamReference import StreamReference


class Asset(object):
    """ADH Asset definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 asset_type_id: str = None, metadata: list[MetadataItem] = None,
                 stream_references: list[StreamReference] = None,
                 status: StatusConfiguration = None,
                 created_date: datetime = None, modified_date: datetime = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param asset_type_id: not required
        :param metadata: not required
        :param stream_references: not required
        :param status: not required
        :param created_date: not required
        :param modified_date: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.AssetTypeId = asset_type_id
        self.Metadata = metadata
        self.StreamReferences = stream_references
        self.Status = status
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
        not required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        not required
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
    def AssetTypeId(self) -> str:
        """
        not required
        :return:
        """
        return self.__asset_type_id

    @AssetTypeId.setter
    def AssetTypeId(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__asset_type_id = value

    @property
    def Metadata(self) -> list[MetadataItem]:
        """
        not required
        :return:
        """
        return self.__metadata

    @Metadata.setter
    def Metadata(self, value: list[MetadataItem]):
        """
        not required
        :param value:
        :return:
        """
        self.__metadata = value

    @property
    def StreamReferences(self) -> list[StreamReference]:
        """
        not required
        :return:
        """
        return self.__stream_references

    @StreamReferences.setter
    def StreamReferences(self, value: list[StreamReference]):
        """
        not required
        :param value:
        :return:
        """
        self.__stream_references = value

    @property
    def Status(self) -> StatusConfiguration:
        """
        not required
        :return:
        """
        return self.__status

    @Status.setter
    def Status(self, value: StatusConfiguration):
        """
        not required
        :param value:
        :return:
        """
        self.__status = value

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
        result = {'Id': self.Id}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.AssetTypeId is not None:
            result['AssetTypeId'] = self.AssetTypeId

        if self.Metadata is not None:
            result['Metadata'] = []
            for value in self.Metadata:
                result['Metadata'].append(value.toDictionary())

        if self.StreamReferences is not None:
            result['StreamReferences'] = []
            for value in self.StreamReferences:
                result['StreamReferences'].append(
                    value.toDictionary())

        if self.Status is not None:
            result['Status'] = self.Status.toDictionary()

        if self.CreatedDate is not None:
            result['CreatedDate'] = datetime.isoformat(self.CreatedDate)

        if self.ModifiedDate is not None:
            result['ModifiedDate'] = datetime.isoformat(self.ModifiedDate)

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Asset()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'AssetTypeId' in content:
            result.AssetTypeId = content['AssetTypeId']

        if 'Metadata' in content:
            metadata = content['Metadata']
            if metadata is not None and len(metadata) > 0:
                result.Metadata = []
                for value in metadata:
                    result.Metadata.append(
                        MetadataItem.fromJson(value))

        if 'StreamReferences' in content:
            streamReferences = content['StreamReferences']
            if streamReferences is not None and len(streamReferences) > 0:
                result.StreamReferences = []
                for value in streamReferences:
                    result.StreamReferences.append(
                        StreamReference.fromJson(value))

        if 'Status' in content:
            result.Status = StatusConfiguration.fromJson(
                content['Status'])
        
        if 'CreatedDate' in content:
            result.CreatedDate = isoparse(content['CreatedDate'])

        if 'ModifiedDate' in content:
            result.ModifiedDate = isoparse(content['ModifiedDate'])

        return result
