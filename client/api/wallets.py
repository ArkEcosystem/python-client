from typing import Optional

from client.resource import Resource
from client.types.transactions import TransactionsQuery
from client.types.wallets import WalletTokensForQuery, WalletTokensQuery, WalletsQuery


class Wallets(Resource):

    def all(self, query: Optional[WalletsQuery] = None):
        return self.with_endpoint('api').request_get('wallets', query)

    def top(self, query: Optional[WalletsQuery] = None):
        return self.with_endpoint('api').request_get('wallets/top', query)

    def get(self, wallet_id: str):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}'
        )

    def transactions(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions', query
        )

    def sent_transactions(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions/sent', query
        )

    def received_transactions(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/transactions/received', query
        )

    def votes(
        self,
        wallet_id: str,
        query: Optional[TransactionsQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'wallets/{wallet_id}/votes', query
        )

    def tokens_for(
        self,
        address: str,
        query: Optional[WalletTokensForQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'wallets/{address}/tokens', query
        )

    def tokens(self, query: Optional[WalletTokensQuery] = None):
        return self.with_endpoint('api').request_get(
            'wallets/tokens', query
        )
