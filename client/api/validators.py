from client.resource import Resource


class Validators(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get('validators', query)

    def get(self, validator_id):
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}'
        )

    def blocks(self, validator_id, query={}):
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}/blocks', query
        )

    def voters(self, validator_id, query={}):
        return self.with_endpoint('api').request_get(
            f'validators/{validator_id}/voters', query
        )
