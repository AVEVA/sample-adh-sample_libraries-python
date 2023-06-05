from adh_sample_library_preview import ADHClient, Event, EventType, EventProperty
import urllib3
import json
import requests


urllib3.disable_warnings()

templateSuffix = 'z3'

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
    url = f'https://localhost/piwebapi/eventframes/search?query=TemplateName:={Template1}&databaseWebId=F1RDWF8-0NH0eE2Ev6sUQIlUQA2aLfYhJTSU2x0HFDfseyTwVVNDSElMMTA2MTBcUE9XRVIgR0VORVJBVElPTg'
#TODO update this to b
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
    ADH_ET = EventType(id=EFtemplate["Id"]+templateSuffix, name=EFtemplate["Name"]+templateSuffix,defaultAuthorizationTag="")
    
    for base in EF:
        if base =="Links" or base =="Id" or base =="Security" or base =="CategoryNames" or base =="ExtendedProperties":
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
       # ep = EventProperty(id=efatt_template['Id'], name=efatt_template['Name'], propertyTypeCode=efatt_template['Type'])
       ptc = efatt_template['Type']
       if ptc =='EnumerationValue':
           ptc = 'String'
    
       ep = EventProperty(id=efatt_template['Name'], name=efatt_template['Name'], propertyTypeCode=ptc)
       ADH_ET.Properties.append(ep)

    return ADH_ET

def createADHEventFromEF(EF):
   # ADH_E = Event(id=EF["Id"], name=EF["Name"], eventEndTime=EF["EndTime"], eventStartTime=EF["StartTime"])
    ADH_E = Event(id=EF["Id"], name=EF["Name"], eventEndTime=EF["EndTime"], eventStartTime=EF["StartTime"])

    
    for att in EF:
        if att =="Links" or att =="Id"or att =="Name"or att =="Security" or att =="CategoryNames" or att =="ExtendedProperties":
            continue
        if att =="StartTime" or att =="EndTime":
            continue
        if att =="Event Duration" or att =="Referenced Element Path":
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
        if att["Name"] =="Event Duration" or att["Name"] =="Referenced Element Path":
            continue
        if att =="RefElementWebIds":
            setattr(ADH_E, att, ",".join(EF[att]))
            continue
        val = reqWrap(att["Links"]['Value'])['Value']
        if not isinstance(val,str) and not isinstance(val,int) and not isinstance(val,float):
            val = val['Name']
        setattr(ADH_E, att["Name"], val)

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


efs = getEfsofTemplate('*Production')
EFtemplate = reqWrap(efs[0]["Links"]['Template'])
ADHEventTemplate = createADHEventTemplateFromEFtemaple(efs[0],EFtemplate)
ocs_client.Events.getOrCreateEventType(namespace_id,ADHEventTemplate)

print(ADHEventTemplate.Id)
for ef in efs:
    adE = createADHEventFromEF(ef)
    dictadE = adE.toJsonFulls()
    adEStr = json.dumps(dictadE)

#handle  camelCasing
    indices = [i for i in range(len(adEStr)) if adEStr.startswith('"', i)]
    indices2 = []
    for i in indices:
        indices2.append(i+1)
    a = "".join(c.lower() if i in indices2 else c for i, c in enumerate(adEStr))
#handle bools that are currently set to strings
    a = a.replace('false','"false"')
    a = a.replace('true','"true"')
#handle no spaces
    a = a.replace(' ', '')
#handle dashes in attribute name (specilized cases because dashes are needed in some values)
    a = a.replace('Power-10', 'Power10')

#handle bad values for attributes
    b = a.split('"')
    indexToHandle = []
    index = 0
    for c in b:
        if "valuedoesnothavetherequiredpercentgood" in c or "PIPointDataReferenc" in c or "calcFailed" in c:
            indexToHandle.append(index)
        index= index+1

    offset = 0
    for i in indexToHandle:
        i = i -offset
        b[i-1] = b[i-1] +'-1' +b[i+1]
        b.pop(i)
        b.pop(i)
        offset = offset +2

    a = '"'.join(b)
    
    print(a)    

    #ocs_client.Events.getOrCreateEvent(namespace_id,adE,ADHEventTemplate.Id)
    ocs_client.Events.getOrCreateEventStr(namespace_id,a,ADHEventTemplate.Id)

eventTypes=ocs_client.Events.getEventTypes(namespace_id)
for eventType in eventTypes:
    print(eventType.toJson())
