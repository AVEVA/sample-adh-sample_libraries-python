from __future__ import annotations
import json
from typing import Any

from .BaseClient import BaseClient
from .SDS.SdsBoundaryType import SdsBoundaryType
from .SDS.SdsResultPage import SdsResultPage
from .SDS.SdsStream import SdsStream
from .SDS.SdsResolvedStream import SdsResolvedStream
from .SDS.SdsType import SdsType
from .PatchableSecurable import PatchableSecurable
from .ContentResolvers import BulkContent, DataContent, PagedContent, StreamsContent, ValueContent

class Streams(PatchableSecurable, object):
    """
    Client for interacting with Streams
    """

    def __init__(self, client: BaseClient):
        """
        :param client: base client that handles auth and base routing
        """
        super().__init__(client=client, collection='Streams')

        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()


    def getStream(self, namespace_id: str, stream_id: str) -> SdsStream:
        """
        Retrieves a stream specified by 'stream_id' from the Sds Service
        :param namespace_id: namespace to work against
        :param stream_id: id of the stream
        :return:the Stream as SdsStream
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id)
        
        response = self.__base_client.request(
            'GET',
            self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStream, {stream_id}.')

        return SdsStream.fromJson(response.json())


    def getResolvedStream(self, namespace_id: str, stream_id: str) -> SdsResolvedStream:
        """
        Retrieves a resolved stream specified by 'stream_id' from the Sds Service
        :param namespace_id: namespace to work against
        :param stream_id: id of the stream
        :return:the Stream as SdsResolvedStream
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        
        response = self.__base_client.request(
            'GET',
            self.__resolved_stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get resolved SdsStream, {stream_id}.')

        return SdsResolvedStream.fromJson(response.json())

    def getStreamType(self, namespace_id: str, stream_id: str) -> SdsType:
        """
        Retrieves a stream specified by 'stream_id' from the Sds Service
        :param namespace_id: namespace to work against
        :param stream_id: id of the stream
        :return: the stream type as an SdsType
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id)

        response = self.__base_client.request(
            'GET',
            self.__stream_type_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStream type, {stream_id}.')
            
        return SdsType.fromJson(response.json())


    def getStreams(self, namespace_id: str, query: str = '', skip: int = 0,
                   count: int = 100) -> list[SdsStream]:
        """
        Retrieves a list of streams associated with 'namespace_id' under the current tenant
        :param namespace_id: namespace to work against
        :param query: filtering query
        :param skip: number of streams to skip for paging
        :param count: number of streams to limit to
        :return: array of SdsStreams
        """
        self.__base_client.validateRequiredParameters(namespace_id, query)

        response = self.__base_client.request(
            'GET',
            self.__streams_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            params={'query': query, 'skip': skip, 'count': count})
        self.__base_client.checkResponse(
            response, f'Failed to get all SdsStreams.')

        return StreamsContent(response=response).resolve()

    def getOrCreateStream(self, namespace_id: str, stream: SdsStream) -> SdsStream:
        """
        Tells Sds Service to create a stream based on the local 'stream' SdsStream object
        :param namespace_id: namespace to work against
        :param stream: the stream to Create or retrieve, as a SDsStream
        :return: the created Stream as an SdsStream
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream)
        if stream is None or not isinstance(stream, SdsStream):
            raise TypeError

        response = self.__base_client.request(
            'POST',
            self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream.Id)),
            data=stream.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStream, {stream.Id}.')

        return SdsStream.fromJson(response.json())
        

    def createOrUpdateStream(self, namespace_id: str, stream: SdsStream):
        """
        Tells Sds Service to create a stream based on the local 'stream' SdsStream object
        :param namespace_id: namespace to work against
        :param stream: the stream to Create or update, as a SDsStream
        :return: the created or updated Stream as an SdsStream
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream)
        if not isinstance(stream, SdsStream):
            raise TypeError

        response = self.__base_client.request(
            'PUT',
            self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream.Id)),
            data=stream.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStream, {stream.Id}.')
        

    def updateStreamType(self, namespace_id: str, stream_id: str, stream_view_id: str):
        """
        Tells Sds Service to update a stream based on the local 'stream' SdsStream object
        :param namespace_id: namespace to work against
        :param stream_id: id of the stream to change the type of
        :param stream_view_id: if of the streamview to change the type to
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, stream_view_id)

        response = self.__base_client.request(
            'PUT',
            self.__stream_type_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            params={'streamViewId': stream_view_id})
        self.__base_client.checkResponse(
            response, f'Failed to update SdsStream type, {stream_id}.')

        
    def deleteStream(self, namespace_id: str, stream_id: str):
        """
        Tells Sds Service to delete the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to delete
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id)

        response = self.__base_client.request(
            'DELETE',
            self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete SdsStream, {stream_id}.')


    def createOrUpdateTags(self, namespace_id: str, stream_id: str, tags: list[str]):
        """
        Tells Sds Service to create tags and associate them with the given stream_id
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to update with tags
        :param tags: tags to create or update. expected for is an array of strings
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id)

        response = self.__base_client.request(
            'PUT',
            self.__stream_tags_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            data=json.dumps(tags))
        self.__base_client.checkResponse(
            response, f'Failed to create tags for Stream: {stream_id}.')


    def createOrUpdateMetadata(self, namespace_id: str, stream_id: str, metadata: dict[str, str]):
        """
        Tells Sds Service to create metadata and associate them with the given stream_id
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to update with metadata
        :param metadata: metadata to create or update. expected for is an dict(string,string)
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id)

        response = self.__base_client.request(
            'PUT',
            self.__stream_metadata_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            data=json.dumps(metadata))
        self.__base_client.checkResponse(
            response, f'Failed to create metadata for Stream: {stream_id}.')


    def patchMetadata(self, namespace_id: str, stream_id: str, patch: list[dict, Any]):
        """
        Tells Sds Service to update metadata on the given streamId
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to update with metadata
        :param patch: a JSON patch document
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id)

        response = self.__base_client.request(
            'PATCH',
            self.__stream_metadata_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            data=json.dumps(patch))
        self.__base_client.checkResponse(
            response, f'Failed to update metadata for Stream: {stream_id}.')


    def getTags(self, namespace_id: str, stream_id: str) -> list[str]:
        """
        Tells Sds Service to get tags associated with the given stream_id
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the tags of
        :return: stream's tags
        """
        self.__base_client.validateRequiredParameters(namespace_id)

        response = self.__base_client.request(
            'GET',
            self.__stream_tags_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get tags for Stream: {stream_id}.')

        return response.json()


    def getMetadata(self, namespace_id: str, stream_id: str, key: str) -> Any:
        """
        Tells Sds Service to get metadata associated with the given stream_id and key
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the metadata value of
        :param key: specific metadata field to retrieve
        :return: value at the key
        """
        self.__base_client.validateRequiredParameters(namespace_id)

        response = self.__base_client.request(
            'GET',
            self.__stream_metadatum_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id),
                key=key))
        self.__base_client.checkResponse(
            response, f'Failed to get metadata for Stream: {stream_id}.')

        return response.json()


    # The following section provides functionality to interact with Data
    #  We assume the value(s) passed follow the Sds object patterns
    #  supporting fromJson and toJson method

    def getValue(self, namespace_id: str, stream_id: str, index: int,
                 value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service for value specified by 'index' from Sds Service
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param index: index at which to get a value
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, index)

        return self.getValueUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), index, value_class)

    def getValueUrl(self, url: str, index: int, value_class: type = None, additional_headers = None) -> Any:
        """
        Retrieves JSON object from Sds Service for value specified by 'index' from Sds Service
        :param url: The URL path to the stream
        :param index: index at which to get a value
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :param additional_headers: headers to add, or override if key is already present
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, index)

        response = self.__base_client.request(
            'GET', self.__data_path.format(stream=url), params={'index': index}, additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get value for SdsStream: {url}.')

        return ValueContent(response=response, value_class=value_class).resolve()


    def getFirstValue(self, namespace_id: str, stream_id: str, value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service the first value to be added to
            the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id)

        return self.getFirstValueUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), value_class)

    def getFirstValueUrl(self, url: str, value_class: type = None, additional_headers = None) -> Any:
        """
        Retrieves JSON object from Sds Service the first value to be added to
            the stream specified by 'url'
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :param additional_headers: headers to add, or override if key is already present
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url)

        response = self.__base_client.request(
            'GET', self.__first_path.format(stream=url), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get first value for SdsStream: {url}.')

        return ValueContent(response=response, value_class=value_class).resolve()


    def getLastValue(self, namespace_id: str, stream_id: str, value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service the last value to be added to
            the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id)

        return self.getLastValueUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), value_class)

    def getLastValueUrl(self, url: str, value_class: type = None, additional_headers = None) -> Any:
        """
        Retrieves JSON object from Sds Service the last value to be added to
            the stream specified by 'url'
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :param additional_headers: headers to add, or override if key is already present
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url)

        response = self.__base_client.request(
            'GET', self.__last_path.format(stream=url), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get last value for SdsStream: {url}.')

        return ValueContent(response=response, value_class=value_class).resolve()


    def getWindowValues(self, namespace_id: str, stream_id: str, start: str, end: str, 
                        value_class: type = None, filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param start: Starting index
        :param end: Ending index
        :param value_class: Optionally use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param filter: An optional filter.  By Default it is ''.
        :return: an array of values.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, end)

        return self.getWindowValuesUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), start, end, value_class, filter)


    def getWindowValuesUrl(self, url: str, start: str, end: str, value_class: type = None, filter: str = '', additional_headers = None) -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'url'
        :param url: The URL path to the stream
        :param start: Starting index
        :param end: Ending index
        :param value_class: Optionally use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param filter: An optional filter.  By Default it is ''.
        :param additional_headers: headers to add, or override if key is already present
        :return: an array of values.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, start, end)

        response = self.__base_client.request(
            'GET', self.__data_path.format(stream=url),
            params={'startIndex': start, 'endIndex': end, 'filter': filter},
            additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get window values for SdsStream: {url}.')

        return DataContent(response=response, value_class=value_class).resolve()


    def getWindowValuesPaged(self, namespace_id: str, stream_id: str, start: str,
                             end: str, count: int, continuation_token: str = '', value_class: type = None, 
                             filter: str = '', boundaryType: SdsBoundaryType = None, startBoundaryType: SdsBoundaryType = None,
                             endBoundaryType: SdsBoundaryType = None) -> SdsResultPage:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id' using paging
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param start: Starting index
        :param end: Ending index
        :param count: maximum number of events to return.
        :param continuationToken: token used to retrieve the next page of data.
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param filter: An optional filter.  By Default it is ''.
        :param boundaryType: Optional SdsBoundaryType specifies handling of events at or near the start and end indexes
        :param startBoundaryType: Optional SdsBoundaryType specifies the first value in the result in relation to the start index.
            If startBoundaryType is specified, endBoundaryType must be specified.
        :param endBoundaryType: Optional SdsBoundaryType specifies the last value in the result in relation to the end index.
            If startBoundaryType is specified, endBoundaryType must be specified.
        :return: an SdsResultPage containing the results and the next continuation token.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, end, count, continuation_token)

        return self.getWindowValuesPagedUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), start, end, count, continuation_token, 
            value_class, filter, boundaryType, startBoundaryType, endBoundaryType)

    def getWindowValuesPagedUrl(self, url: str, start: str,end: str, count: int, continuation_token: str = '', value_class: type = None, 
                             filter: str = '', boundaryType: SdsBoundaryType = None, startBoundaryType: SdsBoundaryType = None,
                             endBoundaryType: SdsBoundaryType = None, additional_headers = None) -> SdsResultPage:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'url' using paging
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param start: Starting index
        :param end: Ending index
        :param count: maximum number of events to return.
        :param continuationToken: token used to retrieve the next page of data.
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param filter: An optional filter.  By Default it is ''.
        :param boundaryType: Optional SdsBoundaryType specifies handling of events at or near the start and end indexes
        :param startBoundaryType: Optional SdsBoundaryType specifies the first value in the result in relation to the start index.
            If startBoundaryType is specified, endBoundaryType must be specified.
        :param endBoundaryType: Optional SdsBoundaryType specifies the last value in the result in relation to the end index.
            If startBoundaryType is specified, endBoundaryType must be specified.
        :param additional_headers: headers to add, or override if key is already present
        :return: an SdsResultPage containing the results and the next continuation token.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, start, end, count, continuation_token)

        params = {'startIndex': start, 'endIndex': end, 'filter': filter,
                'count': count, 'continuationToken': continuation_token}

        if boundaryType is not None:
            params['boundaryType'] = boundaryType.value
        if startBoundaryType is not None:
            params['startBoundaryType'] = startBoundaryType.value
        if endBoundaryType is not None:
            params['endBoundaryType'] =  endBoundaryType.value

        response = self.__base_client.request(
            'get', self.__data_path.format(stream=url),
            params=params,
            additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get window values for SdsStream: {url}.')

        return PagedContent(response=response, value_class=value_class).resolve()


    def getWindowValuesForm(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                            end: str, form: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id'.  Use this to get the data in a different
            return form
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
        Type must support .fromJson().
        If None returns a dynamic Python object from the data.
        :param start: Starting index
        :param end: Ending index
        :param form: form of the data
        :return: An array of the data in type specified if value_class
            defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, end)

        return self.getWindowValuesFormUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), value_class, start, end, form)

    def getWindowValuesFormUrl(self, url: str, value_class: type, start: str,
                               end: str, form: str = '', additional_headers = None) -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'url'.  Use this to get the data in a different
            return form
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
        Type must support .fromJson().
        If None returns a dynamic Python object from the data.
        :param start: Starting index
        :param end: Ending index
        :param form: form of the data
        :param additional_headers: headers to add, or override if key is already present
        :return: An array of the data in type specified if value_class
            defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, start, start, end)

        response = self.__base_client.request(
            'GET', self.__data_path.format(stream=url), params={'startIndex': start, 'endIndex': end, 'form': form}, additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get window values for SdsStream: {url}.')
    
        return DataContent(response=response, value_class=value_class).resolve()


    def getRangeValues(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                       skip: int, count: int, reversed: bool, boundary_type: str, filter: str = '',
                       stream_view_id: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: Starting index
        :param skip: number of values to skip after start index.
            Important in paging
        :param count: number of values to return
        :param reversed: which direction to go when getting values
        :param boundary_type: the boundary condition to use.
            Can be an SdsBoundaryType or the integer value
        :param filter: An optional filter.  By Default it is ''.
        :param stream_view_id: streamview to map the results to
        :return: An array of the data in type specified if value_class
            is defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, skip, count, boundary_type)
        if reversed is None or not isinstance(reversed, bool):
            raise TypeError

        return self.getRangeValuesUrl(
            self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            value_class, start, skip, count, reversed, boundary_type, filter, stream_view_id)

    def getRangeValuesUrl(self, url: str, value_class: type, start: str,
                          skip: int, count: int, reversed: bool, boundary_type: str,
                          filter: str = '', stream_view_id: str = '', additional_headers = None) -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'url'
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: Starting index
        :param skip: number of values to skip after start index.
            Important in paging
        :param count: number of values to return
        :param reversed: which direction to go when getting values
        :param boundary_type: the boundary condition to use.
            Can be an SdsBoundaryType or the integer value
        :param filter: An optional filter.  By Default it is ''.
        :param stream_view_id: streamview to map the results to
        :param additional_headers: headers to add, or override if key is already present
        :return: An array of the data in type specified if value_class
            is defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, start, start, skip, count, boundary_type)
        if reversed is None or not isinstance(reversed, bool):
            raise TypeError

        boundary = boundary_type
        if isinstance(boundary_type, SdsBoundaryType):
            boundary = boundary_type.value

        response = self.__base_client.request(
            'GET', self.__transform_path.format(stream=url),
            params={'startIndex': start, 'skip': skip, 'count': count,
                    'reversed': reversed, 'boundary_type': boundary,
                    'filter': filter, 'stream_view_id': stream_view_id},
            additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get range values for SdsStream: {url}.')

        return DataContent(response=response, value_class=value_class).resolve()


    def getRangeValuesInterpolated(self, namespace_id: str, stream_id: str, value_class: type,
                                   start: str, end: str, count: int, filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: starting index
        :param end:  ending index
        :param count: number of datapoints to retrieve
        :param filter: An optional filter.  By Default it is ''.
        :return: An array of the data in type specified if value_class is
        defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, end, count)

        return self.getRangeValuesInterpolatedUrl(
            self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            value_class, start, end, count, filter)

    def getRangeValuesInterpolatedUrl(self, url: str, value_class: type,
                                      start: str, end: str, count: int, filter: str = '', additional_headers = None) -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'url'
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: starting index
        :param end:  ending index
        :param count: number of datapoints to retrieve
        :param filter: An optional filter.  By Default it is ''.
        :param additional_headers: headers to add, or override if key is already present
        :return: An array of the data in type specified if value_class is
        defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, start, end, count)

        response = self.__base_client.request(
            'GET', self.__transform_interpolated_path.format(stream=url),
            params={'startIndex': start, 'endIndex': end, 'count': count, 'filter': filter}, additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get range values for SdsStream: {url}.')

        return DataContent(response=response, value_class=value_class).resolve()


    def getIndexCollectionValues(self, namespace_id: str, stream_id: str, value_class: type,
                                 index: list[str]) -> list[Any]:
        """
        Retrieves JSON object representing values at specific indexes from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: starting index
        :param index: One or more indexes to retrieve events at
        :return: An array of the data in type specified if value_class is
        defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, index)

        return self.getIndexCollectionValuesUrl(
            self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            value_class, index)

    def getIndexCollectionValuesUrl(self, url: str, value_class: type,
                                      index: list[str], additional_headers = None) -> list[Any]:
        """
        Retrieves JSON object representing values at specific indexes from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: starting index
        :param index: One or more indexes to retrieve events at
        :param additional_headers: headers to add, or override if key is already present
        :return: An array of the data in type specified if value_class is
        defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, index)

        params = []
        for i in index:
            params.append(('index', i))

        response = self.__base_client.request(
            'GET', self.__transform_interpolated_path.format(stream=url),
            params=params, additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get range values for SdsStream: {url}.')

        return DataContent(response=response, value_class=value_class).resolve()


    def getSampledValues(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                         end: str, sample_by: str, intervals: str, filter: str = '',
                         stream_view_id: str = '') -> list[Any]:
        """
        Returns data sampled by intervals between a specified start and end index.
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param start: starting index for intervals
        :param end:  ending index for intervals
        :param sample_by: property or properties to use when sampling
        :param intervals: number of intervals requested
        :param boundary: optional SdsBoundaryType specifies the handling of
            events at or near the startIndex and endIndex
        :param start_boundary: optional SdsBoundaryType specifies the handling
            of events at or near the startIndex
        :param end_boundary: optional SdsBoundaryType specifies the handling
            of events at or near the endIndex
        :param filter: optional filter to apply
        :param stream_view_id: optional streamview identifier
        :return: An array of the data in type specified if value_class is
            defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, end, sample_by, intervals)

        return self.getSampledValuesUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), value_class, start, end, sample_by, intervals,
            filter, stream_view_id)

    def getSampledValuesUrl(self, url: str, value_class: type, start: str,
                            end: str, sample_by: str, intervals: str, filter: str = '',
                            stream_view_id: str = '', additional_headers = None) -> list[Any]:
        """
        Returns data sampled by intervals between a specified start and end index.
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param start: starting index for intervals
        :param end:  ending index for intervals
        :param sample_by: property or properties to use when sampling
        :param intervals: number of intervals requested
        :param boundary: optional SdsBoundaryType specifies the handling of
            events at or near the startIndex and endIndex
        :param start_boundary: optional SdsBoundaryType specifies the handling
            of events at or near the startIndex
        :param end_boundary: optional SdsBoundaryType specifies the handling
            of events at or near the endIndex
        :param filter: optional filter to apply
        :param stream_view_id: optional streamview identifier
        :param additional_headers: headers to add, or override if key is already present
        :return: An array of the data in type specified if value_class is
            defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, start, end, sample_by, intervals)

        # if stream_view_id is set, use /transform/ route
        if len(stream_view_id):
            _path = self.__transform_sampled_path.format(stream=url)
        else:
            _path = self.__sampled_path.format(stream=url)

        response = self.__base_client.request(
            'GET',
            _path,
            params={'startIndex': start,
                    'endIndex': end,
                    'sampleBy': sample_by,
                    'intervals': intervals,
                    'filter': filter,
                    'stream_view_id': stream_view_id},
            additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get sampled values for SdsStream: {_path}.')

        return DataContent(response=response, value_class=value_class).resolve()


    def getSummaries(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                     end: str, count: int, stream_view_id: str = '', filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a summary for the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        Note- for this function the default return json string is not a
            JSON array of the value, so the same type definition won't work.
        :param start: starting index
        :param end:  ending index
        :param count: number of datapoints in summary
        :param stream_view_id: streamview to tranform the data into
        :param filter: filter to apply
        :return: An array of the data summary in type specified if value_class
            is defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, end, count)

        return self.getSummariesUrl(self.__stream_path.format(
            tenant_id=self.__tenant,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id)), value_class, start, end, count, stream_view_id, filter)

    def getSummariesUrl(self, url: str, value_class: type, start: str,
                        end: str, count: int, stream_view_id: str = '', filter: str = '', additional_headers = None) -> list[Any]:
        """
        Retrieves JSON object representing a summary for the stream specified by 'url'
        :param url: The URL path to the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        Note- for this function the default return json string is not a
            JSON array of the value, so the same type definition won't work.
        :param start: starting index
        :param end:  ending index
        :param count: number of datapoints in summary
        :param stream_view_id: streamview to transform the data into
        :param filter: filter to apply
        :param additional_headers: headers to add, or override if key is already present
        :return: An array of the data summary in type specified if value_class
            is defined.  Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(url, start, end, count)

        paramsToUse = {'startIndex': start,
                        'endIndex': end,
                        'count': count,
                        'filter': filter}

        # if stream_view_id is set, use /transform/ route and set stream_view_id parameter
        if len(stream_view_id):
            _path = self.__transform_summaries_path.format(stream=url)
            paramsToUse['streamViewId'] = stream_view_id
        else:
            _path = self.__summaries_path.format(stream=url)

        response = self.__base_client.request('GET', _path, paramsToUse, additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get summaries for SdsStream: {_path}.')

        return DataContent(response=response, value_class=value_class).resolve()


    def insertValues(self, namespace_id: str, stream_id: str, values: list[Any]):
        """
        Tells Sds Service to insert the values, defined by the list 'values',
        into the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data into
        :param values: values to sends into ADH.
            Can be string of json array of values.
            Can be an array of values of a type that has toJson defined.
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, values)

        if callable(getattr(values[0], 'toJson', None)):
            events = []
            for value in values:
                events.append(value.toDictionary())
            payload = json.dumps(events)
        else:
            payload = values

        response = self.__base_client.request(
            'POST',
            self.__data_path.format(
                stream=self.__stream_path.format(
                    tenant_id=self.__tenant,
                    namespace_id=namespace_id,
                    stream_id=self.__base_client.encode(stream_id))),
            data=payload)
        self.__base_client.checkResponse(
            response, f'Failed to insert multiple values for SdsStream: {stream_id}.')


    def updateValues(self, namespace_id: str, stream_id: str, values: list[Any]):
        """
        Tells Sds Service to update values defined by the SdsValue list, 'values'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data updated
        :param values: values to update in ADH.
        Can be string of json array of values.
        Can be an array of values of a type that has toJson defined.
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, values)

        if callable(getattr(values[0], 'toJson', None)):
            events = []
            for value in values:
                events.append(value.toDictionary())
            payload = json.dumps(events)
        else:
            payload = values

        response = self.__base_client.request(
            'PUT',
            self.__data_path.format(
                stream=self.__stream_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id))),
            data=payload)
        self.__base_client.checkResponse(
            response, f'Failed to update values for SdsStream: {stream_id}.')


    def replaceValues(self, namespace_id: str, stream_id: str, values: list[Any]):
        """
        Tells Sds Service to replace the values defined by the list 'values'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data replaced
        :param values: values to replace in ADH.
            Can be string of json array of values.
            Can be an array of values of a type that has toJson defined.
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, values)

        if callable(getattr(values[0], 'toJson', None)):
            events = []
            for value in values:
                events.append(value.toDictionary())
            payload = json.dumps(events)
        else:
            payload = values

        response = self.__base_client.request(
            'PUT',
            self.__replace_path.format(
                stream=self.__stream_path.format(
                    tenant_id=self.__tenant,
                    namespace_id=namespace_id,
                    stream_id=self.__base_client.encode(stream_id))),
            data=payload)
        self.__base_client.checkResponse(
            response, f'Failed to replace multiple values for SdsStream: {stream_id}.')


    def removeValue(self, namespace_id: str, stream_id: str, key: str):
        """
        Tells Sds Service to delete the value with a key property matching 'key'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data removed
        :param key: the index to remove
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, key)

        response = self.__base_client.request(
            'DELETE',
            self.__data_path.format(
                stream=self.__stream_path.format(
                    tenant_id=self.__tenant,
                    namespace_id=namespace_id,
                    stream_id=self.__base_client.encode(stream_id))),
            params={'index': key})
        self.__base_client.checkResponse(
            response, f'Failed to remove values for SdsStream: {stream_id}.')


    def removeWindowValues(self, namespace_id: str, stream_id: str, start: str, end: str):
        """
        Tells Sds Service to delete a window of values in the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data removed
        :param start: starting index
        :param end: ending index
        :return:
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_id, start, end)

        response = self.__base_client.request(
            'delete',
            self.__data_path.format(
                stream=self.__stream_path.format(
                    tenant_id=self.__tenant,
                    namespace_id=namespace_id,
                    stream_id=self.__base_client.encode(stream_id))),
            params={'startIndex': start, 'endIndex': end})
        self.__base_client.checkResponse(
            response, f'Failed to remove values for SdsStream: {stream_id}.')


    def getStreamsWindow(self, namespace_id: str, stream_ids: list[str], value_class: type,
                         start: str, end: str, join_mode: int = 1) -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
             specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_ids: ids of the streams to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: Starting index
        :param end: Ending index
        :param joinMode: Join mode, supports numbers or strings.
            Defaults to outer
        :return: an array of values.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__base_client.validateRequiredParameters(namespace_id, stream_ids, start, end, join_mode)
    
        response = self.__base_client.request(
            'GET',
            self.__bulk_join_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            params={'streams': ','.join(stream_ids),
                    'startIndex': start,
                    'endIndex': end,
                    'joinMode': join_mode})
        self.__base_client.checkResponse(
            response, f'Failed to get bulk values for SdsStream: {stream_ids}.')

        return BulkContent(response=response, value_class=value_class).resolve()


    # private methods

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        self.__base_path = self.__uri_api + \
            '/Tenants/{tenant_id}/Namespaces/{namespace_id}'
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/{tenant_id}/Namespaces/{namespace_id}'
        self.__streams_path = self.__base_path + '/Streams'
        self.__stream_path = self.__streams_path + '/{stream_id}'
        self.__resolved_stream_path = self.__base_path_preview  + '/Streams/{stream_id}/Resolved'
        self.__stream_type_path = self.__stream_path + '/Type'
        self.__stream_tags_path = self.__stream_path + '/Tags'
        self.__stream_metadata_path = self.__stream_path + '/Metadata'
        self.__stream_metadatum_path = self.__stream_metadata_path + '/{key}'

        self.__data_path = '{stream}/Data'
        self.__first_path = self.__data_path + '/First'
        self.__last_path = self.__data_path + '/Last'
        self.__transform_path = self.__data_path + '/Transform'
        self.__summaries_path = self.__data_path + '/Summaries'
        self.__transform_summaries_path = self.__transform_path + '/Summaries'
        self.__sampled_path = self.__data_path + '/Sampled'
        self.__transform_sampled_path = self.__transform_path + '/Sampled'
        self.__transform_interpolated_path = self.__transform_path + '/Interpolated'

        self.__replace_path = self.__data_path + '?allowCreate=false'

        self.__bulk_join_path = self.__base_path + '/Bulk/Streams/Data/Joins'