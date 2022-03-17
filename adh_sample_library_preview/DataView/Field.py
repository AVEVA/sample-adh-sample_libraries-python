from __future__ import annotations
import json

from .FieldSource import FieldSource
from ..SDS.SdsSummaryType import SdsSummaryType
from .SummaryDirection import SummaryDirection as SummaryDirectionType


class Field(object):
    """ADH Field definition"""

    def __init__(self, source: FieldSource = None, keys: list[str] = None,
                 stream_reference_names: list[str] = None, label: str = None,
                 include_uom: bool = None, summary_type: SdsSummaryType = None,
                 summary_direction: SummaryDirectionType = None):
        """
        :param source: not required
        :param keys: not required
        :param stream_reference_names: not required
        :param label: not required
        :param include_uom: not required
        :param summary_type: not required
        :param summary_direction: not required
        """
        self.Source = source
        self.Keys = keys
        self.StreamReferenceNames = stream_reference_names
        self.Label = label
        self.IncludeUom = include_uom
        self.SummaryType = summary_type
        self.SummaryDirection = summary_direction

    @property
    def Source(self) -> FieldSource:
        """
        not required
        :return:
        """
        return self.__source

    @Source.setter
    def Source(self, value: FieldSource):
        """
        not required
        :param value:
        :return:
        """
        self.__source = value

    @property
    def Keys(self) -> list[str]:
        """
        not required
        :return:
        """
        return self.__keys

    @Keys.setter
    def Keys(self, value: list[str]):
        """
        not required
        :param value:
        :return:
        """
        self.__keys = value

    @property
    def StreamReferenceNames(self) -> list[str]:
        """
        not required
        :return:
        """
        return self.__stream_reference_names

    @StreamReferenceNames.setter
    def StreamReferenceNames(self, value: list[str]):
        """
        not required
        :param value:
        :return:
        """
        self.__stream_reference_names = value

    @property
    def Label(self) -> str:
        """
        not required
        :return:
        """
        return self.__label

    @Label.setter
    def Label(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__label = value

    @property
    def IncludeUom(self) -> bool:
        """
        not required
        :return:
        """
        return self.__include_uom

    @IncludeUom.setter
    def IncludeUom(self, value: bool):
        """
        not required
        :param value:
        :return:
        """
        self.__include_uom = value

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

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {}

        # optional properties
        if self.Source is not None:
            result['Source'] = self.Source.name

        if self.Keys is not None:
            result['Keys'] = []
            for value in self.Keys:
                result['Keys'].append(value)

        if self.StreamReferenceNames is not None:
            result['StreamReferenceNames'] = []
            for value in self.StreamReferenceNames:
                result['StreamReferenceNames'].append(value)

        if self.Label is not None:
            result['Label'] = self.Label

        if self.IncludeUom is not None:
            result['IncludeUom'] = self.IncludeUom

        if self.SummaryDirection is not None:
            result['SummaryDirection'] = self.SummaryDirection.name

        if self.SummaryType is not None:
            result['SummaryType'] = self.SummaryType.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Field()

        if not content:
            return result

        if 'Source' in content:
            source = content['Source']
            if source is not None:
                result.Source = FieldSource[source]

        if 'Keys' in content:
            keys = content['Keys']
            if keys is not None and len(keys) > 0:
                result.Keys = []
                for value in keys:
                    result.Keys.append(value)

        if 'StreamReferenceNames' in content:
            stream_reference_names = content['StreamReferenceNames']
            if stream_reference_names is not None and len(stream_reference_names) > 0:
                result.StreamReferenceNames = []
                for value in stream_reference_names:
                    result.StreamReferenceNames.append(value)

        if 'Label' in content:
            result.Label = content['Label']

        if 'IncludeUom' in content:
            result.IncludeUom = content['IncludeUom']

        if 'SummaryType' in content:
            if content['SummaryType'] == 'None':
                result.SummaryType = SdsSummaryType['none']
            else:
                result.SummaryType = SdsSummaryType[content['SummaryType']]

        if 'SummaryDirection' in content and content['SummaryDirection'] is not None:
            result.SummaryDirection = SummaryDirectionType[content['SummaryDirection']]

        return result
