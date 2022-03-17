from enum import Enum


class SdsBoundaryType(Enum):
    """
    enum 0-3 fully inclusive
    """
    Exact = 0
    Inside = 1
    Outside = 2
    ExactOrCalculated = 3
