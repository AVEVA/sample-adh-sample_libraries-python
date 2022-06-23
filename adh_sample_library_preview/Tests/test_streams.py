import json
import pytest
from genericpath import exists

from adh_sample_library_preview.ADHClient import ADHClient
from adh_sample_library_preview.BaseClientStub import BaseClientStub
from adh_sample_library_preview.SDS.SdsBoundaryType import SdsBoundaryType
from adh_sample_library_preview.SDS.SdsStream import SdsStream
from adh_sample_library_preview.SDS.SdsType import SdsType
from adh_sample_library_preview.SDS.SdsTypeCode import SdsTypeCode
from adh_sample_library_preview.SDS.SdsTypeProperty import SdsTypeProperty

def create_type(namespace_id, type_id, client: ADHClient):
    double_type = SdsType('doubleType', SdsTypeCode.Double)
    tan_property = SdsTypeProperty('Tan', True, double_type)
    type = SdsType(type_id, SdsTypeCode.Object, [tan_property])

    client.Types.getOrCreateType(namespace_id, type)
    
                
def create_stream(namespace_id, stream_id, type_id, client: ADHClient):
    stream = SdsStream(stream_id, type_id)

    client.Streams.createOrUpdateStream(namespace_id, stream)

    client.Streams.createOrUpdateTags(
        namespace_id, stream_id, ['waves'])

    client.Streams.createOrUpdateMetadata(
        namespace_id, stream_id, {'Region': 'North America'})


def cleanup(namespace_id, type_id, stream_id, client: ADHClient):
    client.Streams.deleteStream(namespace_id, stream_id)
    client.Types.deleteType(namespace_id, type_id)


def get_credentials():
    try:
        with open(
            'appsettings.json',
            'r',
        ) as f:
            cred = json.load(f)
    except Exception as error:
        print(f'Error: {str(error)}')
        print(f'Could not open/read appsettings.json')
        exit()

    return cred


@pytest.fixture
def data():
    if exists('appsettings.json'):
        return get_credentials()
    else:
        return {
            "NamespaceId": "test",
            "StreamId": "test",
            "StartIndex": '2022-01-01',
            "EndIndex": '2022-01-01',
        }
        

@pytest.fixture()
def client(data):
    """ setup any state specific to the execution of the given module."""

    # If test credentials are provided run E2E tests, otherwise run Unit tests
    if exists('appsettings.json'):
        adh_client = ADHClient(api_version=data.get('ApiVersion'), 
                                tenant=data.get('TenantId'), 
                                url=data.get('Resource'), 
                                client_id=data.get('ClientId'), 
                                client_secret=data.get('ClientSecret'), 
                                accept_verbosity=data.get('AcceptVerbosity'))

        create_type(data.get('NamespaceId'), data.get('TypeId'), adh_client)
        create_stream(data.get('NamespaceId'), data.get('StreamId'), data.get('TypeId'), adh_client)

        yield adh_client

        # Clean up resources after tests have run
        cleanup(data.get('NamespaceId'), data.get('TypeId'), data.get('StreamId'), adh_client)
    else:
        base_client = BaseClientStub()
        adh_client = ADHClient(api_version=None, url=None, tenant=None, base_client=base_client)
        yield adh_client


def test_stream_retrieval(client, data):
    client.Streams.getStreams(data.get('NamespaceId'))
    client.Streams.getStream(data.get('NamespaceId'), data.get('StreamId'))
    client.Streams.getResolvedStream(data.get('NamespaceId'), data.get('StreamId'))

def test_range_values(client, data):        
    client.Streams.getRangeValues(data.get('NamespaceId'), data.get('StreamId'), None, data.get('StartIndex'), 0, 100, False, SdsBoundaryType.Exact) 
    client.Streams.getRangeValuesInterpolated(data.get('NamespaceId'), data.get('StreamId'), None, data.get('StartIndex'), data.get('EndIndex'), 100) 


def test_window_values(client, data):
    client.Streams.getWindowValues(data.get('NamespaceId'), data.get('StreamId'), data.get('StartIndex'), data.get('EndIndex'), None) 
    client.Streams.getWindowValuesPaged(data.get('NamespaceId'), data.get('StreamId'), None, data.get('StartIndex'), data.get('EndIndex'), 100) 
    client.Streams.getWindowValuesForm(data.get('NamespaceId'), data.get('StreamId'), None, data.get('StartIndex'), data.get('EndIndex'), 'tableh') 


def test_sampled_values(client, data):
    client.Streams.getSampledValues(data.get('NamespaceId'), data.get('StreamId'),  None, data.get('StartIndex'), data.get('EndIndex'), 'Tan', 1) 
    

def test_index_collection_values(client, data):
    client.Streams.getIndexCollectionValues(data.get('NamespaceId'), data.get('StreamId'), None, [1,2,3]) 


def test_value(client, data):
    client.Streams.getFirstValue(data.get('NamespaceId'), data.get('StreamId'), None)
    client.Streams.getLastValue(data.get('NamespaceId'), data.get('StreamId'), None)
    client.Streams.getValue(data.get('NamespaceId'), data.get('StreamId'), 1, None)


def test_summaries(client, data):
    client.Streams.getSummaries(data.get('NamespaceId'), data.get('StreamId'), None, data.get('StartIndex'), data.get('EndIndex'), 10) 


def test_metadata(client, data):
    client.Streams.getMetadata(data.get('NamespaceId'), data.get('StreamId'), 'Region')
    client.Streams.getStreamType(data.get('NamespaceId'), data.get('StreamId')) 
    client.Streams.getTags(data.get('NamespaceId'), data.get('StreamId'))