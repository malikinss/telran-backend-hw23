# tests/test_dictionary.py

import unittest

from src import Dictionary


class TestDictionary(unittest.TestCase):
    """
    Unit tests for the `Dictionary` class.
    """

    def test_cases(self):
        """
        Test multiple scenarios for `Dictionary`.

        This includes:
            - Adding words
            - Case-insensitive duplicate detection
            - Prefix search
            - Case-insensitive prefix matching
            - Preserving original word casing
            - Empty results
        """
        test_data = [
            # Add single word, simple prefix
            (
                ["Apple"],
                "a",
                ["Apple"],
            ),

            # Prefix match, different case
            (
                ["Apple", "application", "Banana"],
                "APP",
                ["Apple", "application"],
            ),

            # Prefix with no matches
            (
                ["Dog", "Cat", "Mouse"],
                "z",
                [],
            ),

            # Preserve original casing
            (
                ["PyThOn", "pythonista"],
                "py",
                ["PyThOn", "pythonista"],
            ),

            # Multiple words, sorted order by lower-case
            (
                ["banana", "Apple", "apricot"],
                "a",
                ["Apple", "apricot"],
            ),

            # Full word prefix
            (
                ["Test", "Testing", "Tester"],
                "test",
                ["Test", "Tester", "Testing"],
            ),

            # Empty dictionary
            (
                [],
                "a",
                [],
            ),
        ]

        for words, prefix, expected in test_data:
            print(
                f"Testing words: {words} with prefix: '{prefix}' "
                f"expecting: {expected}"
            )
            with self.subTest(words=words, prefix=prefix):
                dictionary = Dictionary()
                for word in words:
                    dictionary.add_word(word)

                self.assertEqual(
                    dictionary.get_words_by_prefix(prefix),
                    expected
                )

    def test_add_word_duplicates(self):
        """
        Test that adding duplicate words (case-insensitive) raises ValueError.
        """
        test_data = [
            ("Apple", "Apple"),
            ("Apple", "apple"),
            ("PYTHON", "python"),
            ("Test", "TeSt"),
        ]

        for first, duplicate in test_data:
            print(f"Testing duplicate addition: '{first}' and '{duplicate}'")
            with self.subTest(first=first, duplicate=duplicate):
                dictionary = Dictionary()
                dictionary.add_word(first)

                with self.assertRaises(ValueError):
                    dictionary.add_word(duplicate)


if __name__ == "__main__":
    print("Running Dictionary tests...")
    unittest.main()
