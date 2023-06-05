from __future__ import annotations
import json

from .EventProperty import EventProperty


class Event(object):
    """ADH Asset definition"""

    def __init__(self, id: str = None, authorizationTags: str = None,
                 eventStartTime: str = None, eventEndTime: str = None, name:str =None):
        """
        """
        self.Id = id
        self.AuthorizationTags = authorizationTags
        self.EventStartTime = eventStartTime
        self.EventEndTime = eventEndTime
        self.Name = name

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
        """"
        required
        :param value:
        :return:
        """
        self.__name = value

    @property
    def AuthorizationTags(self) -> str:
        """
        not required
        :return:
        """
        return self.__authorizationTags

    @AuthorizationTags.setter
    def AuthorizationTags(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__authorizationTags = value

    @property
    def EventStartTime(self) -> str:
        """
        not required
        :return:
        """
        return self.__eventStartTime

    @EventStartTime.setter
    def EventStartTime(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__eventStartTime = value

    @property
    def EventEndTime(self) -> str:
        """
        not required
        :return:
        """
        return self.__eventEndTime

    @EventEndTime.setter
    def EventEndTime(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__eventEndTime = value        

    def toJson(self):
        return json.dumps(self.toDictionary())
    
    def toJsonFulls(self):
        temp = {}
        for att in dir(self):
            if "__" in att:
                continue
            if "fromJson" == att or "toDictionary" == att or "toDictionary" == att or "toJson" == att or "toJsonFulls" == att or "None" == att:
                continue
            if "None" in att:
                continue
            val = getattr(self,att)
            temp[att] = val
         #   print(att +'  ' + str(val))
        return temp

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id}

        # optional properties

        if self.AuthorizationTags is not None:
            result['AuthorizationTags'] = self.AuthorizationTags

        if self.EventStartTime is not None:
            result['EventStartTime'] = self.EventStartTime

        if self.EventEndTime is not None:
            result['EventEndTime'] = self.EventEndTime            

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Event()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'AuthorizationTags' in content:
            result.AuthorizationTags = content['AuthorizationTags']

        if 'EventStartTime' in content:
            result.EventStartTime = content['EventStartTime']

        if 'EventEndTime' in content:
            result.EventEndTime = content['EventEndTime']

        return result
