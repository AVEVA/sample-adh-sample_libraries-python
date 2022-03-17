from __future__ import annotations
import json

from .BaseClient import BaseClient
from .OMF.Topic import Topic
from .Securable import Securable


class Topics(Securable, object):
    """
    Client for interacting with ADH Topics
    This class does not represent the full functionality of the Topics route and is included to allow management of security on the route
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Topics client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='Topics')

        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getTopicById(self, namespace_id: str, topic_id: str) -> Topic:
        """
        Returns the specified Topic
        :param namespace_id: The namespace identifier
        :param topic_id: The topic identifier
        """
        if namespace_id is None:
            raise TypeError
        if topic_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__topic_path.format(
            namespace_id=namespace_id, topic_id=self.__base_client.encode(topic_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get Topic, {topic_id}.')

        result = Topic.fromJson(response.json())
        return result

    def getTopics(self, namespace_id: str) -> list[Topic]:
        """
        Returns a list of Topics
        :param namespace_id: The namespace identifier
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__topics_path.format(
            namespace_id=namespace_id))
        self.__base_client.checkResponse(response, f'Failed to get Topics.')

        results = []
        for i in response.json():
            results.append(Topic.fromJson(i))
        return results

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path = self.__base_client.uri_API + '/Tenants/' + \
            self.__base_client.tenant + '/Namespaces/{namespace_id}'
        self.__topics_path = self.__base_path + '/topics'
        self.__topic_path = self.__topics_path + '/{topic_id}'
