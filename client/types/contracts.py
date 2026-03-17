from typing import Any, TypedDict


class Contract(TypedDict):
    activeImplementation: str
    address: str
    implementations: list[str]
    proxy: str


ContractResponse = dict[str, Contract]


class ContractAbiResponse(TypedDict):
    abi: list[Any]
