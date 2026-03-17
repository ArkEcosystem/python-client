from typing import List, TypedDict

from client.types import PaginatedQuery


# Functional form required: keys include 'from' which is a reserved Python keyword
Transaction = TypedDict(
    'Transaction',
    {
        'hash': str,
        'fee': str,
        'type': int,
        'nonce': str,
        'value': str,
        'network': int,
        'version': int,
        'sequence': int,
        'signature': str,
        'typeGroup': int,
        'expiration': int,
        'to': str,
        'senderPublicKey': str,
        'from': str,
    },
)


class TransactionReceipt(TypedDict):
    gasRefunded: int
    gasUsed: int
    success: bool


# Functional form required: keys include 'from' which is a reserved Python keyword
TransactionResponse = TypedDict(
    'TransactionResponse',
    {
        'hash': str,
        'value': str,
        'blockNumber': str,
        'confirmations': int,
        'data': str,
        'gas': str,
        'gasPrice': str,
        'nonce': str,
        'to': str,
        'from': str,
        'senderPublicKey': str,
        'signature': str,
        'timestamp': str,
        'receipt': TransactionReceipt,
    },
)


class TransactionConfigurationTransactionPool(TypedDict):
    maxTransactionAge: int
    maxTransactionBytes: int
    maxTransactionsInPool: int
    maxTransactionsPerRequest: int
    maxTransactionsPerSender: int


class TransactionConfigurationCore(TypedDict):
    version: str


class TransactionConfigurationResponse(TypedDict):
    core: TransactionConfigurationCore
    height: int
    transactionPool: TransactionConfigurationTransactionPool


class TransactionCreateResponse(TypedDict):
    accept: list[int]
    broadcast: list[int]
    excess: list[int]
    invalid: list[int]


# Functional form required: keys include 'from' which is a reserved Python keyword
TransactionsQuery = TypedDict(
    'TransactionsQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'address': str,
        'asset': str,
        'blockHash': str,
        'from': str,
        'gasPrice': int,
        'hash': str,
        'nonce': int,
        'senderId': str,
        'senderPublicKey': str,
        'timestamp': int,
        'to': str,
        'transactionIndex': int,
        'value': int,
        'fullReceipt': bool,
        'includeTokens': bool,
        'orderBy': str,
    },
    total=False,
)


class UnconfirmedTransactionsQuery(PaginatedQuery, total=False):
    orderBy: str


class TransactionGetQuery(TypedDict, total=False):
    fullReceipt: bool
    includeTokens: bool


class TransactionCreateParams(TypedDict):
    transactions: List[str]
