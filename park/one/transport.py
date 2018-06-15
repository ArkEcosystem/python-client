#!/usr/bin/env python

from park.one.api import API


class Transport(API):
    def list(self):
        return self.get('peer/list')

    def blocksCommon(self, ids):
        return self.get('peer/blocks/common', {"ids": ','.join(ids)})

    def block(self, id):
        return self.get('peer/block', {"id": id})

    def blocks(self):
        return self.get('peer/blocks')

    def createBlock(self, block):
        return self.post('peer/blocks', {"block": block})

    def transactions(self):
        return self.get('peer/transactions')

    def transactionsFromIds(self, ids):
        return self.get('peer/transactionsFromIds', {"ids": ','.join(ids)})

    def createTransaction(self, transaction):
        return self.post('peer/transactions', {"transactions": [transaction]})

    def createBatchTransaction(self, transaction):
        return self.post('peer/transactions', {"transactions": transaction})

    def height(self):
        return self.get('peer/height')

    def status(self):
        return self.get('peer/status')
