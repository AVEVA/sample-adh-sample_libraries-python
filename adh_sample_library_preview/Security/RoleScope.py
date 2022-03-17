from enum import Enum


class RoleScope(Enum):
    """
    enum 0-3 fully inclusive
    """
    none = 0
    Tenant = 1
    Community = 2
    Cluster = 3
