import pytest

from ark.client import ArkClient
from ark.connection import Connection


def test_client_creation_calls_import_api(mocker):
    import_mock = mocker.patch.object(ArkClient, '_import_api')

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')

    assert client.api_version == 'v2'
    assert isinstance(client.connection, Connection)
    assert import_mock.call_count == 1


def test_client_creation_raises_with_wrong_api_version():
    with pytest.raises(Exception) as error:
        ArkClient('http://127.0.0.1:4002', api_version='foo')
    assert 'Only versions "v1" and "v2" are supported' in str(error.value)
