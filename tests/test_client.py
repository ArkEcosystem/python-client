import pytest

from client.client import ArkClient
from client.connection import Connection


def test_client_creation_calls_import_api(mocker):
    import_mock = mocker.patch.object(ArkClient, '_import_api')

    client = ArkClient('http://127.0.0.1:4002')

    assert isinstance(client.connection, Connection)
    assert import_mock.call_count == 1
