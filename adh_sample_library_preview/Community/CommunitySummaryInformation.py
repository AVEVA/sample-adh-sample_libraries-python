from __future__ import annotations
import json


class CommunitySummaryInformation(object):
    """ADH community summary information definition"""

    def __init__(self, total_streams: int = None, streams_contributed: int = None):
        self.TotalStreams = total_streams
        self.StreamsContributed = streams_contributed

    @property
    def TotalStreams(self) -> int:
        return self.__total_streams

    @TotalStreams.setter
    def TotalStreams(self, value: int):
        self.__total_streams = value

    @property
    def StreamsContributed(self) -> int:
        return self.__streams_contributed

    @StreamsContributed.setter
    def StreamsContributed(self, value: int):
        self.__streams_contributed = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'TotalStreams': self.TotalStreams, 'StreamsContributed': self.StreamsContributed}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = CommunitySummaryInformation()

        if not content:
            return result

        if 'TotalStreams' in content:
            result.TotalStreams = content['TotalStreams']

        if 'StreamsContributed' in content:
            result.StreamsContributed = content['StreamsContributed']

        return result
