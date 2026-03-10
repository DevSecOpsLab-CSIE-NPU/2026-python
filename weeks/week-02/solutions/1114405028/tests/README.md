# Week 02 Homework Solutions

Student ID: student

## Project Structure

```
solutions/student/
├── task1_sequence_clean.py    # Sequence processing functions
├── task2_student_ranking.py   # Student ranking functions
├── task3_log_summary.py       # Log summarization functions
├── tests/
│   ├── test_task1.py          # Unit tests for Task 1
│   ├── test_task2.py          # Unit tests for Task 2
│   └── test_task3.py          # Unit tests for Task 3
├── TEST_CASES.md              # Test case documentation
├── TEST_LOG.md                # Test execution logs
├── AI_USAGE.md                # AI assistance documentation
└── README.md                  # This file
```

## Tasks Overview

### Task 1: Sequence Clean
Processes a sequence of integers to:
- Remove duplicates while preserving order
- Sort in ascending and descending order
- Extract even numbers in original order

### Task 2: Student Ranking
Ranks students by:
1. Score (descending)
2. Age (ascending)
3. Name (ascending)
Returns top k students.

### Task 3: Log Summary
Analyzes user action logs to:
- Count total actions per user (sorted by count desc, name asc)
- Find the most frequent action

## Running Tests

To run all tests:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

To run specific task tests:
```bash
python -m unittest tests.test_task1 -v
python -m unittest tests.test_task2 -v
python -m unittest tests.test_task3 -v
```

## Implementation Notes

- All functions are pure functions with no side effects
- Used built-in Python features: sorted(), list comprehensions, Counter
- Followed TDD approach: Red → Green → Refactor
- Comprehensive test coverage with normal, edge, and boundary cases