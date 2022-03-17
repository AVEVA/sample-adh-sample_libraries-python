from __future__ import annotations
import json

from .BaseClient import BaseClient
from .Asset.AssetRule import AssetRule
from .Securable import Securable


class AssetRules(Securable, object):
    """
    Client for interacting with ADH Asset Rules
    This class does not represent the full functionality of the Asset Rules route and is included to allow management of security on the route
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Asset Rules client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='AssetRules', api_suffix='-preview')

        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getAssetRuleById(self, namespace_id: str, asset_rule_id: str) -> AssetRule:
        """
        Returns the specified asset rule
        :param namespace_id: The namespace identifier
        :param asset_rule_id: The asset rule identifier
        """
        if namespace_id is None:
            raise TypeError
        if asset_rule_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__asset_rule_path.format(
            namespace_id=namespace_id, asset_rule_id=self.__base_client.encode(asset_rule_id)))
        self.__base_client.checkResponse(
            response, f'Failed to get asset rule, {asset_rule_id}.')

        result = AssetRule.fromJson(response.json())
        return result

    def getAssetRules(self, namespace_id: str, query: str = '', skip: int = 0, count: int = 100,
                  ) -> list[AssetRule]:
        """
        Returns a list of asset rules
        :param namespace_id: The namespace identifier
        :param query: An optional query string to search for matching asset rules.
        :param skip: An optional parameter representing the zero-based offset of the first asset rule to
        retrieve. If not specified, a default value of 0 is used.
        :param count: An optional parameter, between 1 and 1000 (inclusive), that represents the
        maximum number of retrieved asset rules. If not specified, the default is 100.
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__asset_rules_path.format(
            namespace_id=namespace_id), params={'skip': skip, 'count': count, 'query': query})
        self.__base_client.checkResponse(response, f'Failed to get asset rules.')

        results = []
        for i in response.json():
            results.append(AssetRule.fromJson(i))
        return results

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path = self.__base_client.uri_API + '-preview/Tenants/' + \
            self.__base_client.tenant + '/Namespaces/{namespace_id}'
        self.__asset_rules_path = self.__base_path + '/AssetRules'
        self.__asset_rule_path = self.__asset_rules_path + '/{asset_rule_id}'
