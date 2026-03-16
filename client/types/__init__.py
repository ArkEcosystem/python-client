from typing import TypedDict


PaginatedQuery = TypedDict(
    'PaginatedQuery',
    {
        'page': int,
        'limit': int,
        'offset': int,
    },
    total=False,
)
