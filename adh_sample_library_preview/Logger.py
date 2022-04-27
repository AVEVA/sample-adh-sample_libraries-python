import logging

class LoggerFlags:
    """
    A class that handles logging across the client library
    """
    def __init__(self):
        self.__data_views = False
        self.__base_client = False

    @property
    def DataViews(self) -> bool:
        return self.__data_views

    @DataViews.setter
    def DataViews(self, value: bool):
        self.__data_views = value

    @property
    def BaseClient(self) -> bool:
        return self.__base_client

    @BaseClient.setter
    def BaseClient(self, value: bool):
        self.__base_client = value