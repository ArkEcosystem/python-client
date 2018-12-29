from client.resource import Resource


class Webhooks(Resource):

    def __init__(self):
        self.events = []
        self.conditions = []
        # pass - need to swap ports for call to work

    def test(self):
        print(self)

    def get(self, page=None, limit=100):
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('webhooks', params)

    def retrieve(self, webhook_id):
        return self.request_get('webhooks/{}'.format(webhook_id))

    def create(self, event, target, conditions, enabled=None):
        return self.request_post('webhooks', data={'event': event,
                                                   'target': target,
                                                   'conditions': conditions,
                                                   'enabled': enabled})

    def update(self, webhook_id, event=None, target=None, conditions=None, enabled=None):
        return self.request_put('webhooks/{}'.format(webhook_id),
                                data={'event': event,
                                      'target': target,
                                      'conditions': conditions,
                                      'enabled': enabled})

    def delete(self, webhook_id):
        return self.request_delete('webhooks/{}'.format(webhook_id))