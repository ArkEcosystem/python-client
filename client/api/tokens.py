from typing import Optional

from client.resource import Resource
from client.types import PaginatedQuery
from client.types.tokens import TokenApprovalsQuery, TokenLookupQuery, TokenTransfersQuery, TokensQuery


class Tokens(Resource):

    def all(self, query: Optional[TokensQuery] = None):
        return self.with_endpoint('api').request_get('tokens', query)

    def transfers(self, query: Optional[TokenTransfersQuery] = None):
        return self.with_endpoint('api').request_get(
            'tokens/transfers', query
        )

    def approvals(self, query: Optional[TokenApprovalsQuery] = None):
        return self.with_endpoint('api').request_get(
            'tokens/approvals', query
        )

    def whitelist(self, query: Optional[PaginatedQuery] = None):
        return self.with_endpoint('api').request_get(
            'tokens/whitelist', query
        )

    def get(self, address: str):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}'
        )

    def transfers_for(
        self,
        address: str,
        query: Optional[TokenLookupQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/transfers', query
        )

    def approvals_for(
        self,
        address: str,
        query: Optional[TokenLookupQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/approvals', query
        )

    def holders_for(self, address: str):
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/holders'
        )
