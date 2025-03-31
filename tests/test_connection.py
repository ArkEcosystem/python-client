import pytest

import requests

import responses

from client.connection import Connection, Session
from client.exceptions import ArkHTTPException


def test_connection_creation_sets_default_session_headers_and_variables():
    connection = Connection('http://127.0.0.1:4003')
    assert connection.hosts == {
        'api': 'http://127.0.0.1:4003',
        'transactions': None,
        'evm': None,
    }
    assert isinstance(connection.session, requests.Session)
    assert connection.session.headers['Content-Type'] == 'application/json'


def test_connection_with_hosts_dict():
    connection = Connection({
        'api': 'http://127.0.0.1:4003/api',
        'transactions': 'http://127.0.0.1:4003/transactions',
        'evm': 'http://127.0.0.1:4003/evm',
    })

    assert connection.session.hostname == 'http://127.0.0.1:4003/api'

    connection.with_endpoint('transactions')

    assert connection.session.hostname == 'http://127.0.0.1:4003/transactions'

    connection.with_endpoint('evm')

    assert connection.session.hostname == 'http://127.0.0.1:4003/evm'

    connection.with_endpoint('api')

    assert connection.session.hostname == 'http://127.0.0.1:4003/api'


def test_connection_request_retry_successful():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        body=requests.exceptions.RequestException())
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        body=requests.exceptions.RequestException())
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        json={'success': True},
        status=200
    )

    connection = Connection('http://127.0.0.1:4003')

    data = connection.get('spongebob')
    assert data == {'success': True}
    assert len(responses.calls) == 3
    assert responses.calls[0].request.url == 'http://127.0.0.1:4003/spongebob'


def test_connection_raises_for_request_retry_failure():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        body=requests.exceptions.RequestException())

    connection = Connection('http://127.0.0.1:4003')

    with pytest.raises(ArkHTTPException):
        connection.get('spongebob')

    assert len(responses.calls) == 3


def test_handle_response_raises_for_no_content_in_response():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4003/spongebob',
        status=404
    )

    connection = Connection('http://127.0.0.1:4003')
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

    connection = Connection('http://127.0.0.1:4003')
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

    connection = Connection('http://127.0.0.1:4003')
    response = requests.get('http://127.0.0.1:4003/spongebob')
    body = connection._handle_response(response)
    assert body == {'success': True}


@pytest.mark.parametrize('method,func_name', [
    (responses.GET, 'get'),
    (responses.POST, 'post'),
])
def test_http_methods_call_correct_url_and_return_correct_response(method, func_name):
    responses.add(
        method,
        'http://127.0.0.1:4003/spongebob',
        json={'success': True},
        status=200
    )

    connection = Connection('http://127.0.0.1:4003')
    data = getattr(connection, func_name)('spongebob')
    assert data == {'success': True}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4003/spongebob'


@pytest.mark.parametrize('method,func_name', [
    (responses.GET, 'get'),
    # (responses.POST, 'post'),
])
def test_http_methods_call_correct_url_with_params_and_return_correct_response(method, func_name):
    responses.add(
        method,
        'http://127.0.0.1:4003/spongebob',
        json={'success': True},
        status=200
    )

    connection = Connection('http://127.0.0.1:4003')
    data = getattr(connection, func_name)('spongebob', params={'foo': 'bar'})
    assert data == {'success': True}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4003/spongebob?foo=bar'


def test_session_detects_hostname_correctly():
    session = Session(hostname="test.com")
    assert session.hostname == "test.com"
    assert isinstance(session, requests.Session)


def test_session_throws_error_when_missing_hostname():
    with pytest.raises(ValueError) as exception:
        Session()

        assert exception.value == 'hostname is required'


def test_session_prepends_hostname_to_url():
    responses.add(
        responses.GET,
        'http://test.com/spongebob',
        json={'success': True},
        status=200
    )

    session = Session(hostname="http://test.com")

    session.get('spongebob')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://test.com/spongebob'
