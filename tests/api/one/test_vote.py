import pytest

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


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_vote():
    assert False


@pytest.mark.skip('Need to set up an account and add transaction testing.')
def test_unvote():
    assert False
