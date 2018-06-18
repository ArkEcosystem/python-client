from ark.one.api import API


class Vote(API):
    def vote(self, transaction):
        return self.client.transport().create_transaction(transaction)

    def unvote(self, transaction):
        return self.client.transport().create_transaction(transaction)
