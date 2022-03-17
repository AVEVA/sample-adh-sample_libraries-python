from enum import Enum


class FieldKind(Enum):
    """
    enum 0-4 fully inclusive
    """
    IndexField = 0
    GroupingField = 1
    DataField = 2
    FieldId = 3
    FieldUom = 4
