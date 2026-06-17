# 0617 timeit + 搜尋效能評估

## 任務概述

本次任務是 6/18 搜尋效能完整實驗前的預演。主要目標是先用 TDD 完成 `timeit` 計時裝飾器，再用自己實作的 `timeit` 粗略比較 `linear_search` 與 `binary_search` 的搜尋效能。

## 完成項目

### 任務一：`timing.py`

已完成 `timeit(repeat=3)` 裝飾器，功能包含：

- 保留被裝飾函式的原始回傳值
- 使用 `functools.wraps` 保留 `__name__` 與 `__doc__`
- 每次呼叫實際執行 `repeat` 次
- 每次耗時記錄到 `wrapper.records`
- `wrapper.last_elapsed` 記錄本次 repeat 的平均耗時
- 裝飾器內不使用 `print`
- `repeat` 必須是 `int` 且 `>= 1`
- 無效 `repeat` 使用 `raise ValueError`，不使用 `assert`

### 任務二：`search.py`

已完成兩個搜尋函式：

| 函式 | 說明 |
|---|---|
| `linear_search(data, target)` | 從左到右逐一搜尋，找到回傳 index，找不到回傳 `-1` |
| `binary_search(data, target)` | 對已排序資料做二分搜尋，找到回傳 index，找不到回傳 `-1` |

`binary_search` 對未排序資料的定義：

> 本函式不主動檢查 `data` 是否已排序。若傳入未排序資料，結果不保證正確。這樣設計是為了保留 binary search 的 `O(log n)` 搜尋特性。

## 測試結果

最後一次執行 `pytest` 結果：

```text
collected 17 items

test_search.py ........... [ 64%]
test_timing.py ......      [100%]

17 passed in 0.04s
```

## 搜尋效能評估

本次使用 `benchmark_search.py` 測量 `linear_search` 與 `binary_search`：

| 項目 | 數值 |
|---|---:|
| DATA_SIZE | 100,000 |
| REPEAT | 100 |
| target | 99,999 |

量測結果：

| 方法 | 回傳 index | 平均耗時 |
|---|---:|---:|
| `linear_search` | 99,999 | 0.002735066000132065 秒 |
| `binary_search` | 99,999 | 0.0000014110001029621344 秒 |

粗略比較：

```text
linear_search / binary_search ≈ 1938.39 倍
```

## 觀察與判斷

`binary_search` 在這次測試中明顯比 `linear_search` 快，因為資料已經排序，二分搜尋每次都能把搜尋範圍切半；而 `linear_search` 在 target 位於最後一筆時，必須幾乎掃完整個 list。

不過，`binary_search` 的前提是資料已排序。如果資料原本沒有排序，而且只搜尋一次，先排序再二分搜尋不一定划算；如果同一批資料會重複查詢很多次，排序成本被分攤後，`binary_search` 通常會更有優勢。

## 自我檢查

1. `records` 和 `last_elapsed` 掛在 wrapper 上，可以讓每個被裝飾函式各自保留自己的計時狀態，避免使用全域變數造成資料混在一起。
2. 輸入驗證使用 `raise ValueError`，不使用 `assert`，因為 `assert` 在 Python 最佳化模式下可能被停用。
3. `binary_search` 比 `linear_search` 快的前提是資料已排序。
4. 「排序 + binary」在資料只查一次、資料量不大，或排序成本大於搜尋節省時間時，可能比直接 linear search 慢。
