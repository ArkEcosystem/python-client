import pytest

import requests

import responses

from ark.client import ArkClient
from ark.connection import Connection


def test_connection_init_sets_default_session_headers_and_variables():
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(
        client=client,
        host='127.0.0.1',
        port=4003,
        nethash='12345',
        version='2.0.0'
    )

    assert connection.client == client
    assert connection.host == '127.0.0.1'
    assert connection.port == 4003
    assert connection.nethash == '12345'
    assert connection.version == '2.0.0'

    assert isinstance(connection.session, requests.Session)
    assert connection.session.headers['port'] == '1'
    assert connection.session.headers['API-Version'] == '2'


def test_setting_nethash_adds_it_to_session_headers():
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, None)
    connection.nethash = 'nethash12345'

    assert connection.session.headers['nethash'] == 'nethash12345'


def test_setting_nethash_to_none_removes_it_from_headers():
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, None, nethash='nethash12345')
    assert connection.session.headers['nethash'] == 'nethash12345'

    connection.nethash = None
    assert 'nethash' not in connection.session.headers


def test_setting_version_adds_it_to_session_headers():
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, None)
    connection.version = '2.0.0'

    assert connection.session.headers['version'] == '2.0.0'


def test_setting_version_to_none_removes_it_from_headers():
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, None, version='2.0.0')
    assert connection.session.headers['version'] == '2.0.0'

    connection.version = None
    assert 'version' not in connection.session.headers


def test_build_url_correctly_builds_url():
    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    url = connection._build_url('spongebob')

    assert url == 'http://127.0.0.1:4003/spongebob'


def test_handle_response_raises_for_invalid_response():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        status=404
    )

    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    response = requests.get('http://127.0.0.1:4003/spongebob')

    with pytest.raises(requests.exceptions.HTTPError):
        connection._handle_response(response)


def test_handle_response_retuns_body_from_request():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        json={'success': True},
        status=200
    )

    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    response = requests.get('http://127.0.0.1:4003/spongebob')
    body = connection._handle_response(response)
    assert body == {'success': True}


@pytest.mark.parametrize('method,func_name', [
    (responses.GET, 'get'),
    (responses.POST, 'post'),
    (responses.PUT, 'put'),
    (responses.PATCH, 'patch'),
    (responses.DELETE, 'delete'),
])
def test_http_methods_call_correct_url_and_return_correct_response(method, func_name):
    responses.add(
        method,
        'http://127.0.0.1:4003/spongebob',
        json={'success': True},
        status=200
    )

    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    data = getattr(connection, func_name)('spongebob')
    assert data == {'success': True}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4003/spongebob'


@pytest.mark.parametrize('method,func_name', [
    (responses.GET, 'get'),
    (responses.POST, 'post'),
    (responses.PUT, 'put'),
    (responses.PATCH, 'patch'),
    (responses.DELETE, 'delete'),
])
def test_http_methods_call_correct_url_with_params_and_return_correct_response(method, func_name):
    responses.add(
        method,
        'http://127.0.0.1:4003/spongebob',
        json={'success': True},
        status=200
    )

    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    data = getattr(connection, func_name)('spongebob', params={'foo': 'bar'})
    assert data == {'success': True}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4003/spongebob?foo=bar'


def test_autoconfigure_against_v1():
    responses.add(
        responses.GET,
        'http://192.168.5.5:4002/api/loader/autoconfigure',
        json={'success': True, 'network': {'nethash': 'hash12345'}},
        status=200
    )

    responses.add(
        responses.GET,
        'http://192.168.5.5:4002/api/peers/version',
        json={'success': True, 'version': '1.1.1'},
        status=200
    )

    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v1')
    connection = Connection(client, '127.0.0.1', 4003)

    connection.autoconfigure()
    assert connection.nethash == 'hash12345'
    assert connection.version == '1.1.1'


def test_autoconfigure_against_v2():
    responses.add(
        responses.GET,
        'http://192.168.5.5:4002/node/configuration',
        json={'success': True, 'data': {'nethash': 'hash12345', 'version': '2.2.2'}},
        status=200
    )

    client = ArkClient('192.168.5.5', 4002, nethash='12345', version='2.0.0', api_version='v2')
    connection = Connection(client, '127.0.0.1', 4003)

    connection.autoconfigure()
    assert connection.nethash == 'hash12345'
    assert connection.version == '2.2.2'
