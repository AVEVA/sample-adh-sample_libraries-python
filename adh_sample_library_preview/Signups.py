from __future__ import annotations
from .BaseClient import BaseClient
from .Signup.CreateSignupInput import CreateSignupInput
from .Signup.SignupResources import SignupResources
from .Signup.SignupResourcesInput import SignupResourcesInput
from .Signup.Update import Update
from .Signup.UpdateSignupInput import UpdateSignupInput
from .Signup.Signup import Signup
from .Security.Trustee import Trustee

class Signups(object):
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

        self.__base_client.validateRequiredParameters(namespace_id)
        
        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        response = self.__base_client.request('get', self.__signups_path.format(
            namespace_id=namespace_id), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get signups.')

        results = []
        for i in response.json()['signups']:
            results.append(Signup.fromJson(i))
        return results

    def createSignup(self,
                     namespace_id: str = None,
                     body: CreateSignupInput = None,
                     community_id: str = None) -> Signup:
        """
        Creates a signup for the list of resource identifiers provided. 

        :param str namespace_id: id of namespace to work against
        :param CreateSignupInput body: Input of the signup to be created.
        :param str community_id: Unique Community Identifier.
        """

        self.__base_client.validateRequiredParameters(namespace_id)

        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        if not isinstance(body, CreateSignupInput):
            raise TypeError

        response = self.__base_client.request('post', self.__signups_path.format(
            namespace_id=namespace_id), data=body.toJson(), additional_headers=additional_headers)

        self.__base_client.checkResponse(
            response, f'Failed to create Signup.')

        return Signup.fromJson(response.json())

    def getSignupById(self,
                      namespace_id: str = None,
                      signup_id: str = None,
                      community_id: str = None) -> tuple[Signup, str]:
        """
        Retrieves a signup by signup identifier. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup Identifier.
        :param str community_id: Unique Community Identifier.
        """

        self.__base_client.validateRequiredParameters(namespace_id, signup_id)

        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        response = self.__base_client.request('get', self.__signup_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get Signup, {signup_id}.')

        result = Signup.fromJson(response.json())

        return result

    def updateSignup(self,
                     namespace_id: str = None,
                     signup_id: str = None,
                     body: UpdateSignupInput = None,
                     community_id: str = None) -> Signup:
        """
        Updates the properties (for example, name) of a signup. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup Identifier.
        :param UpdateSignupInput body: Signup input object to replace the existing signup's properties.
        :param str community_id: Unique Community Identifier.
        """

        self.__base_client.validateRequiredParameters(namespace_id, signup_id, body)
        
        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        response = self.__base_client.request('put', self.__signup_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), data=body.toJson(), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to update Signup, {signup_id}.')

        result = Signup.fromJson(response.json())
        return result

    def deleteSignup(self,
                     namespace_id: str = None,
                     signup_id: str = None,
                     community_id: str = None):
        """
        Deletes a signup and related resources. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup unique identifier
        :param str community_id: Unique Community Identifier.
        """

        self.__base_client.validateRequiredParameters(namespace_id, signup_id)

        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        response = self.__base_client.request('delete', self.__signup_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)),additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to delete Signup, {signup_id}.')

    def getSignupOwner(self,
                       namespace_id: str = None,
                       signup_id: str = None,
                       community_id: str = None) -> Trustee:
        """
        Retrieves the trustee (owner) of a signup. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup unique identifier
        :param str community_id: Unique Community Identifier.
        """
        self.__base_client.validateRequiredParameters(namespace_id, signup_id)
        
        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        response = self.__base_client.request('get', self.__signup_owner_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get Signup owner, {signup_id}.')

        result = Trustee.fromJson(response.json())
        return result

    def getSignupResources(self,
                           namespace_id: str = None,
                           signup_id: str = None,
                           community_id: str = None) -> SignupResources:
        """
        Retrieves a model that contains collections of accessible and inaccessible resources for a signup. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Signup unique identifier
        :param str community_id: Unique Community Identifier.
        """
        self.__base_client.validateRequiredParameters(namespace_id, signup_id)
        
        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        response = self.__base_client.request('get', self.__signup_resources_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get Signup resources, {signup_id}.')

        result = SignupResources.fromJson(response.json())

        return result

    def updateSignupResources(self,
                              namespace_id: str = None,
                              signup_id: str = None,
                              body: SignupResourcesInput = None,
                              community_id: str = None):
        """
        Update Signup Resources. 

        :param str namespace_id: id of namespace to work against
        :param str signup_id: Unique Signup Identifier.
        :param SignupResourcesInput body: Signup resources input object to replace signup's resources.
        :param str community_id: Unique Community Identifier.
        """

        self.__base_client.validateRequiredParameters(namespace_id, signup_id, body)

        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        response = self.__base_client.request('post', self.__signup_resources_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), data=body.toJson(), additional_headers=additional_headers)
        self.__base_client.checkResponse(
            response, f'Failed to get Signup resources, {signup_id}.')

    def getUpdates(self,
                    namespace_id: str = None,
                    signup_id: str = None,
                    bookmark: str = None,
                    community_id: str = None ) -> tuple[list[Update], str]:
        """
        Returns a sequence of updates for all resources within the Signup, starting from the sequential marker represented by a provided `Bookmark`. 

        :param str namespace_id: The namespace identifier.
        :param str signup_id: The signup identifier.
        :param str bookmark: An encoded token representing a sequential starting point from which updates are to be retrieved for the current request. A request URI including a starter Bookmark token is provided in the 'Get-Updates' header of a successful Signup activation response.
        :param str community_id: Unique Community Identifier.
        """

        self.__base_client.validateRequiredParameters(namespace_id, signup_id)
        
        additional_headers = BaseClient.getCommunityIdHeader(community_id)

        params = {}
        if bookmark is not None:
            params['bookmark'] = bookmark

        response = self.__base_client.request('get', self.__signup_updates_path.format(
            namespace_id=namespace_id, signup_id=self.__base_client.encode(signup_id)), additional_headers=additional_headers, params=params)
        self.__base_client.checkResponse(
            response, f'Failed to get Signup updates, {signup_id}.')

        data = response.json()['data']
        updates = [Update.fromJson(datum) for datum in data]
        bookmark = response.json()['bookmark']
        
        return updates, bookmark

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        self.__base_path_preview = self.__uri_api + \
            '/Tenants/' + self.__base_client.tenant + \
            '/Namespaces/{namespace_id}'

        self.__signups_path = self.__base_path_preview + '/signups'
        self.__signup_path = self.__signups_path + '/{signup_id}'
        self.__signup_owner_path = self.__signup_path + '/owner'
        self.__signup_resources_path = self.__signup_path + '/resources'
        self.__signup_updates_path = self.__signup_path + '/updates'
