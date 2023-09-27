from __future__ import annotations

from .BaseClient import BaseClient
from .Event.AuthorizationTag import AuthorizationTag
from .Securable import Securable


class AuthorizationTags(Securable, object):

    def __init__(self, client: BaseClient):
        super().__init__(client=client, collection='AuthorizationTags')

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getAuthorizationTags(self,
                      namespace_id: str,
                      skip: int = None,
                      count: int = None,
                      include_deleted: bool = None,
                      filter: str = None) -> list[AuthorizationTag]:
        """
        Gets a list of `AuthorizationTag` objects. 

        :param namespace_id: id of namespace to work against
        :param int skip: Parameter representing the zero-based offset of the first object to retrieve. If unspecified, a default value of 0 is used.
        :param int count: Parameter representing the maximum number of objects to retrieve. If unspecified, a default value of 100 is used.
        :param bool include_deleted: Parameter indicating whether to include soft-deleted Authorization Tags. If unspecified, a default value of false is used.
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

        response = self.__base_client.request('get', self.__authorization_tags_path.format(
            namespace_id=namespace_id, params=params))

        self.__base_client.checkResponse(
            response, f'Failed to get list of Authorization Tags.')

        serialized = response.json()
        results: list[AuthorizationTag] = []
        for i in serialized:
            results.append(AuthorizationTag.fromJson(i))
        return results

    def getAuthorizationTag(self, namespace_id: str,
                     authorization_tag_id: str,
                     include_deleted: bool = None) -> AuthorizationTag:
        """
        Gets the specified `AuthorizationTag`. 

        :param namespace_id: id of namespace to work against
        :param str authorization_tag_id: The authorization tag identifier
        :param bool include_deleted: Parameter indicating whether to include soft-deleted Authorization Tags. If unspecified, a default value of false is used.
        """
        self.__base_client.validateParameters(namespace_id, authorization_tag_id)

        params = {}
        if include_deleted is not None:
            params['includeDeleted'] = include_deleted

        response = self.__base_client.request('get', self.__authorization_tag_path.format(
            namespace_id=namespace_id, authorization_tag_id=authorization_tag_id), params=params)

        self.__base_client.checkResponse(
            response, f'Failed to get Authorization Tag, {authorization_tag_id}.')

        return AuthorizationTag.fromJson(response.json())

    def getOrCreateAuthorizationTag(self, namespace_id: str,
                             authorization_tag_id: str,
                             authorization_tag: AuthorizationTag = None) -> AuthorizationTag:
        """
        Creates the specified `AuthorizationTag`. 

        :param namespace_id: id of namespace to work against
        :param str authorization_tag_id: The authorization tag identifier
        :param AuthorizationTag authorization_tag: An authorization tag object
        """

        self.__base_client.validateParameters(namespace_id, authorization_tag_id)

        if not isinstance(authorization_tag, AuthorizationTag):
            raise TypeError

        response = self.__base_client.request('post', self.__authorization_tag_path.format(
            namespace_id=namespace_id, authorization_tag_id=authorization_tag_id), data=authorization_tag.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to create Authorization Tag, {authorization_tag_id}.')

        return AuthorizationTag.fromJson(response.json())

    def updateAuthorizationTag(self, namespace_id: str,
                        authorization_tag_id: str,
                        authorization_tag: AuthorizationTag = None) -> AuthorizationTag:
        """
        Updates the specified `AuthorizationTag`. 

        :param namespace_id: id of namespace to work against
        :param str authorization_tag_id: The authorization tag identifier
        :param AuthorizationTag authorization_tag: An authorization tag object
        """

        self.__base_client.validateParameters(namespace_id, authorization_tag_id)

        if not isinstance(authorization_tag, AuthorizationTag):
            raise TypeError

        response = self.__base_client.request('put', self.__authorization_tag_path.format(
            namespace_id=namespace_id, authorization_tag_id=authorization_tag_id), data=authorization_tag.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to update Authorization Tag, {authorization_tag_id}.')

        return AuthorizationTag.fromJson(response.json())

    def deleteAuthorizationTag(self, namespace_id: str,
                        authorization_tag_id: str):
        """
        Deletes the specified `AuthorizationTag`. 

        :param namespace_id: id of namespace to work against
        :param str authorization_tag_id: The authorization tag identifier
        """

        self.__base_client.validateParameters(namespace_id, authorization_tag_id)

        response = self.__base_client.request('delete', self.__authorization_tag_path.format(
            namespace_id=namespace_id, authorization_tag_id=authorization_tag_id))

        self.__base_client.checkResponse(
            response, f'Failed to delete Authorization Tag, {authorization_tag_id}.')

    def bulkCreateAuthorizationTags(self, namespace_id: str,
                             authorization_tags: list[AuthorizationTag] = None) -> AuthorizationTag:
        """
        Creates Authorization Tags in bulk. 

        :param namespace_id: id of namespace to work against
        :param list[AuthorizationTag] authorization_tags: A list of authorization tag objects
        """

        self.__base_client.validateParameters(namespace_id)

        if not isinstance(authorization_tags, list[AuthorizationTag]):
            raise TypeError

        response = self.__base_client.request('post', self.__authorization_tags_bulk_path.format(
            namespace_id=namespace_id), data=authorization_tags.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to bulk create Authorization Tags.')
        return AuthorizationTag.fromJson(response.json())

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__authorization_tags_path = self.__base_path_preview + '/AuthorizationTags'
        self.__authorization_tags_bulk_path = self.__base_path_preview + \
            'Bulk/AuthorizationTags'
        self.__authorization_tag_path = self.__base_path_preview + \
            '/AuthorizationTags/{authorization_tag_id}'
