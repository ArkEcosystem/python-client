from typing import Generic, List, TypeVar, TypedDict

from client.types import PaginatedQuery, ResponseMeta

T = TypeVar('T')


class TokenResponse(TypedDict):
    address: str
    decimals: int
    deploymentHash: str
    name: str
    totalSupply: str


class TokenAddressesResponse(TypedDict):
    addresses: dict[str, str]
    decimals: int
    name: str
    supply: str
    symbol: str
    token: str


class TokenActionToken(TypedDict):
    address: str
    name: str
    symbol: str
    decimals: int


# Functional form required: keys include 'from' which is a reserved Python keyword
TokenActionsResponse = TypedDict(
    'TokenActionsResponse',
    {
        'transactionHash': str,
        'from': str,
        'to': str,
        'value': str,
        'functionSig': str,
        'blockNumber': str,
        'timestamp': str,
        'token': TokenActionToken,
    },
)


class TokenWhitelistResponse(TypedDict):
    address: str
    comment: str
    createdAt: str


class TokenAddressHoldersResponse(TypedDict):
    address: str
    balance: int
    tokenAddress: str


class TokenPaginatedResponseData(Generic[T]):
    data: T


class TokenPaginatedResponseResults(Generic[T]):
    meta: ResponseMeta
    results: list[T]


class TokensQuery(PaginatedQuery, total=False):
    ignoreWhitelist: bool
    name: str
    whitelist: List[str]


# Functional form required: keys include 'from' which is a reserved Python keyword
TokenLookupQuery = TypedDict(
    'TokenLookupQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'from': str,
        'to': str,
        'transactionHash': str,
    },
    total=False,
)

# Functional form required: keys include 'from' which is a reserved Python keyword
TokenTransfersQuery = TypedDict(
    'TokenTransfersQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'from': str,
        'to': str,
        'transactionHash': str,
        'addresses': List[str],
        'ignoreWhitelist': bool,
        'whitelist': List[str],
    },
    total=False,
)

# Functional form required: keys include 'from' which is a reserved Python keyword
TokenApprovalsQuery = TypedDict(
    'TokenApprovalsQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'from': str,
        'to': str,
        'transactionHash': str,
        'addresses': List[str],
        'whitelist': List[str],
    },
    total=False,
)
