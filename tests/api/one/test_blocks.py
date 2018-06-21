import responses

from ark import ArkClient


def test_get_calls_correct_url_with_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/get',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.get('spongebob')

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        'http://127.0.0.1:4002/blocks/get?id=spongebob'
    )


def test_all_calls_correct_url_with_default_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.all()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks?limit=20'


def test_all_calls_correct_url_with_passed_in_params():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.all(limit=69, offset=123)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith('http://127.0.0.1:4002/blocks?')
    assert 'limit=69' in responses.calls[0].request.url
    assert 'offset=123' in responses.calls[0].request.url


def test_epoch_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getEpoch',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.epoch()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getEpoch'


def test_height_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getHeight',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.height()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getHeight'


def test_nethash_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getNethash',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.nethash()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getNethash'


def test_fee_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getFee',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.fee()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getFee'


def test_fees_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getFees',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.fees()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getFees'


def test_milestone_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getMilestone',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.milestone()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getMilestone'


def test_reward_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getReward',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.reward()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getReward'


def test_supply_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getSupply',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.supply()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getSupply'


def test_status_calls_correct_url():
    responses.add(
        responses.GET,
        'http://127.0.0.1:4002/blocks/getStatus',
        json={'success': True},
        status=200
    )

    client = ArkClient('http://127.0.0.1:4002', api_version='v1')
    client.blocks.status()

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://127.0.0.1:4002/blocks/getStatus'
