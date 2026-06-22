# AI_LOG

## 一、基本資訊
- 日期：2026-06-22
- 題目：第四題 二分搜尋效能
- 學號：1114405015
- 姓名：簡嘉佑
- 搜尋目標：K = 115（計算：100 + 學號末兩碼 15）

補充：題目包含「搜尋是否存在、統計比較次數、timeit 效能測量、雷達圖繪製」四大部分。

## 二、題目理解紀錄

### 1) 我對題目的拆解
本題有四個核心工作：
1. **搜尋部分**
   - 接收一個升冪整數陣列（題目提供或程式產生）。
   - 用二分搜尋找 K=115。
   - 回報 FOUND idx 或 NOT FOUND，以及比較次數 cmp。
   
2. **效能測量部分**
   - 用 timeit 對同一資料集重複執行 linear 與 binary 各多次。
   - 計算平均耗時並輸出。
   - 判斷誰更快。
   
3. **視覺化部分**
   - 產出雷達圖 assets/radar.png。
   - 五個維度呈現兩種搜尋的權衡（不是絕對結論）。

### 2) 輸入格式（兩種模式）
- **模式 A（題目格式）**：
  - 第 1 行：m（陣列大小）
  - 後續行：m 個整數（可跨行）
  
- **模式 B（自動產生）**：
  - 若無有效輸入，自動產生升冪陣列 [0, 1, ..., 199999]。
  - 目的是確保 n 足夠大，timeit 能看出效能差異。

### 3) 輸出格式
```
FOUND idx cmp=比較次數
  或
NOT FOUND cmp=比較次數
linear: t秒
binary: t秒
=> 誰較快
```

### 4) 易錯點
- 不能搞混「比較次數 cmp」與「執行耗時」。
- 若陣列未排序，binary 會錯誤；需要自動排序。
- timeit 需要取平均，不能只看一次。
- matplotlib 是外部依賴，須小心環境問題。

## 三、AI 協助紀錄（逐步）

### Step 1：規格確認
- AI 協助確認 I/O 模式與 K 值計算。
- AI 提醒「cmp」是演算法核心行為，timeit 是系統成本，兩者都要展示。

### Step 2：演算法設計
- AI 提供 linear_search：逐一掃過，計算比較次數。
- AI 提供 binary_search：標準二分法，計算 mid 每次都是一次 cmp。

### Step 3：輸入處理
- AI 協助設計 parse_or_generate_array：支援兩種模式。
- AI 建議自動排序，確保 binary 正確。

### Step 4：效能測量
- AI 協助整合 timeit.repeat：重複多次取平均（減少雜訊）。
- AI 建議 repeats=5、number=1 為平衡點。

### Step 5：雷達圖設計
- AI 協助選 5 個維度，各自 0..10 正規化。
- AI 協助用 matplotlib 的 polar 座標系。
- AI 提醒設定 matplotlib.use("Agg") 以支援 headless 環境。

### Step 6：文件與測試
- AI 協助編寫 unittest（正常、反例、工具函式）。
- AI 協助補齊 README 與本 AI_LOG。

## 四、關鍵決策與理由

### 決策 A：K = 115（固定值）
- 理由：依作業紙要求，K = 100 + 末兩碼。

### 決策 B：輸入無效時自動建 [0..199999]
- 理由：
  - 題目允許「輸入或產生」。
  - 要比較效能，n 需足夠大（200000）才能看出差異。
  - 小資料集上 timeit 都很快，雜訊比信號大。

### 決策 C：parse 階段自動排序
- 理由：二分搜尋要求升冪陣列，直接排序避免邏輯錯誤。

### 決策 D：分離 cmp 與 timeit
- 理由：
  - cmp 是「演算法層面」的行為（有多少次相等、小於、大於判斷）。
  - timeit 是「執行層面」的成本（受 CPU、記憶體、Python VM 等影響）。
  - 兩者都看，故事才完整：binary 比較次數少但實測不一定更快。

