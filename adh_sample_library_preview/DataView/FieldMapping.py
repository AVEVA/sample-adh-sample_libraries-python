from __future__ import annotations
import json

from ..SDS.SdsSummaryType import SdsSummaryType
from ..SDS.SdsTypeCode import SdsTypeCode
from .DataMapping import DataMapping
from .FieldKind import FieldKind as FieldKindType
from .SummaryDirection import SummaryDirection as SummaryDirectionType


class FieldMapping(object):
    """ADH Field Mapping definition"""

    def __init__(self, id: str = None, label: str = None, field_kind: FieldKindType = None,
                 data_mappings: list[DataMapping] = None, type_code: SdsTypeCode = None,
                 uom: str = None, summary_type: SdsSummaryType = None,
                 summary_direction: SummaryDirectionType = None):
        self.Id = id
        self.Label = label
        self.FieldKind = field_kind
        self.DataMappings = data_mappings
        self.TypeCode = type_code
        self.Uom = uom
        self.SummaryType = summary_type
        self.SummaryDirection = summary_direction

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Label(self) -> str:
        return self.__label

    @Label.setter
    def Label(self, value: str):
        self.__label = value

    @property
    def FieldKind(self) -> FieldKindType:
        return self.__field_kind

    @FieldKind.setter
    def FieldKind(self, value: FieldKindType):
        self.__field_kind = value

    @property
    def DataMappings(self) -> list[DataMapping]:
        return self.__data_mappings

    @DataMappings.setter
    def DataMappings(self, value: list[DataMapping]):
        self.__data_mappings = value

    @property
    def TypeCode(self) -> SdsTypeCode:
        return self.__type_code

    @TypeCode.setter
    def TypeCode(self, value: SdsTypeCode):
        self.__type_code = value

    @property
    def Uom(self) -> str:
        return self.__uom

    @Uom.setter
    def Uom(self, value: str):
        self.__uom = value

    @property
    def SummaryType(self) -> SdsSummaryType:
        return self.__summary_type

    @SummaryType.setter
    def SummaryType(self, value: SdsSummaryType):
        self.__summary_type = value

    @property
    def SummaryDirection(self) -> SummaryDirectionType:
        return self.__summary_direction

    @SummaryDirection.setter
    def SummaryDirection(self, value: SummaryDirectionType):
        self.__summary_direction = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {}

        # optional properties
        if self.Id is not None:
            result['Id'] = self.Id

        if self.Label is not None:
            result['Label'] = self.Label

        if self.FieldKind is not None:
            result['FieldKind'] = self.FieldKind.name

        if self.DataMappings is not None:
            result['DataMappings'] = []
            for value in self.DataMappings:
                result['DataMappings'].append(value.toDictionary())

        if self.TypeCode is not None:
            result['TypeCode'] = self.TypeCode.name

        if self.Uom is not None:
            result['Uom'] = self.Uom

        if self.SummaryType is not None:
            result['SummaryType'] = self.SummaryType.name

        if self.SummaryDirection is not None:
            result['SummaryDirection'] = self.SummaryDirection.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = FieldMapping()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Label' in content:
            result.Label = content['Label']

        if 'FieldKind' in content:
            result.FieldKind = FieldKindType[content['FieldKind']]

        if 'DataMappings' in content:
            data_mappings = content['DataMappings']
            if data_mappings is not None and len(data_mappings) > 0:
                result.DataMappings = []
                for value in data_mappings:
                    result.DataMappings.append(DataMapping.fromJson(value))

        if 'TypeCode' in content:
            result.TypeCode = SdsTypeCode[content['TypeCode']]

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'SummaryType' in content:
            if content['SummaryType'] == 'None':
                result.SummaryType = SdsSummaryType['none']
            else:
                result.SummaryType = SdsSummaryType[content['SummaryType']]

        if 'SummaryDirection' in content and content['SummaryDirection'] is not None:
            result.SummaryDirection = SummaryDirectionType[content['SummaryDirection']]

        return result
