# Data Cleaning

## 題目說明

本題為 Week 18 第一題 Data Cleaning。程式會讀取多組整數陣列，對每一組資料依序完成：

1. 去除重複數字，保留第一次出現的順序
2. 只保留能被整除數 `D` 整除的數字
3. 將結果由小到大排序
4. 若沒有任何數字符合條件，輸出 `NONE`

## 個人參數

學號末兩碼：`14`

| 參數 | 計算方式 | 結果 |
|---|---:|---:|
| 個位數 `u` | `14` 的個位數 | `4` |
| 整除數 `D` | `u % 4 + 2` | `2` |

因此本題保留所有能被 `2` 整除的整數。

## 檔案說明

```text
DataCleaning/
├── data_cleaning.py
├── test_data_cleaning.py
├── README.md
├── PR.md
├── AI_LOG.md
└── TEST_LOG.md
```

| 檔案 | 說明 |
|---|---|
| `data_cleaning.py` | 第一題主程式，包含 `clean_sequence()`、`solve()`、`main()` |
| `test_data_cleaning.py` | pytest 測試檔，共 9 個測試案例 |
| `README.md` | 題目、執行方式與測試方式說明 |
| `PR.md` | Pull Request 說明草稿 |
| `AI_LOG.md` | AI 協作紀錄 |
| `TEST_LOG.md` | 測試紀錄整理 |

## 函式設計

### `clean_sequence(numbers: list[int], d: int) -> list[int]`

處理單一組整數陣列。

流程：

```text
numbers
→ 去除重複，保留第一次出現
→ 保留 number % d == 0
→ sorted()
→ 回傳 list[int]
```

### `solve(input_text: str, d: int = 2) -> str`

處理完整輸入字串，並回傳完整輸出。此函式主要用於 pytest 與檔案式輸入測試。

本函式採用 token-based parsing：

```python
tokens = input_text.split()
```

因此輸入不依賴換行位置，而是依照 `n` 決定接下來要讀取幾個整數。

### `main() -> None`

處理手動互動輸入。

互動輸入時，程式會：

1. 讀取陣列長度 `n`
2. 若 `n == 0`，立即結束輸入並輸出目前累積結果
3. 若 `n > 0`，持續讀取整數，直到收滿 `n` 個
4. 處理該組資料並暫存輸出
5. 回到步驟 1 讀取下一組陣列長度

此設計讓使用者輸入陣列長度為 `0` 並按 Enter 後，就能觸發程式輸出，不需要再按 EOF。

## 輸入格式

```text
n
a1 a2 ... an
n
a1 a2 ... an
0
```

`n = 0` 表示輸入結束，並觸發程式輸出結果。

因為程式依照 `n` 收滿指定數量的整數，所以陣列內容可以分成多行輸入，例如：

```text
8
4 7 4
2 9
2 6 7
3
1 3 5
0
```

也可以將部分資料寫在同一行：

```text
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

## 範例

### Input

```text
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

### Output

```text
2 4 6
NONE
```

## 執行方式

```bash
python data_cleaning.py
```

手動輸入：

```text
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

輸入最後的 `0` 並按 Enter 後，程式會直接輸出：

```text
2 4 6
NONE
```

不需要再按 `Ctrl + Z` 或 `Ctrl + D`。

也可以使用檔案輸入：

```bash
python data_cleaning.py < sample.txt
```

## 測試方式

```bash
pytest
```

目前測試結果：

```text
9 passed
```

## 測試案例涵蓋

| 測試案例 | 驗證內容 |
|---|---|
| `test_sample_case` | 題目基本範例 |
| `test_remove_duplicates_keep_first_then_sort` | 去重、保留第一次出現、最後排序 |
| `test_no_number_divisible_by_d_returns_empty_list` | 無符合條件時回傳空 list |
| `test_no_number_divisible_by_d_outputs_none` | 無符合條件時輸出 `NONE` |
| `test_negative_numbers` | 負數整除與排序 |
| `test_all_duplicates` | 全部重複數字 |
| `test_zero_terminates_input` | `n = 0` 直接結束 |
| `test_multiple_cases` | 多組測資 |
| `test_large_order_and_sorting_behavior` | 大量重複與排序行為 |

## TDD 流程

本題採 TDD 開發：

```text
Red：先撰寫 pytest 測試，確認尚未實作前測試失敗
Green：實作 data_cleaning.py，使測試通過
Refactor：修正輸入解析方式，避免依賴換行
Fix：修正互動輸入流程，讓 n = 0 直接觸發輸出，不再依賴 EOF
Document：整理 README.md、PR.md、AI_LOG.md、TEST_LOG.md
```

## Commit 建議

```bash
git add test_data_cleaning.py
git commit -m "test: add data cleaning tests"

git add data_cleaning.py
git commit -m "feat: implement data cleaning"

git add data_cleaning.py
git commit -m "fix: stop interactive input when array length is zero"

git add README.md PR.md AI_LOG.md TEST_LOG.md
git commit -m "docs: update data cleaning input workflow"
```
