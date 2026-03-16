from typing import List, TypedDict


TokensQuery = TypedDict(
    'TokensQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
        'ignoreWhitelist': bool,
        'name': str,
        'whitelist': List[str],
    },
    total=False,
)

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
