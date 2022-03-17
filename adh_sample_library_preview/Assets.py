from __future__ import annotations
import json

from .BaseClient import BaseClient
from .Asset.Data.DataResults import DataResults
from .Asset.Resolved.ResolvedAsset import ResolvedAsset
from .Asset.Status.StatusData import StatusData
from .Asset.Asset import Asset
from .Securable import Securable


class Assets(Securable, object):
    """
    Client for interacting with ADH Assets
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Assets client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='Assets')

        self.__base_client = client
        self.__setPathAndQueryTemplates()

    def getAssetById(self, namespace_id: str, asset_id: str) -> Asset:
        """
        Returns the specified asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__asset_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get asset, {asset_id}.')

        result = Asset.fromJson(response.json())
        return result

    def getAssets(self, namespace_id: str, query: str = '', skip: int = 0, count: int = 100,
                  ) -> list[Asset]:
        """
        Returns a list of assets
        :param namespace_id: The namespace identifier
        :param query: An optional query string to search for matching assets.
        :param skip: An optional parameter representing the zero-based offset of the first asset to
        retrieve. If not specified, a default value of 0 is used.
        :param count: An optional parameter, between 1 and 1000 (inclusive), that represents the
        maximum number of retrieved assets. If not specified, the default is 100.
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__assets_path.format(
            namespace_id=namespace_id), params={'skip': skip, 'count': count, 'query': query})
        self.__base_client.checkResponse(response, f'Failed to get assets.')

        results = []
        for i in response.json():
            results.append(Asset.fromJson(i))
        return results

    def getOrCreateAsset(self, namespace_id: str, asset: Asset) -> Asset:
        """
        Create a new asset with a specified Id
        If an asset already exists with the same Id and definition, it will be returned instead
        :param namespace_id: The namespace identifier
        :param asset: An asset object
        """
        if namespace_id is None:
            raise TypeError
        if asset is None or not isinstance(asset, Asset):
            raise TypeError

        response = self.__base_client.request('post', self.__asset_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset.Id)), data=asset.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create asset, {asset.Id}.')

        result = Asset.fromJson(response.json())
        return result

    def createAssets(self, namespace_id: str, assets: list[Asset]) -> list[Asset]:
        """
        Creates multiple assets in a single call
        :param namespace_id: The namespace identifier
        :param assets: An list of asset objects
        """
        if namespace_id is None:
            raise TypeError
        if assets is None or not isinstance(assets, list):
            raise TypeError

        dictionary = []
        for value in assets:
            dictionary.append(value.toDictionary())
        response = self.__base_client.request('post', self.__assets_path.format(
            namespace_id=namespace_id), data=json.dumps(dictionary))
        self.__base_client.checkResponse(response, f'Failed to create assets.')

        results = []
        for i in response.json():
            results.append(Asset.fromJson(i))
        return results

    def createOrUpdateAsset(self, namespace_id: str, asset: Asset) -> Asset:
        """
        Create or update an asset with a specified Id
        :param namespace_id: The namespace identifier
        :param asset: An asset object
        """
        if namespace_id is None:
            raise TypeError
        if asset is None or not isinstance(asset, Asset):
            raise TypeError

        response = self.__base_client.request('put', self.__asset_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset.Id)), data=asset.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create or update asset, {asset.Id}.')

        result = Asset.fromJson(response.json())
        return result

    def deleteAsset(self, namespace_id: str, asset_id: str):
        """
        Delete an asset with a specified Id
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError

        response = self.__base_client.request('delete', self.__asset_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete asset, {asset_id}.')

    def deleteAssets(self, namespace_id: str, asset_ids: list[str]):
        """
        Delete all assets with the specified Ids. Use this API to delete up to a maximum of 1000
        assets in one API call.
        :param namespace_id: The namespace identifier
        :param asset_ids: A list of asset identifiers
        """
        if namespace_id is None:
            raise TypeError
        if asset_ids is None or len(asset_ids) == 0:
            raise TypeError

        response = self.__base_client.request('delete', self.__bulk_delete_path.format(
            namespace_id=namespace_id), data=json.dumps(asset_ids))
        self.__base_client.checkResponse(response, f'Failed to delete assets.')

    def getResolvedAsset(self, namespace_id: str, asset_id: str) -> ResolvedAsset:
        """
        Returns the resolved asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__resolved_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get resolved asset, {asset_id}.')

        result = ResolvedAsset.fromJson(response.json())
        return result

    def getResolvedAssets(self, namespace_id: str, asset_ids: list[str]) -> list[ResolvedAsset]:
        """
        Returns bulk resolved assets
        :param namespace_id: The namespace identifier
        :param asset_ids: A list of asset identifiers
        """
        if namespace_id is None:
            raise TypeError
        if asset_ids is None or len(asset_ids) == 0:
            raise TypeError

        response = self.__base_client.request('post', self.__bulk_resolved_path.format(
            namespace_id=namespace_id), data=json.dumps(asset_ids))
        self.__base_client.checkResponse(
            response, f'Failed to get resolved assets.')

        results = []
        for i in response.json():
            results.append(ResolvedAsset.fromJson(i))
        return results

    def getAssetLastData(self, namespace_id: str, asset_id: str) -> DataResults:
        """
        Returns the last stored value for SDS streams in the resolved asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__last_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get last data for resolved asset, {asset_id}.')

        result = DataResults.fromJson(response.json())
        return result

    def getAssetSampledData(self, namespace_id: str, asset_id: str, start_index: str,
                            end_index: str, intervals: int) -> DataResults:
        """
        Returns sampled data for referenced SDS streams in the resolved asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        :param start_index: The start index for the intervals
        :param end_index: The end index for the intervals
        :param intervals: The number of requested intervals
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError
        if start_index is None:
            raise TypeError
        if end_index is None:
            raise TypeError
        if intervals is None:
            raise TypeError

        response = self.__base_client.request('get', self.__sampled_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id), start_index=start_index,
            end_index=end_index, intervals=intervals))
        self.__base_client.checkResponse(
            response, f'Failed to get sampled data for resolved asset, {asset_id}.')

        result = DataResults.fromJson(response.json())
        return result

    def getAssetSummaryData(self, namespace_id: str, asset_id: str, start_index: str,
                            end_index: str, count: int) -> DataResults:
        """
        Returns summary data for referenced SDS streams in the resolved asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        :param start_index: The start index for the intervals
        :param end_index: The end index for the intervals
        :param count: The number of requested intervals
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError
        if start_index is None:
            raise TypeError
        if end_index is None:
            raise TypeError
        if count is None:
            raise TypeError

        response = self.__base_client.request('get', self.__summaries_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id), start_index=start_index,
            end_index=end_index, count=count))
        self.__base_client.checkResponse(
            response, f'Failed to get summary data for resolved asset, {asset_id}.')

        result = DataResults.fromJson(response.json())
        return result

    def getAssetWindowData(self, namespace_id: str, asset_id: str, start_index: str,
                           end_index: str) -> DataResults:
        """
        Returns window data for referenced SDS streams in the resolved asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        :param start_index: The start index for the window
        :param end_index: The end index for the window
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError
        if start_index is None:
            raise TypeError
        if end_index is None:
            raise TypeError

        response = self.__base_client.request('get', self.__window_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id), start_index=start_index,
            end_index=end_index))
        self.__base_client.checkResponse(
            response, f'Failed to get window data for resolved asset, {asset_id}.')

        result = DataResults.fromJson(response.json())
        return result

    def getAssetInterpolatedData(self, namespace_id: str, asset_id: str, start_index: str,
                                 end_index: str, count: int) -> DataResults:
        """
        Returns interpolated data for referenced SDS streams in the resolved asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        :param start_index: The start index for the intervals
        :param end_index: The end index for the intervals
        :param count: The number of requested intervals
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError
        if start_index is None:
            raise TypeError
        if end_index is None:
            raise TypeError
        if count is None:
            raise TypeError

        response = self.__base_client.request('get', self.__interpolated_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id), start_index=start_index,
            end_index=end_index, count=count))
        self.__base_client.checkResponse(
            response, f'Failed to get interpolated data for resolved asset, {asset_id}.')

        result = DataResults.fromJson(response.json())
        return result

    def getAssetStatus(self, namespace_id: str, asset_id: str) -> StatusData:
        """
        Returns the current status of an asset
        :param namespace_id: The namespace identifier
        :param asset_id: The asset identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__status_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(asset_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get asset status, {asset_id}.')

        result = StatusData.fromJson(response.json())
        return result

    def getAssetStatuses(self, namespace_id: str, asset_ids: list[str]) -> list[StatusData]:
        """
        Returns the current status for multiple specified assets
        :param namespace_id: The namespace identifier
        :param asset_ids: A list of asset identifiers
        """
        if namespace_id is None:
            raise TypeError
        if asset_ids is None or len(asset_ids) == 0:
            raise TypeError

        response = self.__base_client.request('post', self.__bulk_status_path.format(
            namespace_id=namespace_id), data=json.dumps(asset_ids))
        self.__base_client.checkResponse(
            response, f'Failed to get asset statuses.')

        results = []
        for i in response.json():
            results.append(StatusData.fromJson(i))
        return results

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path = self.__base_client.uri_API + '/Tenants/' + \
            self.__base_client.tenant + '/Namespaces/{namespace_id}'
        self.__assets_path = self.__base_path + '/Assets'
        self.__bulk_path = self.__base_path + '/Bulk/Assets'
        self.__asset_path = self.__assets_path + '/{asset_id}'
        self.__bulk_delete_path = self.__bulk_path + '/Delete'
        self.__resolved_path = self.__asset_path + '/Resolved'
        self.__bulk_resolved_path = self.__bulk_path + '/Resolved'
        self.__data_path = self.__asset_path + '/Data'
        self.__last_path = self.__data_path + '/Last'
        self.__sampled_path = self.__data_path + \
            '/Sampled?startIndex={start_index}&endIndex={end_index}&intervals={intervals}'
        self.__summaries_path = self.__data_path + \
            '/Summaries?startIndex={start_index}&endIndex={end_index}&count={count}'
        self.__window_path = self.__data_path + \
            '?startIndex={start_index}&endIndex={end_index}'
        self.__interpolated_path = self.__data_path + \
            '/Interpolated?startIndex={start_index}&endIndex={end_index}&count={count}'
        self.__status_path = self.__asset_path + '/Status/Last'
        self.__bulk_status_path = self.__bulk_path + '/Status/Last'
