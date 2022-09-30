from dataclasses import asdict, dataclass
import json
from typing import List


@dataclass
class AdditionalInformation:
    total_count: int

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})

    @staticmethod
    def fromJson(content):
        return AdditionalInformation(**content)

@dataclass
class Result:
    PointId: int = ''
    Name: str = ''
    PointSource: str = ''
    PointType: str = ''
    Descriptor: str = ''
    EngineeringUnits: str = ''
    Id: str = ''
    Name: str = ''
    
    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})

    @staticmethod
    def fromJson(content):
        return Result(**content)


@dataclass
class QueryResult:
    Results: List[Result]
    AdditionalInformation: AdditionalInformation
    QueryType: str = ''

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})

    @staticmethod
    def fromJson(content):
        return QueryResult(**content)