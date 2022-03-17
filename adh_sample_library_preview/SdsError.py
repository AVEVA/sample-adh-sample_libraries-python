class SdsError(Exception):
    """
    Helper class to hold exceptions
    """

    def __init__(self, value: object):
        """
        Set thee exception value
        :param value:
        """
        self.value = value

    def __str__(self) -> str:
        """
        Get the exception
        :return:
        """
        return repr(self.value)
