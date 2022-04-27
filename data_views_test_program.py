"""This sample script demonstrates how to invoke the Data View REST API"""

import json
import copy
import datetime
import logging
import random
import traceback
from adh_sample_library_preview import (DataView, Field, FieldSource, ADHClient, Query,
                                        SdsStream, SdsType, SdsTypeCode, 
                                        SdsTypeProperty, SummaryDirection, SdsSummaryType)

# Sample Data Information
SAMPLE_TYPE_ID_1 = 'Time_SampleType1'
SAMPLE_TYPE_ID_2 = 'Time_SampleType2'
SAMPLE_STREAM_ID_1 = 'dvTank2'
SAMPLE_STREAM_NAME_1 = 'Tank2'
SAMPLE_STREAM_ID_2 = 'dvTank100'
SAMPLE_STREAM_NAME_2 = 'Tank100'
SAMPLE_FIELD_TO_CONSOLIDATE_TO = 'temperature'
SAMPLE_FIELD_TO_CONSOLIDATE = 'ambient_temp'
SAMPLE_FIELD_TO_ADD_UOM_COLUMN_1 = 'pressure'
SAMPLE_FIELD_TO_ADD_UOM_COLUMN_2 = 'temperature'
SUMMARY_FIELD_ID = 'pressure'
SUMMARY_TYPE_1 = 'Mean'
SUMMARY_TYPE_2 = 'Total'

# Data View Information
SAMPLE_DATAVIEW_ID = 'DataView_Sample'
SAMPLE_DATAVIEW_NAME = 'DataView_Sample_Name'
SAMPLE_DATAVIEW_DESCRIPTION = 'A Sample Description that describes that this '\
    'Data View is just used for our sample.'
SAMPLE_QUERY_ID = 'stream'
SAMPLE_QUERY_STRING = 'dvTank*'
SAMPLE_INTERVAL = '00:20:00'


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

def suppress_error(sds_call):
    """Suppresses an error thrown by SDS"""
    try:
        sds_call()
    except Exception as error:
        print(('Encountered Error: {error}'.format(error=error)))


def find_field(fieldset_fields, field_source):
    """Find a field by field source"""
    for field in fieldset_fields:
        if field.Source == field_source:
            return field
    return None


def find_fieldset(fieldsets, fieldset_query_id):
    """Find a fieldset by query id"""
    for fieldset in fieldsets:
        if fieldset.QueryId == fieldset_query_id:
            return fieldset
    return None


def find_field_key(fieldset_fields, field_source, key):
    """Find a field by source and key"""
    for field in fieldset_fields:
        if field.Source == field_source and any(key in s for s in field.Keys):
            return field
    return None


