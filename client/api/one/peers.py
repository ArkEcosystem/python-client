from client.exceptions import ArkParameterException
from client.resource import Resource


class Peers(Resource):

    def get(self, ip, port):
        params = {
            'ip': ip,
            'port': port
        }
        return self.request_get('peers/get', params)

    def all(self, limit=100, offset=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('peers', params)

    def version(self):
        return self.request_get('peers/version')
