from ark.api.resource import Resource
from ark.client import ArkClient
from ark.connection import Connection


def test_request_get_calls_connection_get_with_correct_params(mocker):
    get_mock = mocker.patch.object(Connection, 'get')
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    resource = Resource(connection)
    resource.request_get('spongebob', params={'foo': 'bar'})

    get_mock.assert_called_once_with('spongebob', params={'foo': 'bar'})


def test_request_post_calls_connection_get_with_correct_params(mocker):
    get_mock = mocker.patch.object(Connection, 'post')
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    resource = Resource(connection)
    resource.request_post('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

    get_mock.assert_called_once_with('spongebob', data={'one': 'two'}, params={'foo': 'bar'})


def test_request_put_calls_connection_get_with_correct_params(mocker):
    get_mock = mocker.patch.object(Connection, 'put')
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    resource = Resource(connection)
    resource.request_put('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

    get_mock.assert_called_once_with('spongebob', data={'one': 'two'}, params={'foo': 'bar'})


def test_request_patch_calls_connection_get_with_correct_params(mocker):
    get_mock = mocker.patch.object(Connection, 'patch')
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    resource = Resource(connection)
    resource.request_patch('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

    get_mock.assert_called_once_with('spongebob', data={'one': 'two'}, params={'foo': 'bar'})


def test_request_delete_calls_connection_get_with_correct_params(mocker):
    get_mock = mocker.patch.object(Connection, 'delete')
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    resource = Resource(connection)
    resource.request_delete('spongebob', params={'foo': 'bar'})

    get_mock.assert_called_once_with('spongebob', params={'foo': 'bar'})
