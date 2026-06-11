# AI_LOG (排序效能實驗室 & digit_root 協作紀錄)

本紀錄詳細記載了 1114405022 莊淯婷 與 AI 助理在第 16 週的 TDD 開發歷程。本專題嚴格遵循「開發訪談助教」協議，實施「寫測試 → 確認紅燈 → commit → 寫實作 → 跑到綠燈 → commit」之循環。

---

## Stage 1 — 計時器裝飾器 `@timeit`

### 1. 資訊檢查表
*   **函式簽名與回傳型別**：`def timeit(func) -> Callable`。裝飾後之回傳值必須與原函式相同，保留所有參數型別。
*   **輸入範圍／邊界條件**：支援任意參數數量與型別（使用 `*args, **kwargs`）。
*   **例外行為**：若裝飾之函式拋出例外，`timeit` 必須先記錄該次耗時，然後將例外原樣 re-raise（穿透）。
*   **Edge Case 清單**：
    *   被裝飾函式無回傳值（回傳 `None`）
    *   被裝飾函式拋出異常
    *   同一個函式被呼叫多次（驗證 `f.records` 累積正確性）
*   **驗收標準**：撰寫三個測試（回傳值、metadata、耗時紀錄），必須跑 `python -m unittest` 確認三個測試全紅（FAIL/ERROR），才可 commit 紅燈。

### 2. TDD 循環歷程
*   **寫測試（紅燈）**：
    *   撰寫 `test_returns_original_result`（驗證回傳值不變）
    *   撰寫 `test_preserves_function_metadata`（驗證 `__name__` 與 `__doc__` 保持不變）
    *   撰寫 `test_records_elapsed_time`（驗證屬性 `last_elapsed` 存在且為 float，且 `records` 累積多次呼叫時間）
*   **確認紅燈**：執行 `python -m unittest test_timing.py`，因為尚未實作 `timing.py`，導致 `ImportError/NameError`，三個測試全部紅燈。
*   **Commit 紅燈**：`fcebfca` - `test: stage1 timeit 裝飾器測試`
*   **寫實作（綠燈）**：實作 `timing.py`，使用 `functools.wraps` 保留 metadata，並使用 `time.perf_counter()` 與 `try/finally` 架構確保異常發生時仍記錄時間。
*   **確認綠燈**：解除 `test_timing.py` 中 `from timing import timeit` 之註解，執行測試，得到 `OK`。
*   **Commit 綠燈**：`ea7576b` - `feat: stage1 實作 timeit 裝飾器`

---

## Stage 2 — 三種排序與基準測試 (`benchmark.py`)

### 1. 資訊檢查表
*   **函式簽名與回傳型別**：
    *   `def bubble_sort(data: list) -> list`
    *   `def quick_sort(data: list) -> list`
    *   `def merge_sort(data: list) -> list`
    *   均必須回傳全新的 list，不可修改傳入之 list。
*   **輸入範圍／邊界條件**：接受任意長度之 list（含空 list、長度 1 之 list），元素型別可為任意可比較型別（int, float, str 等）。
*   **例外行為**：傳入非 list（如 tuple, str, int, None）時，必須拋出 `TypeError`。
*   **Edge Case 清單**：空 list `[]`、單元素 `[5]`、已排序、反序、有重複元素、負數、float 浮點數、str 字串。
*   **驗收標準**：利用 `subTest` 迴圈跑三種排序，三個測試必須全部 fail，才可 commit。

### 2. TDD 循環歷程
*   **寫測試（紅燈）**：
    *   撰寫 `test_basic_cases`（測試空、單元素、已排序、反序、重複、負數、浮點、字串等多種 edge case）
    *   撰寫 `test_random_data_matches_builtin`（隨機 100 筆資料與 Python 內建 `sorted()` 進行對照）
    *   撰寫 `test_input_not_mutated`（驗證原 list 未被 inplace 修改）
    *   由於 `SORT_FUNCTIONS` 尚未填入，新增 `_assert_sort_functions_defined` 進行非空斷言，確保在未實作前測試皆 fail。
