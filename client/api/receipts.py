from typing import Optional

from client.resource import Resource
from client.types.receipts import ReceiptContractsQuery, ReceiptQuery, ReceiptsQuery


class Receipts(Resource):
    def all(self, query: Optional[ReceiptsQuery] = None):
        return self.with_endpoint('api').request_get('receipts', query)

    def get(
        self,
        transaction_hash: str,
        query: Optional[ReceiptQuery] = None,
    ):
        return self.with_endpoint('api').request_get(
            f'receipts/{transaction_hash}', query
        )

    def contracts(self, query: Optional[ReceiptContractsQuery] = None):
        return self.with_endpoint('api').request_get(
            'receipts/contracts', query
        )
