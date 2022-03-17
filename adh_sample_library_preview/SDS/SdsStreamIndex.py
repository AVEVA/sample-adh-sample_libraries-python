from __future__ import annotations
import json



class SdsStreamIndex(object):
    """
    Sds Stream Index definitions
    """

    def __init__(self, sds_type_property_id: str = None):
        """
        :param sds_type_property_id: required
        """
        self.SdsTypePropertyId = sds_type_property_id

    @property
    def SdsTypePropertyId(self) -> str:
        """
        required
        :return:
        """
        return self.__sds_type_property_id

    @SdsTypePropertyId.setter
    def SdsTypePropertyId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__sds_type_property_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'SdsTypePropertyId': self.SdsTypePropertyId}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamIndex()

        if not content:
            return result

        if 'SdsTypePropertyId' in content:
            result.SdsTypePropertyId = content['SdsTypePropertyId']

        return result
