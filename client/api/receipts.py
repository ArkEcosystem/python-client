from client.resource import Resource


class Receipts(Resource):
    def all(self, query={}):
        return self.with_endpoint('api').request_get('receipts', query)

    def get(self, transaction_hash: str):
        return self.with_endpoint('api').request_get(
            f'receipts/{transaction_hash}'
        )
