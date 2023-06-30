from __future__ import annotations
from typing import Any
import json

from .BaseClient import BaseClient
from .ContentResolvers import DataContent
from .Securable import Securable


class ReferenceData(Securable, object):

    def __init__(self, client: BaseClient):
        super().__init__(client=client, collection='ReferenceData')

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getReferenceData(self, namespace_id: str, reference_data_type_id: str, id: str = None, fields: str = None,
                  filter: str = None, order_by: str = None, count: int = None, continuation_token: str = None,
                  reference_data_class: type = None) -> list[Any]:
        """
        """

        self.__base_client.validateParameters(namespace_id, reference_data_type_id)

        params = {}
        params['typeId'] = self.__base_client.encode(reference_data_type_id)
        if id is not None:
            params['id'] = id
        if fields is not None:
            params['count'] = count
        if filter is not None:
            params['filter'] = filter
        if order_by is not None:
            params['orderBy'] = order_by
        if count is not None:
            params['count'] = count
        if continuation_token is not None:
            params['continuationToken'] = continuation_token

        response = self.__base_client.request('get', self.__reference_data_path.format(
            namespace_id=namespace_id), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to get reference_data, {reference_data_type_id}.')

        return DataContent(response=response, value_class=reference_data_class).resolve()

    def getOrCreateReferenceData(self, namespace_id: str, reference_data_type_id: str, reference_data: list[Any], reference_data_class: type = None) -> list[Any]:
        """
        """
        self.__base_client.validateParameters(
            namespace_id, reference_data_type_id, reference_data)

        params = {}
        params['typeId'] = self.__base_client.encode(reference_data_type_id)

        if callable(getattr(reference_data[0], 'toJson', None)):
            reference_data = []
            for reference_data in reference_data:
                reference_data.append(reference_data.toDictionary())
            payload = json.dumps(reference_data)
        else:
            payload = reference_data

        response = self.__base_client.request('post', self.__reference_data_path.format(
            namespace_id=namespace_id), data=payload, params=params)
        self.__base_client.checkResponse(
            response, f'Failed to create reference_data, {reference_data_type_id}.')

        return DataContent(response=response, value_class=reference_data_class).resolve()

    def deleteReferenceData(self, namespace_id: str, reference_data_type_id: str, reference_data_id: str = None):
        """
        """
        self.__base_client.validateParameters(
            namespace_id, reference_data_type_id, reference_data_id)

        params = {}
        params['typeId'] = self.__base_client.encode(reference_data_type_id)
        params['id'] = self.__base_client.encode(reference_data_id)

        response = self.__base_client.request('delete', self.__reference_data_path.format(
            namespace_id=namespace_id), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to delete reference_data, {reference_data_id}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__reference_data_path = self.__base_path_preview + '/ReferenceData'
