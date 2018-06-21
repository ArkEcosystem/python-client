from datetime import datetime, timezone

import responses

from ark import ArkClient


def _utc_datetime(*args, **kwargs):
    return datetime(tzinfo=timezone.utc, *args, **kwargs)


def test_transactions_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/statistics/transactions',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.statistics.transactions(
        _utc_datetime(2018, 6, 1),
        _utc_datetime(2018, 6, 20)
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/statistics/transactions?'
    )
    assert 'from=1527804000' in responses.calls[0].request.url
    assert 'to=1529445600' in responses.calls[0].request.url


def test_blocks_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/statistics/blocks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.statistics.blocks(
        _utc_datetime(2018, 6, 1),
        _utc_datetime(2018, 6, 20)
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/statistics/blocks?'
    )
    assert 'from=1527804000' in responses.calls[0].request.url
    assert 'to=1529445600' in responses.calls[0].request.url


def test_votes_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/statistics/votes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.statistics.votes(
        _utc_datetime(2018, 6, 1),
        _utc_datetime(2018, 6, 20)
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/statistics/votes?'
    )
    assert 'from=1527804000' in responses.calls[0].request.url
    assert 'to=1529445600' in responses.calls[0].request.url


def test_unvotes_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/statistics/unvotes',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v2')
    client.statistics.unvotes(
        _utc_datetime(2018, 6, 1),
        _utc_datetime(2018, 6, 20)
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(
        'http://127.0.0.1:4002/statistics/unvotes?'
    )
    assert 'from=1527804000' in responses.calls[0].request.url
    assert 'to=1529445600' in responses.calls[0].request.url
