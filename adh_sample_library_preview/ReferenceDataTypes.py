from __future__ import annotations

from .BaseClient import BaseClient
from .Event.EventGraphReferenceDataType import EventGraphReferenceDataType
from .Securable import Securable


class ReferenceDataTypes(Securable, object):

    def __init__(self, client: BaseClient):
        super().__init__(client=client, collection='ReferenceDataTypes')

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getReferenceDataTypes(self,
                      namespace_id: str,
                      skip: int = None,
                      count: int = None,
                      include_deleted: bool = None,
                      filter: str = None) -> list[EventGraphReferenceDataType]:
        """
        Gets a list of `ReferenceDataType` objects. 

        :param namespace_id: id of namespace to work against
        :param int skip: Parameter representing the zero-based offset of the first object to retrieve. If unspecified, a default value of 0 is used.
        :param int count: Parameter representing the maximum number of objects to retrieve. If unspecified, a default value of 100 is used.
        :param bool include_deleted: Parameter indicating whether to include soft-deleted ReferenceDataTypes. If unspecified, a default value of false is used.
        :param str filter: Parameter representing the condition for results to be filtered by. If unspecified, results are not filtered.
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

        response = self.__base_client.request('get', self.__reference_data_types_path.format(
            namespace_id=namespace_id, params=params))

        self.__base_client.checkResponse(
            response, f'Failed to get list of ReferenceDataTypes.')

        serialized = response.json()
        results: list[EventGraphReferenceDataType] = []
        for i in serialized:
            results.append(EventGraphReferenceDataType.fromJson(i))
        return results

    def createReferenceDataType(self, namespace_id: str,
                             reference_data_type: EventGraphReferenceDataType = None) -> EventGraphReferenceDataType:
        """
        Creates a new `ReferenceDataType` object with server generated Id. 

        :param namespace_id: id of namespace to work against
        :param EventGraphReferenceDataType reference_data_type: A reference data type object
        """

        self.__base_client.validateParameters(namespace_id)

        if not isinstance(reference_data_type, EventGraphReferenceDataType):
            raise TypeError

        response = self.__base_client.request('post', self.__reference_data_types_path.format(
            namespace_id=namespace_id), data=reference_data_type.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to create ReferenceDataType.')

        return EventGraphReferenceDataType.fromJson(response.json())

    def getReferenceDataType(self, namespace_id: str,
                     reference_data_type_id: str,
                     include_deleted: bool = None) -> EventGraphReferenceDataType:
        """
        Gets the specified `ReferenceDataType`. 

        :param namespace_id: id of namespace to work against
        :param str reference_data_type_id: The id of the ReferenceDataType. 
        :param bool include_deleted: Parameter indicating whether to include soft-deleted ReferenceDataTypes. If unspecified, a default value of false is used.
        """
        self.__base_client.validateParameters(namespace_id, reference_data_type_id)

        params = {}
        if include_deleted is not None:
            params['includeDeleted'] = include_deleted

        response = self.__base_client.request('get', self.__reference_data_type_path.format(
            namespace_id=namespace_id, reference_data_type_id=reference_data_type_id), params=params)

        self.__base_client.checkResponse(
            response, f'Failed to get ReferenceDataType, {reference_data_type_id}.')

        return EventGraphReferenceDataType.fromJson(response.json())

    def getOrCreateReferenceDataType(self, namespace_id: str,
                             reference_data_type_id: str,
                             reference_data_type: EventGraphReferenceDataType = None) -> EventGraphReferenceDataType:
        """
        Creates the specified `ReferenceDataType`. 

        :param namespace_id: id of namespace to work against
        :param str reference_data_type_id: The id of the ReferenceDataType. 
        :param EventGraphReferenceDataType reference_data_type: A reference data type object
        """

        self.__base_client.validateParameters(namespace_id, reference_data_type_id)

        if not isinstance(reference_data_type, EventGraphReferenceDataType):
            raise TypeError

        response = self.__base_client.request('post', self.__reference_data_type_path.format(
            namespace_id=namespace_id, reference_data_type_id=reference_data_type_id), data=reference_data_type.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to create ReferenceDataType, {reference_data_type_id}.')

        return EventGraphReferenceDataType.fromJson(response.json())

    def updateReferenceDataType(self, namespace_id: str,
                        reference_data_type_id: str,
                        reference_data_type: EventGraphReferenceDataType = None) -> EventGraphReferenceDataType:
        """
        Updates the specified `ReferenceDataType`. 

        :param namespace_id: id of namespace to work against
        :param str reference_data_type_id: The id of the ReferenceDataType. 
        :param EventGraphReferenceDataType reference_data_type: A reference data type object
        """

        self.__base_client.validateParameters(namespace_id, reference_data_type_id)

        if not isinstance(reference_data_type, EventGraphReferenceDataType):
            raise TypeError

        response = self.__base_client.request('put', self.__reference_data_type_path.format(
            namespace_id=namespace_id, reference_data_type_id=reference_data_type_id), data=reference_data_type.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to update ReferenceDataType, {reference_data_type_id}.')

        return EventGraphReferenceDataType.fromJson(response.json())

    def deleteReferenceDataType(self, namespace_id: str,
                        reference_data_type_id: str):
        """
        Deletes the specified `ReferenceDataType`. 

        :param namespace_id: id of namespace to work against
        :param str reference_data_type_id: The id of the ReferenceDataType. 
        """

        self.__base_client.validateParameters(namespace_id, reference_data_type_id)

        response = self.__base_client.request('delete', self.__reference_data_type_path.format(
            namespace_id=namespace_id, reference_data_type_id=reference_data_type_id))

        self.__base_client.checkResponse(
            response, f'Failed to delete ReferenceDataType, {reference_data_type_id}.')

    def bulkCreateReferenceDataTypes(self, namespace_id: str,
                             reference_data_types: list[EventGraphReferenceDataType] = None) -> EventGraphReferenceDataType:
        """
        Creates ReferenceDataTypes in bulk. 

        :param namespace_id: id of namespace to work against
        :param list[EventGraphReferenceDataType] reference_data_types: 
        """

        self.__base_client.validateParameters(namespace_id)

        if not isinstance(reference_data_types, list[EventGraphReferenceDataType]):
            raise TypeError

        response = self.__base_client.request('post', self.__reference_data_types_bulk_path.format(
            namespace_id=namespace_id), data=reference_data_types.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to bulk create ReferenceDataTypes.')
        return EventGraphReferenceDataType.fromJson(response.json())

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__reference_data_types_path = self.__base_path_preview + '/ReferenceDataTypes'
        self.__reference_data_types_bulk_path = self.__base_path_preview + \
            'Bulk/ReferenceDataTypes'
        self.__reference_data_type_path = self.__base_path_preview + \
            '/ReferenceDataTypes/{reference_data_type_id}'
