# TEST_LOG

## 測試環境

```text
OS: Windows
Python: 3.14.3
pytest: 9.0.3
pluggy: 1.6.0
專案路徑:
D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\DataCleaning
```

## 第一次測試：失敗紀錄

### 執行狀況

第一次執行 pytest 時，是在 `DataCleaning\tests` 目錄內執行。

```text
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\DataCleaning\tests
collected 0 items / 1 error
```

### 錯誤訊息

```text
ImportError while importing test module
ModuleNotFoundError: No module named 'data_cleaning'
```

### 錯誤原因

測試檔中使用：

```python
from data_cleaning import clean_sequence, solve
```

但當 pytest 的 rootdir 位於 `DataCleaning\tests` 時，Python 匯入路徑無法正確找到上一層的 `data_cleaning.py`，因此產生 `ModuleNotFoundError`。

### 修正方式

回到 `DataCleaning` 專案根目錄後再執行：

```powershell
cd D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\DataCleaning
pytest
```

---

## 第二次測試：通過紀錄

### 執行指令

```powershell
pytest
```

### 測試輸出

```text
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\DataCleaning
plugins: anyio-4.13.0
collected 9 items

test_data_cleaning.py .........                                                                 [100%]

========================================= 9 passed in 0.16s ==========================================
```

## 測試結果

```text
9 passed
```

## 測試案例整理

| 測試案例 | 測試目的 | 結果 |
|---|---|---|
| `test_sample_case` | 驗證題目範例 | Passed |
| `test_remove_duplicates_keep_first_then_sort` | 驗證去重、保留第一次出現與排序 | Passed |
| `test_no_number_divisible_by_d_returns_empty_list` | 驗證無符合條件時回傳空 list | Passed |
| `test_no_number_divisible_by_d_outputs_none` | 驗證無符合條件時輸出 `NONE` | Passed |
| `test_negative_numbers` | 驗證負數處理 | Passed |
| `test_all_duplicates` | 驗證全部重複數字 | Passed |
| `test_zero_terminates_input` | 驗證 `n = 0` 直接結束 | Passed |
| `test_multiple_cases` | 驗證多組測資 | Passed |
| `test_large_order_and_sorting_behavior` | 驗證大量重複與排序行為 | Passed |

## 手動輸入修正紀錄

### 原本問題

原本 `main()` 使用 `sys.stdin.read()`，所以即使輸入題目規定的 `0`，終端機仍需額外輸入 EOF 才會觸發輸出。

### 修正後行為

修正後 `main()` 改成互動式讀取。使用者輸入陣列長度 `0` 並按 Enter 後，程式會直接輸出累積結果。

### 建議手動測試

```powershell
python data_cleaning.py
```

輸入：

```text
8
4 7 4 2 9 2 6 7
3
1 3 5
0
```

預期輸出：

```text
2 4 6
NONE
```

## 結論

第一次測試失敗不是功能邏輯錯誤，而是 pytest 執行位置導致匯入路徑錯誤。回到 `DataCleaning` 專案根目錄後重新執行，所有 9 個測試皆通過。後續另修正互動輸入方式，使輸入陣列長度 `0` 時即可觸發程式輸出，不再依賴 EOF。
