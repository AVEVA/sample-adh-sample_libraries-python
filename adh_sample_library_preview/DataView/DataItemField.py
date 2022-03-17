from __future__ import annotations
import json

from ..SDS.SdsTypeCode import SdsTypeCode


class DataItemField(object):
    """ADH Data Item Field definition"""

    def __init__(self, id: str = None, name: str = None, type_code: SdsTypeCode = None,
                 uom: str = None, is_key: bool = None, stream_reference_name: str = None):
        self.Id = id
        self.Name = name
        self.TypeCode = type_code
        self.Uom = uom
        self.IsKey = is_key
        self.StreamReferenceName = stream_reference_name

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

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
    def IsKey(self) -> bool:
        return self.__is_key

    @IsKey.setter
    def IsKey(self, value: bool):
        self.__is_key = value

    @property
    def StreamReferenceName(self) -> str:
        return self.__stream_reference_name

    @StreamReferenceName.setter
    def StreamReferenceName(self, value: str):
        self.__stream_reference_name = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Id': self.Id, 'Name': self.Name, 'TypeCode': self.TypeCode.name, 'Uom': self.Uom,
                'IsKey': self.IsKey, 'StreamReferenceName': self.StreamReferenceName}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataItemField()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'TypeCode' in content:
            result.TypeCode = SdsTypeCode[content['TypeCode']]

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'IsKey' in content:
            result.IsKey = content['IsKey']

        if 'StreamReferenceName' in content:
            result.StreamReferenceName = content['StreamReferenceName']

        return result
