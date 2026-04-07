from typing import TypedDict

from client.types import PaginatedQuery


class Plugin(TypedDict):
    enabled: bool
    estimateTotalCount: bool
    port: int


class PeerResponse(TypedDict):
    blockNumber: int
    ip: str
    latency: int
    plugins: dict[str, Plugin]
    port: int
    ports: dict[str, int]
    version: str


class PeersQuery(PaginatedQuery, total=False):
    ip: str
    orderBy: str
    version: str
