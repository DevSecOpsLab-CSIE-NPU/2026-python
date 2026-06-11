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

## 我用什麼策略完成

### 整體策略：照 TDD 分階段推進

我沒有一次請 AI 產生完整成品，而是依照題目要求把工作拆成五個階段，每個階段都遵守：

1. 先讀該階段規格，確認函式簽名、輸入行為、例外行為、edge case 與驗收標準。
2. 先寫測試，讓測試因為缺少檔案或功能尚未完成而紅燈。
3. 紅燈後 commit `test: stageN ...`，保留開發證據。
4. 再寫最小可用實作，跑到全部 unittest 綠燈。
5. 綠燈後 commit `feat: stageN ...`。

這樣做的目的是讓 `git log --reverse` 可以清楚證明每一階段都是先測試、後實作，而不是先寫完程式再補測試。

### Stage 1 策略：先驗證裝飾器行為，不只測時間

`timeit` 的重點不是只量到時間，而是不能破壞被裝飾函式原本行為。因此我設計測試時先覆蓋：

- 回傳值是否保持不變
- `functools.wraps` 是否保留 `__name__` 與 `__doc__`
- 每次呼叫後是否更新 `last_elapsed`
- `records` 是否累積每次耗時
- 裝飾器內是否沒有 `print`

我採用 `time.perf_counter()` 量測時間，因為它適合做短時間效能量測；耗時記錄掛在 wrapper 上，而不是全域變數，避免多個被裝飾函式互相污染。

### Stage 2 策略：共用測試驗證三種排序一致性

三個排序函式規格相同，所以我使用同一組測試資料搭配 `subTest` 跑過 `bubble_sort`、`quick_sort`、`merge_sort`，避免複製三份幾乎一樣的測試。

測試案例包含：

- 一般亂序資料
- 空 list
- 單元素 list
- 重複值
- 負數
- 已排序資料
- 反向排序資料
- 隨機資料
- 原始 list 不可被修改

實作時我避免使用 `sorted()` 與 `list.sort()`，因為那是 Stage 3 baseline 的用途。排序函式都先複製 `data[:]`，再對複製後的資料排序，確保不會修改呼叫者傳入的原 list。

Benchmark 的策略是固定 `seed`，每個資料量重複多次並取平均，讓不同演算法比較時使用可重現且公平的資料。

### Stage 3 策略：先做 baseline，再用數據驗證加速是否有效

我選擇的加速策略是**演算法優化**，不是 Cython / C 擴充。原因是 Cython 需要額外編譯環境，課堂時間有限，若編譯環境出問題會拖慢進度；演算法優化可以直接用 Python 完成，也比較容易用 unittest 驗證正確性。

我先把 Python 內建 `sorted()` 加入 benchmark，作為 Timsort baseline。接著嘗試演算法優化。

一開始我嘗試 `optimized_bubble_sort` 的提前停止與縮小邊界策略，但在隨機資料下加速效果不穩定，不能當作可靠證據。因此我改用 `optimized_quick_sort`：

- 使用 median-of-three pivot，降低 pivot 選到極端值的機率。
- 小區間改用 insertion sort，減少遞迴與 partition overhead。
- 先 copy 原 list，再在 copy 上做 in-place partition，兼顧不修改輸入與降低中間 list 建立成本。

最後用 benchmark 數據確認 `optimized_quick_sort` 比原本 `quick_sort` 更快，並把加速前後數據寫進 `results.json` 與 README 報告。

依 `results.json` 中 4000 筆資料的結果：

```text
quick_sort:           0.0038757666 秒
optimized_quick_sort: 0.0033977667 秒
```

加速倍數：

```text
0.0038757666 / 0.0033977667 = 1.14x
```

時間減少百分比：

```text
(0.0038757666 - 0.0033977667) / 0.0038757666 * 100 = 12.33%
```

所以我的加速策略是**演算法優化 quick sort**，在 4000 筆資料下約 **1.14 倍加速**，也就是執行時間約**減少 12.33%**。

### Stage 4 策略：用 log scale 避免曲線被 bubble sort 壓扁

因為 `bubble_sort` 是 O(n^2)，時間會比 O(n log n) 的 quick / merge / sorted 大很多。如果用線性 y 軸，其他演算法會全部擠在圖底部，很難比較。因此我在 `plot.py` 使用 log scale。

繪圖測試不只檢查函式能呼叫，還檢查 PNG 檔案真的產生且不是空檔。`matplotlib.use("Agg")` 放在 `plot.py` 開頭，確保在沒有 GUI 的環境也能產生圖片。

README 報告則用 2-3 句說明：

- 誰最快
- O(n^2) 與 O(n log n) 的差異
- 加速版的策略與加速比

### Stage 5 策略：把安全問題寫成會紅的測試再修

我依 OpenSSF Secure Coding Guide for Python 從 Stage 1-4 的程式找出適用項目，沒有盲目套用所有安全建議。

我選擇三個會影響這份程式品質的問題寫成紅燈測試：

- `make_data(-1)` 原本沒有拒絕負數，會產生不合理的空資料。
- `run_benchmark(repeats=0)` 原本會造成除以零。
- `load_results` 原本沒有檢查 JSON 結構，讀到 list 也會接受。

修補策略是：

- 對數字輸入加入 `TypeError` / `ValueError`。
- `load_results` 讀 JSON 後確認結果必須是 mapping。
- 保留 `with open(...)` 管理檔案，避免資源未關閉。
- 明確記錄 `random.Random(seed)` 不適用安全亂數規則，因為 benchmark 需要可重現，不需要不可預測。

### 最後檢查策略

完成後我用以下方式確認成品可交：

- `python -m unittest` 全部通過。
- `python benchmark.py` 能產生 `results.json`。
- `python plot.py` 能產生 `assets/benchmark.png`。
- `git log --reverse` 能看到五階段 `test → feat` 順序。
- 所有作業檔案都放在 `weeks/week-16/solutions/1114405029/0611/`。
- `README.md`、`AI_LOG.md`、`TEST_LOG.md` 都存在。

## 訪談摘要

| 階段 | 問了什麼 | 學生答了什麼 | 檢查表狀態 |
|---|---|---|---|
| Stage 1 | `timeit` 為何不應直接 `print`？ | 直接輸出會造成 side effect，破壞輸出格式與測試重複利用。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 2 | 為什麼要驗證原 list 不被修改？哪個排序最容易犯？ | 避免副作用；bubble sort 最容易因 swap 直接修改輸入。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 3 | 為什麼線性 y 軸會讓差異看不清楚？ | O(n^2) 的 bubble sort 會拉高 y 軸，壓扁 O(n log n) 曲線。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 4 | 為什麼 benchmark 不需改用 `secrets`？ | benchmark 要可重現資料，不是不可預測的安全亂數。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
| Stage 5 | 依 OpenSSF 檢查哪些項目？ | 補輸入驗證、JSON 結構驗證、資源管理紀錄，並說明 random 不適用。 | ✅簽名 ✅輸入範圍 ✅例外 ✅edge case ✅驗收 |
