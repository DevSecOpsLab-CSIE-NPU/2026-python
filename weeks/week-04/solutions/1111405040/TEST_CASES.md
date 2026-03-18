# Week 04 測試案例說明

## 概述

- 測試檔：5 份
- 測試函式：24 個
- 覆蓋面向：
  1. 題目輸出格式
  2. 邊界條件
  3. 核心演算法正確性
  4. 特殊輸入處理

---

## 測資清單

| 編號 | 題號 | 輸入 | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|------|------|------|----------|----------|-----------|--------------|
| 1 | 948 | `1` | Fibonaccimal 為 `1` | `1` | PASS | `test_one_is_single_one` |
| 2 | 948 | `2` | Fibonaccimal 為 `10` | `10` | PASS | `test_two_is_ten` |
| 3 | 948 | `10` | Fibonaccimal 為 `10010` | `10010` | PASS | `test_ten_is_10010` |
| 4 | 948 | `3 / 1 2 10` | 三筆格式化輸出 | 與預期相同 | PASS | `test_solve_multiple_cases` |
| 5 | 10008 | `AaBb` | `A=2, B=2` | `A=2, B=2` | PASS | `test_count_letters_ignores_case` |
| 6 | 10008 | `A1! a?` | 忽略非字母，只統計 `A=2` | `A=2` | PASS | `test_count_letters_ignores_non_letters` |
| 7 | 10008 | `CCAAAB` | 依頻率與字母排序 | `A 3, C 2, B 1` | PASS | `test_sort_by_frequency_then_alphabet` |
| 8 | 10008 | 三行文章輸入 | 依題目格式輸出統計結果 | 與預期相同 | PASS | `test_solve_matches_expected_format` |
| 9 | 10019 | `5` | bit count 為 `2` | `2` | PASS | `test_popcount_basic_value` |
| 10 | 10019 | `26` | 十進位/十六進位 bit count 為 `(3, 3)` | `(3, 3)` | PASS | `test_count_bits_for_twenty_six` |
| 11 | 10019 | `10` | 十進位/十六進位 bit count 為 `(2, 1)` | `(2, 1)` | PASS | `test_count_bits_for_ten` |
| 12 | 10019 | `265` | 十進位/十六進位 bit count 為 `(3, 5)` | `(3, 5)` | PASS | `test_count_bits_for_two_hundred_sixty_five` |
| 13 | 10019 | `3 / 10 26 265` | 三筆輸出 `2 1 / 3 3 / 3 5` | 與預期相同 | PASS | `test_solve_multiple_cases` |
| 14 | 10035 | `123 + 456` | 無進位 | `0` 次進位 | PASS | `test_no_carry` |
| 15 | 10035 | `555 + 555` | 三次進位 | `3` 次進位 | PASS | `test_single_carry` |
| 16 | 10035 | `123 + 594` | 一次進位 | `1` 次進位 | PASS | `test_multiple_carries` |
| 17 | 10035 | 進位數 `2` | 格式化為 `2 carry operations.` | 與預期相同 | PASS | `test_format_carry_result` |
| 18 | 10035 | 含 `0 0` 終止輸入 | 在終止條件前停止處理 | 與預期相同 | PASS | `test_solve_stops_at_zero_zero` |
| 19 | 10038 | `[1]` | 單一元素視為 Jolly | `Jolly` | PASS | `test_single_value_is_jolly` |
| 20 | 10038 | `[1, 4, 2, 3]` | 為 Jolly | `Jolly` | PASS | `test_known_jolly_sequence` |
| 21 | 10038 | `[1, 4, 2, -1, 6]` | 非 Jolly | `Not jolly` | PASS | `test_known_not_jolly_sequence` |
| 22 | 10038 | `[1, 2, 3, 4]` | 差值重複，非 Jolly | `Not jolly` | PASS | `test_repeated_difference_is_not_jolly` |
| 23 | 10038 | 兩行輸入 | 分別輸出 `Jolly` 與 `Not jolly` | 與預期相同 | PASS | `test_solve_multiple_lines` |
| 24 | 948 | 上限 `10` | Fibonacci 清單為 `[1, 2, 3, 5, 8]` | 與預期相同 | PASS | `test_build_fib_numbers_up_to_ten` |

---

## 測試指令

```powershell
cd weeks/week-04/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```
