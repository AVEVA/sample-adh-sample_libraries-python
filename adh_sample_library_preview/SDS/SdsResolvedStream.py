from __future__ import annotations
import json

from .SdsType import SdsType
from .SdsExtrapolationMode import SdsExtrapolationMode
from .SdsInterpolationMode import SdsInterpolationMode
from .SdsStreamIndex import SdsStreamIndex
from .SdsStreamPropertyOverride import SdsStreamPropertyOverride

class SdsResolvedStream(object):
    """Sds resolved stream definition"""

    def __init__(self, id: str = None, type_id: str = None, name: str = None, description: str = None, indexes: list[SdsStreamIndex] = None,
                 interpolation_mode: SdsInterpolationMode = None,
                 extrapolation_mode: SdsExtrapolationMode = None,
                 property_overrides: list[SdsStreamPropertyOverride] = None, 
                 resolved = True, type: SdsType = None):
        """
        :param id: required
        :param type_id: not required
        :param name: not required
        :param description: not required
        :param indexes: array of SdsStreamIndex   not required
        :param interpolation_mode: SdsInterpolationMode   default is null
                                   not required
        :param extrapolation_mode: SdsExtrapolationMode default is null
                                  not required
        :param property_overrides:  array of  SdsStreamPropertyOverride
                                   not required
        :param resolved: not required
        :param type: required
        """
        self.Id = id
        self.TypeId = type_id
        self.Name = name
        self.Description = description
        self.Indexes = indexes
        self.InterpolationMode = interpolation_mode
        self.ExtrapolationMode = extrapolation_mode
        self.PropertyOverrides = property_overrides
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
    def TypeId(self) -> str:
        """
        required
        :return:
        """
        return self.__type_id

    @TypeId.setter
    def TypeId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__type_id = value

    @property
    def Indexes(self) -> list[SdsStreamIndex]:
        """
        not required
        :return:
        """
        return self.__indexes

    @Indexes.setter
    def Indexes(self, value: list[SdsStreamIndex]):
        """
        not required
        :param value:
        :return:
        """
        self.__indexes = value

    @property
    def InterpolationMode(self) -> SdsInterpolationMode:
        """
        not required
        :return:
        """
        return self.__interpolation_mode

    @InterpolationMode.setter
    def InterpolationMode(self, value: SdsInterpolationMode):
        """
        not required
        :param value:
        :return:
        """
        self.__interpolation_mode = value

    @property
    def ExtrapolationMode(self) -> SdsExtrapolationMode:
        """
        not required
        :return:
        """
        return self.__extrapolation_mode

    @ExtrapolationMode.setter
    def ExtrapolationMode(self, value: SdsExtrapolationMode):
        """
        not required
        :param value:
        :return:
        """
        self.__extrapolation_mode = value

    @property
    def PropertyOverrides(self) -> list[SdsStreamPropertyOverride]:
        """
        not required
        :return:
        """
        return self.__property_overrides

    @PropertyOverrides.setter
    def PropertyOverrides(self, value: list[SdsStreamPropertyOverride]):
        """
        not required
        :param value:
        :return:
        """
        self.__property_overrides = value

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
        result = {}

        if self.Id is not None:
            result['Id'] = self.Id

        if self.TypeId is not None:
            result['TypeId'] = self.TypeId

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

        if self.Resolved is not None:
            result['Resolved'] = self.Resolved
            
        if self.Type is not None:
            result['Type'] = self.Type.toDictionary()
        
        return result


    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsResolvedStream()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'TypeId' in content:
            result.TypeId = content['TypeId']

        if 'Indexes' in content:
            indexes = content['Indexes']
            if indexes is not None and len(indexes) > 0:
                result.Indexes = []
                for value in indexes:
                    result.Indexes.append(SdsStreamIndex.fromJson(value))

        if 'InterpolationMode' in content:
            interpolation_mode = content['InterpolationMode']
            if interpolation_mode is not None:
                result.InterpolationMode = SdsInterpolationMode[interpolation_mode]

        if 'ExtrapolationMode' in content:
            extrapolation_mode = content['ExtrapolationMode']
            if extrapolation_mode is not None:
                result.ExtrapolationMode = SdsExtrapolationMode[extrapolation_mode]

        if 'PropertyOverrides' in content:
            property_overrides = content['PropertyOverrides']
            if property_overrides is not None and len(property_overrides) > 0:
                result.PropertyOverrides = []
                for value in property_overrides:
                    result.PropertyOverrides.append(
                        SdsStreamPropertyOverride.fromJson(value))

        if 'Resolved' in content:
            result.Resolved = content['Resolved']

        if 'Type' in content:
            result.Type = SdsType.fromJson(content['Type'])

        return result
