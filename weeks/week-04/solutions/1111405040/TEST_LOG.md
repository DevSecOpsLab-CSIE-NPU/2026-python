# Week 04 測試執行日誌

## 執行環境

- Python 版本：3.10
- 測試框架：unittest
- 測試目錄：`weeks/week-04/solutions/1111405040/tests/`
- 測試指令：

```powershell
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

---

## 第一次執行（失敗）

### 執行結果摘要

- 測試總數：24
- 通過數：22
- 失敗數：2

### 錯誤重點

- `test_count_bits_for_ten`
- `test_solve_multiple_cases`

### 原因分析

- 錯誤集中在 `question_10019.py` 的測試預期值。
- 我原本把輸入 `10` 的第二個答案寫成 `2`。
- 但題目第二個答案是將輸入字串視為十六進位整數，因此 `10` 應解讀為 `0x10 = 16`，bit count 應為 `1`。

### 從失敗到下一步的修改

1. 將 `tests/test_question_10019.py` 中 `count_bits(10)` 的預期值改為 `(2, 1)`。
2. 同步修正整體輸出測試的第一行預期結果為 `2 1`。

---

## 第二次執行（全通過）

### 執行結果摘要

- 測試總數：24
- 通過數：24
- 失敗數：0

### 結果

- 五題的核心演算法與輸出格式皆符合目前測試案例。
- `948` 的 greedy 轉換、`10008` 的排序規則、`10019` 的雙 bit count、`10035` 的進位計算、`10038` 的 Jolly 判定皆通過。

---

## Refactor 紀錄

在確認測試通過後，保留以下設計做為可讀性整理：

1. `question_948.py` 將 Fibonacci 數列建立獨立成 `build_fib_numbers()`。
2. `question_10019.py` 將 bit count 行為拆成 `popcount()` 與 `count_bits()`。
3. `question_10035.py` 分離 `count_carries()` 與 `format_carry_result()`，讓測試可以分開驗證計算與輸出格式。
