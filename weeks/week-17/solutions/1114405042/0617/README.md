# 0617 作業：timeit + 搜尋效能評估

## 專案結構

- `timing.py` — 計時裝飾器 `timeit`（含 `repeat` 取平均）
- `test_timing.py` — 完整 TDD 測試（7 個測試案例全綠）
- `search.py` — `linear_search`、`binary_search`
- `benchmark.py` — 搜尋效能比較腳本
- `benchmark_sort.py` — sort+binary vs linear 比較

## 效能評估（n=100,000，目標在中間）

### 1. 誰快？差多少？

**binary_search 快約 417 倍**（0.002 ms vs 0.696 ms）。二分搜尋 O(log n) 只需 ~17 次比較，線性搜尋 O(n) 平均需 50,000 次比較。

### 2. 「排序 + binary」划不划算？

**單次搜尋不划算**：sort+binary 耗時 8.5 ms，比 linear 的 0.7 ms 慢 12 倍。排序的 O(n log n) 成本太高，無法被單次搜尋攤銷。

### 3. 直覺：交叉點在哪裡？

直覺上，**多次搜尋同一組資料時** 會划算。若對同一資料搜尋 k 次：
- linear 總成本：k × O(n)
- sort+binary 總成本：O(n log n) + k × O(log n)

解得交叉點約 k ≈ log n ≈ 17 次。明天用數據驗證。