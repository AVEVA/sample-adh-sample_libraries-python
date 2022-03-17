from __future__ import annotations
import json

from ..SDS.SdsTypeCode import SdsTypeCode
from .DataViewShape import DataViewShape
from .Field import Field
from .FieldSet import FieldSet
from .Query import Query


class DataView(object):
    """ADH Data View definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 queries: list[Query] = None, index_field: Field = None,
                 data_field_sets: list[FieldSet] = None, grouping_fields: list[Field] = None,
                 index_type_code: SdsTypeCode = None, default_start_index: str = None,
                 default_end_index: str = None, default_interval: str = None,
                 shape: DataViewShape = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param queries: not required
        :param index_field: not required
        :param data_field_sets: not required
        :param grouping_fields: not required
        :param index_type_code: not required
        :param default_start_index: not required
        :param default_end_index: not required
        :param default_interval: not required
        :param shape: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.Queries = queries
        self.IndexField = index_field
        self.DataFieldSets = data_field_sets
        self.GroupingFields = grouping_fields
        self.IndexTypeCode = index_type_code
        self.DefaultStartIndex = default_start_index
        self.DefaultEndIndex = default_end_index
        self.DefaultInterval = default_interval
        self.Shape = shape

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__id = value

    @property
    def Name(self) -> str:
        """
        not required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__name = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self.__description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__description = value

    @property
    def IndexField(self) -> Field:
        """
        not required
        :return:
        """
        return self.__index_field

    @IndexField.setter
    def IndexField(self, value: Field):
        """
        not required
        :param value:
        :return:
        """
        self.__index_field = value

    @property
    def Queries(self) -> list[Query]:
        """
        not required
        :return:
        """
        return self.__queries

    @Queries.setter
    def Queries(self, value: list[Query]):
        """
        not required
        :param value:
        :return:
        """
        self.__queries = value

    @property
    def DataFieldSets(self) -> list[FieldSet]:
        """
        not required
        :return:
        """
        return self.__data_field_sets

    @DataFieldSets.setter
    def DataFieldSets(self, value: list[FieldSet]):
        """
        not required
        :param value:
        :return:
        """
        self.__data_field_sets = value

    @property
    def GroupingFields(self) -> list[Field]:
        """
        not required
        :return:
        """
        return self.__grouping_fields

    @GroupingFields.setter
    def GroupingFields(self, value: list[Field]):
        """
        not required
        :param value:
        :return:
        """
        self.__grouping_fields = value

    @property
    def DefaultStartIndex(self) -> str:
        """
        not required
        :return:
        """
        return self.__default_start_index

    @DefaultStartIndex.setter
    def DefaultStartIndex(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__default_start_index = value

    @property
    def DefaultEndIndex(self) -> str:
        """
        not required
        :return:
        """
        return self.__default_end_index

    @DefaultEndIndex.setter
    def DefaultEndIndex(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__default_end_index = value

    @property
    def DefaultInterval(self) -> str:
        """
        not required
        :return:
        """
        return self.__default_interval

    @DefaultInterval.setter
    def DefaultInterval(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__default_interval = value

    @property
    def IndexTypeCode(self) -> SdsTypeCode:
        """
        not required
        :return:
        """
        return self.__index_type_code

    @IndexTypeCode.setter
    def IndexTypeCode(self, value: SdsTypeCode):
        """
        not required
        :param value:
        :return:
        """
        self.__index_type_code = value

    @property
    def Shape(self) -> DataViewShape:
        """
        not required
        :return:
        """
        return self.__shape

    @Shape.setter
    def Shape(self, value: DataViewShape):
        """
        not required
        :param value:
        :return:
        """
        self.__shape = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.IndexField is not None:
            result['IndexField'] = self.IndexField.toDictionary()

        if self.Queries is not None:
            result['Queries'] = []
            for value in self.Queries:
                result['Queries'].append(value.toDictionary())

        if self.DataFieldSets is not None:
            result['DataFieldSets'] = []
            for value in self.DataFieldSets:
                result['DataFieldSets'].append(value.toDictionary())

        if self.GroupingFields is not None:
            result['GroupingFields'] = []
            for value in self.GroupingFields:
                result['GroupingFields'].append(value.toDictionary())

        if self.DefaultStartIndex is not None:
            result['DefaultStartIndex'] = self.DefaultStartIndex

        if self.DefaultEndIndex is not None:
            result['DefaultEndIndex'] = self.DefaultEndIndex

        if self.DefaultInterval is not None:
            result['DefaultInterval'] = self.DefaultInterval

        if self.IndexTypeCode is not None:
            result['IndexTypeCode'] = self.IndexTypeCode.name

        if self.Shape is not None:
            result['Shape'] = self.Shape.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataView()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'IndexField' in content:
            result.IndexField = Field.fromJson(content['IndexField'])

        if 'Queries' in content:
            queries = content['Queries']
            if queries is not None and len(queries) > 0:
                result.Queries = []
                for value in queries:
                    result.Queries.append(Query.fromJson(value))

        if 'DataFieldSets' in content:
            data_field_sets = content['DataFieldSets']
            if data_field_sets is not None and len(data_field_sets) > 0:
                result.DataFieldSets = []
                for value in data_field_sets:
                    result.DataFieldSets.append(FieldSet.fromJson(value))

        if 'GroupingFields' in content:
            grouping_fields = content['GroupingFields']
            if grouping_fields is not None and len(grouping_fields) > 0:
                result.GroupingFields = []
                for value in grouping_fields:
                    result.GroupingFields.append(Field.fromJson(value))

        if 'DefaultStartIndex' in content:
            result.DefaultStartIndex = content['DefaultStartIndex']

        if 'DefaultEndIndex' in content:
            result.DefaultEndIndex = content['DefaultEndIndex']

        if 'DefaultInterval' in content:
            result.DefaultInterval = content['DefaultInterval']

        if 'IndexTypeCode' in content:
            index_type_code = content['IndexTypeCode']
            if index_type_code is not None:
                result.IndexTypeCode = SdsTypeCode[index_type_code]

        if 'Shape' in content:
            shape = content['Shape']
            if shape is not None:
                result.Shape = DataViewShape[shape]

        return result
