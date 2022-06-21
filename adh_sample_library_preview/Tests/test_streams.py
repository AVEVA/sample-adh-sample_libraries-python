"""This sample script demonstrates how to invoke the Data View REST API"""

from ast import Assert
from datetime import date, datetime, timedelta
from genericpath import exists
import json
from os import name
from types import NoneType
import pytest

from adh_sample_library_preview.ADHClient import ADHClient
from adh_sample_library_preview.EDSClient import EDSClient
from adh_sample_library_preview.SDS.SdsBoundaryType import SdsBoundaryType
from adh_sample_library_preview.SDS.SdsStream import SdsStream
from adh_sample_library_preview.SDS.SdsType import SdsType, SdsTypeProperty, SdsTypeCodeType
from adh_sample_library_preview.SDS.SdsTypeCode import SdsTypeCode
from adh_sample_library_preview.ADHClientStub import ADHClientStub
from adh_sample_library_preview.BaseClientStub import BaseClientStub

# Sample Data Information

def setup_module(module):
    print('SETUP')

    global adh_client
    global namespace_id
    global stream_id
    global tenant_id
    global type_prop_id
    global type_id
    global start_ndx
    global end_ndx
    global base_url

    # If app settings file is configured
    if exists('appsettings2.json'):
        appsettings = get_appsettings() # use a fixture instead\
        namespace_id = appsettings.get('NamespaceId')
        tenant_id = appsettings.get('TenantId')

        adh_client = ADHClient(api_version=appsettings.get('ApiVersion'), 
                                tenant=tenant_id, 
                                url=appsettings.get('Resource'), 
                                client_id=appsettings.get('ClientId'), 
                                client_secret=appsettings.get('ClientSecret'), 
                                accept_verbosity=appsettings.get('AcceptVerbosity'))
    else:
        namespace_id = 'test'
        tenant_id = 'test'
        base_client = BaseClientStub()
        adh_client = ADHClient(base_client)
        # adh_client = ADHClientStub()
        # adh_client = EDSClient()

    start_ndx = 1
    end_ndx = 10

    stream_id = 'PythonSampleLibrary_TestStream_CanDelete'
    type_prop_id = 'PythonSampleLibrary_TestTypeProp_CanDelete'
    type_id = 'PythonSampleLibrary_TestType_CanDelete'
    base_url = f'https://dat-b.osisoft.com/api/v1/Tenants/{tenant_id}/Namespaces/{namespace_id}/Streams/{stream_id}'


def get_appsettings():
    """Open and parse the appsettings.json file"""

    # Try to open the configuration file
    try:
        with open(
            'appsettings.json',
            'r',
        ) as f:
            appsettings = json.load(f)
    except Exception as error:
        print(f'Error: {str(error)}')
        print(f'Could not open/read appsettings.json')
        exit()

    return appsettings


def test_stream_retrieval():
    adh_client.Streams.getStreams(namespace_id)
    adh_client.Streams.getStream(namespace_id, stream_id)
    adh_client.Streams.getResolvedStream(namespace_id, stream_id)


'''
def test_access_control():
    adh_client.Streams.getAccessControl(namespace_id, item_id=stream_id)
    adh_client.Streams.getAccessRights(namespace_id, item_id=stream_id)
    adh_client.Streams.getDefaultAccessControl(namespace_id)
    adh_client.Streams.getOwner(namespace_id, item_id=stream_id)
'''

def test_range_values():        
    assert adh_client.Streams.getRangeValues(namespace_id, stream_id, None, start_ndx, 0, 100, False, SdsBoundaryType.Exact) is not None
    assert adh_client.Streams.getRangeValuesUrl(base_url, None, start_ndx, 0, 100, False, SdsBoundaryType.Exact) is not None
    assert adh_client.Streams.getRangeValuesInterpolated(namespace_id, stream_id, None, start_ndx, end_ndx, 100) is not None
    assert adh_client.Streams.getRangeValuesInterpolatedUrl(base_url, None, start_ndx, end_ndx, 100) is not None

def test_window_values():
    assert adh_client.Streams.getWindowValues(namespace_id, stream_id, start_ndx, end_ndx, None) is not None
    assert adh_client.Streams.getWindowValuesUrl(base_url, start_ndx, end_ndx, None) is not None
    assert adh_client.Streams.getWindowValuesPaged(namespace_id, stream_id, None, start_ndx, end_ndx, 100) is not None
    assert adh_client.Streams.getWindowValuesPagedUrl(base_url, None, start_ndx, end_ndx, 100) is not None
    assert adh_client.Streams.getWindowValuesForm(namespace_id, stream_id, None, start_ndx, end_ndx, 'tableh') is not None
    assert adh_client.Streams.getWindowValuesFormUrl(base_url, None, start_ndx, end_ndx, 'tableh') is not None

def test_sampled_values():
    assert adh_client.Streams.getSampledValues(namespace_id, stream_id,  None, start_ndx, end_ndx, type_prop_id, 1) is not None
    assert adh_client.Streams.getSampledValuesUrl(base_url,  None, start_ndx, end_ndx, type_prop_id, 1) is not None
    
def test_index_collection_values():
    assert adh_client.Streams.getIndexCollectionValues(namespace_id, stream_id, None, [1,2,3]) is not None
    assert adh_client.Streams.getIndexCollectionValuesUrl(base_url, None,  [1,2,3]) is not None

def test_value():
    adh_client.Streams.getFirstValue(namespace_id, stream_id, None)
    adh_client.Streams.getFirstValueUrl(base_url, None)
    adh_client.Streams.getLastValue(namespace_id, stream_id, None)
    adh_client.Streams.getLastValueUrl(base_url, None)
    adh_client.Streams.getValue(namespace_id, stream_id, 1, None)
    adh_client.Streams.getValueUrl(base_url, 1, None)

def test_summaries():
    assert adh_client.Streams.getSummaries(namespace_id, stream_id, None, start_ndx, end_ndx, 10) is not None
    assert adh_client.Streams.getSummariesUrl(base_url, None, start_ndx, end_ndx, 10) is not None

def test_metadata():
    assert adh_client.Streams.getMetadata(namespace_id, stream_id, 'Region') is not None
    assert adh_client.Streams.getStreamType(namespace_id, stream_id) is not None
    assert adh_client.Streams.getTags(namespace_id, stream_id) is not None