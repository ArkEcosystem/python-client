#!/usr/bin/env python

from park.one.api import API


class Loader(API):
    def status(self):
        return self.get('api/'+self.client.api_version+'/loader/status')

    def sync(self):
        return self.get('api/'+self.client.api_version+'/loader/status/sync')

    def autoconfigure(self):
        return self.get('api/'+self.client.api_version+'/loader/autoconfigure')
