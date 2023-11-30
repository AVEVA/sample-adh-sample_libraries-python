from enum import Enum


class SignupState(Enum):
    """
    Signup Status.
    """

    ACTIVATING = 'Activating'
    ACTIVE = 'Active'
    EXPIRED = 'Expired'
    FAILED = 'Failed'
