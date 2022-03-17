from __future__ import annotations
import json

from .BaseClient import BaseClient
from .Tenant.Namespace import Namespace
from .Securable import Securable


class Namespaces(Securable, object):
    """
    Client for interacting with ADH Namespace
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Namespaces client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='Namespaces')

        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getNamespaceById(self, namespace_id: str) -> Namespace:
        """
        Returns the specified Namespace
        :param namespace_id: The namespace identifier
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__namespace_path.format(
            namespace_id=namespace_id))
        self.__base_client.checkResponse(
            response, f'Failed to get Namespace, {namespace_id}.')

        result = Namespace.fromJson(response.json())
        return result

    def getNamespaces(self, region: str = '') -> list[Namespace]:
        """
        Returns a list of Namespaces
        :param region: An optional region string identifier.
        """

        response = self.__base_client.request('get', self.__namespaces_path, params={'region': region})
        self.__base_client.checkResponse(response, f'Failed to get Namespaces.')

        results = []
        for i in response.json():
            results.append(Namespace.fromJson(i))
        return results

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__tenant_path = self.__base_client.uri_API + '/Tenants/' + \
            self.__base_client.tenant
        self.__namespaces_path = self.__tenant_path + '/Namespaces'
        self.__namespace_path = self.__namespaces_path + '/{namespace_id}'
