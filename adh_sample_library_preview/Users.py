from __future__ import annotations
import json

from .BaseClient import BaseClient
from .Security import User
from .Security import UserInvitation


class Users(object):
    """
    Client for interacting with Users
    """

    AADIdentityProviderId = 'e2398938-bf8f-40fa-b380-d538ece2bfc2'
    GoogleIdentityProviderId = 'd2a478ca-52e3-4fd4-9d93-ded440476364'
    MicrosoftIdentityProviderId = '68a3a33b-b9dd-4eea-884f-87daefc4ff0f'

    def __init__(self, client: BaseClient):
        """
        :param client: base client that handles auth and base routing
        """
        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getUserById(self, user_id: str) -> User:
        """
        Returns the specified User
        :param user_id: The user identifier
        """

        if user_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__user_path.format(
            tenant_id=self.__tenant, user_id=self.__base_client.encode(user_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get User, {user_id}.')

        result = User.fromJson(response.json())
        return result
    
    def getUsers(self, skip: int = 0, count: int = 100) -> list[User]:
        """
        Retrieves a list of users under the current tenant
        :param skip: number of streams to skip for paging
        :param count: number of streams to limit to
        :return: array of Users
        """

        response = self.__base_client.request(
            'get',
            self.__users_path.format(
                tenant_id=self.__tenant),
            params={'skip': skip, 'count': count})
        self.__base_client.checkResponse(
            response, 'Failed to get all Users.')

        content = response.json()
        results: list[User] = []
        for item in content:
            results.append(User.fromJson(item))
        return results

    def getInvitationById(self, invitation_id: str) -> UserInvitation:
        """
        Returns the specified User Invitation
        :param invitation_id: The user invitation
        """

        if invitation_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__invitation_path.format(
            tenant_id=self.__tenant, user_id=invitation_id))
        self.__base_client.checkResponse(
            response, f'Failed to get User Invitation, {invitation_id}.')

        result = UserInvitation.fromJson(response.json())
        return result

    def getInvitations(self, skip: int = 0, count: int = 100) -> list[UserInvitation]:
        """
        Retrieves a list of invitations under the current tenant
        :param skip: number of streams to skip for paging
        :param count: number of streams to limit to
        :return: array of Users
        """

        response = self.__base_client.request(
            'get',
            self.__invitations_path.format(
                tenant_id=self.__tenant),
            params={'skip': skip, 'count': count})
        self.__base_client.checkResponse(
            response, 'Failed to get all Invitations.')

        content = response.json()
        results: list[UserInvitation] = []
        for item in content:
            results.append(UserInvitation.fromJson(item))
        return results

    def createUser(self, user: User) -> User:
        """
        Creates a new tenant user
        :param user: A user object
        """
        if user is None or not isinstance(user, User):
            raise TypeError

        response = self.__base_client.request(
            'post', self.__users_path.format(tenant_id=self.__tenant), data=user.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create User')

        result = User.fromJson(response.json())
        return result

    def getOrCreateUser(self, user: User) -> User:
        """
        Gets a user based on the user object and creates it if it does not exist
        :param user: the user to create or retrieve
        :return: the retrieved or created User
        """
        if user is None or not isinstance(user, User):
            raise TypeError

        response = self.__base_client.request(
            'post',
            self.__user_path.format(
                tenant_id=self.__tenant,
                user_id=self.__base_client.encode(user.Id)),
            data=user.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create User, {user.Id}.')

        result = User.fromJson(response.json())
        return result

    def getOrCreateInvitation(self, user_id: str, user_invitation: UserInvitation) -> UserInvitation:
        """
        Gets a user invitation based on the user object and creates one if it does not exist
        :param user_id: the user id to create an invitation for
        :param user_invitation: the user invitation to create or retrieve
        :return: the retrieved or created UserInvitation
        """
        if user_id is None:
            raise TypeError
        if user_invitation is None or not isinstance(user_invitation, UserInvitation):
            raise TypeError

        response = self.__base_client.request(
            'post',
            self.__user_invitation_path.format(
                tenant_id=self.__tenant,
                user_id=self.__base_client.encode(user_id)),
            data=user_invitation.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create User Invitation, {user_id}.')

        result = UserInvitation.fromJson(response.json())
        return result

    def createOrUpdateUser(self, user: User):
        """
        Creates or updates a user
        :param user: the user to create or update
        :return: the created or updated User
        """
        if user is None or not isinstance(user, User):
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__user_path.format(
                tenant_id=self.__tenant,
                user_id=self.__base_client.encode(user.Id)),
            data=user.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create User, {user.Id}.')

    def createOrUpdateInvitation(self, user_id: str, user_invitation: UserInvitation):
        """
        Creates or updates a user invitation
        :param user_id: the user id to create or update an invitation for
        :param user_invitation: the user invitation to create or update
        :return: the created or updated UserInvitation
        """
        if user_id is None:
            raise TypeError
        if user_invitation is None or not isinstance(user_invitation, UserInvitation):
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__user_invitation_path.format(
                tenant_id=self.__tenant,
                user_id=self.__base_client.encode(user_id)),
            data=user_invitation.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create UserInviation, {user_id}.')

    def deleteUser(self, user_id: str):
        """
        Deletes the user specified by user_id
        :param user_id: id of the user to delete
        :return:
        """
        if user_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__user_path.format(
                tenant_id=self.__tenant,
                user_id=self.__base_client.encode(user_id)))
        self.__base_client.checkResponse(
            response, f'Failed to delete User, {user_id}.')

    def deleteInvitation(self, user_id: str):
        """
        Deletes the invitation for the user specified by user_id
        :param user_id: id of the user to delete the invitation for
        :return:
        """
        if user_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__user_invitation_path.format(
                tenant_id=self.__tenant,
                stream_id=user_id))
        self.__base_client.checkResponse(
            response, f'Failed to delete invitation, {user_id}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        self.__tenant_path = self.__uri_api + \
            '/Tenants/{tenant_id}'

        self.__invitations_path = self.__tenant_path + '/Invitations'
        self.__invitation_path = self.__invitations_path + '/{invitation_id}'

        self.__users_path = self.__tenant_path + '/Users'

        self.__user_path = self.__users_path + '/{user_id}'
        self.__user_invitation_path = self.__user_path + '/Invitation'
