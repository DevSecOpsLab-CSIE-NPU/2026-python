# Test Cases

## Case 1: Normal input for Task 1
- Input: `5 3 5 2 9 2 8 3 1`
- Expected output: dedupe `5 3 2 9 8 1`, asc `1 2 2 3 3 5 5 8 9`, desc `9 8 5 5 3 3 2 2 1`, evens `2 2 8`
- Actual output: same as expected
- Result: PASS
- Test function: `tests/test_task1.py::test_clean_sequence_example_case`
- Key fix from fail to pass: kept first-appearance order during dedupe.

## Case 2: Boundary empty input for Task 1
- Input: `` (empty list)
- Expected output: all four sequences are empty
- Actual output: all four sequences are empty
- Result: PASS
- Test function: `tests/test_task1.py::test_clean_sequence_empty_input`
- Key fix from fail to pass: handled empty tokens safely before conversion.

## Case 3: Tie sorting for Task 2
- Input: students with same score and age: `(tom,90,20)`, `(amy,90,20)`
- Expected output: `amy` before `tom`
- Actual output: `amy` before `tom`
- Result: PASS
- Test function: `tests/test_task2.py::test_rank_students_tie_break_by_name`
- Key fix from fail to pass: added `name` as the third key in sorting.

## Case 4: Official sample for Task 3
- Input: 8 log records from homework statement
- Expected output: `bob 4`, `alice 3`, `chris 1`, `top_action: login 3`
- Actual output: same as expected
- Result: PASS
- Test function: `tests/test_task3.py::test_summarize_logs_example_case`
- Key fix from fail to pass: combined user/action counting and explicit sorting.

## Case 5: Counterexample tie for top action in Task 3
- Input: records `[(amy, view), (bob, login)]`
- Expected output: top action should be lexical smallest among ties => `login 1`
- Actual output: `login 1`
- Result: PASS
- Test function: `tests/test_task3.py::test_summarize_logs_action_tie_break_by_action_name`
- Key fix from fail to pass: deterministic tie-break with `min(action)`.
