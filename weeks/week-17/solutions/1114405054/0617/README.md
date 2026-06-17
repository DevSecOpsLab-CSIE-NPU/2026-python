# 0617 預演 — timeit + 搜尋效能評估

## 任務一：timeit

- 支援 `@timeit(repeat=n)` 裝飾器工廠
- 每次呼叫內部跑 `repeat` 次，記錄每次耗時到 `f.records`，`f.last_elapsed` 為平均值
- `repeat < 1` → `raise ValueError`

## 任務二：搜尋評估

### 實驗設定

- 資料量：10,000,000 筆已排序整數
- 搜尋目標：最後一個元素（最差情況 for linear）
- repeat=5 取平均

### 結果

| 演算法 | 平均時間 (s) |
|--------|-------------|
| linear_search | 0.9197 |
| binary_search | 0.000004 |

### 評估

1. **誰快？** binary_search 快約 **20 萬倍**（O(log n) vs O(n)）。
2. **排序 + binary 划不划算？** 如果只查一次，排序成本（O(n log n)）遠高於 linear 的一次掃描，不划算。但如果查詢次數多，排序成本分攤後 binary 會勝出。
3. **交叉點直覺**：單次查詢時，linear 在小資料集更快（無預處理成本）；多次查詢時，排序 + binary 很快就回本。精確交叉點待 6/18 用數據量出來。
