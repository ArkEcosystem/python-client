from ark.resource import Resource


class Vote(Resource):
    def vote(self, transaction):
        return self.client.transport().create_transaction(transaction)

    def unvote(self, transaction):
        return self.client.transport().create_transaction(transaction)
