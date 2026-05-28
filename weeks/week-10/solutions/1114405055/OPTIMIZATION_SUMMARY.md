# 測試檔案優化說明

## test_task10189.easy.py
**原始檔案**: test_task10189.py
**優化內容**:
- 合併 `test_sample_case()` 和 `test_single_mine()` 兩個測試方法
- 使用統一的 `test_all_cases()` 方法搭配 `subTest` 執行
- 測試用例改用元組列表 `cases` 集中管理
- 簡化路徑設置：`sys.path.insert(0, str(Path(__file__).resolve().parent))`
- **代碼行數**: 24 行 → 15 行（減少 38%）
- **易維護性**: 新增測試只需在 `cases` 列表中新增元組

## test_task10190.easy.py
**原始檔案**: test_task10190.py
**優化內容**:
- 合併 `test_valid_and_invalid()` 和 `test_non_divisible_midway()` 兩個測試方法
- 使用統一的 `test_all_cases()` 方法
- 測試用例以列表管理，易於擴展
- 相同的路徑設置簡化
- **代碼行數**: 20 行 → 15 行（減少 25%）
- **測試集中化**: 所有測試數據在 `cases` 列表中明確列出

## test_task10193.easy.py
**原始檔案**: test_task10193.py
**優化內容**:
- 合併 `test_mixed_pairs()` 和 `test_all_need_love()` 兩個測試方法
- 使用統一的 `test_all_cases()` 方法
- 長字符串保持可讀性，使用列表管理測試用例
- 路徑設置統一簡化
- **代碼行數**: 22 行 → 16 行（減少 27%）
- **規範性**: 預期輸出格式統一存放

## test_task10221.easy.py
**原始檔案**: test_task10221.py
**優化內容**:
- 保留兩個獨立測試方法（因功能區分明確）
- 方法名簡化：`test_geometry_values()` → `test_geometry()`
- 方法名簡化：`test_multiple_lines()` → `test_multi_units()`
- 路徑設置統一簡化
- **代碼行數**: 19 行 → 16 行（減少 16%）
- **可讀性**: 移除冗長的名稱，保持清晰的測試意圖

## test_task10222.easy.py
**原始檔案**: test_task10222.py
**優化內容**:
- 合併 `test_decode_sentence()` 和 `test_keep_spaces_and_symbols()` 兩個測試方法
- 使用統一的 `test_all_cases()` 方法搭配 `subTest`
- 測試用例改用元組列表集中管理
- 路徑設置統一簡化
- **代碼行數**: 20 行 → 15 行（減少 25%）
- **一致性**: 與其他簡化檔案風格統一

---

## 總體優化成果

| 檔案 | 原始行數 | 優化後行數 | 減少比例 |
|------|---------|----------|---------|
| test_task10189.easy.py | 24 | 15 | 38% |
| test_task10190.easy.py | 20 | 15 | 25% |
| test_task10193.easy.py | 22 | 16 | 27% |
| test_task10221.easy.py | 19 | 16 | 16% |
| test_task10222.easy.py | 20 | 15 | 25% |
| **總計** | **105** | **77** | **27%** |

## 優化策略

1. **測試用例集中管理**: 使用 `cases` 列表存放輸入輸出對，便於維護和擴展
2. **減少代碼重複**: 合併相似的測試方法，使用 `subTest` 進行多用例測試
3. **簡化路徑邏輯**: 統一使用 `sys.path.insert(0, str(Path(__file__).resolve().parent))`
4. **提高可讀性**: 簡化方法名稱，移除冗長描述
5. **保持功能完整**: 所有測試邏輯和覆蓋範圍保持不變
