from __future__ import annotations

from requests.models import Response
from .AbstractBaseClient import AbstractBaseClient

class BaseClientStub(AbstractBaseClient):
    """Stubbed BaseClient to use for testing."""

    def __init__(self):
        print('Creating stub')
        self.__tenant = 'tenant'
        self.__uri_api = 'url' 

   
    @property
    def uri_API(self) -> str:
        """
        Returns the base URL plus api versioning information
        :return:
        """
        return self.__uri_api


    @property
    def tenant(self) -> str:
        """
        Returns the tenant ID
        :return:
        """
        return self.__tenant


    def request(self, method: str, url: str, params=None, data=None, headers=None, additional_headers=None, **kwargs):
        response = Response()
        response.code = "ok"
        response.status_code = 200
        response._content = b'{ "key" : "a" }'
        return response


    def validateParameters(*args):
        for arg in args:
            if arg is None:
                raise TypeError
            if type(arg) is list and not arg:
                raise TypeError


    def encode(self, url: str):
        return ''


    def checkResponse(self, response, main_message: str):
        pass
