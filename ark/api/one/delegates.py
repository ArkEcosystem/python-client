from ark.exceptions import ArkParameterException
from ark.resource import Resource


class Delegate(Resource):

    def count(self):
        return self.request_get('delegates/count')

    def search(self, query, limit=20, offset=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'q': query,
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('delegates/search', params)

    def voters(self, public_key):
        return self.request_get('delegates/voters', {'publicKey': public_key})

    def get(self, public_key=None, username=None):
        if not public_key and not username:
            raise ArkParameterException('publick_key or username need to be specified')

        params = {
            'publicKey': public_key,
            'username': username
        }
        return self.request_get('delegates/get', params)

    def all(self, limit=20, offset=None, order_by=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')

        params = {
            'limit': limit,
            'offset': offset,
            'orderBy': order_by
        }
        return self.request_get('delegates', params)

    def fee(self):
        return self.request_get('delegates/fee')

    def forged_by_account(self, generator_public_key):
        params = {
            'generatorPublicKey': generator_public_key
        }
        return self.request_get('delegates/forging/getForgedByAccount', params)

    def next_forgers(self):
        return self.request_get('delegates/getNextForgers')
