# AI_LOG

## 我問 AI 什麼（逐字紀錄）

| 階段 | 我問 AI 什麼 |
|---|---|
| Stage 1 | 剛剛說的請都幫我都建在week-16裡soulution裡的1114405029裡面，這4點你都幫我處理，只要是有符合標準詳細正確就可以 |
| Stage 2 | 請幫我檢查，並確認都有依序完成以下8步驟 |
| Stage 3 | Stage 2 驗證「原本傳入的 list 沒有被修改」，是為了確保排序函式不會產生副作用（Side Effect）。如果函式直接改動呼叫者傳入的資料，可能會影響後續程式邏輯、造成資料被意外改變，也會讓函式較難重複使用與測試。因此要求排序函式回傳新的排序結果，而保留原始資料不變。 |
| Stage 4 | 因為 Bubble Sort 的時間複雜度是 O(n²)，而 Quick Sort、Merge Sort 和 Python 的 sorted() 大約是 O(n log n)。當資料量變大時，Bubble Sort 的執行時間會遠大於其他演算法。若使用線性（Linear）Y 軸繪圖，為了容納 Bubble Sort 的巨大數值，Y 軸範圍會被拉得很高，導致 Quick Sort、Merge Sort 和 sorted() 的數值都擠在靠近 X 軸的位置，看起來幾乎重疊，難以觀察彼此之間的差異。 |
| Stage 5 | benchmark 的目的在於效能測試與結果重現（reproducibility），而不是產生安全用途的隨機數。因此使用 random.Random(seed) 是合理的。固定的 seed 可以讓每次執行都產生完全相同的測試資料，確保不同排序演算法是在相同條件下進行比較，讓測試結果具有可重現性與公平性。 |

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

## 訪談摘要

| 階段 | 問了什麼 | 學生答了什麼 | 檢查表狀態 |
|---|---|---|---|
| Stage 1 | `timeit` 為何不應直接 `print`？ | 直接輸出會造成 side effect，破壞輸出格式與測試重複利用。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 2 | 為什麼要驗證原 list 不被修改？哪個排序最容易犯？ | 避免副作用；bubble sort 最容易因 swap 直接修改輸入。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 3 | 為什麼線性 y 軸會讓差異看不清楚？ | O(n^2) 的 bubble sort 會拉高 y 軸，壓扁 O(n log n) 曲線。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 4 | 為什麼 benchmark 不需改用 `secrets`？ | benchmark 要可重現資料，不是不可預測的安全亂數。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 5 | 依 OpenSSF 檢查哪些項目？ | 補輸入驗證、JSON 結構驗證、資源管理紀錄，並說明 random 不適用。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
