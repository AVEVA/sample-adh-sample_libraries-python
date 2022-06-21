from .AssetRules import AssetRules
from .Assets import Assets
from .AssetTypes import AssetTypes
from .BaseClient import BaseClient
from .Communities import Communities
from .DataViews import DataViews
from .Namespaces import Namespaces
from .Roles import Roles
from .SharedStreams import SharedStreams
from .Streams import Streams
from .StreamViews import StreamViews
from .Subscriptions import Subscriptions
from .Topics import Topics
from .Types import Types
from .Users import Users

import requests

class ADHClientStub(BaseClient):
    """
    A client that handles communication with AVEVA Data Hub
    """

    def __init__(self):
        """
        Use this to help in communication with ADH
        :param api_version: Version of the api you are communicating with
        :param tenant: Your tenant ID
        :param url: The base URL for your ADH instance
        :param client_id: Your client ID
        :param client_secret: Your client Secret or Key
        :param accept_verbosity: Sets whether in value calls you get all values or just
            non-default values
        """
        
        self.tenant = 'tenant'
        self.uri_API = '/api/'

        self.__asset_rules = AssetRules(self)
        self.__assets = Assets(self)
        self.__asset_types = AssetTypes(self)
        self.__communities = Communities(self)
        self.__data_views = DataViews(self)
        self.__namespaces = Namespaces(self)
        self.__roles = Roles(self)
        self.__sharedStreams = SharedStreams(self)
        self.__streams = Streams(self)
        self.__stream_views = StreamViews(self)
        self.__subscriptions = Subscriptions(self)
        self.__types = Types(self)
        self.__topics = Topics(self)
        self.__users = Users(self)
        
    @property
    def AssetRules(self) -> AssetRules:
        return self.__asset_rules

    @property
    def Assets(self) -> Assets:
        return self.__assets

    @property
    def AssetTypes(self) -> AssetTypes:
        return self.__asset_types

    @property
    def SharedStreams(self) -> SharedStreams:
        return self.__sharedStreams

    @property
    def DataViews(self) -> DataViews:
        return self.__data_views

    @property
    def Streams(self) -> Streams:
        return self.__streams

    @property
    def StreamViews(self) -> StreamViews:
        return self.__stream_views

    @property
    def Types(self) -> Types:
        return self.__types

    @property
    def Communities(self) -> Communities:
        return self.__communities

    @property
    def Namespaces(self) -> Namespaces:
        return self.__namespaces

    @property
    def Roles(self) -> Roles:
        return self.__roles

    @property
    def Subscriptions(self) -> Subscriptions:
        return self.__subscriptions

    @property
    def Topics(self) -> Topics:
        return self.__topics

    @property
    def Users(self) -> Users:
        return self.__users


    def request(self, method: str, url: str, params=None, data=None, headers=None, additional_headers=None, **kwargs):
        response = requests.Response()
        response.code = "ok"
        response.status_code = 200
        response._content = b'{ "key" : "a" }'
        return response