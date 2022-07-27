from .BaseClient import BaseClient
from .Types import Types
from .Streams import Streams
from .StreamViews import StreamViews


class EDSClient:
    """
    A client that handles communication with EDS
    """

    def __init__(self, api_version: str = 'v1', url: str = 'http://localhost:5590',
                 accept_verbosity: bool = False, logging_enabled: bool = False):
        """
        Use this to help in communinication with EDS
        :param api_version: Version of the api you are communicating with, default is v1
        :param url: The base URL for EDS, default is http://localhost:5590
        :param accept_verbosity: Sets whether in value calls you get all values or just
        :param logging_enabled: Sets whether Python logging is enabled
            non-default values
        """
        self.__base_client = BaseClient(
            api_version, 'default', url, None, None, accept_verbosity)
        self.__types = Types(self.__base_client)
        self.__streams = Streams(self.__base_client)
        self.__stream_views = StreamViews(self.__base_client)

    @property
    def uri(self) -> str:
        """
        :return: The uri of this EDS client as a string
        """
        return self.__base_client.uri

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
    def logging_enabled(self) -> bool:
        """
        :return: Whether logging is enabled (default False)
        """
        return self.__base_client.LoggingEnabled

    @logging_enabled.setter
    def logging_enabled(self, value: bool):
        self.__base_client.LoggingEnabled = value

    @property
    def Types(self) -> Types:
        """
        :return: A client for interacting with Types
        """
        return self.__types

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
    def baseClient(self) -> BaseClient:
        """
        :return: A client for interacting with the baseclient directly
        """
        return self.__base_client
