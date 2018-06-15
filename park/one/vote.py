#!/usr/bin/env python

from park.one.api import API


class Vote(API):
    def vote(secret, delegate, secondSecret=None):
        transaction = self.client.voteBuilder().create(secret, delegate,
                                                       secondSecret)

        return self.client.transport().createTransaction(transaction)

    def unvote(secret, delegate, secondSecret=None):
        transaction = self.client.voteBuilder().delete(secret, delegate,
                                                       secondSecret)

        return self.client.transport().createTransaction(transaction)
