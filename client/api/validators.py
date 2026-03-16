from typing import Optional

from client.api.blocks import BlocksQuery
from client.api.wallets import WalletsQuery
from client.resource import Resource
from client.types.validators import ValidatorsQuery


class Validators(Resource):

    def all(self, query: Optional[ValidatorsQuery] = None):
        return self.with_endpoint('api').request_get('validators', query)

    def get(self, validator_id: str):
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}'
        )

    def blocks(
        self,
        validator_id: str,
        query: Optional[BlocksQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}/blocks', query
        )

    def voters(
        self,
        validator_id: str,
        query: Optional[WalletsQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}/voters', query
        )
