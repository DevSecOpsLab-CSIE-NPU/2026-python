# TEST_LOG

## Red run (failure)

- **執行指令**:
  ```bash
  python3 -m unittest discover -s tests -p "test_*.py" -v
  ```
- **結果**: 12 tests, 2 failures
- **修改紀錄**: 我當時不小心把 Task 1 的 `desc` 排序寫成 `sorted(nums)`（升冪），導致與題目要求（降冪）不符；修正為 `sorted(nums, reverse=True)` 後測試通過。

## Green run (all passing)

- **執行指令**:
  ```bash
  python3 -m unittest discover -s tests -p "test_*.py" -v
  ```
- **結果**: 12 tests, 0 failures
- **修改紀錄**: 修正 Task 1 `desc` 排序為降冪後，所有測試皆通過。
