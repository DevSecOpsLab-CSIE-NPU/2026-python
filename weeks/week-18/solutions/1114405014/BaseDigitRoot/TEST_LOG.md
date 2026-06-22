# TEST_LOG

## 測試環境

```text
OS: Windows
Python: 3.14.3
pytest: 9.0.3
pluggy: 1.6.0
專案路徑:
D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\BaseDigitRoot
```

## 測試目標

本次測試目標為第三題 Base Digit Root，確認下列功能：

1. 十進位整數能正確轉換為指定進位的 digits list
2. 能在 `base = 5` 下正確計算數字根
3. 可處理多行輸入與空白分隔輸入
4. 負數輸入會丟出 `ValueError`
5. 非法 base 會丟出 `ValueError`

---

## 第一次測試：Red 階段

### 執行指令

```powershell
pytest
```

### 測試結果

```text
collected 0 items / 1 error
ModuleNotFoundError: No module named 'base_digit_root'
```

### 錯誤原因

測試檔 `test_base_digit_root.py` 已先寫好，並使用：

```python
from base_digit_root import to_base_digits, digit_root_in_base, solve
```

但當時主程式 `base_digit_root.py` 尚未完成或尚未被正確放在測試可匯入的位置，因此 pytest 在 collection 階段出現 `ModuleNotFoundError`。

### 判斷

這符合 TDD 的 Red 階段，代表測試已經先於實作存在，接下來需要撰寫主程式讓測試通過。

---

## 第二次測試：Green 階段

### 執行指令

```powershell
pytest
```

### 測試輸出

```text
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\BaseDigitRoot
plugins: anyio-4.13.0
collected 14 items

test_base_digit_root.py ..............                                                          [100%]

========================================= 14 passed in 0.06s =========================================
```

### 測試結果

```text
14 passed
```

---

## 測試案例整理

| 測試案例 | 測試目的 | 結果 |
|---|---|---|
| `test_to_base_digits_zero` | 驗證 `0` 轉為 `[0]` | Passed |
| `test_to_base_digits_single_digit` | 驗證小於 base 的數字 | Passed |
| `test_to_base_digits_base_value` | 驗證 `5` 轉成 `[1, 0]` | Passed |
| `test_to_base_digits_multiple_digits` | 驗證 `24` 轉成 `[4, 4]` | Passed |
| `test_digit_root_zero` | 驗證 `0` 的數字根 | Passed |
| `test_digit_root_number_less_than_base` | 驗證小於 base 時直接回傳 | Passed |
| `test_digit_root_equal_to_base` | 驗證 `5` 的數字根為 `1` | Passed |
| `test_digit_root_requires_repeated_sum` | 驗證 `24` 需反覆加總 | Passed |
| `test_digit_root_power_of_base` | 驗證 `25 = 100₅` 的數字根 | Passed |
| `test_digit_root_larger_number` | 驗證 `124 = 444₅` 的數字根 | Passed |
| `test_solve_multiple_lines` | 驗證多行輸入 | Passed |
| `test_solve_space_separated_input` | 驗證空白分隔輸入 | Passed |
| `test_invalid_negative_number_raises_value_error` | 驗證負數例外 | Passed |
| `test_invalid_base_less_than_two_raises_value_error` | 驗證非法 base 例外 | Passed |

---

## 手動驗算紀錄

### 測資

```text
0 8 63
```

### base

```text
base = 5
```

### 驗算

```text
0 = 0₅ → 0

8 = 13₅
1 + 3 = 4

63 = 223₅
2 + 2 + 3 = 7
7 = 12₅
1 + 2 = 3
```

### 預期輸出

```text
0
4
3
```

## 結論

本題完成 TDD 流程：

```text
Red：測試先寫，第一次 pytest 出現 ModuleNotFoundError
Green：完成 base_digit_root.py 後，pytest 14 passed
Refactor：函式拆分為 validate、to_base_digits、digit_root_in_base、solve
Document：整理 README.md、AI_LOG.md、TEST_LOG.md
```
