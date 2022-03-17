from __future__ import annotations
import json

from .CommunityTenant import CommunityTenant


class Community(object):
    """ADH community definition"""

    def __init__(self, id: str = None, name: str = None, alias: str = None, description: str = None,
                 tenants: list[CommunityTenant] = None, date_created: str = None,
                 streams_contributed_count: int = None,
                 total_streams_contributed_count: int = None):
        self.Id = id
        self.Name = name
        self.Alias = alias
        self.Description = description
        self.Tenants = tenants
        self.DateCreated = date_created
        self.StreamsContributedCount = streams_contributed_count
        self.TotalStreamsContributedCount = total_streams_contributed_count

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Alias(self) -> str:
        return self.__alias

    @Alias.setter
    def Alias(self, value: str):
        self.__alias = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def Tenants(self) -> list[CommunityTenant]:
        return self.__tenants

    @Tenants.setter
    def Tenants(self, value: list[CommunityTenant]):
        self.__tenants = value

    @property
    def DateCreated(self) -> str:
        return self.__date_created

    @DateCreated.setter
    def DateCreated(self, value: str):
        self.__date_created = value

    @property
    def StreamsContributedCount(self) -> int:
        return self.__streams_contributed_count

    @StreamsContributedCount.setter
    def StreamsContributedCount(self, value: int):
        self.__streams_contributed_count = value

    @property
    def TotalStreamsContributedCount(self) -> int:
        return self.__total_streams_contributed_count

    @TotalStreamsContributedCount.setter
    def TotalStreamsContributedCount(self, value: int):
        self.__total_streams_contributed_count = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Id': self.Id, 'Name': self.Name, 'Alias': self.Alias,
                  'Description': self.Description, 'Tenants': [], 'DateCreated': self.DateCreated,
                  'StreamsContributedCount': self.StreamsContributedCount,
                  'TotalStreamsContributedCount': self.TotalStreamsContributedCount}

        if self.Tenants is not None:
            for value in self.Tenants:
                result['Tenants'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Community()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Alias' in content:
            result.Alias = content['Alias']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Tenants' in content:
            tenants = content['Tenants']
            if tenants is not None and len(tenants) > 0:
                result.Tenants = []
                for value in tenants:
                    result.Tenants.append(CommunityTenant.fromJson(value))

        if 'DateCreated' in content:
            result.DateCreated = content['DateCreated']

        if 'StreamsContributedCount' in content:
            result.StreamsContributedCount = content['StreamsContributedCount']

        if 'TotalStreamsContributedCount' in content:
            result.TotalStreamsContributedCount = content['TotalStreamsContributedCount']

        return result
