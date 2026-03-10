from client.resource import Resource


class Blocks(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get('blocks', query)

    def get(self, block_id):
        return self.with_endpoint('api').request_get(f'blocks/{block_id}')

    def first(self):
        return self.with_endpoint('api').request_get('blocks/first')

    def last(self):
        return self.with_endpoint('api').request_get('blocks/last')

    def transactions(self, block_id, query={}):
        return self.with_endpoint('api').request_get(
            f'blocks/{block_id}/transactions', query
        )
