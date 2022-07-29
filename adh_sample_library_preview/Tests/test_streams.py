import inspect
import json
import pytest

from adh_sample_library_preview.ADHClient import ADHClient
from adh_sample_library_preview.BaseClientStub import BaseClientStub
from adh_sample_library_preview.SDS.SdsBoundaryType import SdsBoundaryType
from adh_sample_library_preview.SDS.SdsStream import SdsStream
from adh_sample_library_preview.SDS.SdsType import SdsType
from adh_sample_library_preview.SDS.SdsTypeCode import SdsTypeCode
from adh_sample_library_preview.SDS.SdsTypeProperty import SdsTypeProperty


class Value:
    """Represents a data point to be injected into Sds Service"""

    def __init__(self):
        self._tan = None

    @property
    def tan(self):
        return self._tan

    @tan.setter
    def tan(self, tan):
        self._tan = tan

    def isprop(self):
        """Check whether a field is a property of an object"""
        return isinstance(self, property)

    def toJson(self):
        """Converts the object into JSON"""
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        """Converts the object into a dictionary"""
        dictionary = {}
        for prop in inspect.getmembers(type(self),
                                       lambda v: isinstance(v, property)):
            if hasattr(self, prop[0]):
                dictionary[prop[0]] = prop[1].fget(self)

        return dictionary
    
    @staticmethod
    def fromJson(json_obj):
        """Creates the object from JSON"""
        return Value.fromDictionary(json_obj)

    @staticmethod
    def fromDictionary(content):
        """Creates the object from a dictionary"""
        value = Value()

        if len(content) == 0:
            return value

        for prop in inspect.getmembers(type(value),
                                       lambda v: isinstance(v, property)):
            # Pre-Assign the default
            prop[1].fset(value, 0)

            # If found in JSON object, then set
            if prop[0] in content:
                value = content[prop[0]]
                if value is not None:
                    prop[1].fset(value, value)

        return value


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

    values = []
    for i in range(1, 3):
        val = Value()
        val.tan = i
        values.append(val)

    client.Streams.insertValues(namespace_id, stream_id, values)


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


@pytest.fixture(scope="session")
def e2e(pytestconfig):
    return pytestconfig.getoption("e2e")


@pytest.fixture
def data(e2e):
    if e2e:
        return get_credentials()
    else:
        return {
            "NamespaceId": "test",
            "StreamId": "test",
            "StartIndex": '2022-01-01',
            "EndIndex": '2022-01-01',
        }
        

@pytest.fixture()
def client(data, e2e):
    """ setup any state specific to the execution of the given module."""

    # If test credentials are provided run E2E tests, otherwise run Unit tests
    if e2e:
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

def test_range_values(client, data):        
    client.Streams.getRangeValues(data.get('NamespaceId'), data.get('StreamId'), Value, data.get('StartIndex'), 0, 100, False, SdsBoundaryType.Exact) 
    client.Streams.getRangeValuesInterpolated(data.get('NamespaceId'), data.get('StreamId'), Value, data.get('StartIndex'), data.get('EndIndex'), 100) 


def test_window_values(client, data):
    client.Streams.getWindowValues(data.get('NamespaceId'), data.get('StreamId'), data.get('StartIndex'), data.get('EndIndex'), Value) 
    client.Streams.getWindowValuesPaged(data.get('NamespaceId'), data.get('StreamId'), data.get('StartIndex'), data.get('EndIndex'), 100, value_class=Value) 
    client.Streams.getWindowValuesForm(data.get('NamespaceId'), data.get('StreamId'), Value, data.get('StartIndex'), data.get('EndIndex'), 'tableh') 


def test_sampled_values(client, data):
    client.Streams.getSampledValues(data.get('NamespaceId'), data.get('StreamId'),  Value, data.get('StartIndex'), data.get('EndIndex'), 'Tan', 1) 
    

def test_index_collection_values(client, data):
    client.Streams.getIndexCollectionValues(data.get('NamespaceId'), data.get('StreamId'), Value, [1,2,3]) 


def test_value(client, data):
    client.Streams.getFirstValue(data.get('NamespaceId'), data.get('StreamId'), Value)
    client.Streams.getLastValue(data.get('NamespaceId'), data.get('StreamId'), Value)
    client.Streams.getLastValue(data.get('NamespaceId'), data.get('StreamId'), None)
    client.Streams.getValue(data.get('NamespaceId'), data.get('StreamId'), 1, Value)


def test_summaries(client, data):
    client.Streams.getSummaries(data.get('NamespaceId'), data.get('StreamId'), None, data.get('StartIndex'), data.get('EndIndex'), 10) 


def test_metadata(client, data):
    client.Streams.getMetadata(data.get('NamespaceId'), data.get('StreamId'), 'Region')
    client.Streams.getStreamType(data.get('NamespaceId'), data.get('StreamId')) 
    client.Streams.getTags(data.get('NamespaceId'), data.get('StreamId'))