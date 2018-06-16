from ark.two.api import API


class Block2(API):
    def blocks(self, parameters=None):
        return self.get('api/v2/blocks', parameters)

    def block(self, id, parameters=None):
        return self.get(f'api/v2/blocks/{id}', parameters)

    def blockTransactions(self, id, parameters=None):
        return self.get(f'api/v2/blocks/{id}/transactions', parameters)

    def blockSearch(self, parameters=None):
        raise NotImplementedError()