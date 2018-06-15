#!/usr/bin/env python

from park.one.api import API

class Peer(API):
    # TO FIX - PEER FUNCTION NOT WORKING
    def peer(self, ip, port):
        return self.get('api/peers/get', {"ip": ip, "port": port})

    def peers(self, parameters={}):
        return self.get('api/peers', parameters)

    def version(self):
        return self.get('api/peers/version')
