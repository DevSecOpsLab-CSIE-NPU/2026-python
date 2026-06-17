# 0617 — timeit + 搜尋效能評估（學生：1112405062）

## 效能評估

### 實驗設定
- `linear_search` vs `binary_search` 各跑 30 次，取平均
- 資料為隨機整數 sorted list（n = 100, 1k, 10k, 100k）
- target 為 list 內隨機一筆

### 結果

| Size | Linear avg (s) | Binary avg (s) | Ratio (linear/binary) |
|------|---------------|---------------|----------------------|
| 100 | 0.0000069 | 0.0000006 | 11.3x |
| 1,000 | 0.0000016 | 0.0000008 | 2.0x |
| 10,000 | 0.0000685 | 0.0000011 | 61.7x |
| 100,000 | 0.0020857 | 0.0000015 | 1387.4x |

### 直覺判斷

1. **誰快**——binary search 在每個量級都更快，且資料越大差距越懸殊（100k 時快 ~1400 倍）。
2. **排序划不划算**——如果資料只需排序一次、查詢很多次，排序成本可以被攤提，binary search 非常划算。但若只查一次，O(n log n) 排序 + O(log n) 二分可能不如直接 O(n) linear。
3. **直覺**——linear search 跑起來像 O(n)，每增 10 倍耗時也增約 10 倍。binary search 的 O(log n) 增長極慢，100→100k（1000 倍）耗時只從 0.6µs 增加到 1.5µs。

> 精確交叉點留待 6/18 完整實驗室量測。

## 檔案一覽

- `timing.py` — `timeit` 裝飾器（支援 `@timeit` / `@timeit(repeat=N)`）
- `search.py` — `linear_search` / `binary_search`
- `test_timing.py` — timeit 測試（9 案例）
- `test_search.py` — search 測試（17 案例）
- `benchmark.py` — 效能量測腳本
- `AI_LOG.md` — AI 協作紀錄
- `TEST_LOG.md` — 測試執行紀錄
