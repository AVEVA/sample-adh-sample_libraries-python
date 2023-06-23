from __future__ import annotations
from typing import Any
import json

from .BaseClient import BaseClient
from .ContentResolvers import DataContent
from .Securable import Securable


class Events(Securable, object):

    def __init__(self, client: BaseClient):
        super().__init__(client=client, collection='Events')

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getEvents(self, namespace_id: str, event_type_id: str, id: str = None, fields: str = None,
                  filter: str = None, order_by: str = None, count: int = None, continuation_token: str = None,
                  event_class: type = None) -> list[Any]:
        """
        """

        self.__base_client.validateParameters(namespace_id, event_type_id)

        params = {}
        params['event_type_id'] = self.__base_client.encode(event_type_id)
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

        response = self.__base_client.request('get', self.__events_path.format(
            namespace_id=namespace_id), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to get events, {event_type_id}.')

        return DataContent(response=response, event_class=event_class).resolve()

    def getOrCreateEvents(self, namespace_id: str, event_type_id: str, events: list[Any], event_class: type = None) -> list[Any]:
        """
        """
        self.__base_client.validateParameters(
            namespace_id, event_type_id, events)

        params = {}
        params['event_type_id'] = self.__base_client.encode(event_type_id)

        if callable(getattr(events[0], 'toJson', None)):
            events = []
            for event in events:
                events.append(event.toDictionary())
            payload = json.dumps(events)
        else:
            payload = events

        response = self.__base_client.request('post', self.__events_path.format(
            namespace_id=namespace_id), data=payload, params=params)
        self.__base_client.checkResponse(
            response, f'Failed to create events, {event_type_id}.')

        return DataContent(response=response, event_class=event_class).resolve()

    def deleteEvent(self, namespace_id: str, event_type_id: str, event_id: str = None):
        """
        """
        self.__base_client.validateParameters(
            namespace_id, event_type_id, event_id)

        params = {}
        params['event_type_id'] = self.__base_client.encode(event_type_id)
        params['event_id'] = self.__base_client.encode(event_id)

        response = self.__base_client.request('delete', self.__events_path.format(
            namespace_id=namespace_id), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to delete event, {event_id}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__events_path = self.__base_path_preview + '/Events'
