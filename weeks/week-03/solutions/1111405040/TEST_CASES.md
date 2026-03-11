# Week 03 測試案例說明

## 概述

本作業包含 5 題，共 **19 個測試函式**：

| 題號 | 測試函式數 | 主要測試重點 |
|------|-----------|-------------|
| QUESTION-100 | 5 | cycle length 正確性、區間處理、範例整合 |
| QUESTION-118 | 3 | LOST 判定、scent 機制、官方範例 |
| QUESTION-272 | 3 | 引號替換規則、跨行處理、無引號輸入 |
| QUESTION-299 | 5 | 交換次數計算、多筆測資、邊界輸入 |
| QUESTION-490 | 3 | 旋轉邏輯、不等長輸入、空輸入 |
| **總計** | **19** | |

---

## QUESTION-100：The 3n + 1 Problem

### 測試策略

1. 驗證已知 cycle length（如 `22 -> 16`）。
2. 驗證基底值（`1 -> 1`）。
3. 驗證區間查詢與反向輸入（`10 1`）。
4. 驗證整段範例輸入輸出。

### 5 個測試函式

- `test_cycle_length_22`
- `test_cycle_length_1`
- `test_range_1_10`
- `test_range_reverse_order`
- `test_sample`

---

## QUESTION-118：Mutant Flatworld Explorers

### 測試策略

1. 驗證機器人掉落時會留下 scent。
2. 驗證後續機器人在同點會忽略危險前進指令。
3. 驗證官方範例整體輸出。

### 3 個測試函式

- `test_robot_lost_and_scent`
- `test_uva_sample`
- `test_scent_prevents_second_loss`

---

## QUESTION-272：TEX Quotes

### 測試策略

1. 驗證單行引號交替替換。
2. 驗證多行文字中引號替換。
3. 驗證無引號內容不被修改。

### 3 個測試函式

- `test_single_line`
- `test_multi_line`
- `test_no_quotes`

---

## QUESTION-299：Train Swapping

### 測試策略

1. 驗證已排序與反向排序的交換次數。
2. 驗證一般小型案例。
3. 驗證多筆測資解析與輸出格式。
4. 驗證 `L=0` 邊界情況。

### 5 個測試函式

- `test_sorted`
- `test_reverse`
- `test_single_case`
- `test_multiple_cases`
- `test_zero_length_train`

---

## QUESTION-490：Rotating Sentences

### 測試策略

1. 驗證基本旋轉結果。
2. 驗證不等長行補空白後旋轉。
3. 驗證空輸入輸出。

### 3 個測試函式

- `test_hello_world`
- `test_different_lengths`
- `test_empty_input`

---

## 測試執行

### 執行全部測試

```bash
cd weeks/week-03/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 執行單一測試模組

```bash
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_100 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_118 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_272 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_299 -v
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest tests.test_question_490 -v
```

---

## 測試覆蓋範圍

| 類別 | Q100 | Q118 | Q272 | Q299 | Q490 |
|------|------|------|------|------|------|
| 正常案例 | 2 | 1 | 1 | 2 | 1 |
| 邊界案例 | 2 | 1 | 1 | 2 | 2 |
| 整合案例 | 1 | 1 | 1 | 1 | 0 |
| **小計** | **5** | **3** | **3** | **5** | **3** |

**總計：19 個測試函式**
