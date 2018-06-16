from ark.two.api import API


class Transaction2(API):

    def create(self, transaction):
        raise NotImplementedError()

    def transaction(self, id):
        return self.get(f'api/v2/transactions/{id}')

    def unconfirmedTransaction(self, id):
        return self.get(f'api/v2/transactions/unconfirmed/{id}')

    def transactions(self, parameters=None):
        return self.get('api/v2/transactions', parameters)

    def unconfirmedTransactions(self, parameters=None):
        return self.get('api/v2/transactions/unconfirmed', parameters)

    def transactionTypes(self, parameters=None):
        return self.get('api/v2/transactions/types', parameters)

    def transactionFees(self, parameters=None):
        return self.get('api/v2/transactions/fees', parameters)

    def transactionSearch(self, parameters=None):
        raise NotImplementedError()
