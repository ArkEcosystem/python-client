from client.resource import Resource


class Peers(Resource):

    def all(self, os=None, status=None, port=None, version=None, order_by=None,
            page=None, limit=100):

        params = {
            'os': os,
            'status': status,
            'port': port,
            'version': version,
            'orderBy': order_by,
            'page': page,
            'limit': limit,
        }
        return self.request_get('peers', params)

    def get(self, ip):
        return self.request_get('peers/{}'.format(ip))
