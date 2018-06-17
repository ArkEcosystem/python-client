from ark.two.api import API


class Peer2(API):

    def peer(self, ip):
        return self.get('api/v2/peers/{0}'.format(ip))

    def peers(self, parameters=None):
        return self.get('api/v2/peers', parameters)
