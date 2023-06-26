﻿from __future__ import annotations

from .BaseClient import BaseClient
from .Event.EventGraphEventType import EventGraphEventType
from .Securable import Securable


class EventTypes(Securable, object):

    def __init__(self, client: BaseClient):
        super().__init__(client=client, collection='EventTypes')

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getEventTypes(self,
                      namespace_id: str,
                      skip: int = None,
                      count: int = None,
                      include_deleted: bool = None,
                      filter: str = None) -> list[EventGraphEventType]:
        """
        Gets a list of `EventType` objects. 

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

        response = self.__base_client.request('get', self.__event_types_path.format(
            namespace_id=namespace_id, params=params))

        self.__base_client.checkResponse(
            response, f'Failed to get list of Event Types.')

        serialized = response.json()
        results: list[EventGraphEventType] = []
        for i in serialized:
            results.append(EventGraphEventType.from_json(i))
        return results

    def createEventType(self, namespace_id: str,
                        event_type: EventGraphEventType = None) -> EventGraphEventType:
        """
        Creates a new `EventType` object with server generated Id. 

        :param namespace_id: id of namespace to work against
        :param EventGraphEventType event_type: 
        """

        self.__base_client.validateParameters(namespace_id)

        if not isinstance(event_type, EventGraphEventType):
            raise TypeError

        response = self.__base_client.request('post', self.__event_types_path.format(
            namespace_id=namespace_id), data=event_type.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to create Event Type.')

        return EventGraphEventType.from_json(response.json())

    def getEventType(self, namespace_id: str,
                     event_type_id: str,
                     include_deleted: bool = None) -> EventGraphEventType:
        """
        Gets the specified `EventType`. 

        :param namespace_id: id of namespace to work against
        :param str event_type_id: 
        :param bool include_deleted: 
        """
        self.__base_client.validateParameters(namespace_id, event_type_id)

        params = {}
        if include_deleted is not None:
            params['includeDeleted'] = include_deleted

        response = self.__base_client.request('get', self.__event_type_path.format(
            namespace_id=namespace_id, event_type_id=event_type_id), params=params)

        self.__base_client.checkResponse(
            response, f'Failed to get Event Type, {event_type_id}.')

        return EventGraphEventType.from_json(response.json())

    def getOrCreateEventType(self, namespace_id: str,
                             event_type_id: str,
                             event_type: EventGraphEventType = None) -> EventGraphEventType:
        """
        Creates the specified `EventType`. 

        :param namespace_id: id of namespace to work against
        :param str event_type_id: 
        :param EventGraphEventType event_type: 
        """

        self.__base_client.validateParameters(namespace_id, event_type_id)

        if not isinstance(event_type, EventGraphEventType):
            raise TypeError

        response = self.__base_client.request('post', self.__event_type_path.format(
            namespace_id=namespace_id, event_type_id=event_type_id), data=event_type.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to create Event Type, {event_type_id}.')

        return EventGraphEventType.from_json(response.json())

    def updateEventType(self, namespace_id: str,
                        event_type_id: str,
                        event_type: EventGraphEventType = None) -> EventGraphEventType:
        """
        Updates the specified `EventType`. 

        :param namespace_id: id of namespace to work against
        :param str id: 
        :param EventGraphEventType event_type: 
        """

        self.__base_client.validateParameters(namespace_id, event_type_id)

        if not isinstance(event_type, EventGraphEventType):
            raise TypeError

        response = self.__base_client.request('put', self.__event_type_path.format(
            namespace_id=namespace_id, event_type_id=event_type_id), data=event_type.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to update Event Type, {event_type_id}.')

        return EventGraphEventType.from_json(response.json())

    def deleteEventType(self, namespace_id: str,
                        event_type_id: str):
        """
        Deletes the specified `EventType`. 

        :param namespace_id: id of namespace to work against
        :param str event_type_id: 
        """

        self.__base_client.validateParameters(namespace_id, event_type_id)

        response = self.__base_client.request('delete', self.__event_type_path.format(
            namespace_id=namespace_id, event_type_id=event_type_id))

        self.__base_client.checkResponse(
            response, f'Failed to delete Event Type, {event_type_id}.')

    def bulkCreateEventTypes(self, namespace_id: str,
                             event_types: list[EventGraphEventType] = None) -> EventGraphEventType:
        """
        Creates Event Types in bulk. 

        :param namespace_id: id of namespace to work against
        :param list[EventGraphEventType] event_types: 
        """

        self.__base_client.validateParameters(namespace_id)

        if not isinstance(event_types, list[EventGraphEventType]):
            raise TypeError

        response = self.__base_client.request('post', self.__event_types_bulk_path.format(
            namespace_id=namespace_id), data=event_types.to_json())

        self.__base_client.checkResponse(
            response, f'Failed to bulk create Event Types.')
        return EventGraphEventType.from_json(response.json())

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__event_types_path = self.__base_path_preview + '/EventTypes'
        self.__event_types_bulk_path = self.__base_path_preview + \
            'Bulk/EventTypes'
        self.__event_type_path = self.__base_path_preview + \
            '/EventTypes/{event_type_id}'
