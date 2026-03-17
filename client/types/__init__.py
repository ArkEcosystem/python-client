from typing import Generic, TypeVar, TypedDict


T = TypeVar('T')


class PaginatedQuery(TypedDict, total=False):
    page: int
    limit: int
    offset: int


class ResponseMeta(TypedDict):
    totalCountIsEstimate: bool
    count: int
    first: str
    last: str
    next: str | None
    pageCount: int
    previous: str | None
    self: str
    totalCount: int


class Response(TypedDict, Generic[T]):
    data: T


class PaginatedResponse(TypedDict, Generic[T]):
    meta: ResponseMeta
    data: list[T]
