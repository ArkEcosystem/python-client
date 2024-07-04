from client.resource import Resource


class Blockchain(Resource):

    def blockchain(self):
        return self.request_get('blockchain')
