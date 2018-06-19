from ark.api.resource import Resource


class Signature(Resource):
    def fee(self):
        return self.request_get('api/signatures/fee')

    def create(self, transaction):
        return self.client.transport().create_transaction(transaction)
