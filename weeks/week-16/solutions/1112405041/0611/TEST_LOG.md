# TEST_LOG.md - Week 16 開發證據紀錄

## [Stage 1] 裝飾器測試
- **RED**: `ImportError` - 尚未建立 `timing.py`。
- **GREEN**: `Ran 3 tests... OK`

## [Stage 2] 排序正確性
- **RED**: `AssertionError` - 最初未正確處理回傳新串列。
- **GREEN**: `Ran 1 test... OK` (內含 6 組測資)

## [Stage 3] 效能與對照
- **VERIFIED**: `results.json` 已包含 baseline 數據，且符合 O(n log n) 趨勢。

## [Stage 4] 繪圖輸出
- **VERIFIED**: `assets/benchmark.png` 成功生成且非空。

## [Stage 5] 安全性驗證
- **RED**: `test_results_json_is_safe` 最初因測試邏輯錯誤而紅燈。
- **GREEN**: `Ran 2 tests... OK` (已驗證 JSON 使用與 with 語句)

