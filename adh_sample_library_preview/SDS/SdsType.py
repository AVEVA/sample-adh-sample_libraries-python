from __future__ import annotations  # To type hint the enclosing class
import json

from .SdsExtrapolationMode import SdsExtrapolationMode
from .SdsInterpolationMode import SdsInterpolationMode
from .SdsTypeCode import SdsTypeCode as SdsTypeCodeType
from .SdsTypeProperty import SdsTypeProperty


class SdsType(object):
    """Sds type definitions"""

    def __init__(self, id: str = None, sds_type_code: SdsTypeCodeType = None,
                 properties: list[SdsTypeProperty] = None, name: str = None,
                 description: str = None, is_generic_type: bool = None,
                 is_reference_type: bool = None, generic_arguments: list[SdsType] = None,
                 base_type: SdsType = None, derived_types: list[SdsType] = None,
                 interpolation_mode: SdsInterpolationMode = None,
                 extrapolation_mode: SdsExtrapolationMode = None):
        """
        :param id: required
        :param sds_type_code: required
        :param properties: required
        :param name: not required
        :param description: not required
        :param is_generic_type: not required
        :param is_reference_type: not required
        :param generic_arguments: not required
        :param base_type: not required
        :param derived_types: not required
        :param interpolation_mode: not required
        :param extrapolation_mode: not required
        """
        self.Id = id
        self.SdsTypeCode = sds_type_code
        self.Properties = properties
        self.Name = name
        self.Description = description
        self.IsGenericType = is_generic_type
        self.IsReferenceType = is_reference_type
        self.GenericArguments = generic_arguments
        self.BaseType = base_type
        self.DerivedTypes = derived_types
        self.InterpolationMode = interpolation_mode
        self.ExtrapolationMode = extrapolation_mode

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """
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
    def SdsTypeCode(self) -> SdsTypeCodeType:
        """
        required
        :return:
        """
        return self.__type_code

    @SdsTypeCode.setter
    def SdsTypeCode(self, value: SdsTypeCodeType):
        """
        required
        :param value:
        :return:
        """
        self.__type_code = value

    @property
    def IsGenericType(self) -> bool:
        """
        not required
        :return:
        """
        return self.__is_generic_type

    @IsGenericType.setter
    def IsGenericType(self, value: bool):
        """
        not required
        :param value:
        :return:
        """
        self.__is_generic_type = value

    @property
    def IsReferenceType(self) -> bool:
        """
        not required
        :return:
        """
        return self.__is_reference_type

    @IsReferenceType.setter
    def IsReferenceType(self, value: bool):
        """
        not required
        :param value:
        :return:
        """
        self.__is_reference_type = value

    @property
    def GenericArguments(self) -> list[SdsType]:
        """
        not required
        :return:
        """
        return self.__generic_arguments

    @GenericArguments.setter
    def GenericArguments(self, value: list[SdsType]):
        """
        not required
        :param value:
        :return:
        """
        self.__generic_arguments = value

    @property
    def Properties(self) -> list[SdsTypeProperty]:
        """
        required
        :return:
        """
        return self.__properties

    @Properties.setter
    def Properties(self, value: list[SdsTypeProperty]):
        """
        required
        :param value:
        :return:
        """
        self.__properties = value

    @property
    def BaseType(self) -> SdsType:
        """
        not required
        :return:
        """
        return self.__base_type

    @BaseType.setter
    def BaseType(self, value: SdsType):
        """
        not required
        :param value:
        :return:
        """
        self.__base_type = value

    @property
    def DerivedTypes(self) -> list[SdsType]:
        """
        not required
        :return:
        """
        return self.__base_types

    @DerivedTypes.setter
    def DerivedTypes(self, value: list[SdsType]):
        """
        not required
        :param value:
        :return:
        """
        self.__base_types = value

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

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id,
                  'SdsTypeCode': self.SdsTypeCode.name, 'Properties': []}
        if self.Properties is not None:
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.IsGenericType is not None:
            result['IsGenericType'] = self.IsGenericType

        if self.IsReferenceType is not None:
            result['IsReferenceType'] = self.IsReferenceType

        if self.GenericArguments is not None:
            result['GenericArguments'] = []
            for value in self.GenericArguments:
                result['GenericArguments'].append(value.toDictionary())

        if self.BaseType is not None:
            result['BaseType'] = self.BaseType.toDictionary()

        if self.DerivedTypes is not None:
            result['DerivedTypes'] = []
            for value in self.DerivedTypes:
                result['DerivedTypes'].append(value.toDictionary())

        if self.InterpolationMode is not None:
            result['InterpolationMode'] = self.InterpolationMode.name

        if self.ExtrapolationMode is not None:
            result['ExtrapolationMode'] = self.ExtrapolationMode.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsType()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'SdsTypeCode' in content and type(content['SdsTypeCode']) == int:
            result.SdsTypeCode = SdsTypeCodeType(content['SdsTypeCode'])
        elif 'SdsTypeCode' in content and type(content['SdsTypeCode']) == str:
            result.SdsTypeCode = SdsTypeCodeType[content['SdsTypeCode']]

        if 'IsGenericType' in content:
            result.IsGenericType = content['IsGenericType']

        if 'IsReferenceType' in content:
            result.IsReferenceType = content['IsReferenceType']

        if 'GenericArguments' in content:
            generic_arguments = content['GenericArguments']
            if generic_arguments is not None and len(generic_arguments) > 0:
                result.GenericArguments = []
                for value in generic_arguments:
                    result.GenericArguments.append(SdsType.fromJson(value))

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Properties = []
                for value in properties:
                    result.Properties.append(SdsTypeProperty.fromJson(value))

        if 'BaseType' in content:
            result.BaseType = SdsType.fromJson(content['BaseType'])

        if 'DerivedTypes' in content:
            derived_types = content['DerivedTypes']
            if derived_types is not None and len(derived_types) > 0:
                result.DerivedTypes = []
                for value in derived_types:
                    result.DerivedTypes.append(SdsType.fromJson(value))

        if 'InterpolationMode' in content:
            interpolation_mode = content['InterpolationMode']
            if interpolation_mode is not None:
                if type(interpolation_mode) == int:
                    result.InterpolationMode = SdsInterpolationMode(
                        interpolation_mode)
                elif type(interpolation_mode) == str:
                    result.InterpolationMode = SdsInterpolationMode[
                        interpolation_mode]

        if 'ExtrapolationMode' in content:
            extrapolation_mode = content['ExtrapolationMode']
            if extrapolation_mode is not None:
                if type(extrapolation_mode) == int:
                    result.ExtrapolationMode = SdsExtrapolationMode(
                        extrapolation_mode)
                elif type(extrapolation_mode) == str:
                    result.ExtrapolationMode = SdsExtrapolationMode[
                        extrapolation_mode]

        return result
