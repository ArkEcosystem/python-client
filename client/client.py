from dotenv import load_dotenv
import inspect
import pkgutil
from importlib import import_module
import os
from pathlib import Path

from client.connection import Connection
from client.exceptions import ArkParameterException
from client.resource import Resource

class ArkClient(object):

    def __init__(self, hostname):
        """
        :param string hostname: Node hostname. Examples: `http://127.0.0.1:4003` or
            `http://my.domain.io/api/`. This is to allow people to server the api
            on whatever url they want.
        """
        self.connection = Connection(hostname)
        self._import_api()

    def _import_api(self):
        """
        Dynamically imports API endpoints.
        """
        modules = pkgutil.iter_modules([str(Path(__file__).parent / 'api')])
        print(modules)
        for _, name, _ in modules:
            module = import_module('client.api.{}'.format(name))
            for attr in dir(module):
                # If attr name is `Resource`, skip it as it's a class and also has a
                # subclass of Resource
                if attr == 'Resource':
                    continue

                attribute = getattr(module, attr)
                if inspect.isclass(attribute) and issubclass(attribute, Resource):
                    # Set module class as a property on the client
                    if name == "webhooks":
                        #new_connection = self._swap_port()
                        setattr(self, name, attribute(self._swap_port()))  
                    else:
                        setattr(self, name, attribute(self.connection))
     
    def _swap_port(self):
        """
        Dynamically swaps Webhooks port during module import
        """
        env = str(Path.home()) + '/.ark/.env'
        if os.path.exists(env) is True:
            load_dotenv(env)
            api = os.getenv('ARK_API_PORT') 
            webhook = os.getenv('ARK_WEBHOOKS_PORT')
        else:
            api = '4003'
            webhook = '4004'

        return Connection(self.connection.hostname.replace(api, webhook))
