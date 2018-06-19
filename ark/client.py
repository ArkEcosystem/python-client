import inspect
import pkgutil
from importlib import import_module
from pathlib import Path

from ark.api.resource import Resource
from ark.connection import Connection


VERSION_TO_STRING_MAPPING = {
    'v1': 'one',
    'v2': 'two',
}


class ArkClient(object):

    def __init__(self, host, port, nethash=None, version=None, api_version='v2'):
        if api_version not in ['v1', 'v2']:
            raise Exception('Only versions "v1" and "v2" are supported')

        self.api_version = api_version

        self.connection = Connection(self, host, port, nethash, version)
        self.import_api()
        self.connection.autoconfigure()

    def import_api(self):
        """
        Dinamically imports endpoints for correct api version.
        """
        version = VERSION_TO_STRING_MAPPING[self.api_version]
        # Get all modules under the wanted version folder
        modules = pkgutil.iter_modules([str(Path(__file__).parent / 'api' / version)])
        for _, name, _ in modules:
            module = import_module('.{}'.format(name), package='ark.api.{}'.format(version))

            for attr in dir(module):
                # If attr name is `Resource`, skip it as it's a class and also has a
                # subclass of Resource
                if attr == 'Resource':
                    continue

                attribute = getattr(module, attr)
                if inspect.isclass(attribute) and issubclass(attribute, Resource):
                    # Set module class as a property on the client
                    setattr(self, name, attribute(self.connection))
