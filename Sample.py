from adh_sample_library_preview import ADHClient, Event, EventType, EventProperty
import urllib3
import json
import requests


urllib3.disable_warnings()


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

def get():
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


def getEfsofTemplate(Template1):
    '''Sends the request out to the preconfigured endpoint'''
    url = f'https://localhost/piwebapi/eventframes/search?query=TemplateName:={Template1}&databaseWebId=F1RDWF8-0NH0eE2Ev6sUQIlUQAV06UgR9aGUWo0iiSMVIxiAVVNDSElMMTA2MTBcREFUQUJBU0Ux'

    response = requests.get(
        url,
        verify=False,
        timeout=60
    )

    eventframes = response.json()
    return eventframes["Items"]

def reqWrap(url):
    response = requests.get(
        url,
        verify=False,
        timeout=60
    )     
    return response.json()



def createADHEventTemplateFromEFtemaple(EF, EFtemplate):    
    ADH_ET = EventType(id=EFtemplate["Id"]+'z', name=EFtemplate["Name"]+'z',defaultAuthorizationTag="")
    
    for base in EF:
        if base =="Links" or base =="Id" or base =="Security" or base =="CAtegoryNames" or base =="ExtendedProperties":
            continue
        if base =="StartTime" or base =="EndTime":
            continue
#        if base =="Name":
 #           continue
        print(base)
        ep = EventProperty(id=base,propertyTypeCode='string')
        ADH_ET.Properties.append(ep)

    #need to add referenced assets spot -- probably need a better thing than this...
    for asset in EF["RefElementWebIds"]:
        i=0
        ep = EventProperty(id=f"Asset{i}", name=f"Asset{i}", propertyTypeCode="Asset")
        ADH_ET.Properties.append(ep)
        i= i+1
    
    EFAtt_templates = reqWrap(EFtemplate["Links"]['AttributeTemplates'])
    for efatt_template in EFAtt_templates["Items"]:
        ep = EventProperty(id=efatt_template['Id'], name=efatt_template['Name'], propertyTypeCode=efatt_template['Type'])
        ADH_ET.Properties.append(ep)

    return ADH_ET


def createADHEventFromEF(EF):
   # ADH_E = Event(id=EF["Id"], name=EF["Name"], eventEndTime=EF["EndTime"], eventStartTime=EF["StartTime"])
    ADH_E = Event(id=EF["Id"], eventEndTime=EF["EndTime"], eventStartTime=EF["StartTime"])

    
    for att in EF:
        if att =="Links" or att =="Id"or att =="Name"or att =="Security" or att =="CategoryNames" or att =="ExtendedProperties":
            continue
        if att =="StartTime" or att =="EndTime":
            continue
        if att =="RefElementWebIds":
            setattr(ADH_E, att, ",".join(EF[att]))
            continue
        setattr(ADH_E, att, EF[att])
    
    atts = reqWrap(EF["Links"]['Attributes'])['Items']

    for att in atts:
        if att =="Links" or att =="Id"or att =="Name"or att =="Security" or att =="CategoryNames" or att =="ExtendedProperties":
            continue
        if att =="StartTime" or att =="EndTime":
            continue
        if att =="RefElementWebIds":
            setattr(ADH_E, att, ",".join(EF[att]))
            continue
        setattr(ADH_E, att["Name"], reqWrap(att["Links"]['Value'])['Value'])

    assets = reqWrap(EF["Links"]['ReferencedElements'])
    for asset in assets['Items']:
        i=0
        setattr(ADH_E, f"Asset{i}", {'id': asset["Name"]})
        i= i+1



    
    return ADH_E


appsettings = get_appsettings()

resource = appsettings.get('Resource')
api_version = appsettings.get('ApiVersion')
tenant_id = appsettings.get('TenantId')
namespace_id = appsettings.get('NamespaceId')
client_id = appsettings.get('ClientId')
client_secret = appsettings.get('ClientSecret')

ocs_client = ADHClient(api_version, tenant_id, resource, client_id, client_secret)


efs = getEfsofTemplate('Template1')
EFtemplate = reqWrap(efs[0]["Links"]['Template'])
ADHEventTemplate = createADHEventTemplateFromEFtemaple(efs[0],EFtemplate)
ocs_client.Events.getOrCreateEventType(namespace_id,ADHEventTemplate)

for ef in efs:
    adE = createADHEventFromEF(ef)
    dictadE = adE.toJsonFulls()
    adEStr = json.dumps(dictadE)

    indices = [i for i in range(len(adEStr)) if adEStr.startswith('"', i)]
    indices2 = []
    for i in indices:
        indices2.append(i+1)
    a = "".join(c.lower() if i in indices2 else c for i, c in enumerate(adEStr))
    a = a.replace('false','"false"')
    a = a.replace('true','"true"')

 #   for i in index:
 #       adEStr[i+1] = adEStr[i+1].lower() 

    

    print(a)
    #ocs_client.Events.getOrCreateEvent(namespace_id,adE,ADHEventTemplate.Id)
    ocs_client.Events.getOrCreateEventStr(namespace_id,a,ADHEventTemplate.Id)

eventTypes=ocs_client.Events.getEventTypes(namespace_id)
for eventType in eventTypes:
    print(eventType.toJson())
