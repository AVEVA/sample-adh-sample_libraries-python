from enum import Enum


class NamespaceProvisioningState(Enum):
    """
    enum 0-3 inclusive
    """
    Creating = 0
    Active = 1
    Deleting = 2
    Deleted = 3