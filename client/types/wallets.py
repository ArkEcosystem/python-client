from typing import List, TypedDict

from client.types import PaginatedQuery


class ValidatorLastBlock(TypedDict):
    id: str
    height: int
    timestamp: int


class WalletAttributes(TypedDict, total=False):
    username: str
    vote: str
    validatorRank: int
    validatorApproval: int
    validatorResigned: bool
    validatorLastBlock: ValidatorLastBlock
    validatorPublicKey: str
    validatorForgedFees: str
    validatorForgedTotal: str
    validatorVoteBalance: str
    validatorVotersCount: int
    validatorForgedRewards: str
    validatorProducedBlocks: int


class WalletResponse(TypedDict):
    address: str
    publicKey: str
    balance: str
    nonce: str
    attributes: WalletAttributes
    updated_at: str
    tokenCount: int


# Functional form required: keys contain dots (e.g. 'balance.from') which are not valid Python identifiers
WalletsQuery = TypedDict(
    'WalletsQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'address': str,
        'publicKey': str,
        'balance': int,
        'balance.from': int,
        'balance.to': int,
        'nonce': int,
        'nonce.from': int,
        'nonce.to': int,
        'attributes': str,
        'orderBy': str,
    },
    total=False,
)


class WalletTokensForQuery(TypedDict, total=False):
    ignoreWhitelist: bool
    minBalance: int
    name: str
    whitelist: List[str]


class WalletTokensQuery(PaginatedQuery, total=False):
    addresses: List[str]
    ignoreWhitelist: bool
    minBalance: int
    whitelist: List[str]
