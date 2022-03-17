from __future__ import annotations
import json
from enum import Enum
from typing import Any


from .SdsInterpolationMode import SdsInterpolationMode


class SdsTypeProperty(object):
    """
    Sds type property definition
    """

    def __init__(self, id: str = None, is_key: bool = None, sds_type: 'SdsType' = None,
                 name: str = None, description: str = None, order: int = None,
                 fixed_size: int = None, value: Any = None, uom: str = None,
                 interpolation_mode: SdsInterpolationMode = None):
        """
        :param id: required
        :param is_key: required
        :param sds_type: required
        :param name: not required
        :param description: not required
        :param order: not required
        :param fixed_size: not required
        :param value: not required
        :param uom: not required
        :param interpolation_mode: not required
        """
        self.Id = id
        self.IsKey = is_key
        self.SdsType = sds_type
        self.Name = name
        self.Description = description
        self.Order = order
        self.FixedSize = fixed_size
        self.Value = value
        self.Uom = uom
        self.InterpolationMode = interpolation_mode

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
    def Order(self) -> int:
        """
        not required
        :return:
        """
        return self.__order

    @Order.setter
    def Order(self, value: int):
        """
        not required
        :param value:
        :return:
        """
        self.__order = value

    @property
    def IsKey(self) -> bool:
        """
        required
        :return:
        """
        return self.__is_key

    @IsKey.setter
    def IsKey(self, value: bool):
        """
        required
        :param value:
        :return:
        """
        self.__is_key = value

    @property
    def FixedSize(self) -> int:
        """
        not required
        :return:
        """
        return self.__fixed_size

    @FixedSize.setter
    def FixedSize(self, value: int):
        """
        not required
        :param value:
        :return:
        """
        self.__fixed_size = value

    @property
    def SdsType(self) -> 'SdsType':
        """
        required
        :return:
        """
        return self.__sds_type

    @SdsType.setter
    def SdsType(self, value: 'SdsType'):
        """
        required
        :param value:
        :return:
        """
        self.__sds_type = value

    @property
    def Value(self) -> Any:
        """
        not required
        :return:
        """
        return self.__value

    @Value.setter
    def Value(self, value: Any):
        """
        not required
        :param value:
        :return:
        """
        self.__value = value

    @property
    def Uom(self) -> str:
        """
        not required
        :return:
        """
        return self.__uom

    @Uom.setter
    def Uom(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__uom = value

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

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id, 'IsKey': self.IsKey,
                  'SdsType': self.SdsType.toDictionary()}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.Order is not None:
            result['Order'] = self.Order

        if self.FixedSize is not None:
            result['FixedSize'] = self.FixedSize

        if self.Value is not None:
            if (isinstance(self.Value, Enum)):
                result['Value'] = self.Value.name
            else:
                result['Value'] = self.Value

        if self.Uom is not None:
            result['Uom'] = self.Uom

        if self.InterpolationMode is not None:
            result['InterpolationMode'] = self.InterpolationMode.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsTypeProperty()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Order' in content:
            result.Order = content['Order']

        if 'IsKey' in content:
            result.IsKey = content['IsKey']

        if 'FixedSize' in content:
            result.FixedSize = content['FixedSize']

        if 'SdsType' in content:
            from .SdsType import SdsType
            result.SdsType = SdsType.fromJson(content['SdsType'])

        if 'Value' in content:
            result.Value = content['Value']

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'InterpolationMode' in content:
            interpolation_mode = content['InterpolationMode']
            if interpolation_mode is not None:
                result.InterpolationMode = SdsInterpolationMode(
                    interpolation_mode)

        return result
