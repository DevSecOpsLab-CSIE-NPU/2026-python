# 0617 — timeit + 搜尋效能評估

## 任務一：timeit 裝飾器

用 TDD 實作 `timing.py`，提供 `timeit` 裝飾器，規格：
- 回傳值不變；`functools.wraps` 保留 metadata
- 每次呼叫跑 `repeat` 次（預設 3），每次耗時記錄在 `f.records`
- `f.last_elapsed` = 本次 `repeat` 的平均耗時
- 裝飾器內不准 `print`
- `repeat < 1` → `raise ValueError`

## 任務二：搜尋效能評估

### benchmark 結果（n = 100,000）

| 搜尋方法 | 平均耗時 |
|---------|---------|
| linear_search | 0.002880s |
| binary_search | 0.000004s |

**binary 比 linear 快 732 倍。**

### 評估

1. **誰快？差多少？**
   binary_search 明顯更快，在 100,000 筆資料下快了約 732 倍。這是因為 linear_search 是 O(n)，binary_search 是 O(log n)，隨著 n 增大差距會更明顯。

2. **「排序 + binary」划不划算？我的直覺是：**
   如果只需要搜尋一次，排序的成本（O(n log n)）可能比直接 linear_search（O(n)）還高，不划算。但如果要搜尋很多次，先排序一次再用 binary_search 就划算了。交叉點大概在「搜尋次數 > n / log n」左右。

3. **精確交叉點是明天 6/18 要用數據量出來的。**
