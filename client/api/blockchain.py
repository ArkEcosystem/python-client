from client.resource import Resource


class Blockchain(Resource):

    def blockchain(self):
        return self.with_endpoint('api').request_get('blockchain')
