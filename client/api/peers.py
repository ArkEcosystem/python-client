from client.resource import Resource


class Peers(Resource):

    def all(self, query={}):
        return self.with_endpoint('api').request_get('peers', query)

    def get(self, ip):
        return self.with_endpoint('api').request_get(f'peers/{ip}')
