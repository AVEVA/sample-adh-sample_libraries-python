﻿from __future__ import annotations

from .BaseClient import BaseClient
from .Event.EventGraphEnumeration import EventGraphEnumeration
from .Securable import Securable


class Enumerations(Securable, object):

    def __init__(self, client: BaseClient):
        super().__init__(client=client, collection='Enumerations')

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getEnumerations(self,
                      namespace_id: str,
                      skip: int = None,
                      count: int = None,
                      include_deleted: bool = None,
                      filter: str = None) -> list[EventGraphEnumeration]:
        """
        Gets a list of `Enumeration` objects. 

        :param namespace_id: id of namespace to work against
        :param int skip: 
        :param int count: 
        :param bool include_deleted: 
        :param str filter: 
        """
        self.__base_client.validateParameters(namespace_id)

        params = {}
        if skip is not None:
            params['skip'] = skip
        if count is not None:
            params['count'] = count
        if include_deleted is not None:
            params['includeDeleted'] = include_deleted
        if filter is not None:
            params['filter'] = filter

        response = self.__base_client.request('get', self.__enumerations_path.format(
            namespace_id=namespace_id, params=params))

        self.__base_client.checkResponse(
            response, f'Failed to get list of Enumerations.')

        serialized = response.json()
        results: list[EventGraphEnumeration] = []
        for i in serialized:
            results.append(EventGraphEnumeration.from_json(i))
        return results

    def getOrCreateEnumeration(self, namespace_id: str,
                             enumeration: EventGraphEnumeration = None) -> EventGraphEnumeration:
        """
        Creates a new `Enumeration` object. 

        :param namespace_id: id of namespace to work against
        :param EventGraphEnumeration enumeration: 
        """

        self.__base_client.validateParameters(namespace_id)

        if not isinstance(enumeration, EventGraphEnumeration):
            raise TypeError

        response = self.__base_client.request('post', self.__enumerations_path.format(
            namespace_id=namespace_id), data=enumeration.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to create Enumeration.')

        return EventGraphEnumeration.from_json(response.json())

    def getEnumeration(self, namespace_id: str,
                     enumeration_id: str,
                     include_deleted: bool = None) -> EventGraphEnumeration:
        """
        Gets the specified `Enumeration`. 

        :param namespace_id: id of namespace to work against
        :param str enumeration_id: 
        :param bool include_deleted: 
        """
        self.__base_client.validateParameters(namespace_id, enumeration_id)

        params = {}
        if include_deleted is not None:
            params['includeDeleted'] = include_deleted

        response = self.__base_client.request('get', self.__enumeration_path.format(
            namespace_id=namespace_id, enumeration_id=enumeration_id), params=params)

        self.__base_client.checkResponse(
            response, f'Failed to get Enumeration, {enumeration_id}.')

        return EventGraphEnumeration.from_json(response.json())

    def getOrCreateEnumeration(self, namespace_id: str,
                             enumeration_id: str,
                             enumeration: EventGraphEnumeration = None) -> EventGraphEnumeration:
        """
        Creates the specified `Enumeration`. 

        :param namespace_id: id of namespace to work against
        :param str enumeration_id: 
        :param EventGraphEnumeration enumeration: 
        """

        self.__base_client.validateParameters(namespace_id, enumeration_id)

        if not isinstance(enumeration, EventGraphEnumeration):
            raise TypeError

        response = self.__base_client.request('post', self.__enumerations_path.format(
            namespace_id=namespace_id, enumeration_id=enumeration_id), data=enumeration.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to create Enumeration, {enumeration_id}.')

        return EventGraphEnumeration.from_json(response.json())

    def updateEnumeration(self, namespace_id: str,
                        enumeration_id: str,
                        enumeration: EventGraphEnumeration = None) -> EventGraphEnumeration:
        """
        Updates the specified `Enumeration`. 

        :param namespace_id: id of namespace to work against
        :param str id: 
        :param EventGraphEnumeration enumeration: 
        """

        self.__base_client.validateParameters(namespace_id, enumeration_id)

        if not isinstance(enumeration, EventGraphEnumeration):
            raise TypeError

        response = self.__base_client.request('put', self.__enumerations_path.format(
            namespace_id=namespace_id, enumeration_id=enumeration_id), data=enumeration.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to update Enumeration, {enumeration_id}.')

        return EventGraphEnumeration.from_json(response.json())

    def deleteEnumeration(self, namespace_id: str,
                        enumeration_id: str):
        """
        Deletes the specified `Enumeration`. 

        :param namespace_id: id of namespace to work against
        :param str enumeration_id: 
        """

        self.__base_client.validateParameters(namespace_id, enumeration_id)

        response = self.__base_client.request('delete', self.__enumerations_path.format(
            namespace_id=namespace_id, enumeration_id=enumeration_id))

        self.__base_client.checkResponse(
            response, f'Failed to delete Enumeration, {enumeration_id}.')

    def bulkCreateEnumerations(self, namespace_id: str,
                             enumerations: list[EventGraphEnumeration] = None) -> EventGraphEnumeration:
        """
        Creates Enumerations in bulk. 

        :param namespace_id: id of namespace to work against
        :param list[EventGraphEnumeration] enumerations: 
        """

        self.__base_client.validateParameters(namespace_id)

        if not isinstance(enumerations, list[EventGraphEnumeration]):
            raise TypeError

        response = self.__base_client.request('post', self.__enumerations_path_bulk_path.format(
            namespace_id=namespace_id), data=enumerations.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to bulk create Enumerations.')
        return EventGraphEnumeration.from_json(response.json())

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__enumerations_path = self.__base_path_preview + '/Enumerations'
        self.__enumerations_path_bulk_path = self.__base_path_preview + \
            'Bulk/Enumerations'
        self.__enumeration_path = self.__base_path_preview + \
            '/Enumerations/{enumeration_id}'