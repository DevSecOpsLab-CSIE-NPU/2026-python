# AI_LOG

## Stage 1: `@timeit` 裝飾器

### 訪談摘要與檢查表狀態

| 項目 | 問了什麼 | 學生答了什麼 / AI 提供的內容 | 檢查表狀態 |
| --- | --- | --- | --- |
| 1. 函式簽名與回傳型別 | `timeit` 裝飾器與 wrapper 的簽名與回傳值 | 裝飾器收 `func` 回傳 `wrapper`；`wrapper` 收 `*args, **kwargs` 回傳原函式結果，並以 `functools.wraps` 保留 metadata | ✅ 已確認 |
| 2. 輸入範圍／邊界條件 | 裝飾器需相容什麼輸入參數形式 | 無參數、僅位置參數、僅關鍵字參數、混合參數及僅限關鍵字參數 | ✅ 已確認 |
| 3. 例外行為 | 函式拋出例外時的處理與時間記錄 | 例外需繼續外拋，且使用 `try...finally` 結構在例外時仍記錄執行時間 | ✅ 已確認 |
| 4. edge case 清單 | 什麼樣的邊緣情況必須測試 | 例外發生的時間記錄、多次呼叫的獨立與累計問題、生成器延遲求值等 | ✅ 已確認 |
| 5. 驗收標準 | 實作前測試應看到何種紅燈 | 因尚未實作，執行時會引發 `ModuleNotFoundError` 或是測試斷言失敗 | ✅ 已確認 |

### 我問 AI 什麼
請幫我確認 Stage 1 的需求與測試案例規格，並協助建立紅燈測試。

### AI 給了什麼
建立了 Stage 1 `test_timing.py` 測試，覆蓋回傳值不變性、Metadata 保留、多輪呼叫時間累計以及例外拋出時的時間記錄。

### 我改了什麼
確認測試代碼符合規格，執行後順利得到 `ModuleNotFoundError` 紅燈，隨後討論並實作 `timing.py` 透過所有測試轉為綠燈。


## Stage 2: 三種排序與量測

### 訪談摘要與檢查表狀態

| 項目 | 問了什麼 | 學生答了什麼 / AI 提供的內容 | 檢查表狀態 |
| --- | --- | --- | --- |
| 1. 函式簽名與回傳型別 | bubble, quick, merge 排序及 make_data / run_benchmark 的簽名與回傳型別 | 排序簽名為 `sort_func(data: list) -> list`，回傳全新排序後的 list。量測為 `make_data(n, seed)` 回傳 list 及 `run_benchmark` 回傳 dict。 | ✅ 已確認 |
| 2. 輸入範圍／邊界條件 | 排序的元素型態與陣列大小範圍 | 支援 int 與 float 等可比較型態。O(n^2) 的 bubble_sort 資料量約在 1000 左右，O(n log n) 演算法可處理 10,000+。 | ✅ 已確認 |
| 3. 例外行為 | 傳入 None 或非 list 型態時的行為 | 應拋出 `TypeError`。 | ✅ 已確認 |
| 4. edge case 清單 | 排序正確性的邊緣情況測試 | 空陣列 `[]`、單一元素 `[42]`、已排序、反向排序、完全重複元素，以及輸入的原 list 不被修改。 | ✅ 已確認 |
| 5. 驗收標準 | 實作前如何呈現合格紅燈 | 執行測試時先出現 `ModuleNotFoundError`，建立空 sorts.py 後測試斷言失敗出現 `AssertionError`。 | ✅ 已確認 |

### 我問 AI 什麼
請幫我確認 Stage 2 的排序與量測規格，並協助設計 `test_sorts.py` 以 subTest 跑多個排序演算法的紅燈測試。

### AI 給了什麼
建立了 `test_sorts.py` 測試骨架並補齊基本/邊緣案例測試、隨機數據對照組、原陣列不被修改測試、例外參數處理測試。

### 我改了什麼
確認以 subTest 的迴圈形式測試 bubble_sort, quick_sort, merge_sort。跑紅燈後，實作 `sorts.py` 中的三種排序演算法，隨後建立 `benchmark.py` 記錄量測時間並導出 `results.json`，完成綠燈測試。


## Stage 3: 加速與 Timsort 對照實驗

### 訪談摘要與檢查表狀態

| 項目 | 問了什麼 | 學生答了什麼 / AI 提供的內容 | 檢查表狀態 |
| --- | --- | --- | --- |
| 1. 函式簽名與回傳型別 | 加速版排序函式的名稱與簽名 | 優化快速排序命名為 `quick_sort_optimized(data: list) -> list`，回傳全新已排序的 list。 | ✅ 已確認 |
| 2. 輸入範圍／邊界條件 | 處理小規模數據時的臨界點優化 | 當陣列大小 $n \le 10$ 時，切換至插入排序（Insertion Sort）以減少遞迴呼叫的 overhead。 | ✅ 已確認 |
| 3. 例外行為 | 例外行為是否與 Stage 2 保持一致 | 一致，傳入 None 或非 list 時拋出 `TypeError`。 | ✅ 已確認 |
| 4. edge case 清單 | 優化策略的特定邊緣情況 | 初始陣列長度即小於臨界點（如 5）、完全排序或反向排序，均須能直接交由插入排序或正確劃分，無遞迴溢出。 | ✅ 已確認 |
| 5. 驗收標準 | 加速實作前的測試紅燈 | 在 `test_sorts.py` 中導入並添加 `quick_sort_optimized`，確認未定義時拋出 `ImportError`；定義空 stub 時測試出 `AssertionError`。 | ✅ 已確認 |

