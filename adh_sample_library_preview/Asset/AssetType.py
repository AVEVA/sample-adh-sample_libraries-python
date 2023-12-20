from __future__ import annotations
from datetime import datetime
from dateutil.parser import isoparse
import json

from .Status.StatusConfiguration import StatusConfiguration
from .MetadataItem import MetadataItem
from .TypeReference import TypeReference


class AssetType(object):
    """ADH Asset Type definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 metadata: MetadataItem = None,
                 type_references: list[TypeReference] = None,
                 status: StatusConfiguration = None,
                 created_date: datetime = None,
                 modified_date: datetime = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param metadata: not required
        :param type_references: not required
        :param status_mapping: not required
        :param created_date: not required
        :param modified_date: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.Metadata = metadata
        self.TypeReferences = type_references
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
    def TypeReferences(self) -> list[TypeReference]:
        """
        not required
        :return:
        """
        return self.__type_references

    @TypeReferences.setter
    def TypeReferences(self, value: list[TypeReference]):
        """
        not required
        :param value:
        :return:
        """
        self.__type_references = value

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

        if self.Metadata is not None:
            result['Metadata'] = []
            for value in self.Metadata:
                result['Metadata'].append(value.toDictionary())

        if self.TypeReferences is not None:
            result['TypeReferences'] = []
            for value in self.TypeReferences:
                result['TypeReferences'].append(value.toDictionary())

        if self.Status is not None:
            result['Status'] = self.Status.toDictionary()

        if self.CreatedDate is not None:
            result['CreatedDate'] = datetime.isoformat(self.CreatedDate)

        if self.ModifiedDate is not None:
            result['ModifiedDate'] = datetime.isoformat(self.ModifiedDate)

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = AssetType()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Metadata' in content:
            metadata = content['Metadata']
            if metadata is not None and len(metadata) > 0:
                result.Metadata = []
                for value in metadata:
                    result.Metadata.append(MetadataItem.fromJson(value))

        if 'TypeReferences' in content:
            type_references = content['TypeReferences']
            if type_references is not None and len(type_references) > 0:
                result.TypeReferences = []
                for value in type_references:
                    result.TypeReferences.append(
                        TypeReference.fromJson(value))

        if 'Status' in content:
            result.Status = StatusConfiguration.fromJson(content['Status'])

        if 'CreatedDate' in content:
            result.CreatedDate = isoparse(content['CreatedDate'])

        if 'ModifiedDate' in content:
            result.ModifiedDate = isoparse(content['ModifiedDate'])

        return result