def main(test=False):
    """This function is the main body of the Data View sample script"""
    exception = None

    appsettings = get_appsettings()

    print('--------------------------------------------------------------------')
    print(' ######                      #    #                 ######  #     # ')
    print(' #     #   ##   #####   ##   #    # # ###### #    # #     #  #   #  ')
    print(' #     #  #  #    #    #  #  #    # # #      #    # #     #   # #   ')
    print(' #     # #    #   #   #    # #    # # #####  #    # ######     #    ')
    print(' #     # ######   #   ###### #    # # #      # ## # #          #    ')
    print(' #     # #    #   #   #    #  #  #  # #      ##  ## #          #    ')
    print(' ######  #    #   #   #    #   ##   # ###### #    # #          #    ')
    print('--------------------------------------------------------------------')

    # Step 0 - set up logger
    log_file = 'logfile.txt'
    log_level = logging.DEBUG
    logging.basicConfig(filename=log_file, encoding='utf-8', level=log_level, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(module)16s,line: %(lineno)4d %(levelname)8s | %(message)s')

    # Step 1
    print()
    print('Step 1: Authenticate against ADH')
    adh_client = ADHClient(appsettings.get('ApiVersion'),
                           appsettings.get('TenantId'),
                           appsettings.get('Resource'),
                           appsettings.get('ClientId'),
                           appsettings.get('ClientSecret'))

    namespace_id = appsettings.get('NamespaceId')
    #namespace_id = 'fake'

    #adh_client.LoggerFlags.DataViews = True
    #adh_client.__base_client.__logger_flags.DataViews = True

    print(namespace_id)
    print(adh_client.uri)

    try:

        # Step 2
        print()
        print('Step 2: Create types, streams, and data')
        times = create_data(namespace_id, adh_client)
        sample_start_time = times[0]
        sample_end_time = times[1]

        # Step 3
        print()
        print('Step 3: Create a data view')
        dataview = DataView(SAMPLE_DATAVIEW_ID,
                            SAMPLE_DATAVIEW_NAME, SAMPLE_DATAVIEW_DESCRIPTION)
        adh_client.DataViews.postDataView(namespace_id, dataview)

        # Step 4
        print()
        print('Step 4: Retrieve the data view')
        dataview = adh_client.DataViews.getDataView(
            namespace_id, SAMPLE_DATAVIEW_ID)
        print(dataview.toJson())

        # Step 5
        print()
        print('Step 5: Add a query for data items')
        query = Query(SAMPLE_QUERY_ID, value=SAMPLE_QUERY_STRING)
        dataview.Queries = [query]
        # No Data View returned, success is 204
        adh_client.DataViews.putDataView(namespace_id, dataview)

        # Step 6
        print()
        print('Step 6: View items found by the query')
        print('List data items found by the query:')
        data_items = adh_client.DataViews.getResolvedDataItems(
            namespace_id, SAMPLE_DATAVIEW_ID, SAMPLE_QUERY_ID)
        print(data_items.toJson())

        print('List ineligible data items found by the query:')
        data_items = adh_client.DataViews.getResolvedIneligibleDataItems(
            namespace_id, SAMPLE_DATAVIEW_ID, SAMPLE_QUERY_ID)
        print(data_items.toJson())

        # Step 7
        print()
        print('Step 7: View fields available to include in the data view')
        available_fields = adh_client.DataViews.getResolvedAvailableFieldSets(
            namespace_id, SAMPLE_DATAVIEW_ID)
        print(available_fields.toJson())

        # Step 8
        print()
        print('Step 8: Include some of the available fields')
        dataview.DataFieldSets = available_fields.Items
        adh_client.DataViews.putDataView(namespace_id, dataview)

        print('List available field sets:')
        available_fields = adh_client.DataViews.getResolvedAvailableFieldSets(
            namespace_id, SAMPLE_DATAVIEW_ID)
        print(available_fields.toJson())

        print('Retrieving interpolated data from the data view:')
        dataview_data = adh_client.DataViews.getDataInterpolated(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, interval=SAMPLE_INTERVAL)
        print(str(dataview_data))
        print(len(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view interpolated data'

        print('Retrieving stored data from the data view:')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time)
        print(str(dataview_data))
        print(len(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view stored data'

        # Step 9
        print()
        print('Step 9: Group the data view')
        grouping = Field(source=FieldSource.Id,
                         label='{DistinguisherValue} {FirstKey}')
        dataview.GroupingFields = [grouping]
        # No DataView returned, success is 204
        adh_client.DataViews.putDataView(namespace_id, dataview)

        print('Retrieving interpolated data from the data view:')
        dataview_data = adh_client.DataViews.getDataInterpolated(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, interval=SAMPLE_INTERVAL)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view interpolated data'

        print('Retrieving stored data from the data view:')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view stored data'

        # Step 10
        print()
        print('Step 10: Identify data items')
        identify = dataview.GroupingFields.pop()
        dataview_dataitem_fieldset = find_fieldset(
            dataview.DataFieldSets, SAMPLE_QUERY_ID)
        dataview_dataitem_fieldset.IdentifyingField = identify
        # No Data View returned, success is 204
        adh_client.DataViews.putDataView(namespace_id, dataview)

        print('Retrieving interpolated data from the data view:')
        dataview_data = adh_client.DataViews.getDataInterpolated(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, interval=SAMPLE_INTERVAL)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view interpolated data'

        print('Retrieving stored data from the data view:')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view stored data'

        # Step 11
        print()
        print('Step 11: Consolidate data fields')
        field1 = find_field_key(dataview_dataitem_fieldset.DataFields,
                                FieldSource.PropertyId, SAMPLE_FIELD_TO_CONSOLIDATE_TO)
        field2 = find_field_key(dataview_dataitem_fieldset.DataFields,
                                FieldSource.PropertyId, SAMPLE_FIELD_TO_CONSOLIDATE)
        print(field1.toJson())
        print(field2.toJson())
        field1.Keys.append(SAMPLE_FIELD_TO_CONSOLIDATE)
        dataview_dataitem_fieldset.DataFields.remove(field2)
        # No Data View returned, success is 204
        adh_client.DataViews.putDataView(namespace_id, dataview)

        print('Retrieving interpolated data from the data view:')
        dataview_data = adh_client.DataViews.getDataInterpolated(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, interval=SAMPLE_INTERVAL)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view interpolated data'

        print('Retrieving stored data from the data view:')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view stored data'

        # Step 12
        print()
        print('Step 12: Add Units of Measure Column')
        field1 = find_field_key(dataview_dataitem_fieldset.DataFields,
                                FieldSource.PropertyId, SAMPLE_FIELD_TO_ADD_UOM_COLUMN_1)
        field2 = find_field_key(dataview_dataitem_fieldset.DataFields,
                                FieldSource.PropertyId, SAMPLE_FIELD_TO_ADD_UOM_COLUMN_2)
        
        field1.IncludeUom = True
        field2.IncludeUom = True
        adh_client.DataViews.putDataView(namespace_id, dataview)

        print('Retrieving interpolated data from the data view:')
        dataview_data = adh_client.DataViews.getDataInterpolated(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, interval=SAMPLE_INTERVAL)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view interpolated data'

        print('Retrieving stored data from the data view:')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view stored data'

        # Step 13
        print()
        print('Step 13: Add Summaries Columns')
        # find the field for which we want to add a couple summary columns
        ref_field = find_field_key(dataview_dataitem_fieldset.DataFields,
                                FieldSource.PropertyId, SAMPLE_FIELD_TO_ADD_UOM_COLUMN_1)
        
        # deep copy the field twice so we can change properties
        field1 = copy.deepcopy(ref_field)
        field2 = copy.deepcopy(ref_field)
        
        # set the summary properties and add the fields to the data fields array
        field1.SummaryDirection = SummaryDirection.Forward
        field1.SummaryType = SdsSummaryType[SUMMARY_TYPE_1]
        field2.SummaryDirection = SummaryDirection.Forward
        field2.SummaryType = SdsSummaryType[SUMMARY_TYPE_2]

        dataview_dataitem_fieldset.DataFields.append(field1)
        dataview_dataitem_fieldset.DataFields.append(field2)
        
        adh_client.DataViews.putDataView(namespace_id, dataview)

        print('Retrieving interpolated data from the data view:')
        dataview_data = adh_client.DataViews.getDataInterpolated(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, interval=SAMPLE_INTERVAL)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view interpolated data'

        print('Retrieving stored data from the data view:')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time)
        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view stored data'

        # Step 14
        print()
        print('Step 14: Iterate through pages of results')

        print('Retrieving interpolated data from the data view with a page size of 2 rows to force paging:')
        dataview_data, next_page, first_page = adh_client.DataViews.getDataInterpolated(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, interval=SAMPLE_INTERVAL, count=2)

        # iterate through each subsequent page of results until there are no more pages
        while next_page != None:
            data_page, next_page, first_page = adh_client.DataViews.getDataInterpolated(url=next_page)
            dataview_data.extend(data_page)

        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view interpolated data'

        print('Retrieving stored data from the data view with a page size of 2 rows to force paging:')
        dataview_data, next_page, first_page = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=sample_start_time,
            end_index=sample_end_time, count=2)

        # iterate through each subsequent page of results until there are no more pages
        while next_page != None:
            data_page, next_page, first_page = adh_client.DataViews.getDataInterpolated(url=next_page)
            dataview_data.extend(data_page)

        print(str(dataview_data))
        assert len(dataview_data) > 0, 'Error getting data view stored data'

        # Step 15
        print()
        print('Step 15: Demonstrate verbosity header usage')

        print('Writing null values to the streams')
        # Keep the times in the future, guaranteeing no overlaps with existing data
        null_data_start_time = datetime.datetime.now() + datetime.timedelta(hours=1)
        null_data_end_time = null_data_start_time + datetime.timedelta(hours=1)

        # The first value is only a pressure, keeping temperature as null. Vice versa for the second
        values = [{"time": null_data_start_time.isoformat(timespec='seconds'), "pressure": 100}, # temperature is null
                  {"time": null_data_end_time.isoformat(timespec='seconds'), "temperature": 50}] # pressure is null
        adh_client.Streams.insertValues(namespace_id, SAMPLE_STREAM_ID_1, json.dumps(values))
        adh_client.Streams.insertValues(namespace_id, SAMPLE_STREAM_ID_2, json.dumps(values))

        print()
        print('Data View results will not include null values written to nullable properties if the accept-verbosity header is set to non-verbose.')
        print('The values just written include nulls for one of the properties; note the presence or absense of these values in the following outputs:')
        print()
        print('Retrieving these values in the data view with the base client setting of accept-verbosity set to False will use accept-verbosity: non-verbose')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=null_data_start_time,
            end_index=null_data_end_time)
        print()
        print(str(dataview_data))
        print()

        print('The client\'s accept-verbosity setting can be overridden at the query level with the verbose parameter, returning verbose data view data')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=null_data_start_time,
            end_index=null_data_end_time, verbose=True)
        print()
        print(str(dataview_data))
        print()

        print('Alternatively, enabling the base client\'s accept-verbosity setting will also result in verbose data view output, but is a client-wide setting')
        adh_client.acceptverbosity = True

        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=null_data_start_time,
            end_index=null_data_end_time)
        print()
        print(str(dataview_data))
        print()

        print('A verbose client can also be overridden to show non-verbose data view output using the verbose parameter.')
        dataview_data = adh_client.DataViews.getDataStored(
            namespace_id, SAMPLE_DATAVIEW_ID, start_index=null_data_start_time,
            end_index=null_data_end_time, verbose=False)
        print()
        print(str(dataview_data))
        print()

        print()
        print('Setting the accept-verbosity back to the original value')
        adh_client.acceptverbosity = False

    except Exception as error:
        print((f'Encountered Error: {error}'))
        print()
        traceback.print_exc()
        print()
        exception = error

    finally:

        #######################################################################
        # Data View deletion
        #######################################################################

        # Step 16
        print()
        print('Step 16: Delete sample objects from OCS')
        print('Deleting data view...')

        suppress_error(lambda: adh_client.DataViews.deleteDataView(
            namespace_id, SAMPLE_DATAVIEW_ID))

        # check, including assert is added to make sure we deleted it
        dataview = None
        try:
            dataview = adh_client.DataViews.getDataView(
                namespace_id, SAMPLE_DATAVIEW_ID)
        except Exception as error:
            # Exception is expected here since Data View has been deleted
            dataview = None
        finally:
            assert dataview is None, 'Delete failed'
            print('Verification OK: Data View deleted')

        print('Deleting sample streams...')
        suppress_error(lambda: adh_client.Streams.deleteStream(
            namespace_id, SAMPLE_STREAM_ID_1))
        suppress_error(lambda: adh_client.Streams.deleteStream(
            namespace_id, SAMPLE_STREAM_ID_2))

        print('Deleting sample types...')
        suppress_error(lambda: adh_client.Types.deleteType(
            namespace_id, SAMPLE_TYPE_ID_1))
        suppress_error(lambda: adh_client.Types.deleteType(
            namespace_id, SAMPLE_TYPE_ID_2))

        if test and exception is not None:
            raise exception
    print('Complete!')


