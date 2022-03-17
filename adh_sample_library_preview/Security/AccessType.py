from enum import Enum


class AccessType(Enum):
    """
    enum 0-1 inclusive
    """
    Allowed = 0
    Denied = 1
