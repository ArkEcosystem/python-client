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


def test_status():
    res = ARK.loader.status()
    assert res['success'] is True
    assert 'loaded' in res
    assert 'now' in res
    assert 'blocksCount' in res


def test_sync():
    res = ARK.loader.sync()
    assert res['success'] is True
    assert 'syncing' in res
    assert 'blocks' in res
    assert 'height' in res
    assert 'id' in res


def test_autoconfigure():
    res = ARK.loader.autoconfigure()
    assert res['success'] is True
    assert 'network' in res
