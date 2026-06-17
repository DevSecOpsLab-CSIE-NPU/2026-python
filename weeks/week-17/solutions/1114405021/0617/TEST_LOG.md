# TEST_LOG — 0617 timeit + 搜尋效能評估

## 任務一：timeit 裝飾器（紅燈）

```
$ python -m unittest test_timing.py
EEEEEEEEEE
...
FAILED (errors=10)
```

commit: `a79662c test: 0617 timeit 裝飾器測試`

## 任務一：timeit 裝飾器（綠燈）

```
$ python -m unittest test_timing.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.460s
OK
```

commit: `2af0c62 feat: 0617 實作 timeit 裝飾器`

## 任務二：搜尋演算法（綠燈）

```
$ python -m unittest test_search.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.000s
OK
```

## 全部測試（任務一 + 任務二）

```
$ python -m unittest test_timing.py test_search.py -v
...
Ran 18 tests in 0.128s
OK
```

## Benchmark 結果

```
       n   linear (s)   binary (s)      ratio
--------------------------------------------
     100     0.000002     0.000002       1.47x
    1000     0.000027     0.000002      12.07x
   10000     0.000294     0.000004      81.13x
  100000     0.003101     0.000013     246.14x
```
