from __future__ import annotations
from dataclasses import dataclass
import json
from typing import Any, TypeVar, Generic

from ..Units import SdsUom

T = TypeVar('T')


@dataclass
class UomValueInput(Generic[T]):
    Value: T = None
    Uom: SdsUom = None

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.Value is not None:
            result['Value'] = self.Value

        if self.Uom is not None:
            result['Uom'] = self.Uom.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> UomValueInput:
        result = UomValueInput()

        if not content:
            return result

        if 'Value' in content:
            result.Value = content['Value']

        if 'Uom' in content:
            result.Uom = SdsUom.fromJson(content['Uom'])

        return result
