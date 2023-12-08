from __future__ import annotations

from .BaseClient import BaseClient
from .Unit import SdsUom


class Units(object):
    def __init__(self, client: BaseClient):
        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getUnitOfMeasureById(self, namespace_id: str, uom_id: str) -> SdsUom:
        """
        Returns the unit of measure corresponding to the specified uomId within a given namespace.
        :param namespace_id: The namespace identifier
        :param uom_id: The uom identifier
        """
        if namespace_id is None:
            raise TypeError
        if uom_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__unit_path.format(
                namespace_id=namespace_id, uom_id=self.__base_client.encode(uom_id)
            ),
        )
        self.__base_client.checkResponse(response, f'Failed to get uom, {uom_id}.')

        result = SdsUom.fromJson(response.json())
        return result

    def getUnitsofMeasure(
        self,
        namespace_id: str,
        filter: str = '',
        skip: int = 0,
        count: int = 100,
        order_by: str = '',
    ) -> list[SdsUom]:
        """
        Returns a list of all available units of measure in the system.Returns a list of assets
        :param namespace_id: The namespace identifier
        :param filter: Filter expression.
        :param skip: Parameter representing the zero-based offset of the first SdsUomQuantity to retrieve. If not specified, a default value of 0 is used.
        :param count: Parameter representing the maximum number of SdsUomQuantity to retrieve. If not specified, a default value of 100 is used.
        :param order_by: Parameter representing sorted order of returned objects. A field name is required. The sorting is based on the stored values for the given field.
        For example, orderby=name would sort the returned results by the name values (ascending by default).
        Additionally, a value can be provided along with the field name to identify whether to sort ascending or descending,
        by using values asc or desc, respectively.
        For example, orderby=name desc would sort the returned results by the name values, descending.
        If no value is specified, there is no sorting of results.
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__units_path.format(namespace_id=namespace_id),
            params={'filter': filter, 'skip': skip, 'count': count, order_by: order_by},
        )
        self.__base_client.checkResponse(response, f'Failed to get uoms.')

        results = []
        for i in response.json():
            results.append(SdsUom.fromJson(i))
        return results

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path_preview = (
            self.__uri_api
            + '/Tenants/'
            + self.__base_client.tenant
            + '/Namespaces/{namespace_id}'
        )

        self.__units_path = self.__base_path_preview + '/Units'
        self.__unit_path = self.__units_path + '/{uom_id}'
