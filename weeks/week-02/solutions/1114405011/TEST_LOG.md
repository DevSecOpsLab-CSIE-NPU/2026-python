# TEST_LOG

## Task 1 - 錯誤
- Command:
  - `python -m unittest discover -s tests -p "test_task1.py" -v`
- Result:
  - total: 1
  - pass: 0
  - fail: 1
- Note:
  - 當時 `test_task1.py` 還是 `test_todo_red`，確認先失敗再進入實作。

## Task 1 - 通過
- Command:
  - `python -m unittest discover -s tests -p "test_task1.py" -v`
- Result:
  - total: 4
  - pass: 4
  - fail: 0
- Note:
  - 完成 `parse_input/process_numbers/format_output/main` 後通過。

## Task 2 - Red
- Command:
  - `python -m unittest discover -s tests -p "test_task2.py" -v`
- Result:
  - total: 1
  - pass: 0
  - fail: 1
- Note:
  - `test_task2.py` 一開始用 `test_todo_red` 當 TDD 起點。

## Task 2 - Green
- Command:
  - `python -m unittest discover -s tests -p "test_task2.py" -v`
- Result:
  - total: 4
  - pass: 4
  - fail: 0
- Note:
  - 完成多條件排序實作後，全數通過。

## Task 3 - Red
- Command:
  - `python -m unittest discover -s tests -p "test_task3.py" -v`
- Result:
  - total: 1
  - pass: 0
  - fail: 1
- Note:
  - `test_task3.py` 一開始用 `test_todo_red` 當 TDD 起點。

## Task 3 - Green
- Command:
  - `python -m unittest discover -s tests -p "test_task3.py" -v`
- Result:
  - total: 4
  - pass: 4
  - fail: 0
- Note:
  - 完成 `parse_input/summarize/format_output/main` 後通過。

## 最後檢查
- Command:
  - `python -m unittest discover -s tests -p "test_*.py" -v`
- Result:
  - total: 12
  - pass: 12
  - fail: 0

