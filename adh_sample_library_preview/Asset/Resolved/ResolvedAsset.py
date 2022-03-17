from __future__ import annotations
import json

from ..MetadataItem import MetadataItem
from .ResolvedStatus import ResolvedStatus
from .ResolvedStream import ResolvedStream
from .UnresolvedStream import UnresolvedStream


class ResolvedAsset(object):
    def __init__(self, id: str = None, name: str = None, description: str = None,
                 asset_type_id: str = None, asset_type_name: str = None,
                 metadata: list[MetadataItem] = None, streams: list[ResolvedStream] = None,
                 unresolved_streams: list[UnresolvedStream] = None, status: ResolvedStatus = None):
        self.Id = id
        self.Name = name
        self.Description = description
        self.AssetTypeId = asset_type_id
        self.AssetTypeName = asset_type_name
        self.Metadata = metadata
        self.Streams = streams
        self.UnresolvedStreams = unresolved_streams
        self.Status = status

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def AssetTypeId(self) -> str:
        return self.__asset_type_id

    @AssetTypeId.setter
    def AssetTypeId(self, value: str):
        self.__asset_type_id = value

    @property
    def AssetTypeName(self) -> str:
        return self.__asset_type_name

    @AssetTypeName.setter
    def AssetTypeName(self, value: str):
        self.__asset_type_name = value

    @property
    def Metadata(self) -> list[MetadataItem]:
        return self.__metadata

    @Metadata.setter
    def Metadata(self, value: list[MetadataItem]):
        self.__metadata = value

    @property
    def Streams(self) -> list[ResolvedStream]:
        return self.__streams

    @Streams.setter
    def Streams(self, value: list[ResolvedStream]):
        self.__streams = value

    @property
    def UnresolvedStreams(self) -> list[UnresolvedStream]:
        return self.__unresolved_streams

    @UnresolvedStreams.setter
    def UnresolvedStreams(self, value: list[UnresolvedStream]):
        self.__unresolved_streams = value

    @property
    def Status(self) -> ResolvedStatus:
        return self.__status

    @Status.setter
    def Status(self, value: ResolvedStatus):
        self.__status = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Id': self.Id, 'Name': self.Name, 'Description': self.Description,
                  'AssetTypeId': self.AssetTypeId, 'AssetTypeName': self.AssetTypeName,
                  'Metadata': [], 'Streams': [], 'Status': self.Status.toDictionary()}

        if self.Metadata is not None:
            for value in self.Metadata:
                result['Metadata'].append(value.toDictionary())

        if self.Streams is not None:
            for value in self.Streams:
                result['Streams'].append(value.toDictionary())

        if self.UnresolvedStreams is not None:
            for value in self.UnresolvedStreams:
                result['UnresolvedStreams'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedAsset()

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

        if 'AssetTypeName' in content:
            result.AssetTypeName = content['AssetTypeName']

        if 'Metadata' in content:
            metadata = content['Metadata']
            if metadata is not None and len(metadata) > 0:
                result.Metadata = []
                for value in metadata:
                    result.Metadata.append(
                        MetadataItem.fromJson(value))

        if 'Streams' in content:
            streams = content['Streams']
            if streams is not None and len(streams) > 0:
                result.Streams = []
                for value in streams:
                    result.Streams.append(
                        ResolvedStream.fromJson(value))

        if 'UnresolvedStreams' in content:
            unresolved_streams = content['UnresolvedStreams']
            if unresolved_streams is not None and len(unresolved_streams) > 0:
                result.UnresolvedStreams = []
                for value in unresolved_streams:
                    result.UnresolvedStreams.append(
                        UnresolvedStream.fromJson(value))

        if 'Status' in content:
            result.Status = ResolvedStatus.fromJson(
                content['Status'])

        return result
