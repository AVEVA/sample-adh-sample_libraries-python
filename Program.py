from adh_sample_library_preview import (
    ADHClient,
)

import json
import datetime
import pandas as pd

appsettings = {}
with open('appsettings.json', 'r') as f:
    appsettings = json.load(f)

adh_client = ADHClient(
        appsettings.get('ApiVersion'),
        appsettings.get('TenantId'),
        appsettings.get('Resource'),
        appsettings.get('ClientId'),
        appsettings.get('ClientSecret')
    )
namespaceid = appsettings.get('NamespaceId')


selectedEventType = "MESJobHourlyResponse"

jsonEvents = []
c_token = True


""" start = "2024-04-17 00:00:00"
end = "2024-04-17 00:00:00"
timeFilter = 'starttime ge '+start+' AND starttime le '+end
#while c_token:
jsonEvents = adh_client.Events.getEvents(namespaceid,selectedEventType,filter=timeFilter,continuation_token="")
  #c_token = jsonEvents.get('ContinuationToken') """

jsonAssets = adh_client.Assets.getResolvedAsset(namespaceid,'truck1')
print(jsonAssets)






