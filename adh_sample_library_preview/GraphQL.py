from __future__ import annotations
from typing import Any
import json

from .BaseClient import BaseClient


class GraphQL(object):

    def __init__(self, client: BaseClient):

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def executeQuery(self, namespace_id: str, query: str, variables: str = None, operation_name: str = None, continuation: str = None, metrics: bool = None, data_class: type = None) -> Any:
        """
        Executes a GraphQL Query or Mutation based on the query arguments of a GET request.
        It returns a GraphQLResponse in JSON format. The format of the response varies depending on the request.
        For more details specific to GraphQL, see the GraphQL POST method (it is the recommended approach for working with GraphQL).

        :param namespace_id: id of namespace to work against
        :param query: GraphQL query to send
        :param variables: One or more named variables and their values that support the query. This is a serialized Dictionary<string, object?>. The object is the variable value and can be a scalar or any supported schema type or type collection (serialized JSON).
        :param operation_name: The name of the operation.
        :param continuation: Additional data for querying the next page of data. Use this when the GraphQL response has a continuation token in its extension data.
        :param metrics: Enables collection of metrics. These are added to the GraphQL response in its extension data.
        :param data_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        """

        self.__base_client.validateParameters(namespace_id)

        request_body = {
            'query': query
        }

        params = {}
        if variables is not None:
            params['variables'] = variables
        if operation_name is not None:
            params['operation_name'] = operation_name
        if continuation is not None:
            params['continuation'] = continuation
        if metrics is not None:
            params['metrics'] = metrics
        
        response = self.__base_client.request('post', self.__graph_ql_path.format(
            namespace_id=namespace_id), data=json.dumps(request_body), params=params)
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

    def checkForSchemaChanges(self, namespace_id: str, body: str = 'force') -> Any:
        """
        Executes a GraphQL Query or Mutation based on the GraphQLRequest body content in a POST request.
        The query or mutation will run against a loaded GraphQL schema that defines all the Types and API's available for an ADH namespace.
        The request query property contains the GraphQL query or mutation.
        The request variables property can be used to pass named values into a query or mutation. The value can be a scalar or any schema defined type or type collection (serialized JSON).
        
        :param namespace_id: id of namespace to work against
        """

        self.__base_client.validateParameters(namespace_id)
        response = self.__base_client.request('post', self.__graph_ql_schema_path.format(
            namespace_id=namespace_id), data=body, additional_headers={'Content-type': 'text/plain'})
        self.__base_client.checkResponse(
            response, f'Failed to force schema change.')

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
        self.__graph_ql_schema_path = self.__graph_ql_path + '/schema'
