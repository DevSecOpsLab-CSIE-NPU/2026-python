# Week 02 Python Homework

## Completed Tasks

### Task 1: Sequence Clean

Removes duplicate numbers from a sequence while preserving the first occurrence order.
This is implemented by iterating through the list and tracking previously seen values using a set.

### Task 2: Student Ranking

Sorts student records using multiple sorting rules:

1. Score in descending order
2. Age in ascending order
3. Name in alphabetical order

Implemented using:

```
sorted(students, key=lambda x: (-x["score"], x["age"], x["name"]))
```

### Task 3: Log Summary

Counts the number of actions performed by each user and identifies the most common action.
This is implemented using `defaultdict` to count user events and `Counter` to track action frequencies.

---

## Python Version

Python 3.8 or higher

---

## Running the Programs

Execute each task script from the command line:

```bash
python task1_sequence_clean.py
python task2_student_ranking.py
python task3_log_summary.py
```

---

## Running Tests

Run all tests using Python unittest:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## Data Structures Used

* **Lists**: Used to store and iterate through sequences of numbers and records.
* **Sets**: Used to track previously seen numbers efficiently when removing duplicates.
* **Dictionaries**: Used to store structured student records.
* **Counter / defaultdict**: Used to simplify frequency counting for user actions.

---

## Bug Encountered & Fix

An early implementation of student ranking sorted scores incorrectly because the sorting rule only used `reverse=True`.

The issue was fixed by implementing multi-condition sorting:

```
sorted(students, key=lambda x: (-x["score"], x["age"], x["name"]))
```

This ensures correct ordering by score, age, and name.

---

## Red → Green → Refactor Summary

### Task 1

Initial tests failed because duplicate removal did not preserve the first occurrence order.
This was fixed by using a set to track seen elements while iterating through the list.
After tests passed, the code was refactored to separate the logic into a helper function.

### Task 2

Initial tests failed because sorting only considered score.
This was fixed by implementing multi-condition sorting using `(-score, age, name)`.
Afterward, the ranking logic was refactored into a reusable function.

### Task 3

Initial tests failed due to incorrect counting logic for user actions.
This was corrected by using `defaultdict` for user counts and `Counter` for action frequency.
The code was then refactored to keep the summary logic modular and testable.
