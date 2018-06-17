from ark.two.api import API


class Block2(API):
    def blocks(self, parameters=None):
        return self.get('api/v2/blocks', parameters)

    def block(self, id, parameters=None):
        return self.get('api/v2/blocks/{0}'.format(id), parameters)

    def blockTransactions(self, id, parameters=None):
        return self.get('api/v2/blocks/{0}/transactions'.format(id), parameters)

    def blockSearch(self, parameters=None):
        raise NotImplementedError()
