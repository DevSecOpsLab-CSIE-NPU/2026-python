# Week 02 Test Cases

## Case 1: 一般情況 - Task 1

- 輸入：`5 3 5 2 9 2 8 3 1`
- 預期輸出：
  - `dedupe: 5 3 2 9 8 1`
  - `asc: 1 2 2 3 3 5 5 8 9`
  - `desc: 9 8 5 5 3 3 2 2 1`
  - `evens: 2 2 8`
- 實際輸出：
  - `dedupe: 5 3 2 9 8 1`
  - `asc: 1 2 2 3 3 5 5 8 9`
  - `desc: 9 8 5 5 3 3 2 2 1`
  - `evens: 2 2 8`
- 是否通過：PASS
- 對應測試：`tests/test_task1.py::test_solve_formats_sample_output`
- 關鍵修改點：將去重改為保留第一次出現順序的掃描法。

## Case 2: 邊界情況 - Task 3

- 輸入：`0`
- 預期輸出：`top_action: none 0`
- 實際輸出：`top_action: none 0`
- 是否通過：PASS
- 對應測試：`tests/test_task3.py::test_solve_handles_zero_events`
- 關鍵修改點：補上空輸入分支，避免 Counter 取值失敗。

## Case 3: 同分排序 - Task 2

- 輸入：
  - `6 3`
  - `amy 88 20`
  - `bob 88 19`
  - `zoe 92 21`
  - `ian 88 19`
  - `leo 75 20`
  - `eva 92 20`
- 預期輸出：
  - `eva 92 20`
  - `zoe 92 21`
  - `bob 88 19`
- 實際輸出：
  - `eva 92 20`
  - `zoe 92 21`
  - `bob 88 19`
- 是否通過：PASS
- 對應測試：`tests/test_task2.py::test_solve_outputs_top_k_sample`
- 關鍵修改點：排序 key 改成 score 反向、age 正向、name 正向。

## Case 4: 反例 - Task 1

- 輸入：`1 1 1 1`
- 預期輸出：
  - `dedupe: 1`
  - `asc: 1 1 1 1`
  - `desc: 1 1 1 1`
  - `evens:`
- 實際輸出：
  - `dedupe: 1`
  - `asc: 1 1 1 1`
  - `desc: 1 1 1 1`
  - `evens:`
- 是否通過：PASS
- 對應測試：`tests/test_task1.py::test_dedupe_preserves_first_occurrence`
- 關鍵修改點：確認去重不能用 `set` 直接輸出。

## Case 5: 最容易測錯 - Task 3

- 輸入：
  - `8`
  - `alice login`
  - `bob login`
  - `alice view`
  - `alice logout`
  - `bob view`
  - `bob view`
  - `chris login`
  - `bob logout`
- 預期輸出：
  - `bob 4`
  - `alice 3`
  - `chris 1`
  - `top_action: login 3`
- 實際輸出：
  - `bob 4`
  - `alice 3`
  - `chris 1`
  - `top_action: login 3`
- 是否通過：PASS
- 對應測試：`tests/test_task3.py::test_solve_handles_sample_input`
- 關鍵修改點：user 總數排序需先比總數，再比名稱。

## Case 6: 重複值 - Task 2

- 輸入：
  - `4 2`
  - `ann 90 20`
  - `amy 90 20`
  - `bob 90 19`
  - `zoe 85 21`
- 預期輸出：
  - `bob 90 19`
  - `amy 90 20`
- 實際輸出：
  - `bob 90 19`
  - `amy 90 20`
- 是否通過：PASS
- 對應測試：`tests/test_task2.py::test_rank_students_sorts_by_score_age_name`
- 關鍵修改點：同分同齡時再用姓名字母序穩定決定順序。
