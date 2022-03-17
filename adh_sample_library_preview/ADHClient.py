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

class ADHClient:
    """
    A client that handles communication with AVEVA Data Hub
    """

    def __init__(self, api_version: str, tenant: str, url: str, client_id: str,
                 client_secret: str = None, accept_verbosity: bool = False):
        """
        Use this to help in communinication with ADH
        :param api_version: Version of the api you are communicating with
        :param tenant: Your tenant ID
        :param url: The base URL for your ADH instance
        :param client_id: Your client ID
        :param client_secret: Your client Secret or Key
        :param accept_verbosity: Sets whether in value calls you get all values or just
            non-default values
        """
        self.__base_client = BaseClient(api_version, tenant, url, client_id,
                                        client_secret, accept_verbosity)
        self.__asset_rules = AssetRules(self.__base_client)
        self.__assets = Assets(self.__base_client)
        self.__asset_types = AssetTypes(self.__base_client)
        self.__communities = Communities(self.__base_client)
        self.__data_views = DataViews(self.__base_client)
        self.__namespaces = Namespaces(self.__base_client)
        self.__roles = Roles(self.__base_client)
        self.__sharedStreams = SharedStreams(self.__base_client)
        self.__streams = Streams(self.__base_client)
        self.__stream_views = StreamViews(self.__base_client)
        self.__subscriptions = Subscriptions(self.__base_client)
        self.__types = Types(self.__base_client)
        self.__topics = Topics(self.__base_client)
        self.__users = Users(self.__base_client)

    @property
    def uri(self) -> str:
        """
        :return: The uri of this ADH client as a string
        """
        return self.__base_client.uri

    @property
    def tenant(self) -> str:
        """
        :return: The tenant of this ADH client as a string
        """
        return self.__base_client.tenant

    @property
    def acceptverbosity(self) -> bool:
        """
        :return: Whether this will include the accept verbosity header
        """
        return self.__base_client.AcceptVerbosity

    @acceptverbosity.setter
    def acceptverbosity(self, value: bool):
        self.__base_client.AcceptVerbosity = value

    @property
    def request_timeout(self) -> int:
        """
        :return: Request timeout in seconds (default 30 secs)
        """
        return self.__base_client.RequestTimeout

    @request_timeout.setter
    def request_timeout(self, value: int):
        self.__base_client.RequestTimeout = value

    @property
    def AssetRules(self) -> AssetRules:
        """
        :return: A client for interacting with Asset Rules
        """
        return self.__asset_rules

    @property
    def Assets(self) -> Assets:
        """
        :return: A client for interacting with Assets
        """
        return self.__assets

    @property
    def AssetTypes(self) -> AssetTypes:
        """
        :return: A client for interacting with Asset Types
        """
        return self.__asset_types

    @property
    def SharedStreams(self) -> SharedStreams:
        """
        :return: A client for interacting with Streams shared in a Community
        """
        return self.__sharedStreams

    @property
    def DataViews(self) -> DataViews:
        """
        :return: A client for interacting with Data Views
        """
        return self.__data_views

    @property
    def Streams(self) -> Streams:
        """
        :return: A client for interacting with Streams
        """
        return self.__streams

    @property
    def StreamViews(self) -> StreamViews:
        """
        :return: A client for interacting with Stream Views
        """
        return self.__stream_views

    @property
    def Types(self) -> Types:
        """
        :return: A client for interacting with Types
        """
        return self.__types

    @property
    def Communities(self) -> Communities:
        """
        :return: A client for interacting with Communities
        """
        return self.__communities

    @property
    def Namespaces(self) -> Namespaces:
        """
        :return: A client for interacting with Namespaces
        """
        return self.__namespaces

    @property
    def Roles(self) -> Roles:
        """
        :return: A client for interacting with Roles
        """
        return self.__roles

    @property
    def Subscriptions(self) -> Subscriptions:
        """
        :return: A client for interacting with Subscriptions
        """
        return self.__subscriptions

    @property
    def Topics(self) -> Topics:
        """
        :return: A client for interacting with Topics
        """
        return self.__topics

    @property
    def Users(self) -> Users:
        """
        :return: A client for interacting with Users
        """
        return self.__users

    @property
    def baseClient(self) -> BaseClient:
        """
        :return: A client for interacting with the baseclient directly
        """
        return self.__base_client
