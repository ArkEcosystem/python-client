from client.resource import Resource


class Webhooks(Resource):

    def all(self, page=None, limit=20):
        params = {
            'page': page,
            'limit': limit
        }
        return self.request_get('webhooks', params)

    def create(self, event, target, conditions, enabled=None):
        data = {
            'event': event,
            'target': target,
            'conditions': conditions,
            'enabled': enabled
        }
        return self.request_post('webhooks', data)

    def get(self, webhook_id):
        return self.request_get('webhooks/{}'.format(webhook_id))

    def update(self, webhook_id, event=None, target=None, conditions=None, enabled=None):
        data = {}
        if event:
            data.update({'event': event})
        if target:
            data.update({'target': target})
        if conditions is not None:
            data.update({'conditions': conditions})
        if enabled is not None:
            data.update({'enabled': enabled})
        return self.request_put('webhooks/{}'.format(webhook_id), data=data)

    def delete(self, webhook_id):
        return self.request_delete('webhooks/{}'.format(webhook_id))
