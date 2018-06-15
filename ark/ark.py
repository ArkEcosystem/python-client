#!/usr/bin/env python

# WORK IN PROGRESS
from ark.one.account import Account
from ark.one.block import Block
from ark.one.delegate import Delegate
from ark.one.loader import Loader
from ark.one.peer import Peer
from ark.one.signature import Signature
from ark.one.transaction import Transaction
from ark.one.transport import Transport
from ark.one.vote import Vote

'''
# WORK IN PROGRESS
from ark.two.account import Account2
from ark.two.block import Block2
from ark.two.delegate import Delegate2
from ark.two.loader import Loader2
from ark.two.multisignature import MultiSignature2
from ark.two.peer import Peer2
from ark.two.signature import Signature2
from ark.two.transaction import Transaction2
from ark.two.transport import Transport2
from ark.two.vote import Vote2
'''

# TO DO - ADD P2P CALLS


class ArkClient:
    def __init__(self, ip, port, nethash, version, api_version="v1"):
        self.connection(ip, port, nethash, version, api_version)

    def connection(self, ip, port, nethash, version, api_version):
        self.ip = ip
        self.port = port
        self.nethash = nethash
        self.version = version
        self.api_version = api_version

    def accounts(self):
        if self.api_version == "v1":
            return Account(self)
        else:
            return Account2(self)

    def blocks(self):
        if self.api_version == "v1":
            return Block(self)
        else:
            return Block2(self)

    def delegates(self):
        if self.api_version == "v1":
            return Delegate(self)
        else:
            return Delegate2(self)

    def loaders(self):
        if self.api_version == "v1":
            return Loader(self)
        else:
            return Loader2(self)

    def peers(self):
        if self.api_version == "v1":
            return Peer(self)
        else:
            return Peer2(self)

    def signatures(self):
        if self.api_version == "v1":
            return Signature(self)
        else:
            return Signature2(self)

    def transactions(self):
        if self.api_version == "v1":
            return Transaction(self)
        else:
            return Transaction2(self)

    def transport(self):
        if self.api_version == "v1":
            return Transport(self)
        else:
            return Transport2(self)

    def votes(self):
        if self.api_version == "v1":
            return Vote(self)
        else:
            return Vote2(self)
