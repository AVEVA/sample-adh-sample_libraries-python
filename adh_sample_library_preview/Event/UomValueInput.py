from __future__ import annotations
from dataclasses import dataclass
import json
from typing import Any, TypeVar, Generic

from ..Units import SdsUom

T = TypeVar('T')


def _pascalToCamelCase(dictionary: dict[str, Any]):
    camel_case_dictionary = {}
    for k, v in dictionary.items():
        if isinstance(v, list):
            l = []
            for i in v:
                l.append(_pascalToCamelCase(i))
            camel_case_dictionary.update({k[:1].lower() + k[1:]: l})
        elif isinstance(v, dict):
            camel_case_dictionary.update({k[:1].lower() + k[1:]: _pascalToCamelCase(v)})
        else:
            camel_case_dictionary.update({k[:1].lower() + k[1:]: v})
    return camel_case_dictionary


def _camelToPascalCase(dictionary: dict[str, Any]):
    pascal_case_dictionary = {}
    for k, v in dictionary.items():
        if isinstance(v, list):
            l = []
            for i in v:
                l.append(_camelToPascalCase(i))
            pascal_case_dictionary.update({k[:1].upper() + k[1:]: l})
        elif isinstance(v, dict):
            pascal_case_dictionary.update(
                {k[:1].upper() + k[1:]: _camelToPascalCase(v)}
            )
        else:
            pascal_case_dictionary.update({k[:1].upper() + k[1:]: v})
    return pascal_case_dictionary


@dataclass
class UomValueInput(Generic[T]):
    Value: T = None
    Uom: SdsUom = None

    def toJson(self) -> str:
        return json.dumps(self.toDictionary())

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.Value is not None:
            result['value'] = self.Value

        if self.Uom is not None:
            result['uom'] = _pascalToCamelCase(self.Uom.toDictionary())
        return result

    @staticmethod
    def fromJson(content: dict[str, Any]) -> UomValueInput:
        result = UomValueInput()

        if not content:
            return result

        if 'value' in content:
            result.Value = content['value']

        if 'uom' in content:
            result.Uom = SdsUom.fromJson(_camelToPascalCase(content['uom']))

        return result
