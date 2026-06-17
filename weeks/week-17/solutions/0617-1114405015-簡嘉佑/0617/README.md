# 0617 Search Eval Solution

本次在 `n = 200000`、`repeat = 5` 的量測下，`linear_search` 平均約 `0.0041901s`，`binary_search` 平均約 `0.0000020s`，`binary_search` 約快 `2095` 倍。若資料原本已排序、或同一份資料會被查很多次，通常「先排序 + binary」會划算；但若只查一次且資料未排序，排序成本可能吃掉優勢。今天我的直覺是：查詢次數越多、資料越大，`sort + binary` 越容易勝出；交叉點要在 6/18 再用完整實驗量出來。

## Files

- `timing.py`: `timeit` decorator implementation
- `test_timing.py`: unit tests for `timeit`
- `search.py`: `linear_search` and `binary_search`
- `test_search.py`: basic tests for search functions
- `benchmark_search.py`: quick benchmark script
