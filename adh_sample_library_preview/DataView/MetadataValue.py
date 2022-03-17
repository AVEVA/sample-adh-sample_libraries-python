from __future__ import annotations
import json
from typing import Any

from ..SDS.SdsTypeCode import SdsTypeCode


class MetadataValue(object):
    """ADH Metadata Value definition"""

    def __init__(self, name: str = None, value: Any = None, description: str = None,
                 type_code: SdsTypeCode = None, uom: str = None):
        self.Name = name
        self.Value = value
        self.Description = description
        self.TypeCode = type_code
        self.Uom = uom

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Value(self) -> Any:
        return self.__value

    @Value.setter
    def Value(self, value: Any):
        self.__value = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

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

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Name': self.Name, 'Value': self.Value, 'Description': self.Description,
                'TypeCode': self.TypeCode.name, 'Uom': self.Uom}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = MetadataValue()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Value' in content:
            result.Value = content['Value']

        if 'Description' in content:
            result.Description = content['Description']

        if 'TypeCode' in content:
            result.TypeCode = SdsTypeCode[content['TypeCode']]

        if 'Uom' in content:
            result.Uom = content['Uom']

        return result
