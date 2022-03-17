from enum import Enum


class SdsSearchMode(Enum):
    """
    enum 0-4 fully inclusive
    """
    Exact = 0
    ExactOrNext = 1
    Next = 2
    ExactOrPrevious = 3
    Previous = 4
