# AVEVA Data Hub Python Library Sample

| :loudspeaker: **Notice**: This library is an AVEVA Data Hub targeted version of the ocs_sample_library_preview. The ocs_sample_library_preview library is being deprecated and this library should be used moving forward. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Version:** 0.10.2_preview

[![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/ADH/aveva.sample-adh-sample_libraries-python?branchName=main)](https://dev.azure.com/osieng/engineering/_build/latest?definitionId=4674&branchName=main)

This sample library requires Python 3.7+. You can download Python [here](https://www.python.org/downloads/).

- **NOTE**: The library previously required Python 3.9+ to take advantage of type annotations. To provide compatibility with environments that cannot upgrade Python to 3.9, `from __future__ import annotations` was added to each necessary file. [This provides backwards compatibility down to Python 3.7](https://docs.python.org/3/library/__future__.html).

## About the library

The python ADH library is an introductory language-specific example of programming against Aveva Data Hub ([ADH](https://www.osisoft.com/Solutions/OSIsoft-Cloud-Services/)). It is intended as instructional samples only and are not for production use. _The samples also work on OSIsoft Cloud Services unless otherwise noted._

They can be obtained by running: `pip install adh_sample_library_preview`

The library is not intended to show every endpoint and every option/parameter for endpoints it has. The library is known to be incomplete.

Other language libraries and samples are available on [GitHub](https://github.com/osisoft/OSI-Samples).

## Testing

The library is tested using PyTest. To test locally, make sure that PyTest is installed, then navigate to the Tests directory and run the test classes by executing 
```
python -m pytest {testclass} 
```

where {testclass} is the name of a test class, for example ./test_baseclient.py. 

Optionally to run end to end tests, rename the appsettings.placeholder.json file to appsettings.json and populate the fields, (This file is included in the gitignore and will not be pushed to a remote repository), then run 
```
python -m pytest {testclass} --e2e True
```

## Logging

Every request made by the library is logged using the standard [Python logging library](https://docs.python.org/3/library/logging.html). If the client application using the library creates a logger, then library will log to it at the following levels:

| Level | Usage                                                                                                                      |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| Error | any non 200-level response code, along with the error message                                                              |
| Info  | all request urls and verbs <br/> all response status codes                                                                 |
| Debug | data payload and all request headers (Authorization header value redacted) <br/> response content and all response headers |

The process for creating a logger is described in the [Logging HOWTO documentation](https://docs.python.org/3/howto/logging.html).

An example walkthrough is shown here:

### Logger Creation Example

To initiate logging, the client must create a logger, defining a log file, a desired log level, and default formatting:

```python
    # Step 0 - set up logger
    log_file = 'logfile.txt'
    log_level = logging.INFO
    logging.basicConfig(filename=log_file, encoding='utf-8', level=log_level, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(module)16s,line: %(lineno)4d %(levelname)8s | %(message)s')
```

This creates a logger object that streams any logged messages to the desired output. The libraries called by the client, including this `ADH Sample Library Python`, that have implemented logging will send their messages to this logger automatically.

The [log level](https://docs.python.org/3/library/logging.html#logging-levels) specified will result in any log at that level _or higher_ to be logged. For example, `INFO` captures `INFO`, `WARNING`, `ERROR`, and `CRITICAL`, but ignores `DEBUG`.

### Logger Usage Example

To change the log level after creation, the level can be set using the following command

```python
logging.getLogger().setLevel(logging.DEBUG)
```

This concept is particularly helpful when debugging a specific call within the application. Logging can be changed before and after a call to the library in order to provide debug logs for that specific call only, without flooding the logs with debug entries for every other call to the library.

An example of this can be seen here.

```python
    # Step 4 - Retrieve the data view
    original_level = logging.getLogger().level
    logging.getLogger().setLevel(logging.DEBUG)

    dataview = adh_client.DataViews.getDataView(
        namespace_id, SAMPLE_DATAVIEW_ID)

    logging.getLogger().setLevel(original_level)
```

Note that the original level was recorded, logging was set to debug, the `getDataView` call was performed, then logging was set to its previous level. The logs will contain debug message for only this call, and all other calls before and after will be logged with their original level.

---

Developed using Python 3.10.1

[AVEVA Samples](https://github.com/osisoft/OSI-samples) are licensed under the Apache 2 license.

For the main ADH sample libraries page [ReadMe](https://github.com/osisoft/OSI-Samples-ADH/blob/main/docs/SAMPLE_LIBRARIES.md)  
For the main ADH samples page [ReadMe](https://github.com/osisoft/OSI-Samples-ADH)  
For the main AVEVA samples page [ReadMe](https://github.com/osisoft/OSI-Samples)
