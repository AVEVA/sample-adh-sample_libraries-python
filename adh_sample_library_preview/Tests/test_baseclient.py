import json
import pytest
from requests import Response

from adh_sample_library_preview.BaseClient import BaseClient
from adh_sample_library_preview.SdsError import SdsError

def setup_module(module):
    print('SETUP')
    global baseClient
    baseClient = BaseClient(api_version='api_version', tenant='tenant', url='https://dat-b.osisoft.com',
        client_id=None, client_secret=None, accept_verbosity='accept_verbosity')


def test_check_response():
    response = Response()

    response.status_code = 300
    with pytest.raises(SdsError):
        baseClient.checkResponse(response=response)

    response.status_code = 199
    with pytest.raises(SdsError):
        baseClient.checkResponse(response=response)

    response.status_code = 200
    baseClient.checkResponse(response=response)

def test_resolve_content():
    response = Response()
    response.code = "ok"
    response.status_code = 200
    content = { "key" : "a" }
    response._content = json.dumps(content).encode()
    assert baseClient.resolveContent(response=response, value_class=None).keys() == content.keys()