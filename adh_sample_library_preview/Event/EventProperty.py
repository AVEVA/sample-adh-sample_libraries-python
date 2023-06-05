from __future__ import annotations
import json


class EventProperty(object):
    """ADH Asset definition"""

    def __init__(self, id: str = None, name: str = None, propertyTypeCode: str = None,
                 graphQLName: str = None, flags: str = None,
                 state: str = None):
        """
        """
        self.Id = id
        self.Name = name
        self.PropertyTypeCode = propertyTypeCode
        self.GraphQLName = graphQLName
        self.Flags = flags
        self.State = state

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
    def PropertyTypeCode(self) -> str:
        """
        not required
        :return:
        """
        return self.__propertyTypeCode

    @PropertyTypeCode.setter
    def PropertyTypeCode(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__propertyTypeCode = value

    @property
    def GraphQLName(self) -> str:
        """
        not required
        :return:
        """
        return self.__graphQLName

    @GraphQLName.setter
    def GraphQLName(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__graphQLName = value

    @property
    def Flags(self) -> str:
        """
        not required
        :return:
        """
        return self.__flags

    @Flags.setter
    def Flags(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__flags = value

    @property
    def State(self) -> str:
        """
        not required
        :return:
        """
        return self.__state

    @State.setter
    def State(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__state = value



    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.PropertyTypeCode is not None:
            result['PropertyTypeCode'] = self.PropertyTypeCode

        if self.Flags is not None:
            result['Flags'] = self.Flags

        if self.State is not None:
            result['State'] = self.State

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = EventProperty()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'PropertyTypeCode' in content:
            result.PropertyTypeCode = content['PropertyTypeCode']

        if 'Flags' in content:
            result.Flags = content['Flags']

        if 'State' in content:
            result.State = content['State']        

        return result
