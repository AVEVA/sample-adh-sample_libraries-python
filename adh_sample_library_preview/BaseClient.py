from __future__ import annotations
import logging
import requests

from .AbstractBaseClient import AbstractBaseClient
from .Authentication import Authentication
from .SdsError import SdsError


class BaseClient(AbstractBaseClient):
    """Handles communication with Sds Service. Internal Use"""

    def __init__(self, api_version: str, tenant: str, url: str, client_id: str = None,
                 client_secret: str = None, accept_verbosity: bool = False, logging_enabled: bool = False):
        self.__api_version = api_version
        self.__tenant = tenant
        self.__url = url  # if resource.endswith("/")  else resource + "/"
        self.__accept_verbosity = accept_verbosity
        self.__request_timeout = None
        if (client_id is not None):
            self.__auth_object = Authentication(
                tenant, url, client_id, client_secret)
            self.__auth_object.getToken()
        else:
            self.__auth_object = None

        self.__uri_api = url + '/api/' + api_version
        self.__session = requests.Session()
        self.__logging_enabled = logging_enabled

    @property
    def uri(self) -> str:
        """
        Gets the base url
        :return:
        """
        return self.__url

    @property
    def uri_API(self) -> str:
        """
        Returns the base URL plus api versioning information
        :return:
        """
        return self.__uri_api

    @property
    def api_version(self) -> str:
        """
        Returns just the base api versioning information
        :return:
        """
        return self.__api_version

    @property
    def tenant(self) -> str:
        """
        Returns the tenant ID
        :return:
        """
        return self.__tenant

    @property
    def AcceptVerbosity(self) -> bool:
        return self.__accept_verbosity

    @AcceptVerbosity.setter
    def AcceptVerbosity(self, value: bool):
        self.__accept_verbosity = value

    @property
    def RequestTimeout(self) -> int:
        return self.__request_timeout

    @RequestTimeout.setter
    def RequestTimeout(self, value: int):
        self.__request_timeout = value

    @property
    def LoggingEnabled(self) -> bool:
        return self.__logging_enabled

    @LoggingEnabled.setter
    def LoggingEnabled(self, value: bool):
        self.__logging_enabled = value

    def _getToken(self) -> str:
        """
        Gets the bearer token
        :return:
        """
        return self.__auth_object.getToken()


    def encode(self, url: str):
        """
        Url encodes a provided url string
        :return:
        """
        return requests.utils.quote(url, safe=':')


    def sdsHeaders(self) -> dict[str, str]:
        """
        Gets the base headers needed for SDS call
        :return:
        """
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json'}
        if (self.__auth_object is not None):
            headers['Authorization'] = 'Bearer %s' % self._getToken()
        if (self.__accept_verbosity):
            # All possible routes should call the same verbosity header function to ensure case sensitivity
            # accept-verbosity and Accept-Verbosity would not overwrite each other, leading to unpredicable response from ADH
            headers.update(BaseClient.getVerbosityHeader(True))
        if self.__request_timeout is not None:
            headers['Request-Timeout'] = str(self.__request_timeout)

        return headers


    def communityHeaders(self, community_id: str):
        """
        DEPRECATED - Use the additional_headers parameter on the BaseClient.request method 
        and the getCommunityIdHeader function to add a community id header to a REST call\n\n
        Gets the base headers needed for a Communities call
        :param community_id: id of the community
        :return:
        """
        headers = self.sdsHeaders()
        headers['community-id'] = community_id

        return headers


    def sdsNonVerboseHeader(self):
        """
        DEPRECATED - Use the additional_headers parameter on the BaseClient.request method 
        and the getVerbosityHeader function to add or override an accept-verbosity header to a REST call\n\n
        Gets the base headers needed for an SDS call and adds accept-verbosity: non-verbose
        :return:
        """
        headers = self.sdsHeaders()
        headers['accept-verbosity'] = 'non-verbose'

        return headers


    @staticmethod
    def getCommunityIdHeader(community_id: str) -> dict[str, str]:
        return { 'Community-id': community_id }


    @staticmethod
    def getVerbosityHeader(verbose: bool) -> dict[str, str]:
        verbosity_string = 'verbose' if verbose else 'non-verbose'
        return { 'Accept-Verbosity': verbosity_string } 


    def request(self, method: str, url: str, params=None, data=None, headers=None, additional_headers=None, **kwargs):
        
        # Start with the necessary headers for SDS calls, such as authorization and content-type
        if not headers:
            headers = self.sdsHeaders()
        
        # Extend this with the additional headers provided that either suppliment or override the default values
        # This allows additional headers to be added to the HTTP call without blocking the base header call
        if additional_headers:
            headers.update(additional_headers)

        if self.__logging_enabled:
            # Announce the url and method
            logging.info(f'executing request - method: {method}, url: {url}')

            # if debug level is desired, dump the payload and the headers (redacting the auth header)
            logging.debug(f'data: {data}')
            for header,value in headers.items():
                if header.lower() != "authorization":
                    logging.debug(f'{header}: {value}')
                else:
                    logging.debug(f'{header}: <redacted>')

        return self.__session.request(method, url, params=params, data=data, headers=headers, **kwargs)


    def checkResponse(self, response, main_message: str):

        if self.__logging_enabled:
            # Announce the status code
            logging.info(f'request executed in {response.elapsed.microseconds / 1000}ms - status code: {response.status_code}')

            # if debug level is desired, dump the response text and all headers
            logging.debug(f'response text: {response.text}')
            for header,value in response.headers.items():
                logging.debug(f'{header}: {value}')


        if response.status_code < 200 or response.status_code >= 300:
            status = response.status_code
            reason = response.text
            url = response.url

            if 'Operation-Id' in response.headers:
                opId = response.headers['Operation-Id']
                error = f'  {status}:{reason}.  URL {url}  OperationId {opId}'
            else:
                error = f'  {status}:{reason}.  URL {url}'

            response.close()

            message = main_message + error
            if self.__logging_enabled:
                logging.error(message)
            raise SdsError(message)

        # this happens on a collection return that is partially successful
        if response.status_code == 207:
            status = response.status_code
            error = response.json['Error']
            reason = response.json['Reason']
            errors = str(response.json['ChildErrors'])
            url = response.url

            if 'Operation-Id' in response.headers:
                opId = response.headers['Operation-Id']
                errorToWrite = f'  {status}:{error}:{reason}. \n\n{errors}\n\n  URL {url}  OperationId {opId}'
            else:
                errorToWrite = f'  {status}:{error}:{reason}. \n\n{errors}\n\n  URL {url}'

            response.close()

            message = main_message + errorToWrite
            raise SdsError(message)


    def validateParameters(*args):
        for arg in args:
            if arg is None:
                raise TypeError
            if type(arg) is list and not arg:
                raise TypeError


    def __del__(self):
        if hasattr(self, '__session'):
            self.__session.close()
