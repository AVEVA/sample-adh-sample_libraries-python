import json
import pytest

from adh_sample_library_preview.BaseClient import BaseClient
from adh_sample_library_preview.SDS.SdsResultPage import SdsResultPage
from adh_sample_library_preview.SDS.SdsStream import SdsStream
from adh_sample_library_preview.SdsError import SdsError
from requests import Response


@pytest.fixture
def baseClient():
    return BaseClient(api_version='api_version', tenant='tenant', url='https://test.com',
        client_id=None, client_secret=None, accept_verbosity='accept_verbosity')

@pytest.fixture
def content():
    return { "someKey" : "someValue" }

@pytest.fixture
def response(content):
    response = Response()
    response.code = "ok"
    response.status_code = 200
    response._content = json.dumps(content).encode()
    return response


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


def test_resolve_content(baseClient, response, content):
    assert baseClient.resolveContent(response=response, value_class=None).keys() == content.keys()


def test_resolve_value_content(baseClient, response, content):
    assert baseClient.resolveValueContent(response=response, value_class=None).keys() == content.keys()


def test_resolve_paged_content(baseClient, response):
    assert isinstance(baseClient.resolvePagedContent(response=response, value_class=None), SdsResultPage)


def test_resolve_bulk_content(baseClient, response, content):
    assert baseClient.resolveBulkContent(response=response, value_class=None).keys() == content.keys()


def test_resolve_streams_content(baseClient):
    response = Response()
    content = [{ "Id" : "test" }]
    response._content = json.dumps(content).encode()
    
    value = baseClient.resolveStreamsContent(response=response)
    assert isinstance(value, list) 
    assert isinstance(value[0], SdsStream)
    assert value[0].Id == 'test'


def test_resolve_content(baseClient):
    response = Response()
    response.code = "ok"
    response.status_code = 200
    content = { "someKey" : "someValue" }
    response._content = json.dumps(content).encode()
    
    assert baseClient.resolveValueContent(response=response, value_class=None).keys() == content.keys()


def test_validate_parameters_raises_error(baseClient):
    with pytest.raises(TypeError):
        baseClient.validateParameters('good', 'gooder', None)

    with pytest.raises(TypeError):
        baseClient.validateParameters('good', 'gooder', [])


def test_validate_parameters_valid(baseClient):
    baseClient.validateParameters('good', 'gooder', 'goodest')