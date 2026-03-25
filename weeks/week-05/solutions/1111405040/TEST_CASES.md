# Week 05 測試案例說明

## 概述

- 測試檔：5 份
- 測試函式：20 個
- 覆蓋面向：
  1. 基本題意
  2. 排序與中位數
  3. 週末排除規則
  4. EOF 與多組輸入
  5. 機率與區間統計

---

## 測資清單

| 編號 | 題號 | 輸入 | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|------|------|------|----------|----------|-----------|--------------|
| 1 | 10041 | `[2, 4, 6]` | 最小距離和為 `4` | `4` | PASS | `test_min_total_distance_basic` |
| 2 | 10041 | `[2, 4, 6, 8]` | 最小距離和為 `8` | `8` | PASS | `test_min_total_distance_even_count` |
| 3 | 10041 | `[10, 2, 4, 6]` | 可處理未排序輸入，距離和 `10` | `10` | PASS | `test_min_total_distance_unsorted_input` |
| 4 | 10041 | `2 / (2 2 4) / (3 2 4 6)` | 輸出 `2`、`4` | `2`、`4` | PASS | `test_solve_multiple_cases` |
| 5 | 10050 | `14, [3]` | 罷工日為 `3` 天 | `3` | PASS | `test_single_party` |
| 6 | 10050 | `14, [3, 4]` | 罷工日為 `5` 天 | `5` | PASS | `test_multiple_parties` |
| 7 | 10050 | `7, [1]` | 扣掉週五週六後為 `5` 天 | `5` | PASS | `test_ignore_friday_and_saturday` |
| 8 | 10050 | 兩組測資 | 輸出 `5`、`5` | `5`、`5` | PASS | `test_solve_multiple_cases` |
| 9 | 10055 | `10, 12` | 絕對差 `2` | `2` | PASS | `test_absolute_difference_basic` |
| 10 | 10055 | `10000000000, 1` | 絕對差 `9999999999` | `9999999999` | PASS | `test_absolute_difference_large_numbers` |
| 11 | 10055 | `5, 5` | 絕對差 `0` | `0` | PASS | `test_absolute_difference_same_number` |
| 12 | 10055 | 三行配對輸入 | 逐行輸出三個差值 | 與預期相同 | PASS | `test_solve_multiple_lines` |
| 13 | 10056 | `p = 0` | 獲勝機率為 `0.0` | `0.0` | PASS | `test_probability_zero_when_p_is_zero` |
| 14 | 10056 | `n = 1, p = 0.5, i = 1` | 最終獲勝機率為 `1.0` | `1.0` | PASS | `test_single_player_eventually_wins` |
| 15 | 10056 | `n = 3, p = 0.5, i = 2` | 機率約 `0.285714...` | 約 `0.285714...` | PASS | `test_general_case` |
| 16 | 10056 | 三組測資 | 輸出 `0.0000`、`1.0000`、`0.2857` | 與預期相同 | PASS | `test_solve_format` |
| 17 | 10057 | `[1, 2, 3]` | `(2, 1, 1)` | `(2, 1, 1)` | PASS | `test_odd_count_numbers` |
| 18 | 10057 | `[1, 2, 2, 4]` | `(2, 2, 1)` | `(2, 2, 1)` | PASS | `test_even_count_same_middle_value` |
| 19 | 10057 | `[1, 2, 4, 6]` | `(2, 2, 3)` | `(2, 2, 3)` | PASS | `test_even_count_middle_range` |
| 20 | 10057 | 兩組測資 | 輸出 `2 1 1`、`2 2 3` | 與預期相同 | PASS | `test_solve_multiple_cases` |

---

## 測試指令

```powershell
cd weeks/week-05/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```
