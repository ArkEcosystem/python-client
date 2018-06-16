from ark.two.api import API


class Wallet(API):

    def wallet(self, id):
        return self.get(f'api/v2/wallets/{id}')

    def wallets(self, parameters=None):
        return self.get('api/v2/wallets', parameters)

    def walletsTop(self, parameters=None):
        return self.get('api/v2/wallets/top', parameters)

    def walletTransactions(self, id, parameters=None):
        return self.get(f'api/v2/wallets/{id}/transactions', parameters)

    def walletSend(self, id, parameters=None):
        return self.get(f'api/v2/wallets/{id}/transactions/sent', parameters)

    def walletReceive(self, id, parameters=None):
        return self.get(f'api/v2/wallets/{id}/transactions/received', parameters)

    def walletVotes(self, id, parameters=None):
        return self.get(f'api/v2/wallets/{id}/votes', parameters)

    def walletSearch(self, parameters=None):
        raise NotImplementedError()