### 我問 AI 什麼
請幫我確認 Stage 3 的加速方案與測試整合，如何優化快速排序並加入 built-in sorted 作為 baseline。

### AI 給了什麼
提供了在 `test_sorts.py` 中引入 `quick_sort_optimized` 的紅燈測試代碼，並提供混合快速排序/插入排序的優化實作，以及在 `benchmark.py` 中添加 `builtin_sorted` 及 `quick_sort_optimized`。

### 我改了什麼
將 `quick_sort_optimized` 加入共用測試，並寫入空 stub 跑出紅燈；之後在 `sorts.py` 實作了當 $n \le 10$ 時切換至插入排序的混合快速排序，並在 `benchmark.py` 中新增該演算法與 Python 內建 `sorted()` 當 baseline。數據測得：在 $n=4000$ 時，原始 `quick_sort` 耗時約 0.0078 秒，優化後的 `quick_sort_optimized` 提升至約 0.0069 秒，加速比約為 12% 左右。


## Stage 4: 畫圖與報告

### 訪談摘要與檢查表狀態

| 項目 | 問了什麼 | 學生答了什麼 / AI 提供的內容 | 檢查表狀態 |
| --- | --- | --- | --- |
| 1. 函式簽名與回傳型別 | 讀取與繪圖的函式簽名與儲存路徑 | `load_results(path: str) -> dict` 與 `plot_results(results: dict, out_path: str) -> None`。圖片儲存於 `assets/benchmark.png`。 | ✅ 已確認 |
| 2. 輸入範圍／邊界條件 | X與Y軸的物理意義，與為什麼Y軸要用 log scale | X軸為資料量，Y軸為耗時。因為 Bubble sort (O(n^2)) 與 Quick sort (O(n log n)) 耗時跨度達數個數量級，不使用對數尺度會導致 O(n log n) 曲線被壓扁在最底部。 | ✅ 已確認 |
| 3. 例外行為 | 讀檔不存在或格式損毀的行為 | 應捕捉 `FileNotFoundError` 與 `json.JSONDecodeError` 並優雅退出。 | ✅ 已確認 |
| 4. edge case 清單 | 繪圖輸出的邊緣案例測試 | 輸出目錄不存在時應自動建立，生成的 PNG 檔案大小不能為 0 字節，若資料為空應安全 return。 | ✅ 已確認 |
| 5. 驗收標準 | 實作繪圖前的 TDD 紅燈 | 建立 `test_plot.py`，因尚未實作 `plot.py` 而出現 `ModuleNotFoundError`。建立空 stub 後測試斷言失敗。 | ✅ 已確認 |

### 我問 AI 什麼
請幫我規劃 Stage 4 繪圖模組的紅燈測試與 `plot.py` 實作，包含 y 軸 Log 尺度的設定與 matplotlib 無介面環境（Agg）的配置。

### AI 給了什麼
建立了 `test_plot.py` 測試以檢查圖表生成與 JSON 讀取功能，並在 `plot.py` 實作中設定 `matplotlib.use("Agg")` 以及 `plt.yscale("log")` 繪製比較折線圖。

### 我改了什麼
執行紅燈測試發現環境缺 `matplotlib` 套件，手動執行 `pip install matplotlib` 進行安裝。安裝完成後，執行 `test_plot.py` 通過所有測試，隨後執行 `python plot.py` 順利產出 `assets/benchmark.png` 比較圖表。


## Stage 5: 安全性自掃

### 訪談摘要與檢查表狀態

| 項目 | 問了什麼 | 學生答了什麼 / AI 提供的內容 | 檢查表狀態 |
| --- | --- | --- | --- |
| 1. 函式簽名與回傳型別 | 安全性檢查是否修改原有簽名 | 不需要，安全性檢查旨在加強程式碼魯棒性，故原有函式名與簽名不作修改。 | ✅ 已確認 |
| 2. 輸入範圍／邊界條件 | 防範 make_data 負數或極大值輸入 | 限制 size 必須為正數，並設定最大上限為 100000 避免 DoS 攻擊與記憶體耗盡。 | ✅ 已確認 |
| 3. 例外行為 | 讀檔與寫檔例外處理 | 必須捕捉具體例外（如 FileNotFoundError, JSONDecodeError, PermissionError），禁止使用 except 全包。 | ✅ 已確認 |
| 4. edge case 清單 | 三個安全性規則檢查案例 | 檔案洩漏與 Context Manager with 語句檢查、make_data 負數/巨大數防禦、make_data 傳入非法參數型態檢查。 | ✅ 已確認 |
| 5. 驗收標準 | 安全檢查實作前測試紅燈 | 建立 `test_security.py`，因原 `make_data` 無例外拋出檢查而出現 `AssertionError: ValueError/TypeError not raised`。 | ✅ 已確認 |

### 我問 AI 什麼
請幫我規劃 Stage 5 安全自掃，找出 Stage 1-4 程式碼中的安全性隱患，編寫 `test_security.py` 並修復。

### AI 給了什麼
規劃了針對 `make_data` 函式傳入負數、巨大數以及非整數參數之安全性防衛測試（`test_security.py`），並提供 `make_data` 對應之防衛檢查實作。

### 我改了什麼
執行 `test_security.py` 得到 3 個預期的紅燈失敗。隨後在 `benchmark.py` 中的 `make_data` 新增了對 `n`（非 int、負數、大於 100000）與 `seed`（非 int）的型態與邊界防禦性檢查，使所有安全性與功能性測試皆轉為綠燈。




