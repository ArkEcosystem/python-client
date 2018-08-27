from ark.resource import Resource


class Signatures(Resource):

    def fee(self):
        return self.request_get('signatures/fee')
