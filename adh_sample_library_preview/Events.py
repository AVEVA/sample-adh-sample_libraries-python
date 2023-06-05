from __future__ import annotations
import json

from .BaseClient import BaseClient
from .Event.Event import Event
from .Event.AuthorizationTag import AuthorizationTag
from .Event.EventProperty import EventProperty
from .Event.EventType import EventType

from .Securable import Securable


class Events(Securable, object):
    """
    Client for interacting with ADH Assets
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Assets client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='Events')

        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getEventsByTypeId(self, namespace_id: str, typeId: str) -> list[Event]:
        """
        Returns the specified asset
        """
        if namespace_id is None:
            raise TypeError
        if typeId is None:
            raise TypeError

        response = self.__base_client.request('get', self.__events_path.format(
            namespace_id=namespace_id, typeId=self.__base_client.encode(typeId)))
        self.__base_client.checkResponse(
            response, f'Failed to get typeId, {typeId}.')

        results = []
        for i in response.json():
            results.append(Event.fromJson(i))

        return results
    

    def getEventByTypeId(self, namespace_id: str, typeId: str, id: str) -> Event:
        """
        Returns the specified asset
        """
        if namespace_id is None:
            raise TypeError
        if typeId is None:
            raise TypeError

        response = self.__base_client.request('get', self.__events_path.format(
            namespace_id=namespace_id, typeId=self.__base_client.encode(typeId)), params={'id': id})
        self.__base_client.checkResponse(
            response, f'Failed to get typeId, {typeId}.')

        result = Event.fromJson(response.json())

        return result   
    
    

    def getOrCreateEvent(self, namespace_id: str, event: Event, type_id:str) -> Event:
        """
        """
        if namespace_id is None:
            raise TypeError
        if event is None or not isinstance(event, Event):
            raise TypeError

        response = self.__base_client.request('post', self.__event_path.format(
            namespace_id=namespace_id, type_id=self.__base_client.encode(type_id)), data=event.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create asset, {event.Id}.')

        result = Event.fromJson(response.json())
        return result
    

    def getOrCreateEventStr(self, namespace_id: str, eventStr: str, type_id:str) -> Event:
        """
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('post', self.__event_path.format(
            namespace_id=namespace_id, type_id=self.__base_client.encode(type_id)), data=eventStr)
        self.__base_client.checkResponse(
            response, f'Failed to create asset, {eventStr}.')

        result = Event.fromJson(response.json())
        return result
    
    

    def getOrCreateEventString(self, namespace_id: str, eventStr: str, type_id:str) -> Event:
        """
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('post', self.__event_path.format(
            namespace_id=namespace_id, type_id=self.__base_client.encode(type_id)), data=eventStr)
        self.__base_client.checkResponse(
            response, f'Failed to create asset, {eventStr}.')

        result = Event.fromJson(response.json())
        return result
    

    def getOrCreateEventType(self, namespace_id: str, eventType: EventType) -> EventType:
        """
        """
        if namespace_id is None:
            raise TypeError
        if eventType is None or not isinstance(eventType, EventType):
            raise TypeError

        response = self.__base_client.request('post', self.__eventType_path.format(
            namespace_id=namespace_id, eventType_id= eventType.Id), data=eventType.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create asset, {eventType.Id}.')

        result = Event.fromJson(response.json())
        return result
    

    def getEventTypes(self, namespace_id: str) -> list[EventType]:
        """
        Returns the specified asset
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__eventTypes_path.format(
            namespace_id=namespace_id))
        self.__base_client.checkResponse(
            response, f'Failed to get typeId')

        results = []
        for i in response.json():
            results.append(Event.fromJson(i))

        return results
    
    

    def getAuthorizationTags(self, namespace_id: str) -> list[AuthorizationTag]:
        """
        Returns the specified asset
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__authorizationTags_path.format(
            namespace_id=namespace_id))
        self.__base_client.checkResponse(
            response, f'Failed to get typeId')

        results = []
        for i in response.json():
            results.append(Event.fromJson(i))

        return results      
    

    def getAuthorizationTags(self, namespace_id: str) -> list[AuthorizationTag]:
        """
        Returns the specified asset
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__authorizationTags_path.format(
            namespace_id=namespace_id))
        self.__base_client.checkResponse(
            response, f'Failed to get typeId')

        results = []
        for i in response.json():
            results.append(Event.fromJson(i))

        return results

    

    def getAuthorizationTag(self, namespace_id: str, authorizationTag_id: str ) -> list[AuthorizationTag]:
        """
        Returns the specified asset
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__authorizationTags_path.format(
            namespace_id=namespace_id, authorizationTag_id=self.__base_client.encode(authorizationTag_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get typeId')

        results = []
        for i in response.json():
            results.append(Event.fromJson(i))

        return results
    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """   
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant +'/Namespaces/{namespace_id}'
        
        self.__events_path = self.__base_path_preview + '/Events'
        self.__event_path = self.__base_path_preview + '/Events?typeId={type_id}'
        self.__eventTypes_path = self.__base_path_preview + '/EventTypes'
        self.__eventType_path = self.__base_path_preview + '/EventTypes/{eventType_id}'
        self.__authorizationTags_path = self.__base_path_preview + '/AuthorizationTags'
        self.__authorizationTags_path = self.__authorizationTags_path + '/{authorizationTag_id}'