def create_data(namespace_id, adh_client: ADHClient):
    """Creates sample data for the script to use"""

    double_type = SdsType('doubleType', SdsTypeCode.NullableDouble)
    datetime_type = SdsType('dateTimeType', SdsTypeCode.DateTime)

    pressure_property = SdsTypeProperty('pressure', False, double_type, uom='bar')
    temperature_property = SdsTypeProperty(SAMPLE_FIELD_TO_CONSOLIDATE_TO, False,
                                            double_type, uom='degree Celsius')
    ambient_temperature_property = SdsTypeProperty(SAMPLE_FIELD_TO_CONSOLIDATE, False,
                                            double_type, uom='degree Celsius')
    time_property = SdsTypeProperty('time', True, datetime_type)

    sds_type_1 = SdsType(
        SAMPLE_TYPE_ID_1, SdsTypeCode.Object, [
            pressure_property, temperature_property, time_property],
        description='This is a sample Sds type for storing Pressure type '
                    'events for Data Views')

    sds_type_2 = SdsType(
        SAMPLE_TYPE_ID_2, SdsTypeCode.Object, [
            pressure_property, ambient_temperature_property, time_property],
        description='This is a new sample Sds type for storing Pressure type '
                    'events for Data Views')

    print('Creating SDS Types...')
    adh_client.Types.getOrCreateType(namespace_id, sds_type_1)
    adh_client.Types.getOrCreateType(namespace_id, sds_type_2)

    stream1 = SdsStream(
        SAMPLE_STREAM_ID_1,
        SAMPLE_TYPE_ID_1,
        SAMPLE_STREAM_NAME_1,
        'A Stream to store the sample Pressure events')

    stream2 = SdsStream(
        SAMPLE_STREAM_ID_2,
        SAMPLE_TYPE_ID_2,
        SAMPLE_STREAM_NAME_2,
        'A Stream to store the sample Pressure events')

    print('Creating SDS Streams...')
    adh_client.Streams.createOrUpdateStream(namespace_id, stream1)
    adh_client.Streams.createOrUpdateStream(namespace_id, stream2)

    sample_start_time = datetime.datetime.now() - datetime.timedelta(hours=1)
    sample_end_time = datetime.datetime.now()

    values1 = []
    values2 = []

    def value_with_time(timestamp, value, field_name, value2):
        """Formats a JSON data object"""
        return f'{{"time": "{timestamp}", "pressure": {str(value)}, "{field_name}": {str(value2)}}}'

    print('Generating values...')
    for i in range(1, 30, 1):
        timestamp = (sample_start_time + datetime.timedelta(minutes=i * 2)
                     ).isoformat(timespec='seconds')
        val1 = value_with_time(timestamp, random.uniform(
            0, 100), SAMPLE_FIELD_TO_CONSOLIDATE_TO, random.uniform(50, 70))
        val2 = value_with_time(timestamp, random.uniform(
            0, 100), SAMPLE_FIELD_TO_CONSOLIDATE, random.uniform(50, 70))

        values1.append(val1)
        values2.append(val2)

    print('Sending values...')
    adh_client.Streams.insertValues(
        namespace_id,
        SAMPLE_STREAM_ID_1,
        str(values1).replace("'", ""))
    adh_client.Streams.insertValues(
        namespace_id,
        SAMPLE_STREAM_ID_2,
        str(values2).replace("'", ""))

    return (sample_start_time, sample_end_time)


if __name__ == '__main__':
    main()
