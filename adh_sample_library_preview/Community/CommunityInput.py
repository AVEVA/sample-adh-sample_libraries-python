from __future__ import annotations
import json


class CommunityInput(object):
    """ADH community input definition"""

    def __init__(
        self,
        name: str = None,
        description: str = None,
        preferred_region_id: str = None,
        contact_email: str = None,
    ):
        self.Name = name
        self.Description = description
        self.PreferredRegionId = preferred_region_id
        self.ContactEmail = contact_email

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def PreferredRegionId(self) -> str:
        return self.__preferred_region_id

    @PreferredRegionId.setter
    def PreferredRegionId(self, value: str):
        self.__preferred_region_id = value

    @property
    def ContactEmail(self) -> str:
        return self.__contact_email

    @ContactEmail.setter
    def ContactEmail(self, value: str):
        self.__contact_email = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}

        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.PreferredRegionId is not None:
            result['PreferredRegionId'] = self.PreferredRegionId

        if self.ContactEmail is not None:
            result['ContactEmail'] = self.ContactEmail

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = CommunityInput()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'PreferredRegionId' in content:
            result.PreferredRegionId = content['PreferredRegionId']

        if 'ContactEmail' in content:
            result.ContactEmail = content['ContactEmail']

        return result
