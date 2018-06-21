from ark.exceptions import ArkParameterException
from ark.resource import Resource


class Accounts(Resource):

    def balance(self, address):
        return self.request_get('accounts/getBalance', {'address': address})

    def public_key(self, address):
        return self.request_get('accounts/getPublicKey', {'address': address})

    def delegates(self, address):
        return self.request_get('accounts/delegates', {'address': address})

    def delegates_fee(self):
        return self.request_get('accounts/delegates/fee')

    def get(self, address):
        return self.request_get('accounts', {'address': address})

    def all(self, limit=20, offset=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('accounts/getAllAccounts', params)

    def top(self, limit=20, offset=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('accounts/top', params)

    def count(self):
        return self.request_get('accounts/count')
