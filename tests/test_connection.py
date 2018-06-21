import pytest

import requests

import responses

from ark.connection import Connection
from ark.exceptions import ArkHTTPException


def test_connection_creation_sets_default_session_headers_and_variables():
    connection = Connection('http://127.0.0.1:4003', '2')
    assert connection.hostname == 'http://127.0.0.1:4003'
    assert isinstance(connection.session, requests.Session)
    assert connection.session.headers['port'] == '1'
    assert connection.session.headers['API-Version'] == '2'


@pytest.mark.parametrize('version_number', [
    'foo',
    123
])
def test_connection_creation_raises_with_wrong_api_version_number(version_number):
    with pytest.raises(Exception) as error:
        Connection('http://127.0.0.1:4003', version_number)
    assert 'Only versions "1" and "2" are supported' in str(error.value)


def test_build_url_correctly_builds_url():
    connection = Connection('http://127.0.0.1:4003', '2')
    url = connection._build_url('spongebob')
    assert url == 'http://127.0.0.1:4003/spongebob'


def test_handle_response_raises_for_no_content_in_response():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        status=404
    )

    connection = Connection('http://127.0.0.1:4003', '2')
    response = requests.get('http://127.0.0.1:4003/spongebob')
    with pytest.raises(ArkHTTPException) as exception:
        connection._handle_response(response)

    assert str(exception.value) == 'No content in response'
    assert exception.value.response == response


def test_handle_response_raises_for_success_false_in_response():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        json={'success': False, 'error': 'Best error ever'},
        status=404
    )

    connection = Connection('http://127.0.0.1:4003', '2')
    response = requests.get('http://127.0.0.1:4003/spongebob')
    with pytest.raises(ArkHTTPException) as exception:
        connection._handle_response(response)

    assert str(exception.value) == 'GET 404 http://127.0.0.1:4003/spongebob - Best error ever'
    assert exception.value.response == response


def test_handle_response_retuns_body_from_request():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        json={'success': True},
        status=200
    )

    connection = Connection('http://127.0.0.1:4003', '2')
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

    connection = Connection('http://127.0.0.1:4003', '2')
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

    connection = Connection('http://127.0.0.1:4003', '2')
    data = getattr(connection, func_name)('spongebob', params={'foo': 'bar'})
    assert data == {'success': True}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4003/spongebob?foo=bar'
