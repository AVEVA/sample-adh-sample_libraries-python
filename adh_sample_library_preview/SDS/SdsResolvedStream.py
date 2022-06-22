from __future__ import annotations
import json

from .SdsExtrapolationMode import SdsExtrapolationMode
from .SdsType import SdsType
from .SdsInterpolationMode import SdsInterpolationMode
from .SdsStreamIndex import SdsStreamIndex
from .SdsStreamPropertyOverride import SdsStreamPropertyOverride
from .SdsStream import SdsStream

class SdsResolvedStream(object):
    """Sds resolved stream definition"""

    def __init__(self, id: str, type: SdsType, name: str = None, description: str = None, resolved = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param resolved: required
        :param type: required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.Resolved = resolved
        self.Type = type

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self.__id = value

    @property
    def Name(self) -> str:
        """
        not required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__name = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self.__description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__description = value

    @property
    def Resolved(self) -> bool:
        """
        required
        :return:
        """
        return self.__resolved

    @Resolved.setter
    def Resolved(self, value: bool):
        """
        required
        :param value:
        :return:
        """
        self.__resolved = value

    @property
    def Type(self) -> SdsType:
        """
        not required
        :return:
        """
        return self.__type

    @Type.setter
    def Type(self, value: SdsType):
        """
        not required
        :param value:
        :return:
        """
        self.__type = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id, 'Type': self.Type}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.Indexes is not None:
            result['Indexes'] = []
            for value in self.Indexes:
                result['Indexes'].append(value.toDictionary())

        if self.InterpolationMode is not None:
            result['InterpolationMode'] = self.InterpolationMode.name

        if self.ExtrapolationMode is not None:
            result['ExtrapolationMode'] = self.ExtrapolationMode.name

        if self.PropertyOverrides is not None:
            result['PropertyOverrides'] = []
            for value in self.PropertyOverrides:
                result['PropertyOverrides'].append(
                    value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStream()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Resolved' in content:
            result.Resolved = content['Resolved']

        if 'Type' in content:
            result.Type = content['Type']

        return result
