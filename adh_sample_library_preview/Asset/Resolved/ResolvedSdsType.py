from __future__ import annotations
import json

from ...SDS.SdsTypeCode import SdsTypeCode as SdsTypeCodeType
from .ResolvedEnum import ResolvedEnum


class ResolvedSdsType(object):
    def __init__(self, sds_type_code: SdsTypeCodeType = None, properties: list[ResolvedEnum] = None):
        self.SdsTypeCode = sds_type_code
        self.Properties = properties

    @property
    def SdsTypeCode(self) -> SdsTypeCodeType:
        return self.__sds_type_code

    @SdsTypeCode.setter
    def SdsTypeCode(self, value: SdsTypeCodeType):
        self.__sds_type_code = value

    @property
    def Properties(self) -> list[ResolvedEnum]:
        return self.__properties

    @Properties.setter
    def Properties(self, value: list[ResolvedEnum]):
        self.__properties = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'SdsTypeCode': self.SdsTypeCode.name, 'Properties': []}

        if self.Properties is not None:
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedSdsType()

        if not content:
            return result

        if 'SdsTypeCode' in content:
            result.SdsTypeCode = SdsTypeCodeType[content['SdsTypeCode']]

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Properties = []
                for value in properties:
                    result.Properties.append(
                        ResolvedEnum.fromJson(value))

        return result
