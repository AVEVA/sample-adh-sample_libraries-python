from __future__ import annotations
import json
import re
from typing import Any

from .BaseClient import BaseClient
from .DataView.DataView import DataView
from .DataView.ResolvedDataItems import ResolvedDataItems
from .DataView.FieldSets import ResolvedFieldSets
from .Securable import Securable


class DataViews(Securable, object):
    """
    Client for interacting with Data Views
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Data View client
        :param client: This is the base client that is used to make the calls
        """
        super().__init__(client=client, collection='DataViews')
        
        self.__base_client = client
        self.__urlLinks = re.compile(r'<(\S+)>; rel="(\S+)"')

        self.__setPathAndQueryTemplates()

    def postDataView(self, namespace_id: str, data_view: DataView) -> DataView:
        """
        Tells Sds Service to create a Data View based on local 'dataView' or get if existing
            Data View matches
        :param namespace_id: namespace to work against
        :param data_view: Data View definition. Data View object expected
        :return: Retrieved Data View as Data View object
        """
        if namespace_id is None:
            raise TypeError
        if data_view is None or not isinstance(data_view, DataView):
            raise TypeError

        response = self.__base_client.request(
            'post',
            self.__dataViewPath.format(
                tenant_id=self.__base_client.tenant,
                namespace_id=namespace_id,
                dataView_id=self.__base_client.encode(data_view.Id),
            ),
            data=data_view.toJson()
        )
        self.__base_client.checkResponse(
            response, f'Failed to create Data View, {data_view.Id}.'
        )

        result = DataView.fromJson(response.json())
        return result

    def putDataView(self, namespace_id: str, data_view: DataView):
        """
        Tells Sds Service to update a Data View based on local 'data_view'
        :param namespace_id: namespace to work against
        :param data_view: Data View definition. Data View object expected
        :return: Retrieved Data View as Data View object
        """
        if namespace_id is None:
            raise TypeError
        if data_view is None or not isinstance(data_view, DataView):
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__dataViewPath.format(
                tenant_id=self.__base_client.tenant,
                namespace_id=namespace_id,
                dataView_id=self.__base_client.encode(data_view.Id),
            ),
            data=data_view.toJson()
        )
        self.__base_client.checkResponse(
            response, f'Failed to update Data View, {data_view.Id}.'
        )

    def deleteDataView(self, namespace_id: str, data_view_id: str):
        """
        Tells Sds Service to delete a Data View based on 'dataView_id'
        :param namespace_id: namespace to work against
        :param data_view_id: id of Data View to delete
        """
        if namespace_id is None:
            raise TypeError
        if data_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__dataViewPath.format(
                tenant_id=self.__base_client.tenant,
                namespace_id=namespace_id,
                dataView_id=self.__base_client.encode(data_view_id),
            )
        )
        self.__base_client.checkResponse(
            response, f'Failed to delete Data View, {data_view_id}.'
        )

    def getDataView(self, namespace_id: str, data_view_id: str) -> DataView:
        """
        Retrieves the Data View specified by 'dataView_id' from Sds Service
        :param namespace_id: namespace to work against
        :param data_view_id: id of Data View to get
        :return: Retrieved Data View as Data View object
        """
        if namespace_id is None:
            raise TypeError
        if data_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataViewPath.format(
                tenant_id=self.__base_client.tenant,
                namespace_id=namespace_id,
                dataView_id=self.__base_client.encode(data_view_id),
            )
        )
        self.__base_client.checkResponse(
            response, f'Failed to get Data View, {data_view_id}.'
        )

        dataView = DataView.fromJson(response.json())
        return dataView

    def getDataViews(self, namespace_id: str, skip: int = 0, count: int = 100) -> list[DataView]:
        """
        Retrieves all of the Data Views from Sds Service
        :param namespace_id: namespace to work against
        :param skip: Number of Data Views to skip
        :param count: Number of Data Views to return
        :return: array of Data Views
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataViewsPath.format(
                tenant_id=self.__base_client.tenant, namespace_id=namespace_id
            ),
            params={'skip': skip, 'count': count}
        )
        self.__base_client.checkResponse(response, 'Failed to get Data Views.')

        dataViews = json.loads(response.content)
        results = []
        for t in dataViews:
            results.append(DataView.fromJson(t))
        return results

    def getResolvedDataItems(self, namespace_id: str, data_view_id: str,
                             query_id: str) -> ResolvedDataItems:
        """
        Retrieves all of the resolved data items from the specified Data View from Sds Service
        :param namespace_id: namespace to work against
        :param data_view_id: Data View to work against
        :param query_id: Query to see data items of
        :return:
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataViewResolvedDataItems.format(
                tenant_id=self.__base_client.tenant,
                namespace_id=namespace_id,
                dataView_id=self.__base_client.encode(data_view_id),
                query_id=query_id,
            )
        )
        self.__base_client.checkResponse(
            response, f'Failed to get ResolvedDataitems for Data View, {data_view_id}.'
        )

        result = ResolvedDataItems.fromJson(response.json())
        return result

    def getResolvedIneligibleDataItems(self, namespace_id: str, data_view_id: str,
                                       query_id: str) -> ResolvedDataItems:
        """
        Retrieves all of the resolved ineligible data items from the specified Data View from
            Sds Service
        :param namespace_id: namespace to work against
        :param data_view_id: Data View to work against
        :param query_id: Query to see data items of
        :return:
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataViewResolvedIneligibleDataItems.format(
                tenant_id=self.__base_client.tenant,
                namespace_id=namespace_id,
                dataView_id=self.__base_client.encode(data_view_id),
                query_id=query_id,
            )
        )
        self.__base_client.checkResponse(
            response, f'Failed to get ResolvedIneligibleDataitems for Data View, {data_view_id}.'
        )

        result = ResolvedDataItems.fromJson(response.json())
        return result

    def getResolvedAvailableFieldSets(self, namespace_id: str,
                                      data_view_id: str) -> ResolvedFieldSets:
        """
        Retrieves all of the available field sets from the specified Data View from Sds Service
        :param namespace_id: namespace to work against
        :param data_view_id: Data View to work against
        :return:
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataViewResolvedAvailableFieldSets.format(
                tenant_id=self.__base_client.tenant,
                namespace_id=namespace_id,
                dataView_id=self.__base_client.encode(data_view_id)
            )
        )
        self.__base_client.checkResponse(
            response, f'Failed to get ResolvedAvailableFieldSetsfor Data View, {data_view_id}.'
        )

        result = ResolvedFieldSets.fromJson(response.json())
        return result

    def getDataInterpolated(self, namespace_id: str = None, data_view_id: str = None,
                            count: int = None, form: str = None, start_index: str = None,
                            end_index: str = None, interval: str = None, value_class=None,
                            url: str = None, verbose: bool = None) -> tuple[Any, str, str]:
        """
        Retrieves the interpolated data of the 'dataView_id' from Sds Service
        :param namespace_id: namespace to work against
        :param data_view_id: Data View to work against
        :param count: number of values to return
        :param form: form definition of the response (such as table or csv. leave empty for the json default)
        :param start_index: start index
        :param end_index: end index
        :param interval: interval between values (for datetime indexes, the syntax is d.hh:mm:ss)
        :param value_class: Use this to auto format the data into the defined
            type.  The type is expected to have a fromJson method that takes a
            dynamicObject and converts it into the defined type.
            Otherwise you get a dynamic object
        :param url: a complete url to be called as is; this is intended for a page of results
            using the next or first link headers from a previous call
        :param verbose: an optional parameter that lets the user specify verbose or non-verbose results at the query level.
            By default, it will match the base client's accept_verbosity setting, but can be overridden to True or False
            without affecting the client itself.
        :return:
        """
        if url is None:
            if namespace_id is None:
                raise TypeError
            if data_view_id is None:
                raise TypeError
        
        if verbose is None:
            # if this parameter was not specified, use the base client's setting
            verbose = self.__base_client.AcceptVerbosity 

        # The base client does not add a verbosity header if the client is non-verbose, so for Data Views,
        # this is the only condition that we need to handle here since 'non-verbose' is different from no header at all
        additional_headers = BaseClient.getVerbosityHeader(False) if not verbose else None

        params = {
            'count': count,
            'form': form,
            'startIndex': start_index,
            'endIndex': end_index,
            'interval': interval
        }
        response = {}
        if url:
            response = self.__base_client.request('get', url)
        else:
            response = self.__base_client.request(
                'get',
                self.__dataViewDataInterpolated.format(
                    tenant_id=self.__base_client.tenant,
                    namespace_id=namespace_id,
                    dataView_id=self.__base_client.encode(data_view_id),
                ),
                params=params,
                additional_headers=additional_headers
            )

        self.__base_client.checkResponse(
            response,
            f'Failed to get Data View data interpolated for Data View, {data_view_id}.',
        )

        # build dictionary of first/next page URL links, if any
        links_header = response.headers.get('Link', '')
        links = {link.group(2): link.group(1)
                 for link in self.__urlLinks.finditer(links_header)}

        nextPage = links.get('next', None)
        firstPage = links.get('first', None)

        if form is not None and form.casefold() != "default":
            return response.text, nextPage, firstPage

        content = response.json()

        if value_class is None:
            return content, nextPage, firstPage
        return value_class.fromJson(content), nextPage, firstPage

    def getDataStored(self, namespace_id: str = None, data_view_id: str = None,
                            count: int = None, form: str = None, start_index: str = None,
                            end_index: str = None, value_class=None, url: str = None,
                            verbose: bool = None) -> tuple[Any, str, str]:
        """
        Retrieves the stored data of the 'dataView_id' from Sds Service
        :param namespace_id: namespace to work against
        :param data_view_id: Data View to work against
        :param count: number of values to return
        :param form: form definition of the response (such as table or csv. leave empty for the json default)
        :param start_index: start index
        :param end_index: end index
        :param value_class: Use this to auto format the data into the defined
            type.  The type is expected to have a fromJson method that takes a
            dynamicObject and converts it into the defined type.
            Otherwise you get a dynamic object
        :param url: a complete url to be called as is; this is intended for a page of results
            using the next or first link headers from a previous call
        :param verbose: an optional parameter that lets the user specify verbose or non-verbose results at the query level.
            By default, it will match the base client's accept_verbosity setting, but can be overridden to True or False
            without affecting the client itself.
        :return:
        """
        if url is None:
            if namespace_id is None:
                raise TypeError
            if data_view_id is None:
                raise TypeError

        if verbose is None:
            # if this parameter was not specified, use the base client's setting
            verbose = self.__base_client.AcceptVerbosity 

        # The base client does not add a verbosity header if the client is non-verbose, so for Data Views,
        # this is the only condition that we need to handle here since 'non-verbose' is different from no header at all
        additional_headers = BaseClient.getVerbosityHeader(False) if not verbose else None

        params = {
            'count': count,
            'form': form,
            'startIndex': start_index,
            'endIndex': end_index
        }
        response = {}
        if url:
            response = self.__base_client.request('get', url)
        else:
            response = self.__base_client.request(
                'get',
                self.__dataViewDataStored.format(
                    tenant_id=self.__base_client.tenant,
                    namespace_id=namespace_id,
                    dataView_id=self.__base_client.encode(data_view_id),
                ),
                params=params,
                additional_headers=additional_headers
            )

        self.__base_client.checkResponse(
            response,
            f'Failed to get Data View data stored for Data View, {data_view_id}.',
        )

        # build dictionary of first/next page URL links, if any
        links_header = response.headers.get('Link', '')
        links = {link.group(2): link.group(1)
                 for link in self.__urlLinks.finditer(links_header)}

        nextPage = links.get('next', None)
        firstPage = links.get('first', None)

        if form is not None and form.casefold() != "default":
            return response.text, nextPage, firstPage

        content = response.json()

        if value_class is None:
            return content, nextPage, firstPage
        return value_class.fromJson(content), nextPage, firstPage

    def __setPathAndQueryTemplates(self):
        """
        Internal  Sets the needed URLs
        :return:
        """
        self.__basePath = self.__base_client.uri_API + \
            '/Tenants/{tenant_id}/Namespaces/{namespace_id}'

        self.__dataViewsPath = self.__basePath + '/dataviews'
        self.__dataViewPath = self.__dataViewsPath + '/{dataView_id}'
        self.__dataViewResolved = self.__dataViewPath + '/Resolved'
        self.__dataViewResolvedDataItems = self.__dataViewResolved + \
            '/DataItems/{query_id}'
        self.__dataViewResolvedIneligibleDataItems = self.__dataViewResolved + \
            '/IneligibleDataItems/{query_id}'
        self.__dataViewResolvedAvailableFieldSets = self.__dataViewResolved + '/AvailableFieldSets'
        self.__dataViewData = self.__dataViewPath + '/data'
        self.__dataViewDataInterpolated = self.__dataViewData + '/interpolated'
        self.__dataViewDataStored = self.__dataViewData + '/stored'
