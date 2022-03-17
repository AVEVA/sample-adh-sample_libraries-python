from __future__ import annotations
import json

from ..Security.AccessControlList import AccessControlList
from ..Security.Trustee import Trustee
from .NamespaceProvisioningState import NamespaceProvisioningState


class Namespace(object):
    """ADH namespace definition"""

    def __init__(self, id: str = None, region: str = None, namespace_self: str = None, description: str = None, state: NamespaceProvisioningState = None,
                 owner: Trustee = None, access_control: AccessControlList = None, region_id: str = None, instance_id: str = None):
        self.Id = id
        self.Region = region
        self.Self = namespace_self
        self.Description = description
        self.State = state
        self.Owner = owner
        self.AccessControl = access_control
        self.RegionId = region_id
        self.InstanceId = instance_id

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Region(self) -> str:
        return self.__region

    @Region.setter
    def Region(self, value: str):
        self.__region = value

    @property
    def Self(self) -> str:
        return self.__self

    @Self.setter
    def Self(self, value: str):
        self.__self = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def State(self) -> NamespaceProvisioningState:
        return self.__state

    @State.setter
    def State(self, value: NamespaceProvisioningState):
        self.__state = value

    @property
    def Owner(self) -> Trustee:
        return self.__owner

    @Owner.setter
    def Owner(self, value: Trustee):
        self.__owner = value

    @property
    def AccessControl(self) -> AccessControlList:
        return self.__access_control

    @AccessControl.setter
    def AccessControl(self, value: AccessControlList):
        self.__access_control = value

    @property
    def RegionId(self) -> str:
        return self.__region_id

    @RegionId.setter
    def RegionId(self, value: str):
        self.__region_id = value

    @property
    def InstanceId(self) -> str:
        return self.__instance_id

    @InstanceId.setter
    def InstanceId(self, value: str):
        self.__instance_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Id': self.Id}

        if self.Region is not None:
            result['Region'] = self.Region

        if self.Self is not None:
            result['Self'] = self.Self

        if self.Description is not None:
            result['Description'] = self.Description

        if self.State is not None:
            result['State'] = self.State.value

        if self.Owner is not None:
            result['Owner'] = self.Owner.toDictionary()

        if self.AccessControl is not None:
            result['AccessControl'] = self.AccessControl.toDictionary()

        if self.RegionId is not None:
            result['RegionId'] = self.RegionId

        if self.InstanceId is not None:
            result['InstanceId'] = self.InstanceId

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Namespace()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Region' in content:
            result.Region = content['Region']

        if 'Self' in content:
            result.Self = content['Self']

        if 'Description' in content:
            result.Description = content['Description']

        if 'State' in content:
            result.State = content['State']

        if 'Owner' in content:
            result.Owner = content['Owner']

        if 'AccessControl' in content:
            result.AccessControl = content['AccessControl']

        if 'RegionId' in content:
            result.RegionId = content['RegionId']

        if 'InstanceId' in content:
            result.InstanceId = content['InstanceId']

        return result
