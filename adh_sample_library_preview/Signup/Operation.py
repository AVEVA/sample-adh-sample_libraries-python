from enum import Enum


class Operation(Enum):
    """
    Operations.
    """

    UPDATE = 'Update'
    REPLACE = 'Replace'
    INSERT = 'Insert'
    DELETE = 'Delete'
    DELETEWINDOW = 'DeleteWindow'
