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

