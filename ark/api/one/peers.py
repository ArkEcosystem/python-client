from ark.exceptions import ArkParameterException
from ark.resource import Resource


class Peers(Resource):

    def get(self, ip, port):
        params = {
            'ip': ip,
            'port': port
        }
        return self.request_get('peers/get', params)

    def all(self, limit=20, offset=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('peers', params)

    def version(self):
        return self.request_get('peers/version')
