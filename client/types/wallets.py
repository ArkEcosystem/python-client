from typing import List, TypedDict


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

WalletTokensForQuery = TypedDict(
    'WalletTokensForQuery',
    {
        'addresses': List[str],
        'ignoreWhitelist': bool,
        'minBalance': int,
        'name': str,
        'whitelist': List[str],
    },
    total=False,
)

WalletTokensQuery = TypedDict(
    'WalletTokensQuery',
    {
        'addresses': List[str],
        'ignoreWhitelist': bool,
        'page': int,
        'limit': int,
        'minBalance': int,
        'whitelist': List[str],
    },
    total=False,
)
