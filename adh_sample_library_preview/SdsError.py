from dataclasses import dataclass
import requests


@dataclass
class SdsError(Exception):
    """
    Helper class to hold exceptions
    """

    value: str
    MainMessage: str = None
    Error: str = None
    Reason: str = None
    Resolution: str = None
    ChildErrors: str = None
    StatusCode: int = None
    OperationId: str = None
    Url: str = None
    Response: requests.Response = None

    @classmethod
    def fromResponse(cls, response: requests.Response, main_message: str = None):
        operation_id = response.headers['Operation-Id'] if 'Operation-Id' in response.headers else None

        if response.headers.get('content-type') == 'application/json':
            error = response.json().get('Error', None)
            reason = response.json().get('Reason', None)
            resolution = response.json().get('Resolution', None)
            child_errors = response.json().get('ChildErrors', None)
            child_errors = str(child_errors) if child_errors else None
            return cls(response.text, main_message, error, reason, resolution, child_errors, response.status_code, operation_id, response.url, response)

        return cls(response.text, main_message, StatusCode=response.status_code, OperationId=operation_id, Url=response.url, Response=response)

    def __str__(self) -> str:
        """
        Get the exception
        :return:
        """
        output = ''

        if self.MainMessage:
            output += f'{self.MainMessage}'

        if self.StatusCode:
            output += f'  {self.StatusCode}:'

        if self.Error and self.Reason and self.Resolution:
            output += f'{self.Error}:{self.Reason}:{self.Resolution}'
        else:
            output += f'{self.value}.'

        if self.ChildErrors:
            output += f'  \n\n{self.ChildErrors}\n\n'

        if self.Url:
            output += f'  URL {self.Url}'

        if self.OperationId:
            output += f'  OperationId {self.OperationId}'

        return repr(output)
