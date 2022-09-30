from dataclasses import asdict, dataclass
import json

from .DataSourceAgent import DataSourceAgent

@dataclass
class DataSource:
    Id: str = ""
    Name: str = ""
    TenantId: str = ""
    OcsNamespace: str = ""
    Agent: DataSourceAgent = None

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ''})

    @staticmethod
    def fromJson(content):
        return DataSource(**content)
