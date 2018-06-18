from ark.api.resource import Resource


class Transaction(Resource):
    def transaction(self, id):
        return self._request_get('api/transactions/get', {'id': id})

    def transactions(self, parameters=None):
        return self._request_get('api/transactions', parameters)

    # TO FIX - BOTH UNCONFIRMED TRANSACTION FUNCTIONS SEEM BROKEN
    def unconfirmed_transaction(self, id):
        return self._request_get('api/transactions/unconfirmed/get', {'id': id})

    def unconfirmed_transactions(self, parameters=None):
        return self._request_get('api/transactions/unconfirmed', parameters)

    def create(self, transaction):
        return self.client.transport().create_transaction(transaction)
