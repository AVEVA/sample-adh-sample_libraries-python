import enum
import json
from dataclasses import dataclass, asdict
from .PI import PI

class QueryType(str, enum.Enum):
    PI = 'PIPoint',
    AF = 'AFElementSearchByAttribute'

@dataclass
class Query:
    Skip: int = 0
    Count: int = 200
    PI: PI = ""
    AF: str = ""
    QueryType: str = ""
    Id: str = ""
    Status: str = ""
    DatabaseName: str = ""
    QueryString: str = ""
    AttributeName: str = ""

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})

    @staticmethod
    def fromJson(content):
        return Query(**content)