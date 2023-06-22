from enum import Enum


class PropertyTypeFlags(Enum):

    NONE = 'None'
    INDEXED = 'Indexed'
    REQUIRED = 'Required'
    IS_COLLECTION = 'IsCollection'
    REVERSE_LOOKUP = 'ReverseLookup'
