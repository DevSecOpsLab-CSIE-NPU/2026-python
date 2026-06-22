# TEST_LOG

## 測試環境

```text
OS: Windows
Python: 3.14.3
pytest: 9.0.3
pluggy: 1.6.0
專案路徑:
D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance
```

## 測試目標

本次測試目標為第四題 Search Performance，確認下列功能：

1. `TARGET = 114`
2. Linear Search 能正確搜尋並計算比較次數
3. Binary Search 能正確搜尋並計算比較次數
4. `solve()` 能解析輸入、排序、搜尋並輸出結果
5. `benchmark_search()` 能回傳時間指標
6. `make_radar_chart()` 能產生 PNG
7. 圖表功能分離成 `plot.py` 後仍可被主程式匯入
8. `test_plot.py` 能獨立測試圖表模組

---

## 第一次測試：Red 階段

### 執行指令

```powershell
pytest
```

### 測試結果

```text
collected 0 items / 1 error
ModuleNotFoundError: No module named 'search_performance'
```

### 錯誤原因

測試檔 `test_search_performance.py` 已經先建立，並嘗試匯入：

```python
from search_performance import (...)
```

但當時主程式 `search_performance.py` 尚未完成或尚未放在正確位置，因此 pytest 在 collection 階段失敗。

### 判斷

這符合 TDD 的 Red 階段，表示測試先於實作存在。

---

## 第二次測試：Matplotlib backend 失敗

### 執行指令

```powershell
pytest
```

### 測試結果

```text
collected 14 items
test_search_performance.py .............F
1 failed, 13 passed
```

### 失敗測試

```text
test_make_radar_chart_creates_png_file
```

### 錯誤訊息摘要

```text
_tkinter.TclError: invalid command name "tcl_findLibrary"
```

### 錯誤原因

`make_radar_chart()` 呼叫：

```python
fig = plt.figure(figsize=(6, 6))
```

Matplotlib 預設使用 Tk backend，pytest 執行環境無法正常建立 Tk 視窗，因此發生 `_tkinter.TclError`。

### 修正方式

在 `import matplotlib.pyplot as plt` 之前加入：

```python
import matplotlib
matplotlib.use("Agg")
```

`Agg` 是非互動式 backend，適合 pytest、CI 與只輸出 PNG 的場景。

---

## 第三次測試：搜尋主流程通過

### 執行指令

```powershell
pytest
```

### 測試結果

```text
collected 14 items
test_search_performance.py .............. [100%]
14 passed in 1.10s
```

### 判斷

加入 `Agg` backend 後，雷達圖測試通過，搜尋主流程與圖表產生功能皆正常。

---

## 第四次測試：拆分 plot.py 後匯入錯誤

### 執行指令

```powershell
pytest
```

### 測試結果

```text
collected 0 items / 2 errors
ModuleNotFoundError: No module named 'plot'
```

### 失敗原因

重構後 `search_performance.py` 改成：

```python
from plot import make_radar_chart
```

`test_plot.py` 也使用：

```python
from plot import inverse_score, make_radar_chart
```

但當時 `plot.py` 尚未放入正確資料夾，因此 pytest 無法匯入。

### 修正方式

將 `plot.py` 放入與 `search_performance.py`、`test_plot.py` 同一層目錄：

```text
SearchPerformance/
├── search_performance.py
├── plot.py
├── test_search_performance.py
└── test_plot.py
```

---

## 第五次測試：全部通過

### 執行指令

```powershell
pytest
```

### 測試結果

```text
collected 18 items

test_plot.py ....                                                                               [ 22%]
test_search_performance.py ..............                                                       [100%]

18 passed in 1.48s
```

---

## 測試案例整理

### `test_search_performance.py`

| 測試案例 | 測試目的 | 結果 |
|---|---|---|
| `test_target_value` | 驗證 `TARGET = 114` | Passed |
| `test_linear_search_found` | 線性搜尋找得到 | Passed |
| `test_linear_search_not_found` | 線性搜尋找不到 | Passed |
| `test_binary_search_found` | 二分搜尋找得到 | Passed |
| `test_binary_search_not_found` | 二分搜尋找不到 | Passed |
| `test_binary_search_empty_array` | 空陣列 | Passed |
| `test_binary_search_single_element_found` | 單一元素找到 | Passed |
| `test_binary_search_single_element_not_found` | 單一元素找不到 | Passed |
| `test_binary_search_with_duplicates_returns_valid_index` | 重複元素回傳合法 index | Passed |
| `test_solve_sorts_array_and_searches_target` | `solve()` 排序後搜尋 | Passed |
| `test_solve_target_not_found` | `solve()` 找不到目標 | Passed |
| `test_solve_accepts_numbers_across_multiple_lines` | 輸入可跨多行 | Passed |
| `test_benchmark_search_returns_time_metrics` | benchmark 回傳時間指標 | Passed |
| `test_make_radar_chart_creates_png_file` | 產生雷達圖 PNG | Passed |

### `test_plot.py`

| 測試案例 | 測試目的 | 結果 |
|---|---|---|
| `test_inverse_score_returns_best_score_when_all_values_equal` | best 與 worst 相等時回傳 5 | Passed |
| `test_inverse_score_smaller_value_gets_higher_score` | 較小數值獲得較高分 | Passed |
| `test_make_radar_chart_creates_png_file` | 產生 PNG 檔案 | Passed |
| `test_make_radar_chart_creates_parent_directory` | 自動建立父資料夾 | Passed |

---

## 結論

本題完成 TDD 流程：

```text
Red：先寫 test_search_performance.py，尚未有 search_performance.py 時發生 ModuleNotFoundError
Green：完成主程式後，大多數測試通過
Fix：修正 Matplotlib Tk backend 問題，改用 Agg
Refactor：將圖表功能分離成 plot.py
Test：新增 test_plot.py，最終 pytest 18 passed
Document：整理 README.md、AI_LOG.md、TEST_LOG.md
```
