#!/usr/bin/env python

from ark.one.api import API

class Vote(API):
    def vote(self, transaction):
        return self.client.transport().createTransaction(transaction)

    def unvote(self, transaction):
        return self.client.transport().createTransaction(transaction)
