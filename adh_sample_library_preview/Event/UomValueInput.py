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
        
        case_fold_content = {}
        for k, v in content.items():
            case_fold_content.update({k.casefold(): v})

        if 'value' in case_fold_content:
            result.Value = case_fold_content['value']

        if 'uom' in case_fold_content:
            result.Uom = SdsUom.fromJson(case_fold_content['uom'])

        return result
