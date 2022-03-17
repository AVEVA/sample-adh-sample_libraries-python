from jsonpatch import JsonPatch

from .BaseClient import BaseClient
from .Securable import Securable

class PatchableSecurable(Securable, object):
    """
    Client for interacting with the access control of a collection that is patchable
    """

    def __init__(self, client: BaseClient, collection: str):
        """
        :param client: base client that handles auth and base routing
        :param acl_path: The access control path of the object
        """
        super().__init__(client=client, collection=collection)

        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client
        self.__collection = collection

        self.__setPathAndQueryTemplates()

    def patchDefaultAccessControl(self, namespace_id: str, patch: JsonPatch):
        """
        Patch a collection's default access control list
        :param patch: A JSON Patch document describing the patch operations
        """
        if patch is None:
            raise TypeError

        response = self.__base_client.request(
            'patch', self.__default_collection_acl_path(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            data=patch.to_string())
        self.__base_client.checkResponse(
            response, f'Failed to patch collection access control, {self.__collection}.')

    def patchAccessControl(self, namespace_id: str, item_id: str, patch: JsonPatch):
        """
        Patch an item's access control list
        :param item_id: The item identifier
        :param patch: A JSON Patch document describing the patch operations
        """
        if item_id is None:
            raise TypeError
        if patch is None:
            raise TypeError

        response = self.__base_client.request(
            'patch', self.__item_acl_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                item_id=self.__base_client.encode(item_id)),
            data=patch.to_string())
        self.__base_client.checkResponse(
            response, f'Failed to patch access control, {item_id} in collection {self.__collection}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        if self.__collection == 'Namespaces':
          self.__base_path = self.__uri_api + \
              '/Tenants/{tenant_id}'
        else:
          self.__base_path = self.__uri_api + \
              '/Tenants/{tenant_id}/Namespaces/{namespace_id}'

        self.__default_collection_acl_path = self.__base_path + \
            '/AccessControl/' + self.__collection
        
        self.__collection_path = self.__base_path + '/' + self.__collection

        self.__item_path = self.__collection_path + '/{item_id}'
        self.__item_acl_path = self.__item_path + '/AccessControl'
