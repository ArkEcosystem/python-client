from typing import Optional, Sequence

from client.resource import Resource
from client.types.transactions import TransactionGetQuery, TransactionsQuery, UnconfirmedTransactionsQuery


class Transactions(Resource):

    def all(self, query: Optional[TransactionsQuery] = None):
        return self.with_endpoint('api').request_get(
            'transactions', query
        )

    def create(self, transactions: Sequence[str]):
        return self.with_endpoint('transactions').request_post(
            'transactions', data={'transactions': transactions}
        )

    def get(
        self,
        transaction_id: str,
        query: Optional[TransactionGetQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'transactions/{transaction_id}', query
        )

    def all_unconfirmed(
        self,
        query: Optional[UnconfirmedTransactionsQuery] = None,
    ):
        return self.with_endpoint('transactions').request_get(
            'transactions/unconfirmed', query
        )

    def get_unconfirmed(self, transaction_id: str):
        return self.with_endpoint('transactions').request_get(
            f'transactions/unconfirmed/{transaction_id}'
        )

    def configuration(self):
        return self.with_endpoint('transactions').request_get(
            'configuration'
        )
