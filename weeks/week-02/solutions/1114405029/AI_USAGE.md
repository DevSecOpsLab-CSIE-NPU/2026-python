# AI_USAGE.md - Week 02

## Questions Asked to AI

1. How to remove duplicates from a list while preserving the original order in Python?
2. How to sort a list of dictionaries using multiple conditions with `sorted()` and `key`?
3. How to count occurrences of user actions efficiently in Python?
4. How to structure unit tests using Python’s `unittest` framework?
5. How to handle edge cases such as empty input when processing sequences?

---

## AI Suggestions Adopted

* Used a **set together with a list** to remove duplicates while keeping the first occurrence order in Task1.
* Used **`sorted()` with a lambda key** to implement multi-condition sorting in Task2 (`score`, `age`, `name`).
* Used **`defaultdict` and `Counter`** to count user events and action frequency in Task3.
* Used the **`unittest` framework** to design multiple test cases for normal cases, edge cases, and tie-breaking situations.

---

## AI Suggestions Rejected

* AI suggested directly using `set(numbers)` to remove duplicates.
  This approach was rejected because it does **not preserve the original order** of elements, which violates the assignment requirement.

---

## AI Misleading Case

During development of Task1, AI initially suggested using:

```python
list(set(numbers))
```

to remove duplicates. However, this method changes the order of elements in the list.

To fix this issue, I implemented a solution that tracks seen elements using a set while iterating through the list, ensuring that duplicates are removed while the original order of first occurrence is preserved.
