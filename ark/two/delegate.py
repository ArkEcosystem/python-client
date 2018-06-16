from ark.two.api import API


class Delegate2(API):

    def delegate(self, id):
        return self.get(f'api/v2/delegates/{id}')

    def delegates(self, parameters=None):
        """
         :param page: The number of the page that will be returned.
         :param limit: The number of resources per page.
         :return: List all delegates
        """

        return self.get('api/v2/delegates', parameters)

    def blocks(self, id, parameters=None):
        return self.get(f'api/v2/delegates/{id}/blocks', parameters)

    def voters(self, id, parameters=None):
        return self.get(f'api/v2/delegates/{id}/voters', parameters)