# BinarySearch 測試紀錄

## 測試指令
```bash
python -m unittest test_binary_search.py
```

## 測試結果
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

## 測試案例

| 測試名稱 | 目的 |
|---|---|
| test_linear_found | 驗證線性搜尋找到目標 |
| test_linear_not_found | 驗證線性搜尋找不到目標 |
| test_binary_found | 驗證二分搜尋找到目標 |
| test_binary_not_found | 驗證二分搜尋找不到目標 |
| test_target_at_ends | 驗證目標在陣列開頭與末尾 |

## 效能數據（陣列大小 100,000）
```
FOUND 77 cmp=78
FOUND 77 cmp=14
linear : 0.00000363 s
binary : 0.00000179 s
=> binary faster
```
