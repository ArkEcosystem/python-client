from typing import Optional

from client.resource import Resource
from client.types import PaginatedResponse, Response
from client.types.blocks import BlocksQuery
from client.types.transactions import TransactionResponse
from client.types.validators import ValidatorsQuery
from client.types.wallets import WalletResponse, WalletsQuery


class Validators(Resource):

    def all(self, query: Optional[ValidatorsQuery] = None) -> PaginatedResponse[WalletResponse]:
        return self.with_endpoint('api').request_get('validators', query)

    def get(self, validator_id: str) -> Response[WalletResponse]:
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}'
        )

    def blocks(
        self,
        validator_id: str,
        query: Optional[BlocksQuery] = None,
    ) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}/blocks', query
        )

    def voters(
        self,
        validator_id: str,
        query: Optional[WalletsQuery] = None,
    ) -> PaginatedResponse[WalletResponse]:
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}/voters', query
        )
