from ark.one.api import API


class Delegate(API):

    def count(self):
        return self.get('api/delegates/count')

    def search(self, query, parameters=None):
        if not parameters:
            parameters = {}
        parameters['q'] = query
        return self.get('api/delegates/search', parameters)

    def voters(self, public_key):
        return self.get('api/delegates/voters', {'publicKey': public_key})

    def delegate(self, parameters=None):
        """
        :param publicKey: Unique public key for the delegate.
        :param username: Unique username for the delegate.
        :return: delegate
        """

        return self.get('api/delegates/get', parameters)

    def delegates(self, parameters=None):
        """
         :param offset: The offset of resources that will be returned.
         :param limit: The number of resources per page.
         :param orderBy: The column by which the resources will be sorted.
         :return: delegates
        """

        return self.get('api/delegates', parameters)

    def fee(self):
        return self.get('api/delegates/fee')

    def forged_by_account(self, generator_public_key):
        return self.get('api/delegates/forging/getForgedByAccount',
                        {'generatorPublicKey': generator_public_key})

    def create(self, transaction):
        return self.client.transport().create_transaction(transaction)

    def next_forgers(self):
        return self.get('api/delegates/getNextForgers')
