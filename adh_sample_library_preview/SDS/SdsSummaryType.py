from enum import Flag


class SdsSummaryType(Flag):
    """
    flag 0-4096 not fully inclusive
    """
    none = 0
    Count = 1
    Minimum = 2
    Maximum = 4
    Range = 8
    Mean = 16
    StandardDeviation = 32
    PopulationStandardDeviation = 64
    Total = 128
    Skewness = 256
    Kurtosis = 512
    WeightedMean = 1024
    WeightedStandardDeviation = 2048
    WeightedPopulationStandardDeviation = 4096
