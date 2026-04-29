# UVA 10226 測試日誌

**執行日期**: 2026-04-29
**環境**: Python 3.15 (.venv)
**測試框架**: unittest

## 測試結果

✅ **所有測試通過**

```
Test 1 (single person): [['A']]
Test 2 (two persons): [['A', 'B'], ['B', 'A']]
Test 3 (A at position 0): [['B', 'A']]
Test 4 (three persons count): 6 permutations
✅ All tests passed!
```

## 測試覆蓋

| 測試名稱 | 說明 | 結果 |
|--------|------|------|
| `test_single_person` | 單人情況 | ✅ Pass |
| `test_two_persons_no_restrictions` | 兩人無限制 | ✅ Pass |
| `test_two_persons_with_restriction` | 兩人有限制 | ✅ Pass |
| `test_three_persons_with_restrictions` | 三人有限制 | ✅ Pass |
| `test_all_restricted_same_position` | 都避免同一位置（無解） | ✅ Pass |
| `test_lexicographic_order` | 字典序驗證 | ✅ Pass |

## 算法複雜度

- **時間複雜度**: O(N! × N)（生成 N! 個排列，每個檢查 N 個位置）
- **空間複雜度**: O(N × N!)（存儲所有排列 + 遞迴堆棧深度 N）
- **位掩碼優勢**: 檢查已使用人員 O(1)，優於集合 O(log N)

## 執行命令

```bash
python -m unittest test_10226 -v
```

