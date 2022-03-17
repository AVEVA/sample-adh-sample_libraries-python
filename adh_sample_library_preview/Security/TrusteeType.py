from enum import Enum


class TrusteeType(Enum):
    """
    enum 1-3 inclusive
    """
    User = 1
    Client = 2
    Role = 3
