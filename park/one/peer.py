#!/usr/bin/env python

from park.one.api import API


class Peer(API):
    def peer(self, ip, port):
        return self.get('api/'+self.client.api_version+'/peers/get', {"ip": ip, "port": port})

    def peers(self, parameters={}):
        return self.get('api/'+self.client.api_version+'/peers', parameters)

    def version(self):
        return self.get('api/'+self.client.api_version+'/peers/version')
