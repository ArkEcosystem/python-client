from ark.api.resource import Resource


class Account(Resource):

    def balance(self, address):
        return self._request_get('api/accounts/getBalance', {'address': address})

    def public_key(self, address):
        return self._request_get('api/accounts/getPublicKey', {'address': address})

    def delegates(self, address):
        return self._request_get('api/accounts/delegates', {'address': address})

    def delegates_fee(self):
        return self._request_get('api/accounts/delegates/fee')

    def account(self, address):
        return self._request_get('api/accounts', {'address': address})

    def accounts(self, parameters=None):
        return self._request_get('api/accounts/getAllAccounts', parameters)

    def top(self, parameters=None):
        return self._request_get('api/accounts/top', parameters)

    def count(self):
        return self._request_get('api/accounts/count')
