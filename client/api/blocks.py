from typing import Optional

from client.resource import Resource
from client.types import PaginatedResponse, Response
from client.types.blocks import BlockResponse, BlockTransactionsQuery, BlocksQuery
from client.types.transactions import TransactionResponse


class Blocks(Resource):

    def all(self, query: Optional[BlocksQuery] = None) -> PaginatedResponse[BlockResponse]:
        return self.with_endpoint('api').request_get('blocks', query)

    def get(self, block_hash: str) -> Response[BlockResponse]:
        return self.with_endpoint('api').request_get(f'blocks/{block_hash}')

    def first(self) -> Response[BlockResponse]:
        return self.with_endpoint('api').request_get('blocks/first')

    def last(self) -> Response[BlockResponse]:
        return self.with_endpoint('api').request_get('blocks/last')

    def transactions(
        self,
        block_hash: str,
        query: Optional[BlockTransactionsQuery] = None,
    ) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            f'blocks/{block_hash}/transactions', query
        )
