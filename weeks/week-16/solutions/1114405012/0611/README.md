# Week 16 Stage 6/11 Submission

## 方法
- Stage 1 用 `@timeit` 記錄 wrapper 上的 `last_elapsed` 與 `records`。
- Stage 2 以 bubble / quick / merge 三種排序搭配同一組 `subTest` 驗證。
- Stage 3 在 benchmark 內加入內建 `sorted()` 當 baseline，並提供 `quick_sort_fast` / `merge_sort_fast` 作為加速版。
- Stage 4 用 `matplotlib` 畫圖並輸出 `assets/benchmark.png`。
- Stage 5 以 `ValueError` 與檔案讀取測試檢查安全性相關問題。

## 數據與解讀
- 已產生 `results.json` 與 `assets/benchmark.png`。
- 代表性結果：`bubble_sort` 在 `n=4000` 約 `0.785173s`，`quick_sort_fast` 約 `0.003488s`，內建 `sorted()` 約 `0.000318s`。
- `bubble_sort` 的曲線明顯是平方級成長，`quick_sort` / `merge_sort` 與 `sorted()` 在較大 n 時差距很明顯。

## 安全自掃
| 條目 | 檢查結果 | 處理方式 |
|---|---|---|
| JSON 讀寫 | 使用 `json` | 避免 `pickle` 的反序列化風險 |
| 檔案處理 | 使用 `with open(...)` | 自動關檔 |
| 輸入驗證 | `make_data(-1)` 拋 `ValueError` | 拒絕無效輸入 |
| 不適用 | benchmark 使用 `random` | 這不是安全敏感資料 |
