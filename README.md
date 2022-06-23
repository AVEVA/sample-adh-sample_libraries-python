# AVEVA Data Hub Python Library Sample

| :loudspeaker: **Notice**: This library is an AVEVA Data Hub targeted version of the ocs_sample_library_preview. The ocs_sample_library_preview library is being deprecated and this library should be used moving forward. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Version:** 0.7.6_preview

[![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/ADH/aveva.sample-adh-sample_libraries-python?branchName=main)](https://dev.azure.com/osieng/engineering/_build/latest?definitionId=4674&branchName=main)

This sample library requires Python 3.7+. You can download Python [here](https://www.python.org/downloads/).

- **NOTE**: The library previously required Python 3.9+ to take advantage of type annotations. To provide compatibility with environments that cannot upgrade Python to 3.9, `from __future__ import annotations` was added to each necessary file. [This provides backwards compatibility down to Python 3.7](https://docs.python.org/3/library/__future__.html).

## About the library

The python ADH library is an introductory language-specific example of programming against Aveva Data Hub ([ADH](https://www.osisoft.com/Solutions/OSIsoft-Cloud-Services/)). It is intended as instructional samples only and are not for production use. _The samples also work on OSIsoft Cloud Services unless otherwise noted._

They can be obtained by running: `pip install adh_sample_library_preview`

The library is not intended to show every endpoint and every option/parameter for endpoints it has. The library is known to be incomplete.

Other language libraries and samples are available on [GitHub](https://github.com/osisoft/OSI-Samples).

Tests are done by testing the sample apps that use this.

---

Developed using Python 3.9.5.

[AVEVA Samples](https://github.com/osisoft/OSI-samples) are licensed under the Apache 2 license.

For the main ADH sample libraries page [ReadMe](https://github.com/osisoft/OSI-Samples-ADH/blob/main/docs/SAMPLE_LIBRARIES.md)  
For the main ADH samples page [ReadMe](https://github.com/osisoft/OSI-Samples-ADH)  
For the main AVEVA samples page [ReadMe](https://github.com/osisoft/OSI-Samples)
