from __future__ import annotations
import json

from ..SDS.SdsTypeCode import SdsTypeCode as SdsTypeCodeType


class MetadataItem(object):
    """ADH Asset Metadata Item definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 sds_type_code: SdsTypeCodeType = None, uom: str = None, value: str = None):
        """
        :param id: required
        :param name: required
        :param description: not required
        :param sds_type_code: not required
        :param uom: not required
        :param value: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.SdsTypeCode = sds_type_code
        self.Uom = uom
        self.Value = value

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
        required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        required
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
        not required
        :return:
        """
        return self.__sds_type_code

    @SdsTypeCode.setter
    def SdsTypeCode(self, value: SdsTypeCodeType):
        """
        not required
        :param value:
        :return:
        """
        self.__sds_type_code = value

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
    def Value(self) -> str:
        """
        not required
        :return:
        """
        return self.__value

    @Value.setter
    def Value(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__value = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id, 'Name': self.Name}

        # optional properties
        if self.Description is not None:
            result['Description'] = self.Description

        if self.SdsTypeCode is not None:
            result['SdsTypeCode'] = self.SdsTypeCode.name

        if self.Uom is not None:
            result['Uom'] = self.Uom

        if self.Value is not None:
            result['Value'] = self.Value

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = MetadataItem()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'SdsTypeCode' in content:
            sds_type_code = content['SdsTypeCode']
            if sds_type_code is not None:
                result.SdsTypeCode = SdsTypeCodeType[sds_type_code]

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'Value' in content:
            result.Value = content['Value']

        return result
