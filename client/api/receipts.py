from typing import Optional

from client.resource import Resource
from client.types import PaginatedResponse, Response
from client.types.receipts import ReceiptContractsQuery, ReceiptQuery, ReceiptResponse, ReceiptsQuery


class Receipts(Resource):

    def all(self, query: Optional[ReceiptsQuery] = None) -> PaginatedResponse[ReceiptResponse]:
        return self.with_endpoint('api').request_get('receipts', query)

    def get(
        self,
        transaction_hash: str,
        query: Optional[ReceiptQuery] = None,
    ) -> Response[ReceiptResponse]:
        return self.with_endpoint('api').request_get(
            f'receipts/{transaction_hash}', query
        )

    def contracts(self, query: Optional[ReceiptContractsQuery] = None) -> PaginatedResponse[ReceiptResponse]:
        return self.with_endpoint('api').request_get(
            'receipts/contracts', query
        )
