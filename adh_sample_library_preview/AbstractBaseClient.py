from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractBaseClient(ABC):
    """Defines an interface for a BaseClient object to use when sending requests."""

    @property
    @abstractmethod
    def uri_API(self) -> str:
        """
        Returns the base URL plus api versioning information
        :return:
        """
        pass


    @abstractmethod
    def validateParameters(*args):
        pass


    @abstractmethod
    def request(self, method: str, url: str, params=None, data=None, headers=None, additional_headers=None, **kwargs):
        pass


    @abstractmethod
    def encode(self, url: str):
        pass


    @abstractmethod
    def checkResponse(self, response, main_message: str):
        pass


    @abstractmethod
    def resolveBulkContent(self, response, value_class = None):
        pass


    @abstractmethod
    def resolvePagedContent(response, value_class = None):
        pass


    @abstractmethod
    def resolveStreamsContent(response):
        pass


    @abstractmethod
    def resolveValueContent(response, value_class = None):
        pass


    @abstractmethod
    def resolveContent(response, value_class = None):
       pass
