from ark.api.resource import Resource


class Transport(Resource):
    def __init__(self, client):
        self.client = client
        self.client.port = 4002

    def list(self):
        return self.request_get('peer/list')

    def blocks_common(self, ids):
        return self.request_get('peer/blocks/common', {'ids': ','.join(ids)})

    def block(self, id):
        return self.request_get('peer/block', {'id': id})

    def blocks(self):
        return self.request_get('peer/blocks')

    def create_block(self, block):
        return self.request_post('peer/blocks', data={'block': block})

    def transactions(self):
        return self.request_get('peer/transactions')

    def transactions_from_ids(self, ids):
        return self.request_get('peer/transactionsFromIds', {'ids': ','.join(ids)})

    def create_transaction(self, transaction):
        return self.request_post('peer/transactions', data={'transactions': [transaction]})

    def create_batch_transaction(self, transaction):
        return self.request_post('peer/transactions', data={'transactions': transaction})

    def height(self):
        return self.request_get('peer/height')

    def status(self):
        return self.request_get('peer/status')
