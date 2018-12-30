from client.resource import Resource


class Webhooks(Resource):

    def get(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('webhooks', params)

    def retrieve(self, webhook_id):
        return self.request_get('webhooks/{}'.format(webhook_id))

    def create(self, event, target, conditions, enabled='true'):
        return self.request_post('webhooks', data={'event': event,
                                                   'target': target,
                                                   'conditions': conditions,
                                                   'enabled': enabled})

    def update(self, webhook_id, **kwargs):
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        return self.request_put('webhooks/{}'.format(webhook_id), data={**extra_params})

    def delete(self, webhook_id):
        return self.request_delete('webhooks/{}'.format(webhook_id))
