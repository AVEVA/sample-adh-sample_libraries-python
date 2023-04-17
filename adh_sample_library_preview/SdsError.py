from dataclasses import dataclass


@dataclass
class SdsError(Exception):
    """
    Helper class to hold exceptions
    """

    Text: str
    MainMessage: str = None
    Error: str = None
    Reason: str = None
    Resolution: str = None
    ChildErrors: str = None
    StatusCode: int = None
    OperationId: str = None
    Url: str = None

    @classmethod
    def fromResponse(cls, response: str, main_message: str = None):
        error = response.json().get('Error', None)
        reason = response.json().get('Reason', None)
        resolution = response.json().get('Resolution', None)
        child_errors = response.json().get('ChildErrors', None)
        child_errors = str(child_errors) if child_errors else None
        operation_id = response.headers['Operation-Id'] if 'Operation-Id' in response.headers else None

        return cls(response.text, main_message, error, reason, resolution, child_errors, response.status_code, operation_id, response.url)

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
            output += f'{self.Text}.'

        if self.ChildErrors:
            output += f'  \n\n{self.ChildErrors}\n\n'

        if self.Url:
            output += f'  URL {self.Url}'

        if self.OperationId:
            output += f'  OperationId {self.OperationId}'

        return repr(output)
