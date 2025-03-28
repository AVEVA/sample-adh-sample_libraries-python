# Version History

## 0.10.16_preview / 2025-03-07

- Fixed issue in Update toDictionary function

## 0.10.16_preview / 2025-03-07

- Fixed issue with status enum support
  
## 0.10.15_preview / 2025-01-29

- Fixed regression calling Signups without CommunityId
- BREAKING CHANGE: Changes to parameter order in Signups.createSignup and Signups.updateSignup

## 0.10.14_preview / 2024-12-26

- Fixed issue where variables were not included in GraphQL request

## 0.10.13_preview / 2024-12-03

- Fixed support for communities signups

## 0.10.12_preview / 2024-11-18

- Fixed events url encoding

## 0.10.11_preview / 2024-04-24

- Fixed Assets Bulk Creation

## 0.10.10_preview / 2024-01-18

- Fixed Signups import

## 0.10.9_preview / 2024-01-18

- Fixed toisoformat for Events

## 0.10.8_preview / 2023-12-21

- Implemented ChangeBroker features in the library

## 0.10.7_preview / 2023-12-20

- Fixed fromisoformat backwards compatibilty issue by replacing with dateutil isoparse

## 0.10.6_preview / 2023-12-20

- No changes, forcing update

## 0.10.5_preview / 2023-12-18

- Update Communities, Assets, and Events
- Add appsettings file parsing to library

## 0.10.4_preview / 2023-12-08

- Migrate Pipelines

## 0.10.3_preview / 2023-11-27

- Update Event Store features
- Add Units

## 0.10.2_preview / 2023-11-16

- Add created and modified date to SdsStream, Sdstype, SdsStreamView, SdsResolvedStream, Asset, AssetType and AssetRule

## 0.10.1_preview / 2023-10-10

- Add parquet support

## 0.10.0_preview / 2023-09-20

- Add preview Event Store and Graph QL support

## 0.9.13_preview / 2023-04-17

- Improved SdsError class

## 0.9.12_preview / 2023-03-24

- Added new enumeration in FieldSource for DataViews

## 0.9.11_preview / 2023-03-16

- Fixed pipeline misconfiguration
- Bump version of requests library

## 0.9.10_preview / 2022-09-30

- Resolve bug in Stream.getOrCreateStream

## 0.9.9_preview / 2022-09-27

- Resolve bug in content resolver logic

## 0.9.8_preview / 2022-09-12

- Add stream parameter to Assets data calls

## 0.9.7_preview / 2022-08-17

- Automate dependabot approval and automerge

## 0.9.6_preview / 2022-08-10

- Add dependabot.yml to automate dependency checks

## 0.9.5_preview / 2022-08-09

- Address content resolving bug in SharedStreams

## 0.9.4_preview / 2022-07-30

- Add testing for Streams and BaseClient
- Refactoring

## 0.9.3_preview / 2022-07-18

- Add cache feature to DataViews client class

## 0.9.2_preview / 2022-07-11

- Remove reference to msilib

## 0.9.1_preview / 2022-07-06

- Resolved Stream improvements and bug fixes
- Added skip parameter to getCommunityStreams, which may be a breaking change for some

## 0.9.0_preview / 2022-07-07

- Added logging capabilities to the BaseClient's request and response functions

## 0.8.3_preview / 2022-06-29

- Bump version for re-release

## 0.7.6_preview / 2022-06-20

- Add support for getting Resolved Stream

## 0.7.5_preview / 2022-06-17

- Updated dependencies

## 0.7.4_preview / 2022-05-24

- Fix typo in communities route

## 0.7.3_preview / 2022-05-24

- Update communities queries to be compliant with changes made to the API

## 0.7.2_preview / 2022-04-27

- Fix bug in Users client

## 0.7.1_preview / 2022-03-25

- Initial version of the AVEVA Data Hub preview python sample library. This library replaces https://pypi.org/project/ocs-sample-library-preview/.
