from __future__ import annotations
import json
from typing import Any, Type, TypeVar, Generic

from .Operation import Operation

T = TypeVar("T")


class Update(Generic[T]):
    """
    Represents an update
    """

    def __init__(self, resource_id: str = None, operation: Operation = None, events: list[T] = None):
        """
        :param str resource_id: Resource Identifier
        :param str operation: Operation
        :param Any events: Events
        """
        self.__resource_id = resource_id
        self.__operation = operation
        self.__events = events

    @property
    def ResourceId(self) -> str:
        return self.__resource_id

    @ResourceId.setter
    def ResourceId(self, value: str):
        self.__resource_id = value

    @property
    def Operation(self) -> Operation:
        return self.__operation

    @Operation.setter
    def Operation(self, value: Operation):
        self.__operation = value

    @property
    def Events(self) -> list[T]:
        return self.__events

    @Events.setter
    def Events(self, value: list[T]):
        self.__events = value

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.ResourceId is not None:
            result['ResourceId'] = self.ResourceId

        if self.Operation is not None:
            result['Operation'] = self.Operation.name

        if self.Events is not None:
            for event in self.Events:
                result['Events'].append(event)

        return result

    @staticmethod
    def fromJson(content: dict[str, Any], input_type: Type[T]) -> Update[T]:
        result = Update[T]()

        if not content:
            return result

        if 'resourceId' in content:
            result.ResourceId = content['resourceId']

        if 'operation' in content:
            result.Operation = Operation(content['operation'])

        if 'events' in content:
            events = content['events']
            if events is not None and len(events) > 0:
                result.Events = []
                if input_type is None:
                    for event in events:
                        result.Events.append(event)
                else:
                    for event in events:
                        result.Events.append(input_type.fromJson(event))

        return result