from ark.client import ArkClient
from ark.connection import Connection


def test_client_creation_with_nethash_and_version_does_not_call_autocofigure(mocker):
    autoconfigure_mock = mocker.patch.object(Connection, 'autoconfigure')

    client = ArkClient('192.168.5.5', 4002, nethash='hash12345', version='2.0.0', api_version='v2')

    assert client.api_version == 'v2'
    assert isinstance(client.connection, Connection)
    assert autoconfigure_mock.call_count == 0


def test_client_creation_without_nethash_and_version_call_autocofigure(mocker):
    autoconfigure_mock = mocker.patch.object(Connection, 'autoconfigure')

    client = ArkClient('192.168.5.5', 4002, nethash=None, version=None, api_version='v2')

    assert client.api_version == 'v2'
    assert isinstance(client.connection, Connection)
    assert autoconfigure_mock.call_count == 1
