import json

from adh_sample_library_preview.ADHClient import ADHClient
from adh_sample_library_preview.BaseClientStub import BaseClientStub
from adh_sample_library_preview.SDS.SdsBoundaryType import SdsBoundaryType
from genericpath import exists

def setup_module(module):
    global adh_client
    global namespace_id
    global stream_id
    global tenant_id
    global sample_by_prop_id
    global type_id
    global start_ndx
    global end_ndx

    # If test credentials are provided run E2E tests, otherwise run Unit tests 
    if exists('test_credentials.json'):
        cred = get_credentials()
        namespace_id = cred.get('NamespaceId')
        tenant_id = cred.get('TenantId')
        stream_id = cred.get('StreamId')
        type_id = cred.get('TypeId')
        sample_by_prop_id = cred.get('SampleByPropertyId')
        start_ndx = cred.get('StartIndex')
        end_ndx = cred.get('EndIndex')
        
        adh_client = ADHClient(api_version=cred.get('ApiVersion'), 
                                tenant=tenant_id, 
                                url=cred.get('Resource'), 
                                client_id=cred.get('ClientId'), 
                                client_secret=cred.get('ClientSecret'), 
                                accept_verbosity=cred.get('AcceptVerbosity'))
    else:
        namespace_id = 'test'
        stream_id = 'test'
        tenant_id = 'test'
        type_id = 'test'
        sample_by_prop_id = 'test'
        start_ndx = 1
        end_ndx = 10
        
        base_client = BaseClientStub()
        adh_client = ADHClient(base_client)



def get_credentials():
    try:
        with open(
            'test_credentials.json',
            'r',
        ) as f:
            cred = json.load(f)
    except Exception as error:
        print(f'Error: {str(error)}')
        print(f'Could not open/read test_credentials.json')
        exit()

    return cred


def test_stream_retrieval():
    adh_client.Streams.getStreams(namespace_id)
    adh_client.Streams.getStream(namespace_id, stream_id)
    adh_client.Streams.getResolvedStream(namespace_id, stream_id)


def test_range_values():        
    adh_client.Streams.getRangeValues(namespace_id, stream_id, None, start_ndx, 0, 100, False, SdsBoundaryType.Exact) 
    adh_client.Streams.getRangeValuesInterpolated(namespace_id, stream_id, None, start_ndx, end_ndx, 100) 


def test_window_values():
    adh_client.Streams.getWindowValues(namespace_id, stream_id, start_ndx, end_ndx, None) 
    adh_client.Streams.getWindowValuesPaged(namespace_id, stream_id, None, start_ndx, end_ndx, 100) 
    adh_client.Streams.getWindowValuesForm(namespace_id, stream_id, None, start_ndx, end_ndx, 'tableh') 


def test_sampled_values():
    adh_client.Streams.getSampledValues(namespace_id, stream_id,  None, start_ndx, end_ndx, sample_by_prop_id, 1) 
    

def test_index_collection_values():
    adh_client.Streams.getIndexCollectionValues(namespace_id, stream_id, None, [1,2,3]) 


def test_value():
    adh_client.Streams.getFirstValue(namespace_id, stream_id, None)
    adh_client.Streams.getLastValue(namespace_id, stream_id, None)
    adh_client.Streams.getValue(namespace_id, stream_id, 1, None)


def test_summaries():
    adh_client.Streams.getSummaries(namespace_id, stream_id, None, start_ndx, end_ndx, 10) 


def test_metadata():
    adh_client.Streams.getMetadata(namespace_id, stream_id, 'Region')
    adh_client.Streams.getStreamType(namespace_id, stream_id) 
    adh_client.Streams.getTags(namespace_id, stream_id)