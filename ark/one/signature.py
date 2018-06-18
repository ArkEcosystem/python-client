from ark.one.api import API


class Signature(API):
    def fee(self):
        return self.get('api/signatures/fee')

    def create(self, transaction):
        return self.client.transport().create_transaction(transaction)
