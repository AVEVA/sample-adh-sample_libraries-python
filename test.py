import json
from adh_sample_library_preview.ADHClient import ADHClient

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
namespace_id = appsettings.get('NamespaceId')
tenant_id = appsettings.get('TenantId')

adh_client = ADHClient(api_version=appsettings.get('ApiVersion'), 
                        tenant=tenant_id, 
                        url=appsettings.get('Resource'), 
                        client_id=appsettings.get('ClientId'), 
                        client_secret=appsettings.get('ClientSecret'), 
                        accept_verbosity=appsettings.get('AcceptVerbosity'))

stream = adh_client.Streams.getResolvedStream(namespace_id=namespace_id, stream_id='PowerFlexCTR_0061-01-02-04')
print(stream)