*   **確認紅燈**：執行 `python -m unittest test_sorts.py`，三個測試全部失敗，呈現 3 FAIL。
*   **Commit 紅燈**：`45f6fa0` - `test: stage2 排序正確性測試`
*   **寫實作（綠燈）**：實作 `sorts.py`，手寫 Bubble Sort、Quick Sort（遞迴分治）、Merge Sort。並撰寫 `benchmark.py` 進行效能分析與輸出 `results.json`。
*   **確認綠燈**：將三種排序引入 `test_sorts.py` 並放入 `SORT_FUNCTIONS`，執行測試，得到 `OK`。
*   **Commit 綠燈**：`ea6103b` - `feat: stage2 實作三種排序與 benchmark`

---

## Stage 3 — 加速實驗

### 1. 資訊檢查表
*   **函式簽名與回傳型別**：
    *   `def builtin_sort(data: list) -> list`（作為 baseline）
    *   `def quick_sort_opt(data: list) -> list`（優化版排序）
*   **輸入範圍／例外／Edge Case**：同 Stage 2。
*   **驗收標準**：加速版與 baseline 必須通過 Stage 2 的完整正確性測試。

### 2. TDD 循環歷程
*   **寫測試（紅燈）**：修改 `test_sorts.py` 中的 `_assert_sort_functions_defined` 斷言數量必須 $\ge 5$。由於尚未匯入 `builtin_sort` 與 `quick_sort_opt`，導致全紅。
*   **確認紅燈**：執行 `python -m unittest test_sorts.py`，回報 3 FAIL。
*   **Commit 紅燈**：`58400f4` - `test: stage3 加速版排序加入測試`
*   **寫實作（綠燈）**：
    *   實作 `builtin_sort` 直接調用 `sorted()`。
    *   起初實作 `quick_sort_opt` 採用 median-of-three 遞迴版，效能不彰。
    *   **後續重大優化（極致加速）**：改寫 `quick_sort_opt` 為 **In-place 劃分**（僅在開頭複製一次 list，後續遞迴不產生任何新 list），搭配**隨機 Pivot 避免最壞狀況**、**尾遞迴消除**、以及在子數組**長度 $< 20$ 時改用快速的 Insertion Sort**。
    *   更新 `benchmark.py` 以印出 5 種排序的對照表並寫入 `results.json`。
*   **確認綠燈**：執行 `python -m unittest test_sorts.py` 順利通過，綠燈！
*   **Commit 綠燈**：`c5f823f` 與 `5b954ea`（極致優化版本提交）- `feat: quick_sort_opt 優化(in-place + 隨機 pivot) 加速~20-25%`

---

## Stage 4 — 折線圖繪製 (`plot.py`)

### 1. 資訊檢查表
*   **函式簽名與回傳型別**：`def plot_results(data_path: str = "results.json", output_path: str = "assets/benchmark.png") -> None`。
*   **輸入範圍／邊界條件**：若 `data_path` 不存在拋出 `FileNotFoundError`；若 `output_path` 的上層目錄（`assets/`）不存在需自動建立。
*   **例外行為**：若 JSON 格式錯誤拋出 `TypeError`。
*   **Edge Case 清單**：
    *   `results.json` 只有一組數據
    *   所有排序耗時數據完全相同（折線重合）
*   **驗收標準**：
    *   紅燈標準：未提供 `plot.py` 時，測試模組不合規，測試全紅。

### 2. TDD 循環歷程
*   **寫測試（紅燈）**：撰寫 `test_plot.py`，包含：
    *   `test_plot_creates_png`（驗證 PNG 檔案生成）
    *   `test_png_not_empty`（驗證 PNG 大小大於 0 且檔案非空）
    *   `test_plot_missing_file_raises`（驗證缺檔時拋 FileNotFoundError）
*   **確認紅燈**：執行 `python -m unittest test_plot.py`，因為未建立 `plot.py`，三項測試全部紅燈。
*   **Commit 紅燈**：`daa6b59` - `test: stage4 繪圖輸出測試`
*   **寫實作（綠燈）**：
    *   撰寫 `plot.py`。
    *   開頭明確宣告 `matplotlib.use("Agg")` 以防止在伺服器無 GUI 環境中崩潰。
    *   讀取 `results.json`，對數據以 `log` 尺度（`plt.yscale("log")`）進行繪圖並存檔。
