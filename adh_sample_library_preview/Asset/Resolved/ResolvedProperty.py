from __future__ import annotations
import json

from ...SDS.SdsInterpolationMode import SdsInterpolationMode
from ...SDS.SdsExtrapolationMode import SdsExtrapolationMode
from .ResolvedSource import ResolvedSource
from .ResolvedSdsType import ResolvedSdsType


class ResolvedProperty(object):
    def __init__(self, id: str = None, is_key: bool = None, uom: str = None, order: int = None,
                 interpolation_mode: SdsInterpolationMode = None,
                 extrapolation_mode: SdsExtrapolationMode = None, sds_type: ResolvedSdsType = None,
                 source: ResolvedSource = None):
        self.Id = id
        self.IsKey = is_key
        self.Uom = uom
        self.Order = order
        self.InterpolationMode = interpolation_mode
        self.ExtrapolationMode = extrapolation_mode
        self.SdsType = sds_type
        self.Source = source

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def IsKey(self) -> bool:
        return self.__is_key

    @IsKey.setter
    def IsKey(self, value: bool):
        self.__is_key = value

    @property
    def Uom(self) -> str:
        return self.__uom

    @Uom.setter
    def Uom(self, value: str):
        self.__uom = value

    @property
    def Order(self) -> int:
        return self.__order

    @Order.setter
    def Order(self, value: int):
        self.__order = value

    @property
    def InterpolationMode(self) -> SdsInterpolationMode:
        return self.__interpolation_mode

    @InterpolationMode.setter
    def InterpolationMode(self, value: SdsInterpolationMode):
        self.__interpolation_mode = value

    @property
    def ExtrapolationMode(self) -> SdsExtrapolationMode:
        return self.__extrapolation_mode

    @ExtrapolationMode.setter
    def ExtrapolationMode(self, value: SdsExtrapolationMode):
        self.__extrapolation_mode = value

    @property
    def SdsType(self) -> ResolvedSdsType:
        return self.__sds_type

    @SdsType.setter
    def SdsType(self, value: ResolvedSdsType):
        self.__sds_type = value

    @property
    def Source(self) -> ResolvedSource:
        return self.__source

    @Source.setter
    def Source(self, value: ResolvedSource):
        self.__source = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Id': self.Id, 'IsKey': self.IsKey, 'Uom': self.Uom, 'Order': self.Order,
                'InterpolationMode': self.InterpolationMode.name,
                'ExtrapolationMode': self.ExtrapolationMode.name,
                'SdsType': self.SdsType.toDictionary(), 'Source': self.Source.toDictionary()}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedProperty()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'IsKey' in content:
            result.IsKey = content['IsKey']

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'Order' in content:
            result.Order = content['Order']

        if 'InterpolationMode' in content:
            result.InterpolationMode = SdsInterpolationMode(
                content['InterpolationMode'])

        if 'ExtrapolationMode' in content:
            result.ExtrapolationMode = SdsExtrapolationMode(
                content['ExtrapolationMode'])

        if 'SdsType' in content:
            result.SdsType = ResolvedSdsType.fromJson(
                content['SdsType'])

        if 'Source' in content:
            result.Source = ResolvedSource.fromJson(
                content['Source'])

        return result
