# AI_LOG — 排序效能實驗室

學號：1112405062

---

## Stage 1 — `@timeit` 裝飾器

### 檢查表討論

| 項目 | 問答 |
|------|------|
| 函式簽名 | `timeit(func)` 或 `timeit(**kwargs)(func)`，回傳 wrapper。支援有/無括號兩種用法 |
| 輸入範圍 | 不限參數型別，透過 `*args, **kwargs` |
| 例外行為 | 讓例外自然傳播，用 `finally` 確保時間仍被記錄 |
| Edge cases | 遞迴、generator/async、極快/極慢、repetitions=0、回傳 None、例外時計時、metadata |
| 驗收標準 | 紅燈 = 例外拋出時時間「仍要記錄」；覆蓋正常、例外、雙語法、metadata |

### 我問 AI 什麼

「做 AI 把題目拆成 ≥3 個 test case（含 ≥1 個 edge case）放在 solutions/1112405062/0611」

### AI 給了什麼

給出 `test_timing.py`（7 個測試：4 正常 + 3 edge case）與 `timing.py` class-based 雙語法實作。

### 我改了什麼

無，直接採用 AI 給的測試與實作。

---

## Stage 2 — 三種排序 + benchmark

### 檢查表討論

| 項目 | 問答 |
|------|------|
| 函式簽名 | `bubble/quick/merge_sort(data: list) -> list`、`make_data(n, seed)`、`run_benchmark(sizes) -> dict` |
| 輸入範圍 | data 為可比較數值 list；n ≥ 0；seed 任意 |
| 例外行為 | 空 list → []；非 list / 非數字 → TypeError |
| Edge cases | 空 list、長度 1、已排序、反序、重複值 |
| 驗收標準 | 紅燈 = 例外仍計時；驗正確性、輸入不變、回傳新 list |

### 我問 AI 什麼

「請幫 Stage 2 寫 test_sorts.py（三種排序共用 subTest）與 sorts.py 實作」

### AI 給了什麼

給了 5 個測試（`test_basic_cases`、`test_random_data_matches_builtin`、`test_input_not_mutated`、`test_returns_new_list`、`test_negative_and_large_numbers`），以及 `bubble_sort`（雙層迴圈）、`quick_sort`（pivot = 最後元素）、`merge_sort`（遞迴 + helper）。

### 我改了什麼

接受 AI 實作，未修改。

---

## Stage 3 — 加速實驗

### 檢查表討論

| 項目 | 問答 |
|------|------|
| 函式簽名 | 與 Stage 2 相同，測試透過 SORT_FUNCTIONS 重複使用 |
| 輸入範圍 | 同 Stage 2 |
| 例外行為 | 同 Stage 2 |
| Edge cases | 同 Stage 2 |
| 驗收標準 | baseline = Stage 2 + `sorted()`，加速版須更快且正確 |

### 我問 AI 什麼

「在 sorting_fast.py 實作加速版 quick_sort 與 merge_sort，並在 benchmark 加入 sorted() 當 baseline」

### AI 給了什麼

- `quick_sort_fast`：median-of-3 pivot + insertion sort fallback（< 20 元素）
- `merge_sort_fast`：iterative bottom-up（size 從 1 倍增）
- `benchmark.py`：包含 bubble/quick/merge/quick_fast/merge_fast/sorted，輸出比較表 + `results.json`

### 加速百分比

4000 筆資料：
- quick_sort：0.00639s → **0.00316s（50.6%，2.02x）**
- merge_sort：0.00872s → **0.00620s（28.9%，1.41x）**

### 演算法優化策略

1. **Median-of-3 pivot**：選首、中、尾三值的中位數為 pivot，降低選到極值的機率
2. **Insertion sort fallback**：子陣列 < 20 個元素時切換到 insertion sort，減少遞迴開銷
3. **Tail recursion elimination**：always recurse on smaller half, iterate on larger half
4. **Iterative merge sort**：bottom-up 方式免除遞迴呼叫，提升 cache locality

