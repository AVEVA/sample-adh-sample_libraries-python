from dataclasses import asdict, dataclass
import json

@dataclass
class PointMask:
    Name: str = ""
    PointSource: str = ""
    PointType: str = ""
    Descriptor: str = ""
    ExtendedDescriptor: str = ""
    EngineeringUnits: str = ""
    Location1: str = ""
    Location2: str = ""
    Location3: str = ""
    Location4: str = ""
    Location5: str = ""

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})
        
    @staticmethod
    def fromJson(content):
        return PointMask(**content)
