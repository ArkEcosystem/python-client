from ark.one.account import Account
from ark.one.block import Block
from ark.one.delegate import Delegate
from ark.one.loader import Loader
from ark.one.peer import Peer
from ark.one.signature import Signature
from ark.one.transaction import Transaction
from ark.one.transport import Transport
from ark.one.vote import Vote

from ark.two.wallet import Wallet
from ark.two.block import Block2
from ark.two.delegate import Delegate2
from ark.two.node import Node
from ark.two.peer import Peer2
from ark.two.transaction import Transaction2
from ark.two.p2p import P2p
from ark.two.vote import Vote2

class ArkClient:
    def __init__(self, ip, port, nethash, version, api_version='v1'):
        self.connection(ip, port, nethash, version, api_version)

    def connection(self, ip, port, nethash, version, api_version):
        self.ip = ip
        self.port = port
        self.nethash = nethash
        self.version = version
        self.api_version = api_version

    def accounts(self):
        if self.api_version == 'v1':
            return Account(self)
        else:
            return Wallet(self)

    def blocks(self):
        if self.api_version == 'v1':
            return Block(self)
        else:
            return Block2(self)

    def delegates(self):
        if self.api_version == 'v1':
            return Delegate(self)
        else:
            return Delegate2(self)

    def loaders(self):
        if self.api_version == 'v1':
            return Loader(self)
        else:
            return Node(self)

    def peers(self):
        if self.api_version == 'v1':
            return Peer(self)
        else:
            return Peer2(self)

    def signatures(self):
        if self.api_version == 'v1':
            return Signature(self)

    def transactions(self):
        if self.api_version == 'v1':
            return Transaction(self)
        else:
            return Transaction2(self)

    def transport(self):
        self.port = self.switchConfig("p2p", self.nethash)

        if self.api_version == 'v1':
            return Transport(self)
        else:
            return P2p(self)

    def votes(self):
        if self.api_version == 'v1':
            return Vote(self)
        else:
            return Vote2(self)

    def switchConfig(self, service, nethash):
        switch = {
            '6e84d08bd299ed97c212c886c98a57e36545c8f5d645ca7eeae63a8bd62d8988': {
                "public": 0000,
                "p2p": 0000,
                "webhook": 0000},  # ark mainnet
            '578e820911f24e039733b45e4882b73e301f813a0d2c31330dafda84534ffa23': {
                "public": 4003,
                "p2p": 4002,
                "webhook": 4004}  # ark devnet
        }

        return switch[nethash][service]