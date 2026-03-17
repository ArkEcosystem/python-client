from typing import Optional

from client.resource import Resource
from client.types import PaginatedResponse, Response
from client.types.transactions import TransactionResponse, TransactionsQuery
from client.types.wallets import WalletResponse, WalletTokensForQuery, WalletTokensQuery, WalletsQuery
from client.types.tokens import TokenActionsResponse, TokenPaginatedResponseResults


class Wallets(Resource):

    def all(self, query: Optional[WalletsQuery] = None) -> PaginatedResponse[WalletResponse]:
        return self.with_endpoint('api').request_get('wallets', query)

    def top(self, query: Optional[WalletsQuery] = None) -> PaginatedResponse[WalletResponse]:
        return self.with_endpoint('api').request_get('wallets/top', query)

    def get(self, wallet_id: str) -> Response[WalletResponse]:
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}'
        )

    def transactions(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions', query
        )

    def sent_transactions(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions/sent', query
        )

    def received_transactions(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions/received', query
        )

    def votes(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/votes', query
        )

    def tokens_for(
        self,
        address: str,
        query: Optional[WalletTokensForQuery] = None,
    ) -> TokenPaginatedResponseResults[TokenActionsResponse]:
        return self.with_endpoint('api').request_get(
            f'wallets/{address}/tokens', query
        )

    def tokens(self, query: Optional[WalletTokensQuery] = None) -> TokenPaginatedResponseResults[TokenActionsResponse]:
        return self.with_endpoint('api').request_get(
            'wallets/tokens', query
        )
