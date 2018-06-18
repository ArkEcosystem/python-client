from ark.two.api import API


class Wallet(API):

    def wallet(self, id):
        return self.get('api/v2/wallets/{0}'.format(id))

    def wallets(self, parameters=None):
        return self.get('api/v2/wallets', parameters)

    def wallets_top(self, parameters=None):
        return self.get('api/v2/wallets/top', parameters)

    def wallet_transactions(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/transactions'.format(id), parameters)

    def wallet_send(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/transactions/sent'.format(id), parameters)

    def wallet_receive(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/transactions/received'.format(id), parameters)

    def wallet_votes(self, id, parameters=None):
        return self.get('api/v2/wallets/{0}/votes'.format(id), parameters)

    def wallet_search(self, parameters=None):
        raise NotImplementedError()
