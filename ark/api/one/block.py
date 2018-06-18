from ark.api.resource import Resource


class Block(Resource):
    def block(self, id):
        return self._request_get('api/blocks/get', {'id': id})

    def blocks(self, parameters=None):
        return self._request_get('api/blocks', parameters)

    def epoch(self):
        return self._request_get('api/blocks/getEpoch')

    def height(self):
        return self._request_get('api/blocks/getHeight')

    def nethash(self):
        return self._request_get('api/blocks/getNethash')

    def fee(self):
        return self._request_get('api/blocks/getFee')

    def fees(self):
        return self._request_get('api/blocks/getFees')

    def milestone(self):
        return self._request_get('api/blocks/getMilestone')

    def reward(self):
        return self._request_get('api/blocks/getReward')

    def supply(self):
        return self._request_get('api/blocks/getSupply')

    def status(self):
        return self._request_get('api/blocks/getStatus')
