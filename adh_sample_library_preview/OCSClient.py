from .ADHClient import ADHClient

import warnings
warnings.filterwarnings("default", category=DeprecationWarning, module=__name__)

class OCSClient:
    """
    A client that handles communication with OCS. NOTE: OCSClient is deprecated as OSIsoft Cloud Services has now been migrated to AVEVA Data Hub, use ADHClient instead.
    """
    def __new__(cls, api_version: str, tenant: str, url: str, client_id: str,
                 client_secret: str = None, accept_verbosity: bool = False):
        """
        Use this to help in communinication with ADH
        :param api_version: Version of the api you are communicating with
        :param tenant: Your tenant ID
        :param url: The base URL for your ADH instance
        :param client_id: Your client ID
        :param client_secret: Your client Secret or Key
        :param accept_verbosity: Sets whether in value calls you get all values or just
            non-default values
        """
        return ADHClient(api_version, tenant, url, client_id,
                 client_secret, accept_verbosity)
