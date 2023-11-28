from __future__ import annotations

import json


class SdsUom(object):
    """Data Contract  represting a unit of measure"""

    def __init__(
        self,
        id: str = None,
        abbreviation: str = None,
        name: str = None,
        display_name: str = None,
        quantity_id: str = None,
        conversion_factor: float = None,
        conversion_offset: float = None,
        created_date: str = None,
        modified_date: str = None,
    ):
        """
        :param id: not required
        :param abbreviation: not required
        :param name: not required
        :param display_name: not required
        :param quantity_id: not required
        :param conversion_factor: not required
        :param conversion_offset: not required
        :param created_date: not required
        :param modified_date: not required
        """
        self.__id = id
        self.__abbreviation = abbreviation
        self.__name = name
        self.__display_name = display_name
        self.__quantity_id = quantity_id
        self.__conversion_factor = conversion_factor
        self.__conversion_offset = conversion_offset
        self.__created_date = created_date
        self.__modified_date = modified_date

    @property
    def Id(self) -> str:
        """
        not required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__id = value

    @property
    def Abbreviation(self) -> str:
        """
        not required
        :return:
        """
        return self.__abbreviation

    @Abbreviation.setter
    def Abbreviation(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__abbreviation = value

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
    def DisplayName(self) -> str:
        """
        not required
        :return:
        """
        return self.__display_name

    @DisplayName.setter
    def DisplayName(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__display_name = value

    @property
    def QuantityId(self) -> str:
        """
        not required
        :return:
        """
        return self.__quantity_id

    @QuantityId.setter
    def QuantityId(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__quantity_id = value

    @property
    def ConversionFactor(self) -> float:
        """
        not required
        :return:
        """
        return self.__conversion_factor

    @ConversionFactor.setter
    def ConversionFactor(self, value: float):
        """
        not required
        :param value:
        :return:
        """
        self.__conversion_factor = value

    @property
    def ConversionOffset(self) -> float:
        """
        not required
        :return:
        """
        return self.__conversion_offset

    @ConversionOffset.setter
    def ConversionOffset(self, value: float):
        """
        not required
        :param value:
        :return:
        """
        self.__conversion_offset = value

    @property
    def CreatedDate(self) -> str:
        """
        not required
        :return:
        """
        return self.__created_date

    @CreatedDate.setter
    def CreatedDate(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__created_date = value

    @property
    def ModifiedDate(self) -> str:
        """
        not required
        :return:
        """
        return self.__modified_date

    @ModifiedDate.setter
    def ModifiedDate(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__modified_date = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {}

        if self.Id is not None:
            result['Id'] = self.Id

        if self.Abbreviation is not None:
            result['Abbreviation'] = self.Abbreviation

        if self.Name is not None:
            result['Name'] = self.Name

        if self.DisplayName is not None:
            result['DisplayName'] = self.DisplayName

        if self.QuantityId is not None:
            result['QuantityId'] = self.QuantityId

        if self.ConversionFactor is not None:
            result['ConversionFactor'] = self.ConversionFactor

        if self.ConversionOffset is not None:
            result['ConversionOffset'] = self.ConversionOffset

        if self.CreatedDate is not None:
            result['CreatedDate'] = self.CreatedDate

        if self.ModifiedDate is not None:
            result['ModifiedDate'] = self.ModifiedDate

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsUom()

        if not content:
            return result

        case_fold_content = {}
        for k, v in content.items():
            case_fold_content.update({k.casefold(): v})

        if 'id' in case_fold_content:
            result.Id = case_fold_content['id']

        if 'abbreviation' in case_fold_content:
            result.Abbreviation = case_fold_content['abbreviation']

        if 'displayname' in case_fold_content:
            result.DisplayName = case_fold_content['displayname']

        if 'quantityid' in case_fold_content:
            result.QuantityId = case_fold_content['quantityid']

        if 'conversionfactor' in case_fold_content:
            result.ConversionFactor = case_fold_content['conversionfactor']

        if 'conversionooffset' in case_fold_content:
            result.ConversionOffset = case_fold_content['conversionoffset']

        if 'createddate' in case_fold_content:
            result.CreatedDate = case_fold_content['createddate']

        if 'modifieddate' in case_fold_content:
            result.ModifiedDate = case_fold_content['modifieddate']

        return result
