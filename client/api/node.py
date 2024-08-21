from client.resource import Resource


class Node(Resource):

    def status(self):
        return self.with_endpoint('api').request_get('node/status')

    def syncing(self):
        return self.with_endpoint('api').request_get('node/syncing')

    def configuration(self):
        return self.with_endpoint('api').request_get('node/configuration')

    def crypto(self):
        return self.with_endpoint('api').request_get('node/configuration/crypto')

    def fees(self, days=None):
        params = {
            'days': days,
        }
        return self.with_endpoint('api').request_get('node/fees', params)
