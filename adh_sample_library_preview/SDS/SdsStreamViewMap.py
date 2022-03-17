from __future__ import annotations
import json


from .SdsStreamViewMapProperty import SdsStreamViewMapProperty


class SdsStreamViewMap(object):
    """
    SdsStreamViewMap definitions
    """

    def __init__(self, source_type_id: str = None, target_type_id: str = None,
                 properties: list[SdsStreamViewMapProperty] = None):
        """
        :param source_type_id: required
        :param target_type_id: required
        :param properties: not required
        """
        self.SourceTypeId = source_type_id
        self.TargetTypeId = target_type_id
        self.Properties = properties

    @property
    def SourceTypeId(self) -> str:
        """
        required
        :return:
        """
        return self.__source_type_id

    @SourceTypeId.setter
    def SourceTypeId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__source_type_id = value

    @property
    def TargetTypeId(self) -> str:
        """
        required
        :return:
        """
        return self.__target_type_id

    @TargetTypeId.setter
    def TargetTypeId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__target_type_id = value

    @property
    def Properties(self) -> list[SdsStreamViewMapProperty]:
        """
        not required
        :return:
        """
        return self.__properties

    @Properties.setter
    def Properties(self, value: list[SdsStreamViewMapProperty]):
        """
        not required
        :param value:
        :return:
        """
        self.__properties = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'SourceTypeId': self.SourceTypeId,
                  'TargetTypeId': self.TargetTypeId}

        # optional properties
        if self.Properties is not None:
            result['Properties'] = []
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamViewMap()

        if not content:
            return result

        if 'TargetTypeId' in content:
            result.TargetTypeId = content['TargetTypeId']

        if 'SourceTypeId' in content:
            result.SourceTypeId = content['SourceTypeId']

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Properties = []
                for value in properties:
                    result.Properties.append(
                        SdsStreamViewMapProperty.fromJson(value))

        return result
