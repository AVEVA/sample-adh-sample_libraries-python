from __future__ import annotations

from .BaseClient import BaseClient
from .ContentResolvers import DataContent, ValueContent
from .PItoDataHub import DataSourceAgent, Transfer, DataSource, Query, QueryResult
from .PatchableSecurable import PatchableSecurable

class PItoDataHubConnections(PatchableSecurable, object):
    """
    Client for interacting with PI to Data Hub Data Sources, and their Agents and Transfers  
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the PItoDataHubConnections client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='PItoDataHubConnections')

        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()


    def getDataSources(self, namespaceId: str) -> list[DataSource]:
        """
        Returns all data sources for the namespace.
        :param namespaceId: The namespace to work against
        """
        self.__base_client.validateParameters(namespaceId)

        response = self.__base_client.request(
            'GET', self.__datasources_path.format(tenant_id=self.__tenant, namespaceId=namespaceId))
        
        self.__base_client.checkResponse(
            response, f'Failed to get data sources.')

        return DataContent(response, value_class=DataSource).resolve()


    def getDataSource(self, namespaceId: str, dataSourceId: str) -> DataSource:
        """
        Returns the specified data source.
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source identifier
        """
        self.__base_client.validateParameters(namespaceId, dataSourceId)

        response = self.__base_client.request(
            'GET', 
            self.__datasource_path.format(
                tenant_id=self.__tenant,
                namespaceId=namespaceId, 
                dataSourceId=self.__base_client.encode(dataSourceId)))
        
        self.__base_client.checkResponse(
            response, f'Failed to get data source, {dataSourceId}.')

        return ValueContent(response, DataSource).resolve()


    def getAgents(self, namespaceId: str, dataSourceId: str):
        """
        Returns all agents for the namespace.
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        """
        self.__base_client.validateParameters(namespaceId, dataSourceId)

        response = self.__base_client.request(
            'GET', self.__agents_path.format(
                tenant_id=self.__tenant,
                namespaceId=namespaceId,
                dataSourceId=self.__base_client.encode(dataSourceId)))
        
        self.__base_client.checkResponse(
            response, f'Failed to get agents.')

        return DataContent(response, value_class=DataSourceAgent).resolve()

    def getAgent(self, namespaceId: str, dataSourceId: str, agentId: str):
        """
        Returns all agents for the namespace.
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        """
        self.__base_client.validateParameters(namespaceId, dataSourceId, agentId)

        response = self.__base_client.request(
            'GET', self.__agent_path.format(
                tenant_id=self.__tenant,
                namespaceId=namespaceId,
                dataSourceId=self.__base_client.encode(dataSourceId),
                agentId=self.__base_client.encode(agentId),))
        
        self.__base_client.checkResponse(
            response, f'Failed to get agent with Id {agentId}.')

        return ValueContent(response, value_class=DataSourceAgent).resolve()


    def getTransfers(self, namespaceId: str, dataSourceId: str, agentId: str) -> list[Transfer]:
        """
        Returns the transfers of the namespace
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        :param agentId: The agent of the transfer
        """
        self.__base_client.validateParameters(namespaceId, dataSourceId, agentId)

        response = self.__base_client.request(
            'GET', self.__transfers_path.format(
                tenant_id=self.__tenant,
                namespaceId=namespaceId, 
                dataSourceId=self.__base_client.encode(dataSourceId),
                agentId=self.__base_client.encode(agentId)))
        
        self.__base_client.checkResponse(
            response, f'Failed to get transfers for agent, {agentId}.')

        return DataContent(response, value_class=Transfer).resolve()

    def createTransfer(self, namespaceId: str, dataSourceId: str, agentId: str, transfer: Transfer):
        """
        Create a Transfer using the provided transfer data object
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        :param agentId: The agent of the transfer
        """
        response = self.__base_client.request(
            'POST', self.__transfers_path.format(
                tenant_id=self.__tenant, 
                namespaceId=namespaceId, 
                dataSourceId=self.__base_client.encode(dataSourceId),
                agentId=self.__base_client.encode(agentId)),
                data=transfer.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to get transfers for agent, {agentId}.')

        return ValueContent(response, value_class=Transfer).resolve()

    def deleteTransfer(self, namespaceId: str, dataSourceId: str, agentId: str, transferId: str):
        """
        Create a Transfer using the provided transfer data object
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        :param agentId: The agent of the transfer
        """
        response = self.__base_client.request(
            'DELETE', self.__transfers_path.format(
                tenant_id=self.__tenant,
                namespaceId=namespaceId,
                dataSourceId=self.__base_client.encode(dataSourceId),
                agentId=self.__base_client.encode(agentId),
                transferId=self.__base_client.encode(transferId)))

        self.__base_client.checkResponse(
            response, f'Failed to get transfers for agent, {agentId}.')

    
    def createQuery(self, namespaceId: str, dataSourceId: str, agentId: str, query: Query) -> Query:
        """
        Create a Query using the provided query data object
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        :param agentId: The agent of the transfer
        """
        response = self.__base_client.request(
            'POST', self.__queries_path.format(
                tenant_id=self.__tenant, 
                namespaceId=namespaceId, 
                dataSourceId=self.__base_client.encode(dataSourceId),
                agentId=self.__base_client.encode(agentId)),
                data=query.toJson())

        self.__base_client.checkResponse(
            response, f'Failed to get transfers for agent, {agentId}.')

        return ValueContent(response, value_class=Query).resolve()

    def getQuery(self, namespaceId: str, dataSourceId: str, agentId: str, queryId: str) -> Query:
        """
        Create a Query using the provided query data object
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        :param agentId: The agent of the transfer
        """
        response = self.__base_client.request(
            'GET', self.__query_path.format(
                tenant_id=self.__tenant, 
                namespaceId=namespaceId, 
                dataSourceId=self.__base_client.encode(dataSourceId),
                agentId=self.__base_client.encode(agentId),
                queryId=self.__base_client.encode(queryId)))

        self.__base_client.checkResponse(
            response, f'Failed to get transfers for agent, {agentId}.')

        return ValueContent(response, value_class=Query).resolve()

    def getQueryResult(self, namespaceId: str, dataSourceId: str, agentId: str, queryId: str) -> QueryResult:
        """
        Create a Query using the provided query data object
        :param namespaceId: The namespace to work against
        :param dataSourceId: The data source of the transfer
        :param agentId: The agent of the transfer
        """
        response = self.__base_client.request(
            'GET', self.__query_result_path.format(
                tenant_id=self.__tenant, 
                namespaceId=namespaceId, 
                dataSourceId=self.__base_client.encode(dataSourceId),
                agentId=self.__base_client.encode(agentId),
                queryId=self.__base_client.encode(queryId)))

        self.__base_client.checkResponse(
            response, f'Failed to get transfers for agent, {agentId}.')

        return ValueContent(response, value_class=QueryResult).resolve()


    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        : return:
        """
        self.__basePath = self.__uri_api + \
            '/Tenants/{tenant_id}/Namespaces/{namespaceId}/Pi'
        self.__datasources_path = self.__basePath + '/DataSources'
        self.__datasource_path = self.__datasources_path + '/{dataSourceId}'
        self.__agents_path = self.__datasource_path + '/Agents'
        self.__agent_path = self.__agents_path + '/{agentId}'
        self.__transfers_path = self.__agent_path + '/Transfers'
        self.__queries_path = self.__agent_path + '/Queries'
        self.__query_path = self.__queries_path + '/{queryId}'
        self.__query_result_path = self.__query_path + '/Result'
