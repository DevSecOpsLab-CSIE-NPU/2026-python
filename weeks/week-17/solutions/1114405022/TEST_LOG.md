# TEST_LOG — 0617

## 任務一 timing.py

| 測試 | 狀態 | 備註 |
|------|------|------|
| test_returns_original_result | ✅ PASS | 裝飾前後回傳值一致 |
| test_preserves_function_metadata | ✅ PASS | __name__ / __doc__ 保留 |
| test_records_each_repeat_and_average | ✅ PASS | records 長度 = repeat, last_elapsed = float |
| test_rejects_invalid_repeat | ✅ PASS | repeat < 1 → ValueError |

## 任務二 search.py

| 測試 | 狀態 | 備註 |
|------|------|------|
| test_linear_search_found | ✅ PASS | 正常找到 |
| test_linear_search_not_found | ✅ PASS | 找不到回傳 -1 |
| test_linear_search_empty | ✅ PASS | 空串列 |
| test_linear_search_single | ✅ PASS | 單一元素 |
| test_binary_search_found_sorted | ✅ PASS | 已排序找到 |
| test_binary_search_not_found_sorted | ✅ PASS | 找不到回傳 -1 |
| test_binary_search_empty | ✅ PASS | 空串列 |
| test_binary_search_single | ✅ PASS | 單一元素 |
| test_binary_search_rejects_unsorted | ✅ PASS | 未排序 → ValueError |

---

### 全部測試：13/13 ✅ PASS
