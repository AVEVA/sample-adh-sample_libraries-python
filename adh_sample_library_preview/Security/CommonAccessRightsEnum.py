from enum import Flag


class CommonAccessRightsEnum(Flag):
    """
    flag 0-8 not fully inclusive
    """
    none = 0
    Read = 1
    Write = 2
    Delete = 4
    ManageAccessControl = 8
    Share = 16
    All = 31
