from __future__ import annotations
import json

from .EventProperty import EventProperty


class EventType(object):
    """ADH Asset definition"""

    def __init__(self, id: str = None, name: str = None, defaultAuthorizationTag: str = None,
                 graphQLName: str = None, version: int = 1, state: str = "Active", createdDate: str = None,
                 modifiedDate: str = None,  properties: list[EventProperty] = []):
        """
        """
        self.Id = id
        self.Name = name
        self.DefaultAuthorizationTag = defaultAuthorizationTag
        self.GraphQLName = graphQLName
        self.Version = version
        self.State = state
        self.CreatedDate = createdDate
        self.ModifiedDate = modifiedDate
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
    def DefaultAuthorizationTag(self) -> str:
        """
        not required
        :return:
        """
        return self.__defaultAuthorizationTag

    @DefaultAuthorizationTag.setter
    def DefaultAuthorizationTag(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__defaultAuthorizationTag = value

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

    @property
    def CreatedDate(self) -> str:
        """
        not required
        :return:
        """
        return self.__createdDate

    @CreatedDate.setter
    def CreatedDate(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__createdDate = value       

    @property
    def ModifiedDate(self) -> str:
        """
        not required
        :return:
        """
        return self.__modifiedDate

    @ModifiedDate.setter
    def ModifiedDate(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__modifiedDate = value      

    @property
    def Version(self) -> int:
        """
        not required
        :return:
        """
        return self.__version

    @Version.setter
    def Version(self, value: int):
        """
        not required
        :param value:
        :return:
        """
        self.__version = value

    @property
    def Properties(self) -> list[EventProperty] :
        """
        not required
        :return:
        """
        return self.__properties

    @Properties.setter
    def Properties(self, value: list[EventProperty]):
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
        result = {'Id': self.Id}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.GraphQLName is not None:
            result['GraphQLName'] = self.GraphQLName

        if self.Version is not None:
            result['Version'] = self.Version

        if self.State is not None:
            result['State'] = self.State            

        if self.CreatedDate is not None:
            result['CreatedDate'] = self.CreatedDate

        if self.ModifiedDate is not None:
            result['ModifiedDate'] = self.ModifiedDate

        if self.Properties is not None:
            result['Properties'] = []
            for value in self.Properties:
                result['Properties'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = EventType()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'GraphQLName' in content:
            result.GraphQLName = content['GraphQLName']

        if 'Version' in content:
            result.Version = content['Version']

        if 'State' in content:
            result.State = content['State']

        if 'CreatedDate' in content:
            result.CreatedDate = content['CreatedDate']

        if 'ModifiedDate' in content:
            result.ModifiedDate = content['ModifiedDate']

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Metadata = []
                for value in properties:
                    result.Properties.append(
                        EventProperty.fromJson(value))

        return result
