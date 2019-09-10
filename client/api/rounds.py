from client.resource import Resource


class Rounds(Resource):

    def delegates(self, round_id):
        return self.request_get('rounds/{}/delegates'.format(round_id))
