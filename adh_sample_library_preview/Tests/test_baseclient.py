"""This sample script demonstrates how to invoke the Data View REST API"""

from ast import Assert
from datetime import date, datetime, timedelta
from genericpath import exists
import json
from lib2to3.pytree import Base
from os import name
from types import NoneType
import pytest
from requests import Response

from adh_sample_library_preview.ADHClient import ADHClient
from adh_sample_library_preview.BaseClientStub import BaseClientStub
from adh_sample_library_preview.BaseClient import BaseClient
from adh_sample_library_preview.EDSClient import EDSClient
from adh_sample_library_preview.SDS.SdsBoundaryType import SdsBoundaryType
from adh_sample_library_preview.SDS.SdsStream import SdsStream
from adh_sample_library_preview.SDS.SdsType import SdsType, SdsTypeProperty, SdsTypeCodeType
from adh_sample_library_preview.SDS.SdsTypeCode import SdsTypeCode
from adh_sample_library_preview.ADHClientStub import ADHClientStub
from adh_sample_library_preview.SdsError import SdsError

# Sample Data Information

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
    content = b'{ "key" : "a" }'
    response._content = content

    assert baseClient.resolveContent(response=response, value_class=None) is content