import json
import pytest

from adh_sample_library_preview.BaseClient import BaseClient
from adh_sample_library_preview.SdsError import SdsError
from requests import Response


def setup_module(module):
    global baseClient
    baseClient = BaseClient(api_version='api_version', tenant='tenant', url='https://test.com',
        client_id=None, client_secret=None, accept_verbosity='accept_verbosity')


def test_check_response_OK_response():
    response = Response()
    response.status_code = 200
    baseClient.checkResponse(response=response, main_message='Testing')


def test_check_response_error_response():
    response = Response()

    response.status_code = 300
    with pytest.raises(SdsError):
        baseClient.checkResponse(response=response, main_message='Testing')

    response.status_code = 199
    with pytest.raises(SdsError):
        baseClient.checkResponse(response=response, main_message='Testing')


def test_resolve_content():
    response = Response()
    response.code = "ok"
    response.status_code = 200
    content = { "key" : "a" }
    response._content = json.dumps(content).encode()
    assert baseClient.resolveContent(response=response, value_class=None).keys() == content.keys()


def test_validate_parameters_raises_error():
    with pytest.raises(TypeError):
        baseClient.validateParameters('good', 'gooder', None)

    with pytest.raises(TypeError):
        baseClient.validateParameters('good', 'gooder', [])


def test_validate_parameters_valid():
    baseClient.validateParameters('good', 'gooder', 'goodest')