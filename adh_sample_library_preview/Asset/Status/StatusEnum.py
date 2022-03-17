from enum import Enum


class StatusEnum(Enum):
    """
    enum 0-3 fully inclusive
    """
    Unknown = 0
    Good = 1
    Warning = 2
    Bad = 3
