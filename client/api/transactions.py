from typing import Optional, Sequence

from client.resource import Resource
from client.types import PaginatedResponse, Response
from client.types.transactions import (
    TransactionConfigurationResponse,
    TransactionCreateResponse,
    TransactionGetQuery,
    TransactionResponse,
    TransactionsQuery,
    UnconfirmedTransactionsQuery,
)


class Transactions(Resource):

    def all(self, query: Optional[TransactionsQuery] = None) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            'transactions', query
        )

    def create(self, transactions: Sequence[str]) -> Response[TransactionCreateResponse]:
        return self.with_endpoint('transactions').request_post(
            'transactions', data={'transactions': transactions}
        )

    def get(
        self,
        transaction_id: str,
        query: Optional[TransactionGetQuery] = None,
    ) -> Response[TransactionResponse]:
        return self.with_endpoint('api').request_get(
            f'transactions/{transaction_id}', query
        )

    def all_unconfirmed(
        self,
        query: Optional[UnconfirmedTransactionsQuery] = None,
    ) -> PaginatedResponse[TransactionResponse]:
        return self.with_endpoint('transactions').request_get(
            'transactions/unconfirmed', query
        )

    def get_unconfirmed(self, transaction_id: str) -> Response[TransactionResponse]:
        return self.with_endpoint('transactions').request_get(
            f'transactions/unconfirmed/{transaction_id}'
        )

    def configuration(self) -> Response[TransactionConfigurationResponse]:
        return self.with_endpoint('transactions').request_get(
            'configuration'
        )
