import pytest

from adh_sample_library_preview.ADHClient import ADHClient
from adh_sample_library_preview.BaseClientStub import BaseClientStub
from adh_sample_library_preview.Signups import CreateSignupInput
from adh_sample_library_preview.Signup import ResourceType

@pytest.fixture
def data():
    return {
        "NamespaceId": "testnamespace",
        "SignupName": "TestSignup",
        "StreamIds": ["stream1","stream2"],
        "CommunityId": "testcommunity",
    }
        

@pytest.fixture()
def client():
    """ setup any state specific to the execution of the given module."""
    base_client = BaseClientStub()
    adh_client = ADHClient(api_version=None, url=None, tenant=None, client_id=None, base_client=base_client)
    yield adh_client


def test_create_signup(client, data):
    createSignupInput = CreateSignupInput(None, ResourceType.STREAM, data.get("StreamIds"))
    client.Signups.createSignup(data.get("NamespaceId"), data.get("CommunityId"), createSignupInput)
