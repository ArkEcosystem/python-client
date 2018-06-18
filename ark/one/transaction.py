from ark.one.api import API


class Transaction(API):
    def transaction(self, id):
        return self.get('api/transactions/get', {'id': id})

    def transactions(self, parameters=None):
        return self.get('api/transactions', parameters)

    # TO FIX - BOTH UNCONFIRMED TRANSACTION FUNCTIONS SEEM BROKEN
    def unconfirmed_transaction(self, id):
        return self.get('api/transactions/unconfirmed/get', {'id': id})

    def unconfirmed_transactions(self, parameters=None):
        return self.get('api/transactions/unconfirmed', parameters)

    def create(self, transaction):
        return self.client.transport().create_transaction(transaction)
