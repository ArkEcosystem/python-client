#!/usr/bin/env python

from ark.one.api import API

class Block(API):
    def block(self, id):
        return self.get('api/blocks/get', {"id": id})

    def blocks(self, parameters={}):
        return self.get('api/blocks', parameters)

    def epoch(self):
        return self.get('api/blocks/getEpoch')

    def height(self):
        return self.get('api/blocks/getHeight')

    def nethash(self):
        return self.get('api/blocks/getNethash')

    def fee(self):
        return self.get('api/blocks/getFee')

    def fees(self):
        return self.get('api/blocks/getFees')

    def milestone(self):
        return self.get('api/blocks/getMilestone')

    def reward(self):
        return self.get('api/blocks/getReward')

    def supply(self):
        return self.get('api/blocks/getSupply')

    def status(self):
        return self.get('api/blocks/getStatus')
