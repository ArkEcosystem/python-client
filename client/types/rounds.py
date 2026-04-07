from typing import TypedDict


class RoundResponse(TypedDict):
    round: str
    roundHeight: str
    validators: list[str]
    votes: list[str]
