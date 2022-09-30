
from dataclasses import asdict, dataclass
import json
from .PointMask import PointMask

@dataclass
class AF:
    PointMasks: PointMask = ""

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})

    @staticmethod
    def fromJson(content):
        return PI(**content)
