import responses
from client import Client


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/receipts',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.receipts.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/receipts'
    )


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/receipts',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.receipts.all({
        'query_param1': 'value1',
        'query_param2': 'value2',
    })
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/receipts?')
    assert 'query_param1=value1' in url
    assert 'query_param2=value2' in url


def test_get_calls_correct_url():
    transaction_hash = '12345'
    responses.add(
        responses.GET,
        f'http://127.0.0.1:4002/api/receipts/{transaction_hash}',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.receipts.get(transaction_hash)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        f'http://127.0.0.1:4002/api/receipts/{transaction_hash}'
    )


def test_get_calls_correct_url_with_params():
    transaction_hash = '12345'
    responses.add(
        responses.GET,
        f'http://127.0.0.1:4002/api/receipts/{transaction_hash}',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.receipts.get(transaction_hash, {'format': 'hex'})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith(f'http://127.0.0.1:4002/api/receipts/{transaction_hash}?')
    assert 'format=hex' in url


def test_contracts_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/receipts/contracts',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.receipts.contracts()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/api/receipts/contracts'
    )


def test_contracts_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/receipts/contracts',
        json={'success': True},
        status=200
    )

    client = Client('http://127.0.0.1:4002/api')
    client.receipts.contracts({'status': 'success'})
    assert len(responses.calls) == 1
    url = responses.calls[0].request.url
    assert url.startswith('http://127.0.0.1:4002/api/receipts/contracts?')
    assert 'status=success' in url
