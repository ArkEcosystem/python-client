from ark.resource import Resource


class Block(Resource):
    def block(self, id):
        return self.request_get('blocks/get', {'id': id})

    def blocks(self, parameters=None):
        return self.request_get('blocks', parameters)

    def epoch(self):
        return self.request_get('blocks/getEpoch')

    def height(self):
        return self.request_get('blocks/getHeight')

    def nethash(self):
        return self.request_get('blocks/getNethash')

    def fee(self):
        return self.request_get('blocks/getFee')

    def fees(self):
        return self.request_get('blocks/getFees')

    def milestone(self):
        return self.request_get('blocks/getMilestone')

    def reward(self):
        return self.request_get('blocks/getReward')

    def supply(self):
        return self.request_get('blocks/getSupply')

    def status(self):
        return self.request_get('blocks/getStatus')
