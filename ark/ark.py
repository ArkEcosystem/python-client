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
        version = VERSION_TO_STRING_MAPPING[self.api_version]
        modules = pkgutil.iter_modules([Path(__file__).parent / 'api' / version])

        for _, name, _ in modules:
            module = import_module('.{}'.format(name), package='ark.api.{}'.format(version))

            for attr in dir(module):
                if attr == 'Resource':
                    continue

                attribute = getattr(module, attr)
                if inspect.isclass(attribute) and issubclass(attribute, Resource):
                    setattr(self, name, attribute(self.connection))