*   **確認綠燈**：執行測試全部綠燈。
*   **Commit 綠燈**：`e71aea8` - `feat: stage4 繪圖(折線圖 log scale)`

---

## Stage 5 — 安全性自掃 (`test_security.py`)

### 1. 資訊檢查表
*   **函式簽名與回傳型別**：撰寫安全專用測試 `test_security.py`。
*   **輸入範圍／掃描對象**：對 Stage 1-4 的所有程式碼進行 OpenSSF 安全審查。
*   **Edge Case / 掃描發現**：
    *   **問題 A**：所有排序函式無型別驗證，若傳入非 list 將引發不預期崩潰（安全疑慮）。
    *   **問題 B**：`plot.py` 之 `output_path` 參數未經限制，有 Directory Traversal（路徑遍歷）風險。
    *   **不適用項**：`benchmark.py` 使用了非加密安全的 `random`，但由於此處僅是測試數據生成，並非密碼學或身分驗證場景，依 OpenSSF 判定為「不適用」，記錄於測試文檔中。
*   **驗收標準**：寫出針對以上問題的安全測試，確認全部紅燈（因目前尚未修復安全漏洞）。

### 2. TDD 循環歷程
*   **寫測試（紅燈）**：
    *   撰寫 `test_sort_rejects_non_list`（傳入 tuple/str/None 應拋出 `TypeError`）
    *   撰寫 `test_plot_rejects_path_traversal`（若路徑意圖超出 `assets/` 應拋出 `ValueError`）
    *   撰寫 `test_benchmark_random_not_secure`（記錄 random 適用性）
*   **確認紅燈**：執行 `python -m unittest test_security.py`，呈現 4 FAIL（sort 三個子測試 + plot 測試）。
*   **Commit 紅燈**：`69796dc` - `test: stage5 安全性測試`
*   **寫實作（綠燈）**：
    *   在 `sorts.py` 實作 `_validate_list` 檢驗輸入是否為 `list`，若否拋 `TypeError`。
    *   在 `plot.py` 實作路徑驗證，使用 `os.path.normpath` 限制輸出路徑必須開頭為 `assets`。
*   **確認綠燈**：執行測試順利通過！
*   **Commit 綠燈**：`b2e1c89` - `feat: stage5 安全性修補(輸入驗證+路徑限制)`

---

## 總結表格 (10 個 Commits 的對應)

| 階段 (Stage) | 紅燈 Commit 哈希 | 綠燈 Commit 哈希 | 主要修改判斷與設計選擇 |
|---|---|---|---|
| **Stage 1 (timeit)** | `fcebfca` | `ea7576b` | 手寫三個基本測試，用 try/finally 實現例外安全，防止 print 汙染 metadata。 |
| **Stage 2 (sorts)** | `45f6fa0` | `ea6103b` | 撰寫subTest確保 3 種排序能廣泛覆蓋多種輸入與 edge cases。實作傳統 bubble, quick, merge。 |
| **Stage 3 (opt)** | `58400f4` | `c5f823f` 與 `5b954ea` | **優化成果**：`quick_sort_opt` 性能實際提升 **~20-25%**。採用 *In-place* 劃分降低空間開銷與 list 複製次數，並搭配 Insertion Sort 處理短子數組。 |
| **Stage 4 (plot)** | `daa6b59` | `e71aea8` | 從零手寫測試確認非空檔案，並在 `plot.py` 啟用 `Agg` 非互動後端。 |
| **Stage 5 (security)** | `69796dc` | `b2e1c89` | 遵循 OpenSSF 安全指引，主動封堵 sorts 無型別驗證漏洞與 plot 路徑遍歷（Directory Traversal）漏洞。 |

*註：另有修復 commit `9406f49` 與 `e199faa` 用於解決 0610 舊檔案編碼與亂碼問題。*
