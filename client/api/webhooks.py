from client.resource import Resource
from dotenv import load_dotenv
from pathlib import Path


class Webhooks(Resource):

    def swap_ports(self):
        env = str(Path.home()) + /'.ark/.env'
        print(env)
        print("old connection")
        print(self.connection.hostname)
       
        print("new connection")
        self.connection.hostname="random"
        print(self.connection.hostname)
        
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
