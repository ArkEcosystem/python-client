from typing import Optional

from client.resource import Resource
from client.types import PaginatedQuery, PaginatedResponse, Response
from client.types.tokens import (
    TokenActionsResponse,
    TokenAddressHoldersResponse,
    TokenAddressesResponse,
    TokenApprovalsQuery,
    TokenLookupQuery,
    TokenPaginatedResponseResults,
    TokenResponse,
    TokenTransfersQuery,
    TokenWhitelistResponse,
    TokensQuery,
)


class Tokens(Resource):

    def all(self, query: Optional[TokensQuery] = None) -> PaginatedResponse[TokenResponse]:
        return self.with_endpoint('api').request_get('tokens', query)

    def transfers(self, query: Optional[TokenTransfersQuery] = None) -> TokenPaginatedResponseResults[TokenActionsResponse]:
        return self.with_endpoint('api').request_get(
            'tokens/transfers', query
        )

    def approvals(self, query: Optional[TokenApprovalsQuery] = None) -> TokenPaginatedResponseResults[TokenActionsResponse]:
        return self.with_endpoint('api').request_get(
            'tokens/approvals', query
        )

    def whitelist(self, query: Optional[PaginatedQuery] = None) -> PaginatedResponse[TokenWhitelistResponse]:
        return self.with_endpoint('api').request_get(
            'tokens/whitelist', query
        )

    def get(self, address: str) -> Response[TokenAddressesResponse]:
        return self.with_endpoint('api').request_get(
            f'tokens/{address}'
        )

    def transfers_for(
        self,
        address: str,
        query: Optional[TokenLookupQuery] = None,
    ) -> TokenPaginatedResponseResults[TokenActionsResponse]:
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/transfers', query
        )

    def approvals_for(
        self,
        address: str,
        query: Optional[TokenLookupQuery] = None,
    ) -> TokenPaginatedResponseResults[TokenActionsResponse]:
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/approvals', query
        )

    def holders_for(self, address: str) -> PaginatedResponse[TokenAddressHoldersResponse]:
        return self.with_endpoint('api').request_get(
            f'tokens/{address}/holders'
        )
