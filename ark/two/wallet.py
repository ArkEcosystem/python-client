from ark.two.api import API


class Wallet(API):

    def wallet(self, id):
        return self.get('api/v2/wallets/{0}'.format(id))

    def wallets(self, parameters=None):
        return self.get('api/v2/wallets', parameters)

    def walletsTop(self, parameters=None):
        return self.get('api/v2/wallets/top', parameters)

    def walletTransactions(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/transactions'.format(id), parameters)

    def walletSend(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/transactions/sent'.format(id), parameters)

    def walletReceive(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/transactions/received'.format(id), parameters)

    def walletVotes(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/votes'.format(id), parameters)

    def walletSearch(self, parameters=None):
        raise NotImplementedError()
