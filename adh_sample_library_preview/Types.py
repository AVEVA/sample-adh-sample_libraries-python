from __future__ import annotations
import json

from .SDS.SdsType import SdsType
from .BaseClient import BaseClient
from .PatchableSecurable import PatchableSecurable


class Types(PatchableSecurable, object):
    """
    Handles communication with Sds Service
    """

    def __init__(self, client: BaseClient):
        """
        :param client: base client that handles auth and base routing
        """
        super().__init__(client=client, collection='Types')

        self.__tenant = client.tenant
        self.__url = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getType(self, namespace_id: str, type_id: str) -> SdsType:
        """
        Retrieves the type specified by 'type_id' from Sds Service
        :param namespace_id: id of namespace to work against
        :param type_id: id of the type to get
        :return:the type as an SdsType
        """
        if namespace_id is None:
            raise TypeError
        if type_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__typePath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                type_id=self.__base_client.encode(type_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get SdsType, {type_id}.')

        result = SdsType.fromJson(response.json())
        return result

    def getTypeReferenceCount(self, namespace_id: str, type_id: str) -> dict[str, int]:
        """
        Retrieves the number of times the type is referenced
        :param namespace_id: id of namespace to work against
        :param type_id: id of the type to get references of
        :return: reference count python dynamic object
        """
        if namespace_id is None:
            raise TypeError
        if type_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__typeRefCountPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                type_id=self.__base_client.encode(type_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get SdsType reference count, {type_id}.')

        content = response.json()
        return content

    def getTypes(self, namespace_id: str, skip: int = 0, count: int = 100,
                 query: str = '') -> list[SdsType]:
        """
        Retrieves a list of types associated with the specified 'namespace_id'
            under the current tenant
        :param namespace_id: id of namespace to work against
        :param skip: number of types to skip, used for paging
        :param count: number of types to retrieve
        :param query: optional query.  Default is ''
        :return: array of types as SdsType
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__typesPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            params={'skip': skip, 'count': count, 'query': query})
        self.__base_client.checkResponse(
            response, 'Failed to get all SdsTypes.')

        content = response.json()
        results = []
        for t in content:
            results.append(SdsType.fromJson(t))
        return results

    def getOrCreateType(self, namespace_id: str, type: SdsType) -> SdsType:
        """
        Tells Sds Service to create or get a type based on local 'type'
        or get if existing type matches

        :param namespace_id: id of namespace to work against
        :param type:  the SdsType to create or get
        :return:  the created or retrieved SdsType
        """
        if namespace_id is None:
            raise TypeError
        if type is None or not isinstance(type, SdsType):
            raise TypeError
        response = self.__base_client.request(
            'post',
            self.__typePath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                type_id=self.__base_client.encode(type.Id)),
            data=type.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create type, {type.Id}.')

        result = SdsType.fromJson(response.json())
        return result

    def deleteType(self, namespace_id: str, type_id: str):
        """
        Tells Sds Service to delete the type specified by 'type_id'

        :param namespace_id: id of namespace to work against
        :param type_id:  id of the type to delete
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if type_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__typePath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                type_id=self.__base_client.encode(type_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete SdsType, {type_id}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        used to create needed URI for the other calls
        :return:
        """
        self.__basePath = self.__url + \
            '/Tenants/{tenant_id}/Namespaces/{namespace_id}'
        self.__typesPath = self.__basePath + '/Types'
        self.__typePath = self.__typesPath + '/{type_id}'
        self.__typeRefCountPath = self.__typePath + '/ReferenceCount'
