from dataclasses import asdict, dataclass
import json
@dataclass
class Transfer:
	"""PI to Data Hub Transfer object.

    Represents a Transfer object used in a PI to Data Hub connection.

    Args:
        Name (str): Name of the Transfer. (Requried)
        Description (str): Description of the Transfer. (Requried)
        HistoricalDataStartTime (str): HistoricalDataStartTime of the Transfer. (Requried)
        PIPointIds (str): List of PIPointIds in the Transfer. (Requried)
        MetadataPrivacy (str): MetadataPrivacy of the Transfer. (Requried)
        AutoDeleteCloudObjects (str): Set whether AutoDeleteCloudObjects should be enabled. (Requried)
    """

	Name: str
	Description: str
	HistoricalDataStartTime: str
	PIPointIds: list[int]
	MetadataPrivacy: str
	TotalPointsInTransfer: str
	AutoDeleteCloudObjects: str

	Id: str = ""
	Status: str = ""
	PreviousHistoricChunkStart: str = ""
	CurrentHistoricChunkStart: str = ""
	LatestStreamingRead: str = ""
	HistoricalDataEndTime: str = ""
	TransferredElementsCount: str = ""
	AssetsCreatedCount: str = ""
	AssetsUpdatedCount: str = ""
	AssetsFailedCount: str = ""
	OnPremTransferStatus: str = ""
	DesiredStatus: str = ""
	AFElementIds: list[int]= ""
	PIPointsReferencedByAF: str = ""
	PIPointsWithHealthEvents: str = ""
	AFElementsWithHealthEvents: str = ""
	TransferRevisionNumber: str = ""
	LastEditDate: str = ""
	LastEditBy: str = ""
	PointEdits: str = ""
	StreamErrors: list[str]= ""
	AssetErrors: list[str]= ""
	HistTransferProgress: str = ""
	
	def toJson(self):
		return json.dumps(self.toDictionary())

	def toDictionary(self):
		return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v != ('',) and v != ''})

	@staticmethod
	def fromJson(content):
		if type(content) == list:
			return Transfer(**content[0])
		else:
			return Transfer(**content)
