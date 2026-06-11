# AI_LOG

## 我問 AI 什麼

| 階段 | 我問 AI 什麼 |
|---|---|
| Stage 1 | 請先依 6/11 規格建立 `timeit` 的 unittest，不要先寫實作。 |
| Stage 2 | 請幫我檢查並依序完成 SOP，先寫排序測試，再實作三種排序與 benchmark。 |
| Stage 3 | 請依規則加入 baseline 與加速版排序，並用測試確認加速版排序正確。 |
| Stage 4 | 請加入繪圖測試與 `plot.py`，產生 `assets/benchmark.png` 並寫 README 解讀。 |
| Stage 5 | 請依 OpenSSF Python Secure Coding Guide 做安全自掃，先寫會紅的安全測試，再修補。 |

## AI 給了什麼

| 階段 | AI 給了什麼 |
|---|---|
| Stage 1 | 給了 4 個測試：回傳值不變、保留 metadata、記錄耗時、不准 `print`，再實作 `timeit`。 |
| Stage 2 | 給了共用排序測試，覆蓋基本案例、edge case、隨機資料、輸入不可被修改，並實作 `bubble_sort`、`quick_sort`、`merge_sort`、`benchmark.py`。 |
| Stage 3 | 先加入 `optimized_bubble_sort` 和 `built_in_sorted`，後來發現數據不穩定，又補 `optimized_quick_sort`。 |
| Stage 4 | 給了 `load_results`、`plot_results`、非空 PNG 測試、log scale 圖表與 README 解讀。 |
| Stage 5 | 給了 3 條安全測試：負數資料量、非正 repeats、JSON 結構驗證，並修補輸入驗證與資料驗證。 |

## 我改了什麼

| 階段 | 我改了什麼 |
|---|---|
| Stage 1 | 我確認紅燈是因為缺少 `timing.py`，符合先測試後實作；也確認 `print` 會造成副作用，所以測試必須覆蓋。 |
| Stage 2 | 我確認排序函式必須回傳新 list，不可修改原輸入；特別檢查 bubble sort 先複製資料再交換。 |
| Stage 3 | 我發現早停版 bubble 在隨機資料下不穩定，不能作為可靠加速證據，因此改用 copy 後 in-place quick sort，讓 benchmark 與報告一致。 |
| Stage 4 | 我確認線性 y 軸會讓 O(n log n) 曲線被 O(n^2) 壓扁，因此使用 log scale。 |
| Stage 5 | 我判斷 `random.Random(seed)` 在 benchmark 中是為了可重現，非安全用途，所以不改成 `secrets`；但補上 `ValueError` / `TypeError` 驗證避免錯誤輸入。 |
