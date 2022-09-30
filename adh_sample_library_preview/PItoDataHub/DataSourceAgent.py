from dataclasses import asdict, dataclass
import json

@dataclass
class DataSourceAgent():
    Id: str = ""
    LastCommTime: str = ""
    Version: str = ""
    Status: str = ""
    Description: str = ""
    HostName: str = ""
    Namespace: str = ""
    Region: str = ""
    IsDeprecated: str = ""
    TransferMetrics: str = ""
    PISystem: str = ""

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})

    @staticmethod
    def fromJson(content):
        return DataSourceAgent(**content)
