from client.resource import Resource


class Receipts(Resource):
    def all(self, **kwargs):
        return self.with_endpoint('api').request_get('receipts', kwargs)

    def get(self, transaction_hash: str):
        return self.with_endpoint('api').request_get('receipts', {
            'txHash': transaction_hash,
        })
