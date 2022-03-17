from __future__ import annotations

from .BaseClient import BaseClient
from .SDS.SdsStreamView import SdsStreamView
from .SDS.SdsStreamViewMap import SdsStreamViewMap
from .PatchableSecurable import PatchableSecurable


class StreamViews(PatchableSecurable, object):
    """
    Client for interacting with Stream Views
    """

    def __init__(self, client: BaseClient):
        """
        :param client: base client that handles auth and base routing
        """
        super().__init__(client=client, collection='StreamViews')

        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getStreamView(self, namespace_id: str, stream_view_id: str) -> SdsStreamView:
        """
        Retrieves the streamView specified by 'stream_view_id' from Sds Service
        :param namespace_id: namespace to work against
        :param stream_view_id: streamview id to get
        :return: Stream view as SdsStreamView
        """
        if namespace_id is None:
            raise TypeError
        if stream_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__stream_view_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=self.__base_client.encode(stream_view_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStreamView, {stream_view_id}.')

        result = SdsStreamView.fromJson(response.json())
        return result

    def getStreamViewMap(self, namespace_id: str, stream_view_id: str) -> SdsStreamViewMap:
        """
        Retrieves the streamView map specified by 'stream_view_id' from Sds
            Service
        :param namespace_id: namespace to work against
        :param stream_view_id:  streamview map to get
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__stream_view_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=self.__base_client.encode(stream_view_id)) + '/Map')
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStreamViewMap, {stream_view_id}.')

        result = SdsStreamViewMap.fromJson(response.json())
        return result

    def getStreamViews(self, namespace_id: str, skip: int = 0, count: int = 100,
                        query: str = '') -> list[SdsStreamView]:
        """
        Retrieves a list of streamViews associated with the specified
            'namespace_id' under the current tenant
        :param namespace_id: namespace to work against
        :param skip: number of streamviews to skip for paging
        :param count: number streamviews in a page
        :param query: optional query.  Default is ''
        :return: array of SdsStreamviews
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__stream_views_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            params={'skip': skip, 'count': count, 'query': query})
        self.__base_client.checkResponse(
            response, 'Failed to get all SdsStreamViews.')

        content = response.json()
        results = []
        for item in content:
            results.append(SdsStreamView.fromJson(item))
        return results

    def getOrCreateStreamView(self, namespace_id: str, stream_view: SdsStreamView) -> SdsStreamView:
        """
        Tells Sds Service to create a streamView based on a local
            SdsStreamView object
        :param namespace_id: namespace to work against
        :param stream_view: Streamview object to create in ADH
        :return: created Streamview as SdsStreamview
        """
        if namespace_id is None:
            raise TypeError
        if stream_view is None or not isinstance(stream_view, SdsStreamView):
            raise TypeError

        response = self.__base_client.request(
            'post',
            self.__stream_view_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=self.__base_client.encode(stream_view.Id)),
            data=stream_view.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStreamView, {stream_view.Id}.')

        result = SdsStreamView.fromJson(response.json())
        return result

    def createOrUpdateStreamView(self, namespace_id: str, stream_view: SdsStreamView):
        """
        Tells Sds Service to create a streamView based on a local SdsStreamView object
        :param namespace_id: namespace to work against
        :param stream_view: Streamview object to create or update in ADH
        :return: created Streamview as SdsStream
        """
        if namespace_id is None:
            raise TypeError
        if stream_view is None or not isinstance(stream_view, SdsStreamView):
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__stream_view_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=self.__base_client.encode(stream_view.Id)),
            data=stream_view.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStreamView, {stream_view.Id}.')

    def deleteStreamView(self, namespace_id: str, stream_view_id: str):
        """
        Tells Sds Service to delete the streamView with the specified
            'stream_view_id'
        :param namespace_id: namespace to work against
        :param stream_view_id: id of streamview to delete
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__stream_view_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=self.__base_client.encode(stream_view_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete SdsStreamView, {stream_view_id}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        self.__base_path = self.__uri_api + \
            '/Tenants/{tenant_id}/Namespaces/{namespace_id}'
        self.__stream_views_path = self.__base_path + '/StreamViews'
        self.__stream_view_path = self.__stream_views_path + \
            '/{stream_view_id}'