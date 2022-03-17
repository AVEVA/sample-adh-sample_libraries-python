from __future__ import annotations
import json

from ..SDS.SdsTypeCode import SdsTypeCode
from ..SDS.SdsSummaryType import SdsSummaryType
from .SummaryDirection import SummaryDirection as SummaryDirectionType


class DataMapping(object):
    """ADH Data Mapping definition"""

    def __init__(self, target_id: str = None, target_stream_reference_name: str = None,
                 target_field_key: str = None, type_code: SdsTypeCode = None, uom: str = None,
                 summary_type: SdsSummaryType = None,
                 summary_direction: SummaryDirectionType = None, field_set_index: int = None,
                 field_index: int = None):
        self.TargetId = target_id
        self.TargetStreamReferenceName = target_stream_reference_name
        self.TargetFieldKey = target_field_key
        self.TypeCode = type_code
        self.Uom = uom
        self.SummaryType = summary_type
        self.SummaryDirection = summary_direction
        self.FieldSetIndex = field_set_index
        self.FieldIndex = field_index

    @property
    def TargetId(self) -> str:
        return self.__target_id

    @TargetId.setter
    def TargetId(self, value: str):
        self.__target_id = value

    @property
    def TargetStreamReferenceName(self) -> str:
        return self.__target_stream_reference_name

    @TargetStreamReferenceName.setter
    def TargetStreamReferenceName(self, value: str):
        self.__target_stream_reference_name = value

    @property
    def TargetFieldKey(self) -> str:
        return self.__target_field_key

    @TargetFieldKey.setter
    def TargetFieldKey(self, value: str):
        self.__target_field_key = value

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

    @property
    def FieldSetIndex(self) -> int:
        return self.__field_set_index

    @FieldSetIndex.setter
    def FieldSetIndex(self, value: int):
        self.__field_set_index = value

    @property
    def FieldIndex(self) -> int:
        return self.__field_index

    @FieldIndex.setter
    def FieldIndex(self, value: int):
        self.__field_index = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'TargetId': self.TargetId,
                  'TargetStreamReferenceName': self.TargetStreamReferenceName,
                  'TargetFieldKey': self.TargetFieldKey, 'TypeCode': self.TypeCode.name,
                  'Uom': self.Uom, 'SummaryType': self.SummaryType.name}

        if self.SummaryDirection is not None:
            result['SummaryDirection'] = self.SummaryDirection.name

        if self.FieldSetIndex is not None:
            result['FieldSetIndex'] = self.FieldSetIndex

        if self.FieldIndex is not None:
            result['FieldIndex'] = self.FieldIndex

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataMapping()

        if not content:
            return result

        if 'TargetId' in content:
            result.TargetId = content['TargetId']

        if 'TargetStreamReferenceName' in content:
            result.TargetStreamReferenceName = content['TargetStreamReferenceName']

        if 'TargetFieldKey' in content:
            result.TargetFieldKey = content['TargetFieldKey']

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

        if 'FieldSetIndex' in content:
            result.FieldSetIndex = content['FieldSetIndex']

        if 'FieldIndex' in content:
            result.FieldIndex = content['FieldIndex']

        return result
