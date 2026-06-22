# TEST_LOG - 第四題 二分搜尋效能

## 測試環境
- Python 3.12
- unittest 框架
- 測試日期: 2026/06/22
- K = 103

## 測試結果

```
test_binary_cmp_count ... ok
test_empty_array ... ok
test_first_element ... ok
test_found_middle ... ok
test_generate_sorted_array ... ok
test_large_array_binary ... ok
test_large_array_linear ... ok
test_last_element ... ok
test_linear_cmp_count ... ok
test_linear_search_first ... ok
test_linear_search_found ... ok
test_linear_search_last ... ok
test_linear_search_not_found ... ok
test_not_found ... ok
test_single_element_found ... ok
test_single_element_not_found ... ok

----------------------------------------------------------------------
Ran 16 tests in 0.116s

OK
```

## 主程式測試

輸出:
```
FOUND 52 cmp=18
linear : 0.0000 s
binary : 0.0000 s
=> binary faster
雷達圖已儲存: assets/radar.png
```

符合預期！
