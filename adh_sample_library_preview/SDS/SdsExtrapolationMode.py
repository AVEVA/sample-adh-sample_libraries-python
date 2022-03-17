from enum import Enum


class SdsExtrapolationMode(Enum):
    """
    enum 0-3 fully inclusive
    """
    All = 0
    none = 1
    Forward = 2
    Backward = 3
