# tests/test_club.py

import unittest

from src import Club, Person


class TestClub(unittest.TestCase):
    """
    Unit tests for the `Club` class.
    """

    def test_cases(self):
        """
        Test multiple scenarios for `Club`.

        Includes:
            - Adding persons and duplicates
            - Sorting by id
            - Sorting by age, id
            - Getting persons by age range
        """
        # Table of persons to add (id, age)
        persons_data = [
            (1, 20),
            (2, 25),
            (3, 30),
            (4, 25),
            (5, 35),
        ]

        club = Club()
        # Add persons
        for pid, age in persons_data:
            club.add_person(Person(id=pid, age=age))

        # Test get_all_sorted_id
        expected_ids_by_id = [1, 2, 3, 4, 5]
        result_ids_by_id = [p.id for p in club.get_all_sorted_id()]
        print("Testing get_all_sorted_id")
        self.assertEqual(result_ids_by_id, expected_ids_by_id)

        # Test get_all_sorted_age_id
        expected_ids_by_age = [1, 2, 4, 3, 5]  # sorted by age, then id
        result_ids_by_age = [p.id for p in club.get_all_sorted_age_id()]
        print("Testing get_all_sorted_age_id")
        self.assertEqual(result_ids_by_age, expected_ids_by_age)

        # Test get_persons_by_age with multiple ranges
        age_test_cases = [
            (20, 25, [1, 2, 4]),
            (25, 30, [2, 4, 3]),
            (30, 35, [3, 5]),
            (0, 100, [1, 2, 4, 3, 5]),
            (40, 50, []),
        ]

        for min_age, max_age, expected_ids in age_test_cases:
            print(
                f"Testing get_persons_by_age with range ({min_age}, {max_age})"
            )
            with self.subTest(min_age=min_age, max_age=max_age):
                result = club.get_persons_by_age(min_age, max_age)
                result_ids = [p.id for p in result]
                self.assertEqual(result_ids, expected_ids)

        # Test duplicate addition raises ValueError
        duplicate_person = Person(id=1, age=50)
        with self.assertRaises(ValueError):
            print("Testing addition of duplicate person with id 1")
            club.add_person(duplicate_person)


if __name__ == "__main__":
    print("Running Club unit tests...")
    unittest.main()
