#!/usr/bin/env python

# WORK IN PROGRESS
from park.one.account import Account
from park.one.block import Block
from park.one.delegate import Delegate
from park.one.loader import Loader
from park.one.multisignature import MultiSignature
from park.one.peer import Peer
from park.one.signature import Signature
from park.one.transaction import Transaction
from park.one.transport import Transport
from park.one.vote import Vote

# WORK IN PROGRESS
from park.two.account import Account2
from park.two.block import Block2
from park.two.delegate import Delegate2
from park.two.loader import Loader2
from park.two.multisignature import MultiSignature2
from park.two.peer import Peer2
from park.two.signature import Signature2
from park.two.transaction import Transaction2
from park.two.transport import Transport2
from park.two.vote import Vote2

# TO DO - ADD P2P CALLS

from park.builder.delegate import DelegateBuilder
from park.builder.multisignature import MultiSignatureBuilder
from park.builder.signature import SignatureBuilder
from park.builder.transaction import TransactionBuilder
from park.builder.vote import VoteBuilder


class Park:
    def __init__(self, ip, port, nethash, version, api_version = "v1"):
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

    def multiSignatures(self):
        if self.api_version == "v1":
            return MultiSignature(self)
        else:
            return MultiSignature2(self)

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

    # WORK IN PROGRESS
    def delegateBuilder(self):
        return DelegateBuilder(self)

    def multiSignatureBuilder(self):
        return MultiSignatureBuilder(self)

    def signatureBuilder(self):
        return SignatureBuilder(self)

    def transactionBuilder(self):
        return TransactionBuilder(self)

    def voteBuilder(self):
        return VoteBuilder(self)
