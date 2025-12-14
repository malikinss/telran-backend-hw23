# src/Dictionary.py

from sortedcontainers import SortedKeyList
from typing import List


class Dictionary:
    """
    Stores unique words and provides prefix-based lookup (case-insensitive).
    """

    def __init__(self) -> None:
        """
        Initialize empty dictionary.
        """
        self._words: SortedKeyList = SortedKeyList(
            key=lambda word: word.lower()  # type: ignore[arg-type]
        )
        self._lookup: set[str] = set()

    def add_word(self, word: str) -> None:
        """
        Add a new word to the dictionary.

        Words are stored case-insensitively, but the original casing is
        preserved.

        Args:
            word: Word to add.

        Raises:
            ValueError: If the word already exists (case-insensitive).
        """
        normalized = word.lower()

        if normalized in self._lookup:
            raise ValueError(f"Word '{word}' already exists.")

        self._words.add(word)
        self._lookup.add(normalized)

    def get_words_by_prefix(self, prefix: str) -> List[str]:
        """
        Return all words that start with the given prefix (case-insensitive).

        Args:
            prefix: Prefix to search for.

        Returns:
            List of matching words in sorted order.
        """
        normalized = prefix.lower()
        start_index = self._words.bisect_key_left(normalized)

        result: List[str] = []
        for word in self._words[start_index:]:
            if word.lower().startswith(normalized):
                result.append(word)
            else:
                break

        return result
