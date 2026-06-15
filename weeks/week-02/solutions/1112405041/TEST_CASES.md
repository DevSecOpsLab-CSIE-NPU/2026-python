# TEST_CASES.md - Week 02 測資與驗證紀錄

## Task 1: Sequence Clean
| 序號 | 測試類型 | 輸入 (String) | 預期輸出 (Dedupe / Asc / Desc / Evens) | 結果 | 測試函式 |
|---|---|---|---|---|---|
| 1 | 正常 | `5 3 5 2 9 2 8 3 1` | `5 3 2 9 8 1` / `1 2 2 3 3 5 5 8 9` / `9 8 5 5 3 3 2 2 1` / `2 2 8` | PASS | `test_normal_case` |
| 2 | 邊界 (空) | `` | `""` / `""` / `""` / `""` | PASS | `test_empty_input` |
| 3 | 重複值 | `1 1 1 1` | `1` / `1 1 1 1` / `1 1 1 1` | PASS | `test_all_duplicates` |

## Task 2: Student Ranking
| 序號 | 測試類型 | 輸入 (n, k, data) | 預期輸出 | 結果 | 測試函式 |
|---|---|---|---|---|---|
| 1 | 同分同齡 | `6 3` + 範例資料 | `eva 92 20`, `zoe 92 21`, `bob 88 19` | PASS | `test_normal_ranking` |
| 2 | 同分不同齡 | `3 3` + `a 80 20`, `b 80 19`, `c 80 21` | `b 80 19`, `a 80 20`, `c 80 21` | PASS | `test_age_tie_break` |
| 3 | k 大於 n | `2 5` + `a 90 20`, `b 80 21` | `a 90 20`, `b 80 21` | PASS | `test_k_larger_than_n` |

## Task 3: Log Summary
| 序號 | 測試類型 | 輸入 (m, logs) | 預期輸出 | 結果 | 測試函式 |
|---|---|---|---|---|---|
| 1 | 正常 | `8` + 範例資料 | `bob 4`, `alice 3`, `chris 1` / `top_action: login 3` | PASS | `test_normal_logs` |
| 2 | 邊界 (m=0) | `0` + `[]` | `[]` / `top_action: None 0` | PASS | `test_m_zero` |
| 3 | 次數相同 | `2` + `a x`, `b x` | `a 1`, `b 1` / `top_action: x 2` | PASS | `test_count_tie_break` |
