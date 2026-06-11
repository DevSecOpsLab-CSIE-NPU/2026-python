# AI_LOG — Week 16 / 0611 排序效能實驗室

---

## 提示詞逐字紀錄

| # | 我問 AI 什麼 | AI 給了什麼 | 我改了什麼 |
|---|------------|------------|-----------|
| 1 | 讀 weeks/week-16/in_class/0611-sort-lab.md 設計 3 個以上 test case 符合題目要求 | 針對 Stage 1（timeit）與 Stage 2（三種排序）各設計 5/7 個測試案例，含 edge case 與 subTest | 確認測試邏輯符合規格後直接採用 |
| 2 | 將設計出的 test case 寫測試確認紅燈放到 weeks\week-16\solutions\1111405038\0611 | 建立 test_timing.py 與 test_sorts.py，跑 unittest 確認全紅（ImportError） | 確認兩檔紅燈輸出後 commit |
| 3 | 寫實作放到 C:\...\0611 直到綠燈 | 建立 timing.py（functools.wraps + last_elapsed + records）與 sorts.py（bubble/quick/merge，回傳新 list） | 確認 12 tests OK 後 commit |
| 4 | weeks\week-16\solutions\1111405038\0611 讀檔案檢查後整理要做的和做了什麼跟接下來要做什麼 | 列出已完成 Stage 1/2、缺少 benchmark.py、sorts_fast.py、plot.py、test_stage3/plot/security、README、TEST_LOG、commits | 確認清單後依序進行 Stage 3 |
| 5 | 做 Stage 3 red test | 建立 test_stage3.py，含 baseline timsort 與加速版正確性 4 個測試，跑出 ModuleNotFoundError 紅燈 | 確認紅燈後 commit |
| 6 | 做到綠燈 | 建立 sorts_fast.py（median-of-three + insertion sort + tail-call 優化）與 benchmark.py（含 timsort baseline），16 tests OK | 執行 benchmark.py 產生 results.json 後 commit |
| 7 | 做 Stage 4 的 red test | 建立 test_plot.py，含 load_results 與 plot_results 2 個測試，跑出 ModuleNotFoundError 紅燈 | 確認紅燈後 commit |
| 8 | 做到綠燈 | 建立 plot.py（matplotlib Agg backend、log scale、自動建目錄），18 tests OK，執行後產生 assets/benchmark.png | 確認圖片存在且非空後 commit |
| 9 | 做 Stage 5 red test | 建立 test_security.py，3 條紅測試（n=0 邊界、sizes=0 邊界、JSON 錯誤訊息），1 條已通過（json not pickle） | 確認 3 條失敗後 commit |
| 10 | 做到綠燈 | 修改 benchmark.py（n>0 / sizes>0 驗證）與 plot.py（json.JSONDecodeError 轉 ValueError），22 tests OK | 確認全綠後 commit |
| 11 | 每個測試都要有三個以上 test case | 補充 test_plot.py 至 5 個測試（key 為 int、value 為 float、自動建目錄），25 tests OK | 確認全綠 |

---

## (1) 加速多少百分比

benchmark 在 n=4000 筆資料（repeats=3 次平均）的量測結果：

| 演算法 | n=4000 平均耗時(秒) | 與原版 quick_sort 比較 |
|--------|--------------------|-----------------------|
| bubble_sort | 0.4687 | — |
| quick_sort（原版） | 0.00431 | baseline |
| merge_sort | 0.00512 | — |
| quick_sort_fast（加速版） | 0.00259 | **約加速 40%（0.00431 → 0.00259）** |
| timsort（內建 C 實作） | 0.000264 | — |

quick_sort_fast 相較原版 quick_sort，在 n=4000 時快了約 **40%**。

---

## (2) 演算法優化的策略為何？

採用 Python 純演算法優化（不使用 Cython），策略共三點：

1. **Median-of-Three pivot 選擇**：取 `data[low]`、`data[mid]`、`data[high]` 三者的中間值作為 pivot，避免原版取固定位置在已排序資料上退化成 O(n²)。

2. **小區間切換 Insertion Sort**：當分段長度 ≤ 16 時，改用 insertion sort 而非繼續遞迴，減少遞迴呼叫的常數開銷（cache 友善、無額外 list 建立）。

3. **Tail-call 優化（迴圈取代遞迴）**：先遞迴較小的分段，較大的分段改用 `while` 迴圈推進，降低最差情況下的遞迴深度，避免 Python 預設遞迴上限被觸發。

---

## (3) 依 Python 安全程式原則，修補幾項程式問題

依 OpenSSF Secure Coding Guide for Python 共找到並修補 **3 項**，判定不適用 **1 項**：

| # | OpenSSF 條目 | 問題 | 處理方式 |
|---|-------------|------|---------|
| 1 | Numbers / 邊界條件（CWE-20） | `make_data(n)` 原本允許 `n=0`，會產生空資料進 benchmark，量測結果無意義 | 改為 `n <= 0` 時拋出 `ValueError("n must be > 0")` |
| 2 | Numbers / 邊界條件（CWE-20） | `run_benchmark(sizes=...)` 未驗證 sizes 內是否含非正值，允許 `n=0` 進入量測迴圈 | 增加 `any(n <= 0 for n in sizes)` 檢查，拋出 `ValueError("sizes must be positive")` |
| 3 | Exception Handling（CWE-390） | `load_results()` 直接讓 `json.JSONDecodeError` 拋出，錯誤訊息為底層 parse 細節，不易判讀 | 改為捕捉 `json.JSONDecodeError` 並轉拋 `ValueError("invalid json")` |
| — | Neutralization（CWE-502） | 判定**不適用**：`load_results()` 讀取的是自己產生的 `results.json`，已使用 `json.load()` 而非 `pickle`，不需修改 | 確認用 `json` 正確，無安全疑慮 |