from __future__ import annotations
import json

from .SdsStreamViewMode import SdsStreamViewMode


class SdsStreamViewMapProperty(object):
    """Sds StreamViewMap Property definition"""

    def __init__(self, source_id: str = None, target_id: str = None, mode: SdsStreamViewMode = None,
                 sds_stream_view_map: 'SdsStreamViewMap' = None):
        """
        :param source_id: required
        :param target_id: required
        :param mode: not required
        :param sds_stream_view_map: not required
        """
        self.SourceId = source_id
        self.TargetId = target_id
        self.Mode = mode
        self.SdsStreamViewMap = sds_stream_view_map

    @property
    def SourceId(self) -> str:
        """
        required
        :return:
        """
        return self.__source_id

    @SourceId.setter
    def SourceId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__source_id = value

    @property
    def TargetId(self) -> str:
        """
        required
        :return:
        """
        return self.__target_id

    @TargetId.setter
    def TargetId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__target_id = value

    @property
    def Mode(self) -> SdsStreamViewMode:
        """
        not required
        :return:
        """
        return self.__mode

    @Mode.setter
    def Mode(self, value: SdsStreamViewMode):
        """
        not required
        :param value:
        :return:
        """
        self.__mode = value

    @property
    def SdsStreamViewMap(self) -> 'SdsStreamViewMap':
        """
        not required
        :return:
        """
        return self.__sds_stream_view_map

    @SdsStreamViewMap.setter
    def SdsStreamViewMap(self, value: 'SdsStreamViewMap'):
        """
        not required
        :param value:
        :return:
        """
        self.__sds_stream_view_map = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'SourceId': self.SourceId, 'TargetId': self.TargetId}

        if self.Mode is not None:
            result['Mode'] = self.Mode.name

        if self.SdsStreamViewMap is not None:
            result['SdsStreamViewMap'] = self.SdsStreamViewMap.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamViewMapProperty()

        if not content:
            return result

        if 'SourceId' in content:
            result.SourceId = content['SourceId']

        if 'TargetId' in content:
            result.TargetId = content['TargetId']

        if 'Mode' in content:
            mode = content['Mode']
            if mode is not None:
                result.Mode = SdsStreamViewMode(mode)

        if 'SdsStreamViewMap' in content:
            from .SdsStreamViewMap import SdsStreamViewMap
            result.SdsStreamViewMap = SdsStreamViewMap.fromJson(
                content['SdsStreamViewMap'])

        return result
