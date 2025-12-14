from dataclasses import dataclass, field
from typing import Optional


@dataclass(order=True, frozen=True)
class Person:
    """
    Represents a person with unique identifier and optional age.

    Ordering is based only on `id`.
    Equality and hashing are also based only on `id`,
    which allows safe usage inside sets and sorted containers.
    """

    id: int
    age: Optional[int] = field(compare=False)
