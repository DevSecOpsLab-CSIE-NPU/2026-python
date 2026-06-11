# AI_LOG — 提示詞逐字紀錄

> 規則：提示詞自己打、逐字記入此檔；「我改了什麼」0 字 = 期末考此項 0 分。
> AI 給的測試齊不齊、排序對不對、圖正不正確——**你自己驗收**，驗收標準寫進此欄。

---

## Stage 1｜`@timeit` 裝飾器

### 提示詞（Read spec → Dev for red）

> 「請根據以下規格，幫我寫 test_timing.py 的測試案例，只要測試，不要實作：
> 1. 被裝飾函式的回傳值不變
> 2. 用 functools.wraps 保留 __name__ / __doc__
> 3. 每次呼叫後把耗時記在 f.last_elapsed（float）與 f.records（list）
> 4. 裝飾器內不准 print
> 請用 unittest，至少 4 個 test case，包含 records 累積多次的情況。」

### 我的驗收

- `test_returns_original_result`：確認回傳值與原函式相同 ✓
- `test_preserves_function_metadata`：檢查 `__name__` 與 `__doc__` ✓
- `test_records_elapsed_time`：確認 `last_elapsed` 是 float 且 > 0 ✓
- `test_records_accumulate_on_multiple_calls`：呼叫 3 次，`records` 長度應為 3 ✓
- `test_decorator_does_not_print`：用 `io.StringIO` 捕捉 stdout 確認靜默 ✓
- AI 給的測試我驗收認為完整，覆蓋全部規格條目

### 提示詞（Dev for green）

> 「現在幫我實作 timing.py，讓上面 5 個測試全部通過。函式簽名：def timeit(func)。」

### 我改了什麼

- 確認 `functools.wraps(func)` 套在 wrapper 上，而非直接套在 timeit
- 確認 `wrapper.records = []` 在 wrapper 定義外初始化，讓每次裝飾一個新函式時 records 獨立

---

## Stage 2｜三種排序 + benchmark

### 提示詞（Read spec → Dev for red）

> 「幫我寫 test_sorts.py，測試 bubble_sort / quick_sort / merge_sort 三個函式，
> 要求：(1) 三個函式共用同一組測試，用迴圈 + subTest；
> (2) 測試一般案例、edge case（空 list、單元素、全相同、已排好的）；
> (3) 測試傳入 list 沒被修改；
> (4) 傳入非 list 應拋 TypeError。
> 只要測試，不要實作。」

### 我的驗收

- `test_basic_cases`：一般整數 list ✓；負數 ✓；含重複 ✓；空 list ✓；已排好 ✓
- `test_input_not_mutated`：用 `list(original)` 保留副本後比對 ✓
- `test_random_data_matches_builtin`：用 `sorted()` 當驗證標準 ✓
- `test_non_list_input_raises_type_error`：傳字串、tuple 應拋 TypeError ✓
- Stage 3 加速版也會 append 進 SORT_FUNCTIONS 吃同一組測試 — 這點 AI 的設計我認可

### 提示詞（Dev for green）

> 「現在幫我實作 sorts.py，三個函式都不能用 sorted() 或 list.sort()，
> 且一律回傳新 list，不修改傳入的 data。」

### 我改了什麼

- quick_sort：pivot 取中間 index，用 list comprehension 分三段（less / equal / greater），確認不修改原始 list
- bubble_sort：加 `swapped` 旗標提前停止；複製一份 `arr = list(data)` 保護原始輸入
- merge_sort：遞迴分治，所有 merge 操作都在新 list 上進行

### 提示詞（benchmark）

> 「幫我寫 benchmark.py，make_data(n, seed=42) 產生固定亂數，
> run_benchmark 量測 bubble/quick/merge 在 sizes=(500,1000,2000,4000) 各跑 3 次取平均，
> 用自己的 @timeit 量測，結果存成 results.json，並印出比較表。」

---

## Stage 3｜加速版排序

### 提示詞（Read spec → Dev for red）

> 「我要在 test_sorts.py 加一個 TestStage3AcceleratedSorts 測試類，
> 驗證 SORT_FUNCTIONS 裡有 bubble_sort_fast 和 quick_sort_fast，
> 加速版也要通過 Stage 2 同一組測試。請只寫測試。」

### 我的驗收

