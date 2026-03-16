from typing import Literal, Optional, TypedDict


PayloadData = dict[str, str | int | float]

BlockParameter = Literal["earliest", "latest", "safe", "finalized", "pending"]

EvmBodyPartialParams = TypedDict(
    'EvmBodyPartialParams',
    {
        'jsonrpc': Optional[str],
        'method': str,
        'params': list[PayloadData] | list[PayloadData | BlockParameter | str],
        'id': Optional[int | float],
    },
    total=False,
)
