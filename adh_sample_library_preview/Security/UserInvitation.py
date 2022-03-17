from __future__ import annotations
import json

from .UserInvitationState import UserInvitationState


class UserInvitation(object):
    """ADH trustee definition"""

    def __init__(self, id: str = None, expires_date_time: str = None, issued: str = None, expires: str = None, accepted: str = None,
                 state: UserInvitationState = None, send_invitation: bool = None, identity_provider_id: str = None, tenant_id: str = None, user_id: str = None):
        self.Id = id
        self.ExpiresDateTime = expires_date_time
        self.Issued = issued
        self.Expires = expires
        self.Accepted = accepted
        self.State = state
        self.SendInvitation = send_invitation
        self.IdentityProviderId = identity_provider_id
        self.TenantId = tenant_id
        self.UserId = user_id
    
    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def ExpiresDateTime(self) -> str:
        return self.__expires_date_time

    @ExpiresDateTime.setter
    def ExpiresDateTime(self, value: str):
        self.__expires_date_time = value

    @property
    def Issued(self) -> str:
        return self.__issued

    @Issued.setter
    def Issued(self, value: str):
        self.__issued = value
    
    @property
    def Expires(self) -> str:
        return self.__expires

    @Expires.setter
    def Expires(self, value: str):
        self.__expires = value

    @property
    def Accepted(self) -> str:
        return self.__accepted

    @Accepted.setter
    def Accepted(self, value: str):
        self.__accepted = value

    @property
    def State(self) -> UserInvitationState:
        return self.__state

    @State.setter
    def State(self, value: UserInvitationState):
        self.__state = value

    @property
    def SendInvitation(self) -> str:
        return self.__send_invitation

    @SendInvitation.setter
    def SendInvitation(self, value: str):
        self.__send_invitation = value

    @property
    def IdentityProviderId(self) -> str:
        return self.__identity_provider_id

    @IdentityProviderId.setter
    def IdentityProviderId(self, value: str):
        self.__identity_provider_id = value

    @property
    def TenantId(self) -> str:
        return self.__tenant_id

    @TenantId.setter
    def TenantId(self, value: str):
        self.__tenant_id = value

    @property
    def UserId(self) -> str:
        return self.__user_id

    @UserId.setter
    def UserId(self, value: str):
        self.__user_id = value

    def toJson(self):
      return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}

        if self.Id is not None:
            result['Id'] = self.Id

        if self.ExpiresDateTime is not None:
            result['ExpiresDateTime'] = self.ExpiresDateTime

        if self.Issued is not None:
            result['Issued'] = self.Issued

        if self.Expires is not None:
            result['Expires'] = self.Expires

        if self.Accepted is not None:
            result['Accepted'] = self.Accepted
        
        if self.State is not None:
            result['State'] = self.State.value

        if self.SendInvitation is not None:
            result['SendInvitation'] = self.SendInvitation
        
        if self.IdentityProviderId is not None:
            result['IdentityProviderId'] = self.IdentityProviderId

        if self.TenantId is not None:
            result['TenantId'] = self.TenantId

        if self.UserId is not None:
            result['UserId'] = self.UserId
            
        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = UserInvitation()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'ExpiresDateTime' in content:
            result.ExpiresDateTime = content['ExpiresDateTime']
        
        if 'Issued' in content:
            result.Issued = content['Issued']

        if 'Expires' in content:
            result.Expires = content['Expires']

        if 'Accepted' in content:
            result.Accepted = content['Accepted']

        if 'State' in content:
            result.State = content['State']

        if 'SendInvitation' in content:
            result.SendInvitation = content['SendInvitation']

        if 'IdentityProviderId' in content:
            result.IdentityProviderId = content['IdentityProviderId']

        if 'TenantId' in content:
            result.TenantId = content['TenantId']

        if 'UserId' in content:
            result.UserId = content['UserId']

        return result