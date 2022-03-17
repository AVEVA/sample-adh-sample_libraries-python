from __future__ import annotations
import json


class User(object):
    """ADH trustee definition"""

    def __init__(self, id: str = None, given_name: str = None, surname: str = None, name: str = None, email: str = None, contact_email: str = None, contact_given_name: str = None,
                 contact_surname: str = None, external_user_id: str = None, identity_provider_id: str = None,
                 identity_provider_specific_user_id: str = None, role_ids: list[str] = None):
        self.Id = id
        self.GivenName = given_name
        self.Surname = surname
        self.Name = name
        self.Email = email
        self.ContactEmail = contact_email
        self.ContactGivenName = contact_given_name
        self.ContactSurname = contact_surname
        self.ExternalUserId = external_user_id
        self.IdentityProviderId = identity_provider_id
        self.IdentityProviderSpecificUserId = identity_provider_specific_user_id
        self.RoleIds = role_ids

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def GivenName(self) -> str:
        return self.__given_name

    @GivenName.setter
    def GivenName(self, value: str):
        self.__given_name = value

    @property
    def Surname(self) -> str:
        return self.__surname

    @Surname.setter
    def Surname(self, value: str):
        self.__surname = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Email(self) -> str:
        return self.__email

    @Email.setter
    def Email(self, value: str):
        self.__email = value

    @property
    def ContactEmail(self) -> str:
        return self.__contact_email

    @ContactEmail.setter
    def ContactEmail(self, value: str):
        self.__contact_email = value

    @property
    def ContactGivenName(self) -> str:
        return self.__contact_given_name

    @ContactGivenName.setter
    def ContactGivenName(self, value: str):
        self.__contact_given_name = value

    @property
    def ContactSurname(self) -> str:
        return self.__contact_surname

    @ContactSurname.setter
    def ContactSurname(self, value: str):
        self.__contact_surname = value

    @property
    def ExternalUserId(self) -> str:
        return self.__external_user_id

    @ExternalUserId.setter
    def ExternalUserId(self, value: str):
        self.__external_user_id = value

    @property
    def IdentityProviderId(self) -> str:
        return self.__identity_provider_id

    @IdentityProviderId.setter
    def IdentityProviderId(self, value: str):
        self.__identity_provider_id = value

    @property
    def IdentityProviderId(self) -> str:
        return self.__identity_provider_id

    @IdentityProviderId.setter
    def IdentityProviderId(self, value: str):
        self.__identity_provider_id = value

    @property
    def IdentityProviderSpecificUserId(self) -> str:
        return self.__identity_provider_specific_user_id

    @IdentityProviderSpecificUserId.setter
    def IdentityProviderSpecificUserId(self, value: str):
        self.__identity_provider_specific_user_id = value

    @property
    def RoleIds(self) -> list[str]:
        return self.__role_ids

    @RoleIds.setter
    def RoleIds(self, value: list[str]):
        self.__role_ids = value


    def toJson(self):
      return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Id': self.Id}

        if self.GivenName is not None:
            result['GivenName'] = self.GivenName

        if self.Surname is not None:
            result['Surname'] = self.Surname

        if self.Name is not None:
            result['Name'] = self.Name

        if self.Email is not None:
            result['Email'] = self.Email
        
        if self.ContactEmail is not None:
            result['ContactEmail'] = self.ContactEmail

        if self.ContactGivenName is not None:
            result['ContactGivenName'] = self.ContactGivenName
        
        if self.ContactSurname is not None:
            result['ContactSurname'] = self.ContactSurname

        if self.ExternalUserId is not None:
            result['ExternalUserId'] = self.ExternalUserId

        if self.IdentityProviderId is not None:
            result['IdentityProviderId'] = self.IdentityProviderId

        if self.IdentityProviderSpecificUserId is not None:
            result['IdentityProviderSpecificUserId'] = self.IdentityProviderSpecificUserId

        if self.RoleIds is not None:
            result['RoleIds'] = []
            for value in self.RoleIds:
                result['RoleIds'].append(value)

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = User()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'GivenName' in content:
            result.GivenName = content['GivenName']
        
        if 'Surname' in content:
            result.Surname = content['Surname']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Email' in content:
            result.Email = content['Email']

        if 'ContactEmail' in content:
            result.ContactEmail = content['ContactEmail']

        if 'ContactGivenName' in content:
            result.ContactGivenName = content['ContactGivenName']

        if 'ContactSurname' in content:
            result.ContactSurname = content['ContactSurname']

        if 'ExternalUserId' in content:
            result.ExternalUserId = content['ExternalUserId']

        if 'IdentityProviderId' in content:
            result.IdentityProviderId = content['IdentityProviderId']

        if 'IdentityProviderSpecificUserId' in content:
            result.IdentityProviderSpecificUserId = content['IdentityProviderSpecificUserId']

        if 'RoleIds' in content:
            role_ids = content['RoleIds']
            if role_ids is not None and len(role_ids) > 0:
                result.RoleIds = []
                for value in role_ids:
                    result.RoleIds.append(value)

        return result