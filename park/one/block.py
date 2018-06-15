#!/usr/bin/env python

from park.one.api import API


class Block(API):
    def block(self, id):
        return self.get('api/'+self.client.api_version+'/blocks/get', {"id": id})

    def blocks(self, parameters={}):
        return self.get('api/'+self.client.api_version+'/blocks', parameters)

    def epoch(self):
        return self.get('api/'+self.client.api_version+'/blocks/getEpoch')

    def height(self):
        return self.get('api/'+self.client.api_version+'/blocks/getHeight')

    def nethash(self):
        return self.get('api/'+self.client.api_version+'/blocks/getNethash')

    def fee(self):
        return self.get('api/'+self.client.api_version+'/blocks/getFee')

    def fees(self):
        return self.get('api/'+self.client.api_version+'/blocks/getFees')

    def milestone(self):
        return self.get('api/'+self.client.api_version+'/blocks/getMilestone')

    def reward(self):
        return self.get('api/'+self.client.api_version+'/blocks/getReward')

    def supply(self):
        return self.get('api/'+self.client.api_version+'/blocks/getSupply')

    def status(self):
        return self.get('api/'+self.client.api_version+'/blocks/getStatus')
