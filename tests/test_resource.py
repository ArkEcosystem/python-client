from ark.connection import Connection
from ark.resource import Resource


def test_request_get_calls_connection_get_with_correct_params(mocker):
    get_mock = mocker.patch.object(Connection, 'get')
    connection = Connection('http://127.0.0.1:4003', '2')

    resource = Resource(connection)
    resource.request_get('spongebob', params={'foo': 'bar'})

    get_mock.assert_called_once_with('spongebob', params={'foo': 'bar'})


def test_request_post_calls_connection_post_with_correct_params(mocker):
    post_mock = mocker.patch.object(Connection, 'post')
    connection = Connection('http://127.0.0.1:4003', '2')

    resource = Resource(connection)
    resource.request_post('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

    post_mock.assert_called_once_with('spongebob', data={'one': 'two'}, params={'foo': 'bar'})


def test_request_put_calls_connection_put_with_correct_params(mocker):
    put_mock = mocker.patch.object(Connection, 'put')
    connection = Connection('http://127.0.0.1:4003', '2')

    resource = Resource(connection)
    resource.request_put('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

    put_mock.assert_called_once_with('spongebob', data={'one': 'two'}, params={'foo': 'bar'})


def test_request_patch_calls_connection_patch_with_correct_params(mocker):
    patch_mock = mocker.patch.object(Connection, 'patch')
    connection = Connection('http://127.0.0.1:4003', '2')

    resource = Resource(connection)
    resource.request_patch('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

    patch_mock.assert_called_once_with('spongebob', data={'one': 'two'}, params={'foo': 'bar'})


def test_request_delete_calls_connection_delete_with_correct_params(mocker):
    delete_mock = mocker.patch.object(Connection, 'delete')
    connection = Connection('http://127.0.0.1:4003', '2')

    resource = Resource(connection)
    resource.request_delete('spongebob', params={'foo': 'bar'})

    delete_mock.assert_called_once_with('spongebob', params={'foo': 'bar'})