- `test_accelerated_sorts_available`：驗證 SORT_FUNCTIONS 包含加速版函式名稱 ✓
- 加速版通過 subTest 迴圈 — 確認 SORT_FUNCTIONS append 後可自動被 Stage 2 測試覆蓋 ✓

### 提示詞（Dev for green）

> 「幫我在 sorts.py 實作 bubble_sort_fast 和 quick_sort_fast，
> 演算法優化版（不用 Cython），
> bubble 加 early-exit 旗標，quick 改 median-of-three pivot 選取。
> 同樣回傳新 list，不修改原始 data。
> 接著更新 benchmark.py 加入這兩個函式與 builtin sorted() 作為 baseline，
> 重跑並更新 results.json。」

### 我改了什麼

- `quick_sort_fast`：改用 `median_of_three` 選 pivot，小區間（len<=10）改用 insertion sort
- `bubble_sort_fast`：早停邏輯與原版相同，這版主要是命名區別，數據上改善有限
- 已驗收：4000 筆資料 quick_sort_fast 約 0.011s vs quick_sort 約 0.009s，差距在 noise 範圍，說明此優化效果有限

---

## Stage 4｜畫圖與報告

### 提示詞（Read spec → Dev for red）

> 「幫我寫 test_plot.py，測試 plot.py 的 load_results 和 plot_results，
> 要求：(1) load_results 回傳 dict 且包含正確 key；
> (2) plot_results 確實產生非空的 PNG 檔案。
> 環境限制：plot.py 開頭要加 matplotlib.use('Agg')。
> 只要測試，不要實作。」

### 我的驗收

- `test_load_results_returns_dict`：確認 `"500"` key 存在且含 `"bubble_sort"` ✓
- `test_plot_results_creates_non_empty_png`：用 `tempfile.TemporaryDirectory` 隔離產出路徑，驗證 `Path.exists()` 且 `stat().st_size > 0` ✓

### 提示詞（Dev for green）

> 「幫我實作 plot.py，load_results 讀 JSON，
> plot_results 畫折線圖：x 軸為資料量 n，y 軸為平均秒數（log scale），
> 每個演算法一條線，輸出 PNG 到指定路徑，自動建立父目錄。
> 開頭加 matplotlib.use('Agg')。」

### 我改了什麼

- 確認 `matplotlib.use("Agg")` 在 `import matplotlib.pyplot` 之前呼叫
- `output_path.parent.mkdir(parents=True, exist_ok=True)` 確保 assets/ 目錄自動建立
- `plt.close(figure)` 避免記憶體洩漏

---

## Stage 5｜安全自掃

### 提示詞（Read spec → Dev for red）

> 「對照 OpenSSF Ch03/Ch05/Ch08/Ch04，幫我掃 timing.py、sorts.py、benchmark.py、plot.py，
> 找出至少 3 條真的適用的安全問題，只要寫會紅的 test_security.py 測試，不要修 code。
> 每條要說明對應哪章、問題是什麼。」

### 我的驗收

- Stage 5 AI 給了 5 條測試，我驗收後判定：
  - `test_make_data_rejects_negative_n`：Ch03 boundary，確實是問題 ✓
  - `test_make_data_rejects_zero_n`：Ch03 boundary，同上 ✓
  - `test_plot_results_rejects_empty_results`：Ch08 coding standards，原本拋 IndexError 不清楚 ✓
  - `test_load_results_wraps_json_error_as_value_error`：Ch05，`json.JSONDecodeError` 是 `ValueError` 子類別，Python 自然拋出，已符合具體例外規範，這條測試我保留但判定「已符合」
  - `test_load_results_does_not_use_pickle`：Ch04 CWE-502，確認沒用 pickle ✓
- **不適用判定**：`random` → 統計用途非密碼學，不需改 `secrets`（若改反而扣分）

### 提示詞（Dev for green）

> 「現在幫我修 benchmark.py 的 make_data 加 n<=0 的 ValueError，
> 修 plot.py 的 plot_results 加空 dict 的 ValueError，
> 讓 test_security 全部通過。」

### 我改了什麼

- `benchmark.py`：在 `random.seed(seed)` 前加 `if n <= 0: raise ValueError(f"n must be a positive integer, got {n}")`
- `plot.py`：在 `sizes = ...` 前加 `if not results: raise ValueError("results dict must not be empty")`
- `load_results`：確認用 `json.load` + `with open` 關檔，不需修改
