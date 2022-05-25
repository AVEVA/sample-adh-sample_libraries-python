from __future__ import annotations

from .BaseClient import BaseClient
from .Community.Community import Community
from .Community.CommunityInput import CommunityInput
from .Community.CommunitySummaryInformation import CommunitySummaryInformation
from .Community.StreamSearchResult import StreamSearchResult


class Communities(object):
    """
    Client for interacting with ADH communities
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Communities client
        :param client: This is the base client that is used to make REST calls
        """
        self.__base_client = client
        self.__setPathAndQueryTemplates()

    def getCommunityById(self, community_id: str) -> Community:
        """
        Returns the specified community
        :param community_id: The community identifier
        """
        if community_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get', self.__community_path.format(community_id=self.__base_client.encode(community_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get community, {community_id}.')

        result = Community.fromJson(response.json())
        return result

    def getCommunities(self, skip: int = 0, count: int = 100) -> list[Community]:
        """
        Returns a list of communities
        :param skip: An optional parameter representing the zero-based offset of the first community to
        retrieve. If not specified, a default value of 0 is used.
        :param count: An optional parameter, between 1 and 1000 (inclusive), that represents the
        maximum number of retrieved communities. If not specified, the default is 100.
        """
        response = self.__base_client.request('get', self.__communities_path, params={
                                              'skip': skip, 'count': count})
        self.__base_client.checkResponse(
            response, f'Failed to get communities')

        results = []
        for i in response.json():
            results.append(Community.fromJson(i))
        return results

    def createCommunity(self, community: CommunityInput) -> Community:
        """
        Creates a new community
        :param community: A community input object
        """
        if community is None or not isinstance(community, CommunityInput):
            raise TypeError

        response = self.__base_client.request(
            'post', self.__communities_path, data=community.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create community')

        result = Community.fromJson(response.json())
        return result

    def updateCommunity(self, community: CommunityInput):
        """
        Updates a community with a specified Id
        :param community: A community input object
        """
        if community is None or not isinstance(community, CommunityInput):
            raise TypeError

        response = self.__base_client.request(
            'put', self.__community_path.format(community_id=self.__base_client.encode(community.Id)), data=community.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to update community, {community.Id}')

    def deleteCommunity(self, community_id: str):
        """
        Deletes a community
        :param community_id: The community identifier
        """
        if community_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete', self.__community_path.format(community_id=self.__base_client.encode(community_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete community, {community_id}.')

    def getCommunitySummary(self, community_id: str) -> CommunitySummaryInformation:
        """
        Returns a summary of the specified community
        :param community_id: The community identifier
        """
        if community_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get', self.__summary_path.format(community_id=self.__base_client.encode(community_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get summary for community, {community_id}.')

        result = CommunitySummaryInformation.fromJson(response.json())
        return result

    def getCommunityStreams(self, community_id: str, query: str = '', count: int = 100,
                            search_tenant_id: str = None) -> list[StreamSearchResult]:
        """
        Searches for streams within a community by query
        :param community_id: The community identifier
        :param query: An optional query string to search for matching streams.
        :param count: An optional parameter that represents the maximum number of retrieved streams.
        If not specified, the default is 100.
        """
        if community_id is None:
            raise TypeError

        params = {'query': query, 'count': count}

        if search_tenant_id is not None:
            params['searchTenantId'] = search_tenant_id

        response = self.__base_client.request('get', self.__search_streams_path.format(
            community_id=self.__base_client.encode(community_id)), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to search for streams.')

        results = []
        for i in response.json():
            results.append(StreamSearchResult.fromJson(i))
        return results

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        : return:
        """
        self.__base_path = self.__base_client.uri_API + '-preview/'
        self.__communities_path = self.__base_path + '/Communities'
        self.__community_path = self.__communities_path + '/{community_id}'
        self.__summary_path = self.__community_path + '/Summary'
        self.__search_streams_path = self.__base_path + \
            '/Search/Communities/{community_id}/Streams'
