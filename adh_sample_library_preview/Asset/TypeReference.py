from __future__ import annotations
import json


class TypeReference(object):
    """ADH Asset Type Type Reference definition"""

    def __init__(self, stream_reference_id: str = None, stream_reference_name: str = None,
                 type_id: str = None, description: str = None):
        """
        :param stream_reference_id: required
        :param stream_reference_name: required
        :param type_id: required
        :param description: not required
        """
        self.StreamReferenceId = stream_reference_id
        self.StreamReferenceName = stream_reference_name
        self.TypeId = type_id
        self.Description = description

    @property
    def StreamReferenceId(self) -> str:
        """
        required
        :return:
        """
        return self.__stream_reference_id

    @StreamReferenceId.setter
    def StreamReferenceId(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self.__stream_reference_id = value

    @property
    def StreamReferenceName(self) -> str:
        """
        required
        :return:
        """
        return self.__stream_reference_name

    @StreamReferenceName.setter
    def StreamReferenceName(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__stream_reference_name = value

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
    def TypeId(self) -> str:
        """
        required
        :return:
        """
        return self.__type_id

    @TypeId.setter
    def TypeId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__type_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {
            'StreamReferenceId': self.StreamReferenceId,
            'StreamReferenceName': self.StreamReferenceName,
            'TypeId': self.TypeId
        }

        # optional properties
        if self.Description is not None:
            result['Description'] = self.Description

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = TypeReference()

        if not content:
            return result

        if 'StreamReferenceId' in content:
            result.StreamReferenceId = content['StreamReferenceId']

        if 'StreamReferenceName' in content:
            result.StreamReferenceName = content['StreamReferenceName']

        if 'Description' in content:
            result.Description = content['Description']

        if 'TypeId' in content:
            result.TypeId = content['TypeId']

        return result
