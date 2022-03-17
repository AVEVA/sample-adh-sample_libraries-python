from __future__ import annotations
import json

from .ValueStatusMapping import ValueStatusMapping


class StatusMapping(object):
    """ADH Asset Status Mapping definition"""

    def __init__(self, stream_reference_id: str = None, stream_property_id: str = None,
                 value_status_mappings: list[ValueStatusMapping] = None):
        """
        :param stream_reference_id: required
        :param stream_property_id: required
        :param value_status_mappings: required
        """
        self.StreamReferenceId = stream_reference_id
        self.StreamPropertyId = stream_property_id
        self.ValueStatusMappings = value_status_mappings

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
    def StreamPropertyId(self) -> str:
        """
        required
        :return:
        """
        return self.__stream_property_id

    @StreamPropertyId.setter
    def StreamPropertyId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__stream_property_id = value

    @property
    def ValueStatusMappings(self) -> list[ValueStatusMapping]:
        """
        required
        :return:
        """
        return self.__value_status_mappings

    @ValueStatusMappings.setter
    def ValueStatusMappings(self, value: list[ValueStatusMapping]):
        """
        required
        :param value:
        :return:
        """
        self.__value_status_mappings = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'StreamReferenceId': self.StreamReferenceId,
                  'StreamPropertyId': self.StreamPropertyId, 'ValueStatusMappings': []}

        if self.ValueStatusMappings is not None:
            for value in self.ValueStatusMappings:
                result['ValueStatusMappings'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = StatusMapping()

        if not content:
            return result

        if 'StreamReferenceId' in content:
            result.StreamReferenceId = content['StreamReferenceId']

        if 'StreamPropertyId' in content:
            result.StreamPropertyId = content['StreamPropertyId']

        if 'ValueStatusMappings' in content:
            value_status_mappings = content['ValueStatusMappings']
            if value_status_mappings is not None and len(value_status_mappings) > 0:
                result.ValueStatusMappings = []
                for value in value_status_mappings:
                    result.ValueStatusMappings.append(
                        ValueStatusMapping.fromJson(value))

        return result
