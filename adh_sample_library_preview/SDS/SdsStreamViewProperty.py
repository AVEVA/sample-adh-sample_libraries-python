from __future__ import annotations
import json


class SdsStreamViewProperty(object):
    """Sds StreamView Property definition"""

    def __init__(self, source_id: str = None, target_id: str = None,
                 sds_stream_view: 'SdsStreamView' = None):
        """
        :param source_id: required
        :param target_id: required
        :param sds_stream_view: not required
        """
        self.SourceId = source_id
        self.TargetId = target_id
        self.SdsStreamView = sds_stream_view

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
    def SdsStreamView(self) -> 'SdsStreamView':
        """
        not required
        :return:
        """
        return self.__sds_stream_view

    @SdsStreamView.setter
    def SdsStreamView(self, value: 'SdsStreamView'):
        """
        not required
        :param value:
        :return:
        """
        self.__sds_stream_view = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'SourceId': self.SourceId, 'TargetId': self.TargetId}

        if self.SdsStreamView is not None:
            result['SdsStreamView'] = self.SdsStreamView.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamViewProperty()

        if not content:
            return result

        if 'SourceId' in content:
            result.SourceId = content['SourceId']

        if 'TargetId' in content:
            result.TargetId = content['TargetId']

        if 'SdsStreamView' in content:
            from .SdsStreamView import SdsStreamView
            result.SdsStreamView = SdsStreamView.fromJson(
                content['SdsStreamView'])

        return result
