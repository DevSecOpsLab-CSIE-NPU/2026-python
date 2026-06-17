
# TEST_LOG — 0617 timeit + 搜尋評估
 
執行環境:Python 3.12.8 / `python -m unittest`,工作目錄 `weeks/week-17/solutions/36/0617`。
 
## 任務一 timeit:紅 → 綠
 
### 紅燈(commit `test:` 之前)
`test_timing.py` 補齊測試、解除 `from timing import timeit` 註解,但 `timing.py` 尚未建立:
 
```
ImportError: Failed to import test module: test_timing
ModuleNotFoundError: No module named 'timing'
Ran 1 test in 0.000s
FAILED (errors=1)
```
 
→ 全紅,符合「先紅燈」。commit:`test: 0617 timeit 裝飾器測試`。
 
### 綠燈(寫完 timing.py)
```
Ran 6 tests in 0.000s
OK
```
 
涵蓋規格:
- `test_returns_original_result` — 規格 1 回傳值不變
- `test_preserves_function_metadata` — 規格 2 `functools.wraps`
- `test_records_each_repeat_and_average` — 規格 3 records 累積 + last_elapsed 平均
- `test_repeat_one_runs_function_once_per_call` — edge case repeat=1,副作用不被多算
- `test_default_repeat_runs_function_three_times` — edge case 預設跑 3 次
- `test_rejects_invalid_repeat` — 規格 5 repeat<1 raise ValueError(安全測試)
 
commit:`feat: 0617 實作 timeit 裝飾器`。
 
## 任務二 search:全套綠燈
 
`test_search.py` 共 10 筆(linear 5 + binary 5):回傳 index / 找不到 -1 /
不修改傳入 data / 空 list。與 timeit 測試合跑:
 
```
Ran 16 tests in 0.000s
OK
```
 
## 評估數據(benchmark.py)
`n = 2,000,000`、`data = range(n)`(已排序)、`target` = 最後一個元素:
 
| 函式 | 平均耗時(秒) |
|------|--------------|
| linear_search | ~0.0506 |
| binary_search | ~0.0000044 |
 
→ binary 快約 11,000 倍(詳見 README 評估段)。