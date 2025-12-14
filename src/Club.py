# src/Club.py

from sys import maxsize
from typing import List

from sortedcontainers import SortedKeyList, SortedSet

from .Person import Person


class Club:
    """
    Stores and manages a collection of Person objects with multiple sort
    orders.

    Internally keeps:
    - SortedSet: sorted by natural Person ordering (e.g. by id)
    - SortedKeyList: sorted by (age, id)
    """

    def __init__(self) -> None:
        """
        Initialize empty club collections.
        """
        self.__persons_by_id: SortedSet = SortedSet()
        self.__persons_by_age_id: SortedKeyList = SortedKeyList(
            key=lambda p: (p.age, p.id)  # type: ignore[arg-type]
        )

    def add_person(self, person: Person) -> None:
        """
        Add a new person to the club.

        Args:
            person: Person instance to add.

        Raises:
            ValueError: If a person with the same id already exists.
        """
        if person in self.__persons_by_id:
            raise ValueError(f"Person with id {person.id} already exists")

        self.__persons_by_id.add(person)
        self.__persons_by_age_id.add(person)

    def get_all_sorted_id(self) -> List[Person]:
        """
        Return all persons sorted by id.

        Returns:
            List of persons sorted by their natural ordering.
        """
        return list(self.__persons_by_id)

    def get_all_sorted_age_id(self) -> List[Person]:
        """
        Return all persons sorted by age and then id.

        Returns:
            List of persons sorted by (age, id).
        """
        return list(self.__persons_by_age_id)

    def get_persons_by_age(self, min_age: int, max_age: int) -> List[Person]:
        """
        Return persons whose age is within the given range (inclusive).

        Args:
            min_age: Minimum age.
            max_age: Maximum age.

        Returns:
            List of persons with age between min_age and max_age.
        """
        left_person = Person(id=0, age=min_age)
        right_person = Person(id=maxsize, age=max_age)

        left_index = self.__persons_by_age_id.bisect_left(left_person)
        right_index = self.__persons_by_age_id.bisect_right(right_person)

        return list(self.__persons_by_age_id.islice(left_index, right_index))
