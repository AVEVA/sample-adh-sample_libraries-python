import pytest
from requests import Response

from adh_sample_library_preview.BaseClient import BaseClient
from adh_sample_library_preview.SdsError import SdsError



@pytest.fixture
def baseClient():
    return BaseClient(api_version='api_version', tenant='tenant', url='https://test.com',
        client_id=None, client_secret=None, accept_verbosity='accept_verbosity')


def test_check_response_OK_response(baseClient):
    response = Response()
    response.status_code = 200
    baseClient.checkResponse(response=response, main_message='Testing')


def test_check_response_error_response(baseClient):
    response = Response()

    response.status_code = 300
    with pytest.raises(SdsError):
        baseClient.checkResponse(response=response, main_message='Testing')

    response.status_code = 199
    with pytest.raises(SdsError):
        baseClient.checkResponse(response=response, main_message='Testing')


def test_validate_parameters_raises_error(baseClient):
    with pytest.raises(TypeError):
        baseClient.validateParameters('good', 'gooder', None)

    with pytest.raises(TypeError):
        baseClient.validateParameters('good', 'gooder', [])


def test_validate_parameters_valid(baseClient):
    baseClient.validateParameters('good', 'gooder', 'goodest')