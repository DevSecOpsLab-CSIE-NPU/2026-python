# 測試紀錄 - 0618 搜尋效能實驗室

## Stage 1：timeit 裝飾器

### ❌ 紅燈
```
$ python -m unittest test_timing.py
ImportError: No module named 'timing'
```
### ✅ 綠燈
```
$ python -m unittest test_timing.py
....
Ran 4 tests in 0.000s
OK
```

## Stage 2：搜尋正確性

### ❌ 紅燈
```
$ python -m unittest test_search.py
ImportError: No module named 'search'
```
### ✅ 綠燈
```
$ python -m unittest test_search.py
......
Ran 6 tests in 0.000s
OK
```

## Stage 4：雷達圖輸出

### ❌ 紅燈
```
$ python -m unittest test_plot.py
FAIL: test_radar_png_exists (assets/radar.png 不存在)
```
### ✅ 綠燈
```
$ python -m unittest test_plot.py
..
Ran 2 tests in 0.000s
OK
```

## Stage 5：安全自掃

### ❌ 紅燈
```
$ python -m unittest test_security.py
FAIL: test_make_data_rejects_negative_n (ValueError not raised)
```
### ✅ 綠燈
```
$ python -m unittest test_security.py
...
Ran 3 tests in 0.004s
OK
```

## 全部測試總跑

```
$ python -m unittest discover
............
```