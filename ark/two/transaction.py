from ark.two.api import API


class Transaction2(API):

    def create(self, transaction):
        raise NotImplementedError()

    def transaction(self, id):
        return self.get('api/v2/transactions/{0}'.format(id))

    def unconfirmed_transaction(self, id):
        return self.get('api/v2/transactions/unconfirmed/{0}'.format(id))

    def transactions(self, parameters=None):
        return self.get('api/v2/transactions', parameters)

    def unconfirmed_transactions(self, parameters=None):
        return self.get('api/v2/transactions/unconfirmed', parameters)

    def transaction_types(self, parameters=None):
        return self.get('api/v2/transactions/types', parameters)

    def transaction_fees(self, parameters=None):
        return self.get('api/v2/transactions/fees', parameters)

    def transactio_search(self, parameters=None):
        raise NotImplementedError()
