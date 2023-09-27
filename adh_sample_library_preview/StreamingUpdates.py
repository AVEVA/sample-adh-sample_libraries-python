from __future__ import annotations
from typing import Any

from .BaseClient import BaseClient
from .StreamingUpdates.CreateSignupInput import CreateSignupInput
from .StreamingUpdates.Signup import Signup
from .StreamingUpdates.SignupResourceIds import SignupResourceIds
from .StreamingUpdates.SignupResourcesInput import SignupResourcesInput
from .StreamingUpdates.Trustee import Trustee
from .StreamingUpdates.Update import Update
from .StreamingUpdates.UpdateSignupInput import UpdateSignupInput


class SignupManagerService(object):
    """
    Client for interacting with Signups
    """

    def __init__(self, client: BaseClient):
        """
        :param client: base client that handles auth and base routing
        """

        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getSignups(self,
                   namespace_id: str = None,
                   community_id: str = None) -> list[Signup]:
        """
        Gets all signups in a tenant's namespace. 

        :param str namespace_id: id of namespace to work against
        :param str community_id: Community unique identifier.
        """

        self.__base_client.validateParameters(namespace_id)

        params = {}
        if community_id is not None:
            params['Community-Id'] = community_id

        response = self.__base_client.request('get', self.__signups_path.format(
            namespace_id=namespace_id), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to get signups.')

        results = []
        for i in response.json():
            results.append(Signup.fromJson(i))
        return results

    def createSignup(self,
                     body: CreateSignupInput = None,
                     namespace_id: str = None,
                     community_id: str = None) -> Signup:
        """
        Creates a signup for the list of resource identifiers provided. 

        :param CreateSignupInput body: Input of the signup to be created.
        :param str namespace_id: id of namespace to work against
        :param str community_id: Community unique identifier. Represents a signup for resources shared to the specified Community Id.
        """

        self.__base_client.validateParameters(namespace_id)

        params = {}
        if community_id is not None:
            params['Community-Id'] = community_id

        if not isinstance(body, CreateSignupInput):
            raise TypeError

        response = self.__base_client.request('post', self.__signups_path.format(
            namespace_id=namespace_id), data=body.to_json(), params=params)

        self.__base_client.checkResponse(
            response, f'Failed to create Signup.')

        return Signup.from_json(response.json())

    def getSignupById(self,
                      namespace_id: str = None,
                      signup_id: str = None) -> Signup:
        """
        Retrieves a signup by signup identifier. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup Identifier.
        """

        self.__base_client.validateParameters(namespace_id, signup_id)

        response = self.__base_client.request('get', self.__signup_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get Signup, {signup_id}.')

        result = Signup.fromJson(response.json())
        return result

    def updateSignup(self,
                     body: UpdateSignupInput = None,
                     namespace_id: str = None,
                     signup_id: str = None) -> Signup:
        """
        Updates the properties (for example, name) of a signup. 

        :param UpdateSignupInput body: Signup input object to replace the existing signup's properties.
        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup Identifier.
        """

        self.__base_client.validateParameters(namespace_id, signup_id, body)

        response = self.__base_client.request('put', self.__signup_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), data=body.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to update Signup, {signup_id}.')

        result = Signup.fromJson(response.json())
        return result

    def deleteSignup(self,
                     namespace_id: str = None,
                     signup_id: str = None):
        """
        Deletes a signup and related resources. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup unique identifier
        """

        self.__base_client.validateParameters(namespace_id, signup_id)

        response = self.__base_client.request('delete', self.__signup_path.format(
            namespace_id=namespace_id, asset_id=self.__base_client.encode(signup_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete Signup, {signup_id}.')

    def getSignupOwner(self,
                       namespace_id: str = None,
                       signup_id: str = None) -> Trustee:
        """
        Retrieves the trustee (owner) of a signup. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup unique identifier
        """
        self.__base_client.validateParameters(namespace_id, signup_id)

        response = self.__base_client.request('get', self.__signup_owner_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get Signup owner, {signup_id}.')

        result = Trustee.fromJson(response.json())
        return result

    def getSignupResources(self,
                           namespace_id: str = None,
                           signup_id: str = None) -> SignupResourceIds:
        """
        Retrieves a model that contains collections of accessible and inaccessible resources for a signup. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup unique identifier
        """
        self.__base_client.validateParameters(namespace_id, signup_id)

        response = self.__base_client.request('get', self.__signup_resources_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get Signup resources, {signup_id}.')

        result = SignupResourceIds.fromJson(response.json())
        return result

    def updateSignupResources(self,
                              body: SignupResourcesInput = None,
                              namespace_id: str = None,
                              signup_id: str = None,
                              community_id: str = None):
        """
        Update Signup Resources. 

        :param SignupResourcesInput body: Signup resources input object to replace signup's resources.
        :param str namespace_id: id of namespace to work against
        :param str signup_id: Unique Signup Identifier.
        :param str community_id: Unique Community Identifier.
        """

        self.__base_client.validateParameters(namespace_id, signup_id, body)

        params = {}
        if community_id is not None:
            params['Community-Id'] = community_id

        response = self.__base_client.request('post', self.__signup_resources_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), data=body.toJson(), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to get Signup resources, {signup_id}.')

        result = SignupResourceIds.fromJson(response.json())
        return result

    def getUpdates(self,
                   namespace_id: str = None,
                   signup_id: str = None,
                   bookmark: str = None,
                   value_class: type = None) -> Any:
        """
        Returns a sequence of updates for all resources within the Signup, starting from the sequential marker represented by a provided `Bookmark`. 

        :param str namespace_id: The namespace identifier.
        :param str signup_id: The signup identifier.
        :param str bookmark: An encoded token representing a sequential starting point from which updates are to be retrieved for the current request. A request URI including a starter Bookmark token is provided in the 'Get-Updates' header of a successful Signup activation response.
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        """

        self.__base_client.validateParameters(
            namespace_id, signup_id, bookmark)

        params = {}
        if bookmark is not None:
            params['bookmark'] = bookmark

        response = self.__base_client.request('get', self.__signup_updates_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), params=params)
        self.__base_client.checkResponse(
            response, f'Failed to get Signup updates, {signup_id}.')

        result = Update[value_class].fromJson(response.json())
        return result

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '-preview/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__signups_path = self.__base_path_preview + '/signups'
        self.__signup_path = self.__signups_path + '/{signup_id}'
        self.__signup_owner_path = self.__signup_path + '/owner'
        self.__signup_resources_path = self.__signup_path + '/resources'
        self.__signup_updates_path = self.__signup_path + '/updates'
