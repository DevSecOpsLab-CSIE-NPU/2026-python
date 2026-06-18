# 0617 — timeit + 搜尋效能評估

## 檔案內容

- `timing.py`: `timeit` 裝飾器（支援 `@timeit` 與 `@timeit(repeat=...)`）
- `test_timing.py`: 任務一單元測試
- `search.py`: `linear_search`、`binary_search`
- `test_search.py`: 任務二單元測試
- `AI_LOG.md`: AI 協作紀錄
- `TEST_LOG.md`: 測試與量測紀錄

## 搜尋效能評估（n = 200000, repeat = 5）

- `linear_search` 平均約 `0.00633s`
- `binary_search`（資料已排序）平均約 `0.00000352s`
- `sorted(data) + binary_search` 平均約 `0.03872s`

在已排序資料上，`binary_search` 比 `linear_search` 快非常多（大約快三個數量級）。
但若每次查詢前都要先排序，排序成本會遠大於一次線性搜尋，所以「排序 + binary」在單次查詢通常不划算。
我的直覺是：只有在同一批資料要查很多次時，先排序才會回本。
