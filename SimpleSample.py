from adh_sample_library_preview import AuthorizationTag, ADHClient, EnumerationState, EventGraphEventType, EventGraphEnumeration, EventGraphReferenceDataType, TypeProperty, PropertyTypeCode, PropertyTypeFlags, EventGraphReferenceDataCategory
import urllib3
import json
import requests


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


appsettings = get_appsettings()

resource = appsettings.get('Resource')
api_version = appsettings.get('ApiVersion')
tenant_id = appsettings.get('TenantId')
namespace_id = appsettings.get('NamespaceId')
client_id = appsettings.get('ClientId')
client_secret = appsettings.get('ClientSecret')

client = ADHClient(api_version, tenant_id, resource, client_id, client_secret)

# get event types
event_types = client.EventTypes.getEventTypes(namespace_id)
for event_type in event_types:
    print(event_type.Name)

# get reference data types
print()
reference_data_types = client.ReferenceDataTypes.getReferenceDataTypes(
    namespace_id)
for reference_data_type in reference_data_types:
    print(reference_data_type.Name)

# get Enumerations
print()
enumerations = client.Enumerations.getEnumerations(namespace_id)
for enumeration in enumerations:
    print(enumeration.Name)

# create authorization tag
authorization_tag = AuthorizationTag('TestAuthorizationTag')
authorization_tag = client.AuthorizationTags.getOrCreateAuthorizationTag(
    namespace_id, authorization_tag.Id, authorization_tag)
client.GraphQL.checkForSchemaChanges(namespace_id)

# create enumeration
members = [EnumerationState(name='on', code=1),
           EnumerationState(name='off', code=2)]
enumeration = EventGraphEnumeration(
    members, 'TestEnumeration', 'TestEnumeration', id='TestEnumeration')  # why is a description required here?
enumeration = client.Enumerations.getOrCreateEnumeration(
    namespace_id, enumeration.Id, enumeration)
client.GraphQL.checkForSchemaChanges(namespace_id)

# create reference data type
reference_data_type_name = 'TestReferenceDataType'
reference_data_type_properties = [
    TypeProperty(PropertyTypeCode.ASSET, 'ReferenceAssets', 'ReferenceAssets', 'ReferenceAssets',
                 PropertyTypeFlags.REVERSE_LOOKUP_IS_COLLECTION, property_type_id="none", remote_reference_name=reference_data_type_name),
    TypeProperty(PropertyTypeCode.DOUBLE, 'SomeValue')]
reference_data_type = EventGraphReferenceDataType(
    EventGraphReferenceDataCategory.REFERENCE_DATA, reference_data_type_properties, authorization_tag.Id, reference_data_type_name, id=reference_data_type_name)
reference_data_type = client.ReferenceDataTypes.getOrCreateReferenceDataType(
    namespace_id, reference_data_type.Id, reference_data_type)
client.GraphQL.checkForSchemaChanges(namespace_id)

# create reference data
reference_data_id = "TestReferenceData"
reference_data = [
    {
        "referenceAssets": [
            {"id": "DFPIafServerPrd.osisoft.ext_b4873d35-0e35-11eb-9383-f48c50815f37"}
        ],
        "someValue": 12,
        "id": reference_data_type.Id,
        "authorizationTags": [authorization_tag.Id]
    }
]

reference_data = client.ReferenceData.getOrCreateReferenceData(
    namespace_id, reference_data_type.Id, json.dumps(reference_data))

# create event type
event_type_name = 'TestEventType3'
event_type_properties = [
    TypeProperty(PropertyTypeCode.ASSET, 'ReferenceAssets', 'ReferenceAssets', 'ReferenceAssets',
                 PropertyTypeFlags.REVERSE_LOOKUP_IS_COLLECTION, property_type_id="none", remote_reference_name=event_type_name),
    TypeProperty(PropertyTypeCode.DOUBLE, 'SomeValue')]
event_type = EventGraphEventType(
    event_type_properties, authorization_tag.Id, event_type_name, id=event_type_name, version=1)
event_type = client.EventTypes.getOrCreateEventType(
    namespace_id, event_type_name, event_type)
client.GraphQL.checkForSchemaChanges(namespace_id)

# create events
event_id = "TestEvent"
events = [
    {
        "eventStartTime": "2023-06-23T23:01:38.256Z",
        "eventEndTime": "2023-06-23T23:01:38.256Z",
        "referenceAssets": [
            {"id": "DFPIafServerPrd.osisoft.ext_b4873d35-0e35-11eb-9383-f48c50815f37"}
        ],
        "someValue": 12,
        "id": event_type.Id,
        "authorizationTags": [authorization_tag.Id]
    }
]

events = client.Events.getOrCreateEvents(
    namespace_id, event_type.Id, json.dumps(events))

print()
print(events)

# retrieve events
retrieved_events = client.Events.getEvents(namespace_id, event_type.Id)
print()
print(retrieved_events)

# use a graphQL query to retrieve events
query = '''
{
  events {
    queryTestEventType1 {
      id
      referenceAssets {
        id
      }
      someValue
    }
  }
}
'''
graph_ql_events = client.GraphQL.executeQuery(namespace_id, query=query)
print()
print(graph_ql_events)

# delete events
for event in retrieved_events:
    client.Events.deleteEvent(namespace_id, event_type.Id, event['id'])
