from client.resource import Resource


class Rounds(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get('rounds', query)

    def show(self, round_id):
        return self.with_endpoint('api').request_get(f'rounds/{round_id}')

    def validators(self, round_id):
        return self.with_endpoint('api').request_get(
            f'rounds/{round_id}/validators'
        )