### 決策 E：雷達圖 5 維度正規化
- 理由：
  - 客觀呈現取捨，不落入「binary 一定最快」的誤區。
  - 正規化到 0..10 便於視覺比較。

## 五、演算法摘要

### 1) Linear Search
```
for idx, value in enumerate(arr):
    cmp_count += 1
    if value == target:
        return idx, cmp_count
return -1, cmp_count
```
特點：每個元素都比較一次。

### 2) Binary Search
```
left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    cmp_count += 1
    if arr[mid] == target:
        return mid, cmp_count
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1, cmp_count
```
特點：每次 mid 比較是一次 cmp，最多 log₂n 次。

### 3) Benchmark 邏輯
```
for i in range(repeats):
    time_used = timer.timeit(number=number)
    times.append(time_used)
avg_time = sum(times) / len(times)
```

## 六、手動驗證紀錄

### Case 1：FOUND（包含目標值）
- 輸入：[..., 115, ...]
- binary_search 結果：FOUND idx cmp=?
- 驗證：idx 有效（>= 0），cmp 為正整數。

### Case 2：NOT FOUND（不含目標值）
- 輸入：[0, 2, 4, 6, 8]（不含 115）
- binary_search 結果：NOT FOUND cmp=?
- 驗證：idx = -1，cmp 為正整數。

### Case 3：自動生成
- 無輸入時建 [0..199999]。
- 包含 115，搜尋結果應為 FOUND 115。
- 驗證：cmp <= log₂(200000) ≈ 18。

### Case 4：Timeit 輸出
- linear & binary 都執行數次。
- 輸出均為正浮點數（秒）。
- 驗證：binary 耗時 < linear 耗時（通常，但環境相依）。

### Case 5：雷達圖產生
- 檔案 assets/radar.png 存在且有效。
- 驗證：大小 > 0，可用圖檢視器打開。

## 七、測試策略與覆蓋

### 測試類型
1. **函式單元測試**：linear_search、binary_search。
2. **輸入模式測試**：題目格式、自動產生。
3. **工具函式測試**：format_search_result、faster_label、parse_or_generate_array。
4. **常數驗證**：K = 115。

### 目前狀態
- 已完成 9 個測試函式（全過）。
- 語法與靜態檢查無錯誤。
- 功能驗證：FOUND 16 cmp=5，binary 比 linear 快。

## 八、風險與修正紀錄

### 風險 1：輸入陣列不是升冪
- 修正：parse_or_generate_array 在第 8 行檢查並排序。

### 風險 2：未安裝 matplotlib
- 修正：README 標註依賴，若無法產圖提醒安裝。
- 修正：將繪圖邏輯獨立在 plot_radar.py，便於除錯。

### 風險 3：timeit 有雜訊
- 修正：repeat 5 次取平均（繁殖、GC、CPU 抖動會淡化）。

### 風險 4：K 值代碼硬寫
- 修正：常數放在模組頂端 K=115，便於改動。

## 九、我學到的重點

1. **演算法 vs 實測**：
   - 二分搜尋比較次數確實少（O(log n)）。
   - 但實測時間受 CPU 快取、記憶體存取等影響，不一定呈現線性差異。

2. **正規化與可視化**：
   - 雷達圖能同時呈現多維度，避免單一指標誤導。

3. **測試設計**：
   - 既要測小資料（確認邏輯），也要測大資料（確認效能）。

## 十、交付檔案清單

- question_4_solution.py
- plot_radar.py
- test_question_4.py
- test_input.txt
- test_output_example.txt
- README.md
- AI_LOG.md（本檔）
- assets/radar.png（執行主程式或繪圖函式產生）

## 十一、結論

- 本題已完成搜尋、效能測量、視覺化與文件。
- AI 主要提供規格拆解、核心演算法、測試框架、繪圖邏輯。
- 最終所有決策與驗證由本人確認，可於 demo 時清楚說明四大部分如何連鎖運作。
