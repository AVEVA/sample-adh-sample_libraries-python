from enum import Enum


class PropertyTypeCode(Enum):

    Empty = 'Empty'
    Boolean = 'Boolean'
    Int32 = 'Int32'
    Int64 = 'Int64'
    Double = 'Double'
    DateTime = 'DateTime'
    String = 'String'
    TimeSpan = 'TimeSpan'
    Event = 'Event'
    Enumeration = 'Enumeration'
    ReferenceData = 'ReferenceData'
    Asset = 'Asset'
