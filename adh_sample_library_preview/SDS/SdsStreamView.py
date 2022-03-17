from __future__ import annotations
import json

from .SdsStreamViewProperty import SdsStreamViewProperty


class SdsStreamView(object):
    """
    Sds StreamView definitions
    """

    def __init__(self, id: str = None, source_type_id: str = None, target_type_id: str = None,
                 name: str = None, description: str = None,
                 properties: list[SdsStreamViewProperty] = None):
        """
        :param id: required
        :param source_type_id: required
        :param target_type_id: required
        :param name: not required
        :param description: not required
        :param properties: not required
        """
        self.Id = id
        self.SourceTypeId = source_type_id
        self.TargetTypeId = target_type_id
        self.Name = name
        self.Description = description
        self.Properties = properties

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
    def Properties(self) -> list[SdsStreamViewProperty]:
        """
        not required
        :return:
        """
        return self.__properties

    @Properties.setter
    def Properties(self, value: list[SdsStreamViewProperty]):
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
        result = {'Id': self.Id, 'SourceTypeId': self.SourceTypeId,
                  'TargetTypeId': self.TargetTypeId}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.Properties is not None:
            result['Properties'] = []
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamView()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

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
                        SdsStreamViewProperty.fromJson(value))

        return result
