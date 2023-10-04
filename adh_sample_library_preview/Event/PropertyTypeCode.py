from enum import Enum


class PropertyTypeCode(Enum):

    EMPTY = 'Empty'
    BOOLEAN = 'Boolean'
    INT32 = 'Int32'
    INT64 = 'Int64'
    DOUBLE = 'Double'
    DATE_TIME = 'DateTime'
    STRING = 'String'
    TIME_SPAN = 'TimeSpan'
    EVENT = 'Event'
    ENUMERATION = 'Enumeration'
    REFERENCE_DATA = 'ReferenceData'
    ASSET = 'Asset'
