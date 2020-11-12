from client.connection import Connection
from client.resource import Resource


def test_request_get_calls_connection_get_with_correct_params(mocker):
    get_mock = mocker.patch.object(Connection, 'get')
    connection = Connection('http://127.0.0.1:4003')

    resource = Resource(connection)
    resource.request_get('spongebob', params={'foo': 'bar'})

    get_mock.assert_called_once_with('spongebob', params={'foo': 'bar'})


def test_request_post_calls_connection_post_with_correct_params(mocker):
    post_mock = mocker.patch.object(Connection, 'post')
    connection = Connection('http://127.0.0.1:4003')

    resource = Resource(connection)
    resource.request_post('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

    post_mock.assert_called_once_with('spongebob', data={'one': 'two'}, params={'foo': 'bar'})

