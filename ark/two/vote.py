from ark.two.api import API


class Vote2(API):

    def vote(self, id):
        return self.get('api/v2/votes/{0}'.format(id))

    def votes(self, parameters=None):
        return self.get('api/v2/votes', parameters)
