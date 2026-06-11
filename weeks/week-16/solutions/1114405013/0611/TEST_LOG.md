# TEST_LOG

## Stage 1 紅燈：timeit 測試先失敗

```text
python -m unittest test_timing
失敗原因：還沒有 timing.py，所以找不到 timing 模組。
ModuleNotFoundError: No module named 'timing'
FAILED (errors=1)
```

## Stage 1 綠燈：timeit 實作完成

```text
python -m unittest test_timing
通過結果：4 個 timeit 測試全部通過。
Ran 4 tests
OK
```

## Stage 2 紅燈：排序測試先失敗

```text
python -m unittest test_sorts
失敗原因：還沒有 sorts.py，所以找不到 sorts 模組。
ModuleNotFoundError: No module named 'sorts'
FAILED (errors=1)
```

## Stage 2 綠燈：三種排序與 benchmark 完成

```text
python -m unittest test_sorts test_timing
通過結果：排序測試與 timeit 測試全部通過。
Ran 7 tests
OK

python benchmark.py
已產生三種排序的時間表與 results.json。
algorithm        500       1000      2000      4000
bubble_sort      ...       ...       ...       ...
quick_sort       ...       ...       ...       ...
merge_sort       ...       ...       ...       ...
```

## Stage 3 紅燈：加速版共用測試先失敗

```text
python -m unittest test_sorts
失敗原因：測試已加入加速版排序，但還沒有 sorts_fast.py。
ModuleNotFoundError: No module named 'sorts_fast'
FAILED (errors=1)
```

## Stage 3 綠燈：加速版與 baseline 完成

```text
python -m unittest test_sorts test_timing
通過結果：原本排序和加速版排序都通過同一組測試。
Ran 7 tests
OK

python benchmark.py
已產生含加速版與 sorted_baseline 的 results.json。
algorithm          500       1000      2000      4000
bubble_sort        ...       ...       ...       ...
bubble_sort_fast   ...       ...       ...       ...
quick_sort         ...       ...       ...       ...
quick_sort_fast    ...       ...       ...       ...
merge_sort         ...       ...       ...       ...
sorted_baseline    ...       ...       ...       ...
```

## Stage 4 紅燈：畫圖測試先失敗

```text
python -m unittest test_plot
失敗原因：還沒有 plot.py，所以找不到 plot 模組。
ModuleNotFoundError: No module named 'plot'
FAILED (errors=1)
```

## Stage 4 綠燈：圖表輸出完成

```text
python -m unittest test_timing test_sorts test_plot
通過結果：timeit、排序、畫圖測試全部通過。
Ran 9 tests
OK

python plot.py
確認 assets/benchmark.png 已產生，而且不是空檔。
assets/benchmark.png non-empty
```

## Stage 5 紅燈：安全性測試先失敗

```text
python -m unittest test_security
失敗原因：三個安全邊界還沒處理。
FAILED (failures=2, errors=1)
- 負數資料量沒有丟 ValueError
- repeats=0 造成 ZeroDivisionError
- 非 .json 路徑沒有被拒絕
```

## Stage 5 綠燈：安全性修補完成

```text
python -m unittest test_timing test_sorts test_plot test_security
通過結果：全部 12 個測試通過。
Ran 12 tests
OK

python plot.py
確認圖表仍可正常產生。
plot ok
```

## 最終驗證

```text
python -m unittest test_timing test_sorts test_plot test_security
最後結果：全部測試通過。
Ran 12 tests
OK
```
