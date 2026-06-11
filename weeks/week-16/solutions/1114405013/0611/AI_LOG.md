# AI_LOG

| 階段 | 我問 AI 什麼 | AI 回覆重點 | 我改了什麼 | 驗收標準 |
|---|---|---|---|---|
| Stage 1 拆題 | 跟 AI 把題目拆成 ≥3 個 test case（含 ≥1 個 edge case） | 將 `timeit` 拆成回傳值不變、metadata 保留、耗時紀錄、records 累積、不輸出 stdout。 | 採用 `test_returns_original_result`、`test_preserves_function_metadata`、`test_records_elapsed_time`、`test_does_not_print`。 | 先缺少 `timing.py` 時紅燈，再實作到 `test_timing` 綠燈。 |
| Stage 1 紅燈/綠燈 | 先做紅燈、再寫 `timing.py` | 用 `functools.wraps`、`time.perf_counter()`、`last_elapsed`、`records`。 | 新增 `test_timing.py` 與 `timing.py`。 | `python -m unittest test_timing` 通過。 |
| Stage 2 | 進 Stage 2，寫三種排序與 benchmark | 三種排序共用同一組 `subTest`，排序要回傳新 list，不可修改輸入。 | 新增 `test_sorts.py`、`sorts.py`、`benchmark.py`、`results.json`。 | `python -m unittest test_sorts test_timing` 通過，`python benchmark.py` 產生表格與 JSON。 |
| Stage 3 | 進第三步、詢問我是用什麼加速 | 使用演算法優化：`quick_sort_fast` 採 median-of-three、小區間 insertion sort、降低遞迴深度；另加 `sorted_baseline`。 | 新增 `sorts_fast.py`，更新 `test_sorts.py`、`benchmark.py`、`results.json`。 | 加速版通過共用排序測試，`results.json` 含 baseline 與加速版數據。 |
| Stage 4 | 繼續 Stage 4 | 用 `matplotlib.use("Agg")`，讀 `results.json`，畫 log-scale 折線圖並輸出 PNG。 | 新增 `test_plot.py`、`plot.py`、`assets/benchmark.png`，更新 README 報告。 | `python -m unittest test_timing test_sorts test_plot` 通過，PNG 存在且非空。 |
| Stage 5 | 繼續 Stage 5 | 依 OpenSSF 檢查 Numbers、Neutralization、Coding Standards、Exception Handling，先寫安全測試再修。 | 新增 `test_security.py`，修 `benchmark.py` 與 `plot.py` 輸入驗證，更新 README 安全自掃表。 | `python -m unittest test_timing test_sorts test_plot test_security` 通過。 |

## 加速策略與驗收

- 加速策略：`quick_sort_fast` 使用 median-of-three pivot、小區間 insertion sort、較小半邊遞迴以降低遞迴深度。
- 4000 筆資料量測：`quick_sort` 約 0.00173 秒，`quick_sort_fast` 約 0.00160 秒，約 1.08x 加速。
- 安全修補：修補 3 項測試鎖定的問題：負數資料量、0 次 benchmark 重複、非 `.json` 結果路徑。
