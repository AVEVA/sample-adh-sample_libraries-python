from enum import Enum


class CommunityTenantStatus(Enum):
    """
    enum 0-4 inclusive
    """
    none = 0
    AwaitingConfirmation = 1
    Paused = 2
    Active = 3
    Remove = 4
