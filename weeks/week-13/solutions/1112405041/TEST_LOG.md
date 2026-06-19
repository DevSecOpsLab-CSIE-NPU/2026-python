# 測試執行記錄

## Stage 1：data_loader

### 紅燈
```
$ python -m unittest tests/test_data_loader.py -v
... (10 errors: ModuleNotFoundError)
FAILED (errors=10)
```

### 綠燈
```
$ python -m unittest tests/test_data_loader.py -v
... (9 ok)
OK
```

## Stage 2：analysis

### 紅燈
```
$ python -m unittest tests/test_analysis.py -v
... (8 errors: ModuleNotFoundError)
FAILED (errors=8)
```

### 綠燈
```
$ python -m unittest tests/test_analysis.py -v
test_get_top_depts_length ... ok
...
OK
```

## Stage 3：plot

### 紅燈
```
$ python -m unittest tests/test_plot.py -v
... (3 errors: ModuleNotFoundError)
FAILED (errors=3)
```

### 綠燈
```
$ python -m unittest tests/test_plot.py -v
test_task1_png_created ... ok
test_task1_top_depts_empty ... ok
test_task2_png_created ... ok
OK
```

## Stage 4：輸出驗證

### 綠燈
```
$ python -m unittest tests/test_report.py -v
test_task1_png_exists ... ok
test_task1_png_nonempty ... ok
test_task2_png_exists ... ok
test_task2_png_nonempty ... ok
OK
```

## Stage 5：安全自掃

### 綠燈
```
$ python -m unittest tests/test_security.py -v
... (5 ok)
OK
```
