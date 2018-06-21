import tests.api.one.env as env_v1
import tests.env as env

from ark.client import ArkClient


ARK = ArkClient(
    env.HOST,
    env.PORT,
    env.NETHASH,
    env_v1.VERSION,
    api_version=env_v1.API_VERSION
)


def test_block():
    res = ARK.block.block(env.BLOCK_ID)
    assert res['success'] is True
    assert 'block' in res


def test_blocks():
    res = ARK.block.blocks()
    assert res['success'] is True
    assert 'blocks' in res
    assert len(res['blocks']) == 100


def test_blocks_with_parameters():
    parameters = {'limit': 1}
    res = ARK.block.blocks(parameters=parameters)
    assert res['success'] is True
    assert 'blocks' in res
    assert len(res['blocks']) == 1


def test_epoch():
    res = ARK.block.epoch()
    assert res['success'] is True
    assert res['epoch'] == '2017-03-21T13:00:00.000Z'


def test_height():
    res = ARK.block.height()
    assert res['success'] is True
    assert 'height' in res


def test_nethash():
    res = ARK.block.nethash()
    assert res['success'] is True
    assert res['nethash'] == env.NETHASH


def test_fee():
    res = ARK.block.fee()
    assert res['success'] is True
    assert 'fee' in res


def test_fees():
    res = ARK.block.fees()
    assert res['success'] is True
    assert 'fees' in res


def test_milestone():
    res = ARK.block.milestone()
    assert res['success'] is True
    assert 'milestone' in res


def test_reward():
    res = ARK.block.reward()
    assert res['success'] is True
    assert 'reward' in res


def test_supply():
    res = ARK.block.supply()
    assert res['success'] is True
    assert 'supply' in res


def test_status():
    res = ARK.block.status()
    assert res['success'] is True
    assert 'epoch' in res
    assert 'height' in res
    assert 'fee' in res
    assert 'milestone' in res
    assert 'reward' in res
    assert 'supply' in res
    assert res['nethash'] == env.NETHASH
