
# TEST_LOG — 0618 搜尋效能五階段
 
執行環境：Python 3.12.8 / `python -m unittest`，工作目錄
`weeks/week-17/solutions/1114405036/0618`。每階段先紅後綠。
 
## Stage 1 — timeit
 
紅（`test_timing.py` 已補測試，但 `timing.py` 尚未建立）：
 
```
ImportError: No module named 'timing'
Ran 1 test in 0.000s
FAILED (errors=1)
```
 
綠（寫完 `timing.py`）：
 
```
Ran 6 tests in 0.000s
OK
```
 
涵蓋：回傳值不變 / wraps metadata / records 累積 + last_elapsed 平均 / 自訂 repeat /
不 print / repeat<1 raise ValueError。
 
## Stage 2 — 三種搜尋
 
紅（`test_search.py` 引用尚未建立的 `search.py`）：
 
```
ImportError: No module named 'search'
Ran 1 test in 0.000s
FAILED (errors=1)
```
 
綠（寫完 `search.py`，三搜共用 subTest）：
 
```
Ran 9 tests in 0.000s
OK
```
 
接著 `python benchmark.py` 產生 `results.json`（linear / binary / set）。
 
## Stage 3 — baseline 與交叉點
 
`docs: stage3 加速前預測` 先於數據 commit（`git log --reverse` 可驗順序）。
 
紅（`test_search.py` 加入 `bisect_search` / `builtin_in`，但 `benchmark.py` 尚未提供）：
 
```
ImportError: cannot import name 'bisect_search' from 'benchmark'
FAILED (errors=1)
```
 
綠（`benchmark.py` 加 baseline + `find_crossover`，同一組正確性測試全過）：
 
```
Ran 9 tests in 0.001s
OK
```
 
交叉點（本機）：回本所需查詢次數約 n=1000→4.4、5000→5.2、20000→6.1、80000→7.5。
 
## Stage 4 — 雷達圖
 
紅（`test_plot.py` 引用尚未建立的 `plot.py`）：
 
```
ImportError: No module named 'plot'
Ran 1 test in 0.000s
FAILED (errors=1)
```
 
綠（寫完 `plot.py`，產出 `assets/radar.png`）：
 
```
Ran 1 test in 0.118s
OK
```
 
## Stage 5 — 安全自掃
 
紅（`test_security.py` 三條規則，`benchmark.py` 尚未強化輸入驗證、也沒有 `load_results`）：
 
```
ERROR: test_load_results_round_trips_json — module 'benchmark' has no attribute 'load_results'
ERROR: test_load_results_missing_file_raises — module 'benchmark' has no attribute 'load_results'
FAIL/ERROR: test_make_data_rejects_non_int — TypeError 而非 ValueError
Ran 5 tests in 0.002s
FAILED (failures/errors=3)
```
 
綠（make_data 加明確輸入驗證、加 `load_results`（json、特定例外））：
 
```
Ran 5 tests in 0.002s
OK
```
 
## 全部一起
 
```
$ python -m unittest test_timing test_search test_plot test_security
Ran 21 tests in 0.106s
OK
```