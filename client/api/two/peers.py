from client.resource import Resource
from client.exceptions import ArkParameterException


class Peers(Resource):

    def all(self, os=None, status=None, port=None, version=None, order_by=None,
            page=None, limit=100):
        if(limit > 100):
            raise ArkParameterException('Maximum number of objects to return is 100')
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
