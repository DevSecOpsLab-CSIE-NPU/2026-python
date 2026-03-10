# TEST_CASES

## 1. 一般情況
- 輸入: Task1 `5 3 5 2 9 2 8 3 1`
- 預期: dedupe 5 3 2 9 8 1；asc 1 2 2 3 3 5 5 8 9；desc 9 8 5 5 3 3 2 2 1；evens 2 2 8
- 實際: 與預期一致
- PASS
- 對應: `tests/test_task1.py::test_normal_case`
- 關鍵修正: 實作函式與格式輸出。

## 2. 邊界情況
- 輸入: Task2 `0 0`（無學生）
- 預期: 空列表
- 實際: 空列表
- PASS
- 對應: `tests/test_task2.py::test_empty_students`
- 關鍵修正: 直接回傳 `[]` 並防止 IndexError。

## 3. 重複值 / 同分排序
- 輸入: Task2 `4 4 \na 90 19 \nb 90 19 \nx 90 20 \nc 90 20`
- 預期: `a b c x`
- 實際: `a b c x`
- PASS
- 對應: `tests/test_task2.py::test_tie_break_age_name`
- 關鍵修正: key 排序依據（score desc, age asc, name asc）。

## 4. 反例（容易寫錯）
- 輸入: Task3 `4\nu1 a\nu2 b\nu1 b\nu3 a`
- 預期: user 數 `u1 2,u2 1,u3 1`; top action `a 2`（action tie 取字母序）
- 實際: 同上
- PASS
- 對應: `tests/test_task3.py::test_tie_top_action`
- 關鍵修正: 同頻率 action 取最小字母。

## 5. 最能測出錯誤的一組
- 輸入: Task1 `0 -1 -1 4 4`
- 預期: dedupe 0 -1 4；asc -1 -1 0 4 4；desc 4 4 0 -1 -1；evens 0 4 4
- 實際: 同上
- PASS
- 對應: `tests/test_task1.py::test_negative_and_zero`
- 關鍵修正: 確認去重維持第一次出現且支援負數。
