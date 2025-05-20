import responses
from client import ArkClient


def test_all_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/receipts',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.receipts.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/api/receipts'


def test_all_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/api/receipts',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.receipts.all(query_param1='value1', query_param2='value2')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/api/receipts?')
    assert 'query_param1=value1' in responses.calls[0].request.url
    assert 'query_param2=value2' in responses.calls[0].request.url


def test_get_calls_correct_url():
    transaction_hash = '12345'
    responses.add(
        responses.GET,
        f'http://127.0.0.1:4002/api/receipts/{transaction_hash}',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002/api')
    client.receipts.get(transaction_hash)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == f'http://127.0.0.1:4002/api/receipts/{transaction_hash}'
