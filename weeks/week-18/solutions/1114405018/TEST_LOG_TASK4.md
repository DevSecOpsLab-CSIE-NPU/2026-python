# Binary Search Performance - Test Record (K=118)

## Parameters
- 學號末兩碼: 18
- K = 100 + 18 = 118
- 陣列: 0 ~ 99,999 (升冪排序, 100,000 元素)

## Sample Run
```
FOUND idx=117 cmp=16
linear : 0.000361 s
binary : 0.000221 s
=> binary faster
```

## Binary Search Process (K=118 in 100,000 elements)
| Step | lo | hi | mid | arr[mid] | 比較結果 |
|------|----|----|-----|----------|----------|
| 1 | 0 | 99999 | 49999 | 50000 | > K |
| 2 | 0 | 49998 | 24999 | 25000 | > K |
| 3 | 0 | 24998 | 12499 | 12500 | > K |
| 4 | 0 | 12498 | 6249 | 6250 | > K |
| 5 | 0 | 6248 | 3124 | 3125 | > K |
| 6 | 0 | 3123 | 1561 | 1562 | > K |
| 7 | 0 | 1560 | 780 | 781 | > K |
| 8 | 0 | 779 | 389 | 390 | > K |
| 9 | 0 | 388 | 194 | 195 | > K |
| 10 | 0 | 193 | 96 | 97 | < K |
| 11 | 97 | 193 | 145 | 146 | > K |
| 12 | 97 | 144 | 120 | 121 | > K |
| 13 | 97 | 119 | 108 | 109 | < K |
| 14 | 109 | 119 | 114 | 115 | < K |
| 15 | 115 | 119 | 117 | 118 | = K |
| **總比較次數** | | | | | **16** |

## Timeit 比較 (100 次迭代)
| 方法 | 總耗時 (s) | 單次平均 (μs) |
|------|------------|---------------|
| 線性搜尋 | 0.000361 | 3.61 |
| 二分搜尋 | 0.000221 | 2.21 |
| **結論** | | **二分較快** |

## 測試結果
```
test_binary_search_empty ................ ok
test_binary_search_first_element ........ ok
test_binary_search_found ................ ok
test_binary_search_last_element ......... ok
test_binary_search_not_found ............ ok
test_binary_search_single_element ....... ok
test_linear_search_found ................ ok
test_linear_search_not_found ............ ok
test_timeit_compare_runs ................ ok
```
9/9 tests passed ✅

## 雷達圖
已輸出：`assets/radar.png`
- 維度：小 n 速度、大 n 速度、實作簡易度、最壞情況比較次數、需先排序
- 正規化：各維度在兩方法間 min-max 到 0~1（越小越好維度取倒數）
- 解讀見 README
