from ark.resource import Resource


class Signature(Resource):
    def fee(self):
        return self.request_get('signatures/fee')

    def create(self, transaction):
        return self.client.transport().create_transaction(transaction)
