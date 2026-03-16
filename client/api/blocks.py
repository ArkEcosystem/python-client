from typing import Optional

from client.resource import Resource
from client.types.blocks import BlockTransactionsQuery, BlocksQuery


class Blocks(Resource):

    def all(self, query: Optional[BlocksQuery] = None):
        return self.with_endpoint('api').request_get('blocks', query)

    def get(self, block_hash: str):
        return self.with_endpoint('api').request_get(f'blocks/{block_hash}')

    def first(self):
        return self.with_endpoint('api').request_get('blocks/first')

    def last(self):
        return self.with_endpoint('api').request_get('blocks/last')

    def transactions(
        self,
        block_hash: str,
        query: Optional[BlockTransactionsQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'blocks/{block_hash}/transactions', query
        )
