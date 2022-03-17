from __future__ import annotations
import json

from .BaseClient import BaseClient
from .Asset.AssetType import AssetType
from .Securable import Securable


class AssetTypes(Securable, object):
    """
    Client for interacting with ADH Asset Types
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Asset Types client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='AssetTypes')
        
        self.__base_client = client
        self.__setPathAndQueryTemplates()

    def getAssetTypeById(self, namespace_id: str, asset_type_id: str) -> AssetType:
        """
        Returns the specified asset type
        :param namespace_id: The namespace identifier
        :param asset_type_id: The asset type identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_type_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__asset_type_path.format(
            namespace_id=namespace_id, asset_type_id=self.__base_client.encode(asset_type_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get asset type, {asset_type_id}.')

        result = AssetType.fromJson(response.json())
        return result

    def getAssetTypes(self, namespace_id: str, skip: int = 0, count: int = 100) -> list[AssetType]:
        """
        Returns a list of asset types
        :param namespace_id: The namespace identifier
        :param skip: An optional parameter representing the zero-based offset of the first asset
        type to retrieve. If not specified, a default value of 0 is used.
        :param count: An optional parameter, between 1 and 1000 (inclusive), that represents the
        maximum number of retrieved asset types. If not specified, the default is 100.
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__asset_types_path.format(
            namespace_id=namespace_id), params={'skip': skip, 'count': count})
        self.__base_client.checkResponse(
            response, f'Failed to get asset types.')

        results = []
        for i in response.json():
            results.append(AssetType.fromJson(i))
        return results

    def getOrCreateAssetType(self, namespace_id: str, asset_type: AssetType) -> AssetType:
        """
        Create a new asset type with a specified Id
        If an asset type already exists with the same Id and definition, it will be returned instead
        :param namespace_id: The namespace identifier
        :param asset_type: An asset type object
        """
        if namespace_id is None:
            raise TypeError
        if asset_type is None or not isinstance(asset_type, AssetType):
            raise TypeError

        response = self.__base_client.request('post', self.__asset_type_path.format(
            namespace_id=namespace_id, asset_type_id=self.__base_client.encode(asset_type.Id)), data=asset_type.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create asset type, {asset_type.Id}.')

        result = AssetType.fromJson(response.json())
        return result

    def createAssetTypes(self, namespace_id: str, asset_types: list[AssetType]) -> list[AssetType]:
        """
        Creates multiple asset types in a single call
        :param namespace_id: The namespace identifier
        :param asset_types: A list of asset type objects
        """
        if namespace_id is None:
            raise TypeError
        if asset_types is None or not isinstance(asset_types, list):
            raise TypeError

        dictionary = []
        for value in asset_types:
            dictionary.append(value.toDictionary())
        response = self.__base_client.request('post', self.__asset_types_path.format(
            namespace_id=namespace_id), data=json.dumps(dictionary))
        self.__base_client.checkResponse(
            response, f'Failed to create asset types.')

        results = []
        for i in response.json():
            results.append(AssetType.fromJson(i))
        return results

    def createOrUpdateAssetType(self, namespace_id: str, asset_type: AssetType) -> AssetType:
        """
        Create or update an asset type with a specified Id
        :param namespace_id: The namespace identifier
        :param asset_type: An asset type object
        """
        if namespace_id is None:
            raise TypeError
        if asset_type is None or not isinstance(asset_type, AssetType):
            raise TypeError

        response = self.__base_client.request('put', self.__asset_type_path.format(
            namespace_id=namespace_id, asset_type_id=self.__base_client.encode(asset_type.Id)), data=asset_type.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create or update asset type, {asset_type.Id}.')

        result = AssetType.fromJson(response.json())
        return result

    def deleteAssetType(self, namespace_id: str, asset_type_id: str):
        """
        Delete an asset type with a specified Id
        :param namespace_id: The namespace identifier
        :param asset_type_id: The asset type identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_type_id is None:
            raise TypeError

        response = self.__base_client.request('delete', self.__asset_type_path.format(
            namespace_id=namespace_id, asset_type_id=self.__base_client.encode(asset_type_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete asset type, {asset_type_id}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path = self.__base_client.uri_API + '/Tenants/' + \
            self.__base_client.tenant + '/Namespaces/{namespace_id}'
        self.__asset_types_path = self.__base_path + '/AssetTypes'
        self.__asset_type_path = self.__asset_types_path + '/{asset_type_id}'
