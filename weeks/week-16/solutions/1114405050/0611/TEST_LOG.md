# Test Log

## Stage 1: timeit 裝飾器
```text
# 紅燈 (Red)
FAIL: test_timeit_records_elapsed (test_timing.TestTiming)
AssertionError: AttributeError: 'function' object has no attribute 'last_elapsed'

# 綠燈 (Green)
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s
OK
```

## Stage 2: 三種排序與 benchmark
```text
# 紅燈 (Red)
FAIL: test_bubble_sort_correctness (test_sorts.TestSorts)
AssertionError: Lists differ: [3, 1, 2] != [1, 2, 3]

# 綠燈 (Green)
......
----------------------------------------------------------------------
Ran 6 tests in 0.015s
OK
```

## Stage 3: 加速版排序
```text
# 紅燈 (Red)
FAIL: test_quick_sort_fast_correctness (test_sorts.TestSorts)
AssertionError: NameError: name 'quick_sort_fast' is not defined

# 綠燈 (Green)
........
----------------------------------------------------------------------
Ran 8 tests in 0.021s
OK
```

## Stage 4: 繪圖與報告
```text
# 紅燈 (Red)
FAIL: test_plot_generates_png (test_plot.TestPlot)
AssertionError: FileNotFoundError: assets/benchmark.png does not exist

# 綠燈 (Green)
..
----------------------------------------------------------------------
Ran 2 tests in 0.501s
OK
```

## Stage 5: 安全性自掃
```text
# 紅燈 (Red)
FAIL: test_make_data_handles_negative_size (test_security.TestSecurityRules)
AssertionError: ValueError not raised by make_data

# 綠燈 (Green)
...
----------------------------------------------------------------------
Ran 3 tests in 0.004s
OK
```
