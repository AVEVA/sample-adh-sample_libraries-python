from enum import Enum


class UserInvitationState(Enum):
    """
    enum 0-2 inclusive
    """
    none = 0
    InvitationEmailSent = 1
    InvitationAccepted = 2