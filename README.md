# HW23 – Club and Dictionary Classes

## Task Definition

### Class `Club`

-   **Method:** `get_persons_by_age(min_age: int, max_age: int)`
-   **Functionality:** Returns a list of all `Person` objects with `min_age <= age <= max_age`.
-   **Notes:** Internally uses `SortedKeyList` for efficient age-based range queries.
-   **Requirements:**
    -   Adding persons
    -   Retrieving all persons sorted by id
    -   Retrieving all persons sorted by age and id
    -   Unit tests covering all functionality

### Class `Dictionary`

-   **Methods:**
    -   `add_word(word: str)`: Adds a word to the dictionary. Duplicates (case-insensitive) are disallowed.
    -   `get_words_by_prefix(prefix: str)`: Returns all words starting with the given prefix (case-insensitive), preserving original case.
-   **Requirements:**
    -   Use only containers studied in previous sessions
    -   Unit tests covering all functionality

---

## 📝 Description

This homework focuses on **efficient management of collections**:

-   `Club` demonstrates **person storage and retrieval**, supporting multiple sorting orders and efficient range queries.
-   `Dictionary` demonstrates **case-insensitive word management** with prefix lookups while preserving original word casing.

---

## 🎯 Purpose

-   Learn to work with **sorted containers** (`SortedSet`, `SortedKeyList`)
-   Practice **range queries** and sorting by multiple keys
-   Implement **robust case-insensitive word storage**
-   Write **comprehensive unit tests**

---

## 🔍 How It Works

### Club

1. `SortedSet` stores `Person` objects by `id` for unique identification and sorting.
2. `SortedKeyList` stores `Person` objects sorted by `(age, id)` for fast age range queries.
3. `get_persons_by_age(min_age, max_age)` performs a **binary search** using `bisect_left` and `bisect_right` for range retrieval.

### Dictionary

1. Uses `SortedKeyList` to store words sorted case-insensitively.
2. Maintains a `set` for fast duplicate detection (case-insensitive).
3. `get_words_by_prefix(prefix)` finds all words with the given prefix efficiently using `bisect_key_left`.

---

## 📜 Output Example

```py
from src import Club, Person, Dictionary

# Club example
club = Club()
club.add_person(Person(id=1, age=20))
club.add_person(Person(id=2, age=25))
club.add_person(Person(id=3, age=30))

print([p.id for p in club.get_persons_by_age(20, 25)])  # → [1, 2]

# Dictionary example
dictionary = Dictionary()
dictionary.add_word("Apple")
dictionary.add_word("application")
dictionary.add_word("Banana")

print(dictionary.get_words_by_prefix("app"))  # → ['Apple', 'application']
```

---

## 📦 Usage

```py
from src import Club, Person, Dictionary

# Club usage
club = Club()
club.add_person(Person(id=1, age=22))
club.add_person(Person(id=2, age=28))

persons = club.get_persons_by_age(20, 30)

# Dictionary usage
dictionary = Dictionary()
dictionary.add_word("Python")
dictionary.add_word("pytest")

words = dictionary.get_words_by_prefix("py")
```

---

## 🧪 Running Tests

### Using `unittest` CLI

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Using VSCode Test Explorer

1. Open VSCode
2. Ensure `python.testing.unittestEnabled` is `true` in `.vscode/settings.json`
3. Click **Run All Tests** in the Test Explorer

All tests include:

-   Club: adding persons, duplicate detection, sorting, range queries
-   Dictionary: adding words, duplicate detection, prefix search, case-insensitive matching

---

## ✅ Dependencies

-   Python 3.10+
-   `sortedcontainers` library
-   Standard library only (`unittest`, `dataclasses`, `typing`)

---

## 🗂 Project Structure

```
HW23/
├─ .gitignore
├─ .vscode/
│  ├─ launch.json
│  ├─ settings.json
│  └─ tasks.json
├─ src/
│  ├─ __init__.py
│  ├─ Club.py
│  ├─ Person.py
│  └─ Dictionary.py
└─ tests/
   ├─ __init__.py
   ├─ test_club.py
   └─ test_dictionary.py
```

---

## 📊 Project Status

**Status:** ✅ Completed  
All tests pass successfully, classes are **robust, efficient, and ready for use**.

---

## 📄 License

MIT License

---

## 🧮 Conclusion

This homework demonstrates:

-   Efficient management of persons with multiple sorting criteria
-   Case-insensitive word storage and prefix lookup
-   Usage of `SortedSet` and `SortedKeyList` for performance
-   Comprehensive unit testing and edge case handling

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
© 2025 All rights reserved.
