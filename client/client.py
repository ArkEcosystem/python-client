from client.connection import Connection
from client.api.api_nodes import ApiNodes
from client.api.blockchain import Blockchain
from client.api.blocks import Blocks
from client.api.commits import Commits
from client.api.delegates import Delegates
from client.api.node import Node
from client.api.peers import Peers
from client.api.rounds import Rounds
from client.api.transactions import Transactions
from client.api.votes import Votes
from client.api.wallets import Wallets

class ArkClient(object):

    def __init__(self, hostname):
        """
        :param string hostname: Node hostname. Examples: `http://127.0.0.1:4002` or
            `http://my.domain.io/api/`. This is to allow people to server the api
            on whatever url they want.
        """
        self.connection = Connection(hostname)

    @property
    def api_nodes(self):
        """
        :return: Nodes API
        :rtype: client.api.nodes.Nodes
        """
        return ApiNodes(self.connection)

    @property
    def blockchain(self):
        """
        :return: Blockchain API
        :rtype: client.api.blockchain.Blockchain
        """
        return Blockchain(self.connection)

    @property
    def blocks(self):
        """
        :return: Blocks API
        :rtype: client.api.blocks.Blocks
        """
        return Blocks(self.connection)

    @property
    def commits(self):
        """
        :return: Commits API
        :rtype: client.api.commits.Commits
        """
        return Commits(self.connection)

    @property
    def delegates(self):
        """
        :return: Delegates API
        :rtype: client.api.delegates.Delegates
        """
        return Delegates(self.connection)

    @property
    def node(self):
        """
        :return: Node API
        :rtype: client.api.node.Node
        """
        return Node(self.connection)

    @property
    def peers(self):
        """
        :return: Peers API
        :rtype: client.api.peers.Peers
        """
        return Peers(self.connection)

    @property
    def rounds(self):
        """
        :return: Rounds API
        :rtype: client.api.rounds.Rounds
        """
        return Rounds(self.connection)

    @property
    def transactions(self):
        """
        :return: Transactions API
        :rtype: client.api.transactions.Transactions
        """
        return Transactions(self.connection)

    @property
    def votes(self):
        """
        :return: Votes API
        :rtype: client.api.votes.Votes
        """
        return Votes(self.connection)

    @property
    def wallets(self):
        """
        :return: Wallets API
        :rtype: client.api.wallets.Wallets
        """
        return Wallets(self.connection)
