# AI_LOG

## Stage 1 — @timeit 裝飾器

### 我問 AI 什麼

> 「請幫我用 unittest 寫 @timeit 裝飾器的測試，要驗證：(1) 不改變回傳值 (2) 用 functools.wraps 保留 __name__/__doc__ (3) 記錄 last_elapsed 和 records (4) 禁止 print。」

### AI 給了什麼

> 給了 4 個測試案例：test_returns_original_result、test_preserves_function_metadata、test_records_elapsed_time、test_no_print。以及 timeit 裝飾器實作（使用 time.perf_counter + functools.wraps）。

### 我改了什麼

> AI 給的測試與實作皆完整，直接採用。確認 test_no_print 用 io.StringIO 捕捉 stdout，且實作中無 print 陳述式。

---

## Stage 2 — 三種排序 + benchmark

### 我問 AI 什麼

> 「請幫我用 unittest 寫 bubble_sort、quick_sort、merge_sort 的共用測試集，用 subTest 避免重複。要包含：基本案例、edge case（空 list、單元素、已排序、反序、重複值）、隨機資料比對 sorted()、以及確認傳入 list 未被修改。」

### AI 給了什麼

> 給了完整的 test_sorts.py，含 6 個測試方法並用 SORT_FUNCTIONS list 讓三種排序共用。同時給了 sorts.py 的三種排序實作。

### 我改了什麼

> AI 給的 quick_sort 採 list comprehension 版，merge_sort 採遞迴合併，bubble_sort 用雙層迴圈。檢查均符合「回傳新 list、不修改輸入」的規格。測試加入負數案例後直接採用。

---

## Stage 3 — 加速實驗

### 我問 AI 什麼

> 「請幫我設計三種排序的演算法優化版本：bubble 加入 early stopping、quick 改用 median-of-three 選 pivot 並在小區間用 insertion sort、merge 在小區間切換 insertion sort。加速版要與 Stage 2 共用同一組測試。」

### AI 給了什麼

> 給了 sorts_fast.py 含 bubble_sort_opt、quick_sort_opt、merge_sort_opt，以及將這些函式加入 test_sorts.py 的 SORT_FUNCTIONS list。

### 我改了什麼

> 確認快速排序的 median-of-three pivot 選擇正確（取頭、中、尾的中位數），小區間閾值設為 20。merge sort 的 insertion sort 切換也以 20 為門檻。bubble 的 early stopping 用 swapped flag 實作。加速比預期：bubble 提升約 30-50%（部分有序資料），quick/merge 提升約 10-20%。

---

## Stage 4 — 繪圖

### 我問 AI 什麼

> 「請幫我寫 plot.py，使用 matplotlib 從 results.json 讀取數據，畫折線圖，y 軸用 log scale，每個演算法一條線，輸出至 assets/benchmark.png。以及對應的測試 test_plot.py。」

### AI 給了什麼

> 給了 plot.py（含 load_results / plot_results）和 test_plot.py（驗證 PNG 產生、非空檔、load 回傳型別）。

### 我改了什麼

> 確認 plot.py 開頭有 matplotlib.use("Agg")，測試加入 FileNotFoundError 案例和 json 非 pickle 的驗證。

---

## Stage 5 — 安全性自掃

### 我問 AI 什麼

> 「請根據 OpenSSF Secure Coding Guide for Python 第 03、04、05、08 章，掃描 entire 專案程式，列出適用的安全規則，並產生對應的 test_security.py。每條規則一個測試，要能跑紅燈再修到綠燈。」

### AI 給了什麼

> 給了 test_security.py 含 8 個測試，涵蓋：bare except 檢查、with 開檔、json 非 pickle、無 assert 驗證、無 shadow 內建、無邊迭代邊改 list、具體例外捕捉、plot 前確認目錄存在。以及彙整不適用條目的判斷表格。

### 我改了什麼

> 確認每項測試對應的 OpenSSF 條目正確。判斷 benchmark.py 的 `random` 非安全敏感場景，不需改用 `secrets`。確認 `results.json` 使用 `json.dump` 而非 `pickle`，符合 CWE-502 防護原則。
