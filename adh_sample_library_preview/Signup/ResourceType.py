from enum import Enum


class ResourceType(Enum):
    """
    Type of resource whose access is being bulk updated.
    """

    STREAM = 'Stream'
