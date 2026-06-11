# AI_LOG

## Stage 1

### Prompt 1
- 使用者需求: 閱讀 Stage 1 規格，拆出至少 3 個 test case，包含 edge case。
- AI 回覆重點: 提供 5 個測試案例，涵蓋回傳值、metadata、時間紀錄、空函式邊界、禁止 print。

### Prompt 2
- 使用者需求: 將變更放到 `weeks/week-16/solutions/1114405007`。
- AI 回覆重點: 複製 starter 到學號目錄，新增 `test_timing.py` 紅燈測試。

### Prompt 3
- 使用者需求: 寫測試 -> 確認紅燈 -> commit。
- AI 回覆重點: 執行 `python -m unittest test_timing.py` 確認紅燈，完成 `test:` commit。

### Prompt 4
- 使用者需求: 寫實作 -> 跑到綠燈 -> commit。
- AI 回覆重點: 新增 `timing.py` 的 `timeit` 裝飾器實作，測試全綠並完成 `feat:` commit。

## 測試紀錄
- `python -m unittest test_timing.py` (紅燈): `ModuleNotFoundError: No module named 'timing'`
- `python -m unittest test_timing.py` (綠燈): `Ran 5 tests ... OK`

## 說明
- Stage 1 不涉及排序效能加速，故「加速百分比」與「演算法優化策略」暫不適用，將於 Stage 2/3 補充。
- Stage 1 已遵守「裝飾器內不使用 print」之安全與規格要求。

## Stage 2

### Prompt 5
- 使用者需求: Stage 2 依規格完成測試拆解與紅綠燈流程。
- AI 回覆重點: 補上共用 subTest 測試，含一般案例、隨機資料比對、輸入不可變。

### Prompt 6
- 使用者需求: 寫實作並讓 Stage 2 轉綠。
- AI 回覆重點: 完成 bubble/quick/merge 三種排序，建立 benchmark 與 results.json。

## Stage 3

### Prompt 7
- 使用者需求: 用同樣流程做 Stage 3。
- AI 回覆重點: 先新增 baseline+加速版測試紅燈，再加入 quick_sort_fast 與 builtin_sorted 進 benchmark。

### 加速成效
- 以本機 benchmark 結果估算，quick_sort_fast 相對 quick_sort 平均加速約 43%~48%。
- 以 n=4000 為例: quick_sort 0.004440s, quick_sort_fast 0.002495s，約提升 43.8%。

### 演算法優化策略
- 使用 in-place quick sort，減少遞迴建立新 list 的額外配置。
- 小區間改用 insertion sort，降低遞迴與分割開銷。
- 使用 median-of-three 取 pivot，降低不平衡分割機率。

## Stage 4

### Prompt 8
- 使用者需求: 實作 plot.py，輸出 benchmark PNG。
- AI 回覆重點: 使用 matplotlib Agg 後端繪製 log scale 折線圖，輸出 assets/benchmark.png，測試檔驗證非空檔。

## Stage 5

### Prompt 9
- 使用者需求: 安全性自掃同樣走紅綠燈。
- AI 回覆重點: 先寫 test_security.py 掃出問題，再修補 benchmark 輸入驗證。

### 修補項目（Python 安全程式原則）
- 修補 1: `make_data` 對 n 做型別與非負驗證，避免異常輸入導致不可預期行為。
- 修補 2: `run_benchmark` 對 repeats 做正整數驗證，避免 division by zero 與資源濫用。
- 修補 3: `run_benchmark` 對 sizes 元素做正整數驗證，避免無效尺寸造成邏輯缺陷。

### 不適用條目
- benchmark 使用 `random` 屬效能測試情境，非安全敏感隨機用途，因此不改用 `secrets`。
