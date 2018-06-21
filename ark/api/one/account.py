from ark.resource import Resource


class Account(Resource):

    def balance(self, address):
        return self.request_get('accounts/getBalance', {'address': address})

    def public_key(self, address):
        return self.request_get('accounts/getPublicKey', {'address': address})

    def delegates(self, address):
        return self.request_get('accounts/delegates', {'address': address})

    def delegates_fee(self):
        return self.request_get('accounts/delegates/fee')

    def account(self, address):
        return self.request_get('accounts', {'address': address})

    def accounts(self, parameters=None):
        return self.request_get('accounts/getAllAccounts', parameters)

    def top(self, parameters=None):
        return self.request_get('accounts/top', parameters)

    def count(self):
        return self.request_get('accounts/count')
