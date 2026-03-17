from typing import TypedDict

from typing_extensions import NotRequired

from client.types import PaginatedQuery
from client.types.transactions import Transaction


class Block(TypedDict):
    hash: str
    round: int
    number: int
    reward: str
    version: int
    fee: str
    stateRoot: str
    timestamp: str
    transactionsRoot: str
    amount: str
    gasUsed: int
    transactions: list[Transaction]
    payloadSize: int
    parentHash: str
    publicKey: str
    proposer: str
    transactionCount: int


class BlockResponse(TypedDict):
    hash: str
    number: int
    confirmations: int
    amount: str
    fee: str
    reward: str
    total: str
    proposer: str
    publicKey: str
    username: NotRequired[str]
    transactionsRoot: str
    payloadSize: int
    parentHash: str
    signature: str
    timestamp: str
    transactionsCount: int
    version: int


# Functional form required: keys contain dots (e.g. 'height.from') which are not valid Python identifiers
BlocksQuery = TypedDict(
    'BlocksQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'transform': bool,
        'orderBy': str,
        'id': str,
        'number': int,
        'height.from': int,
        'height.to': int,
        'timestamp': int,
        'timestamp.from': int,
        'timestamp.to': int,
    },
    total=False,
)


class BlockTransactionsQuery(PaginatedQuery, total=False):
    orderBy: str
