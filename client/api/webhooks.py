from client.resource import Resource
from dotenv import load_dotenv
import os
from pathlib import Path


class Webhooks(Resource):

    def swap_ports(self):
        env = str(Path.home()) + '/.ark/.env'
        if os.path.exists(env) is True:
            load_dotenv(env)
            api = os.getenv("ARK_API_PORT") 
            webhook = os.getenv("ARK_WEBHOOKS_PORT")
        else:
            api = "4003"
            webhook = "4004"

        Resource.connection.hostname = Resource.connection.hostname.replace(api,webhook)
        
    def get(self, page=None, limit=100):
        self.swap_ports()
        print(self.connection.hostname)
        params = {
            'page': page,
            'limit': limit,
        }
        return self.request_get('webhooks', params)

    def retrieve(self, webhook_id):
        self.swap_ports()
        return self.request_get('webhooks/{}'.format(webhook_id))

    def create(self, event, target, conditions, enabled=None):
        self.swap_ports()
        return self.request_post('webhooks', data={'event': event,
                                                   'target': target,
                                                   'conditions': conditions,
                                                   'enabled': enabled})

    def update(self, webhook_id, event=None, target=None, conditions=None, enabled=None):
        self.swap_ports()
        return self.request_put('webhooks/{}'.format(webhook_id),
                                data={'event': event,
                                      'target': target,
                                      'conditions': conditions,
                                      'enabled': enabled})

    def delete(self, webhook_id):
        self.swap_ports()
        return self.request_delete('webhooks/{}'.format(webhook_id))
