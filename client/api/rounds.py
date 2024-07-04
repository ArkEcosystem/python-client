from client.resource import Resource


class Rounds(Resource):

    def all(self, **kwargs):
        return self.request_get('rounds', kwargs)

    def show(self, round_id):
        return self.request_get(f'rounds/{round_id}')

    def delegates(self, round_id):
        return self.request_get(f'rounds/{round_id}/delegates')