### 我改了什麼

無直接修改，接受 AI 方案。確認加速版通過 Stage 2 同一組正確性測試。

---

## Stage 4 — 繪圖

### 檢查表討論

| 項目 | 問答 |
|------|------|
| 函式簽名 | `plot_results(data: dict) -> None`，`main()` 執行 |
| 輸入範圍 | 讀 `results.json`，尺寸 10×6 |
| 例外行為 | 檔案不存在 → FileNotFoundError；格式錯 → JSONDecodeError |
| Edge cases | 單筆→正常繪；空 dict→拋錯；時間零→x 軸；log scale→filter/symlog |
| 驗收標準 | 紅燈 = 圖畫錯或例外；測試 PNG 存在 + 非空 > 1KB |

### 我問 AI 什麼

「寫 test_plot.py（4 個測試）與 plot.py（讀 results.json 畫圖，y 軸 log scale，輸出 assets/benchmark.png）」

### AI 給了什麼

`plot.py`：`matplotlib.use("Agg")` → 讀 data dict → 折線圖（y log scale）→ 存 PNG。<br>
`test_plot.py`：測 PNG 存在、非空、空 dict 拋錯、缺欄位拋錯。

### 我改了什麼

發現 test_rejects_missing_fields 測試案例中資料含有 avg 欄位（未真正缺欄位），手動修正為只給 times 不給 avg。

---

## Stage 5 — 安全性自掃

### 掃描依據

OpenSSF Secure Coding Guide for Python（https://best.openssf.org/Secure-Coding-Guide-for-Python/）

### 我問 AI 什麼

「掃 Stage 1–4 所有 .py，依 OpenSSF 指南找出安全問題，寫成 test_security.py」

### AI 給了什麼

`test_security.py` 含 7 條測試：

| 測試 | 結果 |
|------|------|
| `test_sort_rejects_non_list` | ✅ 自然通過 |
| `test_sort_rejects_non_comparable` | ✅ 自然通過 |
| `test_make_data_rejects_negative_n` | ⚠️ 初始紅燈→修正 `sorts.py` 加入驗證 |
| `test_no_eval_or_exec` | ✅ 全專案無使用 |
| `test_no_sorted_in_sorts` | ✅ 通過 |
| `test_plot_uses_agg` | ✅ 通過 |
| `test_random_not_for_security` | ✅ 不適用（附理由） |

### 修補項數

**2 項**修正（加入 `make_data` 負數檢查、修正測試讀檔編碼）

### 掃到但判定不適用

| 安全原則 | 理由 |
|---------|------|
| `random` 改 `secrets` | benchmark 資料非安全敏感 |
| `eval`/`exec`/`subprocess` | 全專案無使用 |
| SQL/OS injection | 無資料庫、無 shell 呼叫 |
| 檔案權限 | `results.json` 寫入固定路徑，無使用者輸入 |

### 我改了什麼

接受 AI 掃描結果。2 項紅燈修正：
1. `sorts.py:make_data` 加入 `if n < 0: raise ValueError`
2. `test_security.py` 讀檔指定 `encoding="utf-8"` 解決 Windows cp950 編碼問題

---

## 階段閘門問答紀錄

| 階段過渡 | 問題 | 回答 |
|---------|------|------|
| S1 → S2 | timeit 為何不准 print？ | 回傳值應以資料形式記錄，讓呼叫端自行呈現；print 會汙染 stdout 且無法被測試斷言 |
| S2 → S3 | 三種排序時間複雜度？worst case？ | bubble O(n²)/O(n)，quick O(n log n)/O(n²)，merge O(n log n)。quick worst case 因 pivot 取極值使分割不平衡 |
| S3 → S4 | Median-of-3 為何改善 worst case？ | 減少選到極值的機率，使分割更平衡，但刻意構造的輸入仍可觸發 |
| S4 → S5 | matplotlib.use("Agg") 用途？ | 避免無 GUI 環境（CI/伺服器）噴 TclError |
