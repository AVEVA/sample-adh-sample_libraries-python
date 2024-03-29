from __future__ import annotations

import json
import logging

from .AssetRules import AssetRules
from .Assets import Assets
from .AssetTypes import AssetTypes
from .AuthorizationTags import AuthorizationTags
from .BaseClient import BaseClient
from .Signups import Signups
from .Communities import Communities
from .DataViews import DataViews
from .Enumerations import Enumerations
from .Events import Events
from .EventTypes import EventTypes
from .GraphQL import GraphQL
from .Namespaces import Namespaces
from .ReferenceData import ReferenceData
from .ReferenceDataTypes import ReferenceDataTypes
from .Roles import Roles
from .SharedStreams import SharedStreams
from .Streams import Streams
from .StreamViews import StreamViews
from .Subscriptions import Subscriptions
from .Topics import Topics
from .Types import Types
from .Units import Units
from .Users import Users


class ADHClient:
    """
    A client that handles communication with AVEVA Data Hub
    """

    def __init__(
        self,
        api_version: str,
        tenant: str,
        url: str,
        client_id: str,
        client_secret: str = None,
        accept_verbosity: bool = False,
        logging_enabled: bool = False,
        **kwargs,
    ):
        """
        Use this to help in communication with ADH
        :param api_version: Version of the api you are communicating with
        :param tenant: Your tenant ID
        :param url: The base URL for your ADH instance
        :param client_id: Your client ID
        :param client_secret: Your client Secret or Key
        :param accept_verbosity: Sets whether in value calls you get all values or just
            non-default values
        :param logging_enabled: Sets whether Python logging is enabled
        """

        if 'base_client' in kwargs:
            self.__base_client = kwargs.get('base_client')
        else:
            self.__base_client = BaseClient(
                api_version,
                tenant,
                url,
                client_id,
                client_secret,
                accept_verbosity,
                logging_enabled,
            )

        self.__asset_rules = AssetRules(self.__base_client)
        self.__assets = Assets(self.__base_client)
        self.__asset_types = AssetTypes(self.__base_client)
        self.__authorization_tags = AuthorizationTags(self.__base_client)
        self.__communities = Communities(self.__base_client)
        self.__data_views = DataViews(self.__base_client)
        self.__enumerations = Enumerations(self.__base_client)
        self.__events = Events(self.__base_client)
        self.__event_types = EventTypes(self.__base_client)
        self.__graph_ql = GraphQL(self.__base_client)
        self.__namespaces = Namespaces(self.__base_client)
        self.__reference_data_types = ReferenceDataTypes(self.__base_client)
        self.__reference_data = ReferenceData(self.__base_client)
        self.__roles = Roles(self.__base_client)
        self.__shared_streams = SharedStreams(self.__base_client)
        self.__signups = Signups(self.__base_client)
        self.__streams = Streams(self.__base_client)
        self.__stream_views = StreamViews(self.__base_client)
        self.__subscriptions = Subscriptions(self.__base_client)
        self.__types = Types(self.__base_client)
        self.__topics = Topics(self.__base_client)
        self.__units = Units(self.__base_client)
        self.__users = Users(self.__base_client)

    @staticmethod
    def fromAppsettings(path: str = None) -> tuple['ADHClient', str]:
        if not path:
            path = 'appsettings.json'

        try:
            with open(
                path,
                'r',
            ) as f:
                appsettings = json.load(f)
        except Exception as error:
            logging.ERROR(f'Error: {str(error)}')
            logging.ERROR(f'Could not open/read appsettings.json')
            exit()

        return (
            ADHClient(
                appsettings.get('ApiVersion'),
                appsettings.get('TenantId'),
                appsettings.get('Resource'),
                appsettings.get('ClientId'),
                appsettings.get('ClientSecret', None),
                appsettings.get('AcceptVerbosity', False),
                appsettings.get('LoggingEnabled', False),
            ),
            appsettings.get('NamespaceId', None),
        )

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
    def logging_enabled(self) -> bool:
        """
        :return: Whether logging is enabled (default False)
        """
        return self.__base_client.LoggingEnabled

    @logging_enabled.setter
    def logging_enabled(self, value: bool):
        self.__base_client.LoggingEnabled = value

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
    def AuthorizationTags(self) -> AuthorizationTags:
        """
        :return: A client for interacting with AuthorizationTags
        """
        return self.__authorization_tags

    @property
    def SharedStreams(self) -> SharedStreams:
        """
        :return: A client for interacting with Streams shared in a Community
        """
        return self.__shared_streams
    
    @property
    def Signups(self) -> Signups:
        """
        :return: A client for interacting with the Change Broker
        """
        return self.__signups

    @property
    def DataViews(self) -> DataViews:
        """
        :return: A client for interacting with Data Views
        """
        return self.__data_views

    @property
    def Enumerations(self) -> Enumerations:
        """
        :return: A client for interacting with Enumerations
        """
        return self.__enumerations

    @property
    def Events(self) -> Events:
        """
        :return: A client for interacting with Events
        """
        return self.__events

    @property
    def EventTypes(self) -> EventTypes:
        """
        :return: A client for interacting with Events
        """
        return self.__event_types

    @property
    def GraphQL(self) -> GraphQL:
        """
        :return: A client for interacting with GraphQL
        """
        return self.__graph_ql

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
    def ReferenceDataTypes(self) -> ReferenceDataTypes:
        """
        :return: A client for interacting with ReferenceDataTypes
        """
        return self.__reference_data_types

    @property
    def ReferenceData(self) -> ReferenceData:
        """
        :return: A client for interacting with ReferenceData
        """
        return self.__reference_data

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
    def Units(self) -> Units:
        """
        :return: A client for interacting with Units
        """
        return self.__units

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
