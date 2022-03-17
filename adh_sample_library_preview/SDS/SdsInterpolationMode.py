from enum import Enum


class SdsInterpolationMode(Enum):
    """
    enum 0-5 fully inclusive
    """
    Continuous = 0
    StepwiseContinuousLeading = 1
    StepwiseContinuousTrailing = 2
    Discrete = 3
    Default = Continuous
    ContinuousNullableLeading = 4
    ContinuousNullableTrailing = 5
