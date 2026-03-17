from typing import Literal, TypedDict


PayloadData = dict[str, str | int | float]

BlockParameter = Literal["earliest", "latest", "safe", "finalized", "pending"]


class EvmBodyPartialParams(TypedDict, total=False):
    jsonrpc: str
    method: str
    params: list[PayloadData] | list[PayloadData | BlockParameter | str]
    id: int | float | None
