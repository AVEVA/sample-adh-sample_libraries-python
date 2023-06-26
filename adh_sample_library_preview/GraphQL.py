from __future__ import annotations
from typing import Any
import json

from .BaseClient import BaseClient


class GraphQL(object):

    def __init__(self, client: BaseClient):

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def executeQuery(self, namespace_id: str, query: str, data_class: type = None) -> Any:
        """
        """

        self.__base_client.validateParameters(namespace_id)

        request_body = {
            'query': query
        }

        response = self.__base_client.request('post', self.__graph_ql_path.format(
            namespace_id=namespace_id), data=json.dumps(request_body))
        self.__base_client.checkResponse(
            response, f'Failed to execute GraphQL query, {query}.')

        result = response.json()

        if data_class is None:
            return result

        if result['extension'] is None:
            return {
                'data': data_class.fromJson(response.json())
            }

        return {
            'data': data_class.fromJson(result['data']),
            'extensions': result['extension']}

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__graph_ql_path = self.__base_path_preview + '/GraphQL'
