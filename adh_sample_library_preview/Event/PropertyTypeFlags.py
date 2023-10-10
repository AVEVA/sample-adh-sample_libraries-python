from enum import Flag


class PropertyTypeFlags(Flag):
    """
    flag 0-16 not fully inclusive
    """
    none = 0
    NoReverseLookup = 1
    Indexed = 2
    Required = 4
    IsCollection = 8
    ReverseLookup = 16
