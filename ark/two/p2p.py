from ark.two.api import API


class P2p(API):

    def list(self):
        return self.get('peer/list')

    def blocks_common(self, ids):
        return self.get('peer/blocks/common', {'ids': ','.join(ids)})

    def blocks(self):
        return self.get('peer/blocks')

    def create_block(self, block):
        return self.post('peer/blocks', {'block': block})

    def transactions(self):
        return self.get('peer/transactions')

    def transactions_from_ids(self, ids):
        return self.get('peer/transactionsFromIds', {'ids': ','.join(ids)})

    def create_transaction(self, transaction):
        return self.post('peer/transactions', {'transactions': transaction})

    def height(self):
        return self.get('peer/height')

    def status(self):
        return self.get('peer/status')
