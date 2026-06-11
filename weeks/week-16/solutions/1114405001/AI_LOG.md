# AI 協作紀錄

## 基本資料
- 學號: 1114405001
- 日期: 2026-06-11
- 主題: Week 16 排序效能實驗室

## Stage 1: timeit 裝飾器

### 提示詞（逐字）
- 按照以下規格作答此題目
- 直接進stage2，然後幫我把ai log的內容直接在1114405001的資料夾內新建一個檔案

### 訪談檢查表
- 函式簽名與回傳型別: 照規格
- 輸入範圍/邊界條件: 不能（依規格）
- 例外行為: TypeError
- edge case 清單: 都無所謂
- 紅燈驗收標準: 先看指定測試全紅，再進綠燈

### 實作與驗收
- 紅燈證據: `python -m unittest test_timing.py`，初次失敗原因為缺少 `timing` 模組
- 綠燈證據: `python -m unittest test_timing.py`，3 tests 全通過
- 完成項目:
  - `timeit` 不改變被裝飾函式回傳值
  - 使用 `functools.wraps`
  - 提供 `last_elapsed` 與 `records`
  - 裝飾器內不使用 `print`

## Stage 2: 三種排序 + benchmark

### 提示詞（逐字）
- 直接進stage2，然後幫我把ai log的內容直接在1114405001的資料夾內新建一個檔案

### 測試與實作
- 測試檔: `test_sorts.py`
- 實作檔: `sorts.py`, `benchmark.py`
- 測試策略:
  - 三種排序共用同一組測試（使用 `subTest`）
  - 一般案例 + 隨機案例 + 不可修改輸入 list

### 紅綠燈紀錄
- 紅燈證據: `python -m unittest test_sorts.py`，失敗原因為缺少 `sorts` 模組
- 綠燈證據: `python -m unittest test_sorts.py`，3 tests 全通過

### benchmark 執行結果
- 指令: `python benchmark.py`
- 已產生: `results.json`
- 輸出表格:
  - bubble_sort: 500=0.010994, 1000=0.051161, 2000=0.209583, 4000=0.857330
  - quick_sort: 500=0.000806, 1000=0.001977, 2000=0.003870, 4000=0.007940
  - merge_sort: 500=0.000868, 1000=0.001916, 2000=0.004082, 4000=0.008541

## Stage 3: baseline + 加速版

### 提示詞（逐字）
- yes

### 測試與實作
- 加速版檔案: `sorts_fast.py`
- 函式: `quick_sort_optimized(data: list) -> list`
- 策略:
  - quick sort 採 median-of-three 選 pivot
  - 小資料區段（長度 <= 16）改用 insertion sort
  - 三向分割（left/equal/right）降低重複值分割成本

### 紅綠燈紀錄
- 紅燈證據: `python -m unittest test_sorts.py`，失敗原因為缺少 `sorts_fast` 模組
- 綠燈證據: `python -m unittest test_sorts.py`，3 tests 全通過（加速版共用 Stage 2 同組測試）

### benchmark 調整
- 新增 baseline: `sorted_builtin`（內建 `sorted()`）
- 新增加速版: `quick_sort_optimized`

### benchmark 執行結果（Stage 3）
- 指令: `python benchmark.py`
- 已更新: `results.json`
- 輸出重點（n=4000）:
  - quick_sort = 0.0088119s
  - quick_sort_optimized = 0.0044917s
  - sorted_builtin = 0.0005457s

### 加速比
- quick_sort -> quick_sort_optimized（n=4000）
  - 時間下降: `(0.0088119 - 0.0044917) / 0.0088119 = 49.03%`
  - 倍率: `0.0088119 / 0.0044917 = 1.96x`

## Stage 4: 繪圖與結果解讀

### 提示詞（逐字）
- yes

### 測試與實作
- 測試檔: `test_plot.py`
- 實作檔: `plot.py`
- 重點:
  - `matplotlib.use("Agg")`
  - 從 `results.json` 載入資料
  - y 軸使用 log scale
  - 輸出 `assets/benchmark.png`

### 紅綠燈紀錄
- 紅燈證據: `python -m unittest test_plot.py`，失敗原因為缺少 `plot` 模組
- 綠燈證據: `python -m unittest test_plot.py`，2 tests 全通過

### 產出
- 指令: `python plot.py`
- 產生檔案: `assets/benchmark.png`（非空檔）

## Stage 5: 安全性自掃與修補

### 提示詞（逐字）
- Yes

### 測試與實作
- 測試檔: `test_security.py`
- 修補檔: `benchmark.py`, `plot.py`

### 紅綠燈紀錄
- 紅燈證據: `python -m unittest test_security.py`，4 tests 全失敗
- 綠燈證據: `python -m unittest test_security.py`，4 tests 全通過

### OpenSSF 條目對照
| 類別 | 問題 | 修補方式 |
|---|---|---|
| 08 Coding Standards / 03 Numbers | `make_data` 會把 `bool` 視為 `int` 接受 | 明確拒絕 `bool`，只接受 `int` |
| 03 Numbers | `run_benchmark` 未限制 `repeats` 正整數 | 新增 `repeats` 型別與 >0 驗證 |
| 05 Exception Handling / 04 Neutralization | `load_results` 對副檔名與 JSON 結構未驗證 | 限制 `.json`、要求 top-level 為 `dict` |
| 03 Numbers | log scale 繪圖未檢查時間值是否正數 | `plot_results` 新增 `y > 0` 驗證 |

### 不適用條目
- `random` 改 `secrets`：不適用。benchmark 目的是「可重現效能實驗」，應使用可固定 seed 的 `random.Random`，而非安全隨機來源。

## 教師要求追蹤欄位（持續更新）
- 加速多少百分比: quick_sort 在 n=4000 時加速 49.03%（1.96x）
- 演算法優化策略: median-of-three + 小區間 insertion sort + 三向分割
- 依 Python 安全程式原則修補幾項問題: 4 項（輸入型別、重複次數邊界、JSON 載入限制、log scale 正數檢查）
