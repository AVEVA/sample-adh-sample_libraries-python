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
        Queries one or many events of a specified TypeId from the Graph Storage.
        The response will vary based on the TypeId and if you query for a single event (by id), or for many events, or for many events with paging.
        :param namespace_id: The namespace identifier
        :param event_type_id: The event TypeId to query
        :param id: The The id of the event to get. If id is specified, then only the fields optional argument will be processed. Also the response JSON will be a single object and not an array.
        :param fields: The names of the fields to be returned separated by spaces. You can specify simple GraphQL syntax for relationships (ex: asset{id}}. If not specified, it defaults to all non-collection properties.
        :param filter: The filter to apply to the query.
        :param order_by: The order by directive specifies the field name and either ascending (asc) or descending (desc). The default is asc.
        :param count: The number of events to return.
        :param continuation_token: Specifies you want a page of data with count events. You must pass an empty token to get the 1st page. The response is different when using paging.
        :param event_class: use this to cast the event into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        """

        self.__base_client.validateParameters(namespace_id, event_type_id)

        params = {}
        params['typeId'] = self.__base_client.encode(event_type_id)
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

        return DataContent(response=response, value_class=event_class).resolve()

    def getOrCreateEvents(self, namespace_id: str, event_type_id: str, events: list[Any], event_class: type = None) -> list[Any]:
        """
        Upserts one or many events of a specified TypeId to the Graph Storage.
        If the body contains a JSON array, it upserts many events. If the body contains a single JSON object it upserts one event.
        :param namespace_id: The namespace identifier
        :param event_type_id: The event TypeId being added or updated
        :param events: A list of event objects
        :param event_class: use this to cast the event into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        """
        self.__base_client.validateParameters(
            namespace_id, event_type_id, events)

        params = {}
        params['typeId'] = self.__base_client.encode(event_type_id)

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

        return DataContent(response=response, value_class=event_class).resolve()

    def deleteEvent(self, namespace_id: str, event_type_id: str, event_id: str = None):
        """
        Deletes one event of a specified TypeId from the Graph Storage.
        :param namespace_id: The namespace identifier
        :param event_type_id: The event TypeId being deleted.
        :param event_id: The event id to delete.
        """
        self.__base_client.validateParameters(
            namespace_id, event_type_id, event_id)

        params = {}
        params['typeId'] = self.__base_client.encode(event_type_id)
        params['id'] = self.__base_client.encode(event_id)

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
