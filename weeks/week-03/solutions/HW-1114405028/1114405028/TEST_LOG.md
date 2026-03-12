# TEST_LOG.md - 測試執行紀錄

## 第一次執行 - RED（失敗）

執行指令：
```
py -m unittest discover -s tests -p "test_*.py" -v
```

**初始狀態**：編寫測試後，核心邏輯尚未完成。

結果摘要：
```
FAILED (failures=1)
```

失敗項目：
- `test_scent_does_not_apply_other_directions` 預期 scent 僅針對特定方向生效

**原因**：測試使用的格子尺寸不適合驗證邊界狀況。

---

## 第二次執行 - GREEN（通過）

執行指令：
```
py -m unittest discover -s tests -p "test_*.py" -v
```

**修正動作**：
1. 在 `robot_core.py` 中實作 `Grid.execute()` 方法
2. 實作方向轉換邏輯（L/R）
3. 實作前進邏輯含邊界檢查與 LOST 狀態
4. 實作 scent 記錄與檢查機制
5. 調整測試用的格子大小為 0×0 以強制所有方向都越界

測試執行結果：
```
test_full_rotation (test_robot_core.TestRobotCore) ... ok
test_illegal_instruction (test_robot_core.TestRobotCore) ... ok
test_left_from_north (test_robot_core.TestRobotCore) ... ok
test_lost_then_ignore_remaining (test_robot_core.TestRobotCore) ... ok
test_move_causes_lost (test_robot_core.TestRobotCore) ... ok
test_move_without_lost (test_robot_core.TestRobotCore) ... ok
test_parse_and_format (test_robot_core.TestRobotCore) ... ok
test_right_from_north (test_robot_core.TestRobotCore) ... ok
test_scent_direction_distinct (test_robot_core.TestRobotCore) ... ok
test_scent_prevents_lost (test_robot_core.TestRobotCore) ... ok
test_ignore_after_scent (test_robot_scent.TestScentBehavior) ... ok
test_scent_does_not_apply_other_directions (test_robot_scent.TestScentBehavior) ... ok
test_scent_storage (test_robot_scent.TestScentBehavior) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.002s

OK
```

**全部通過**：13/13 測試成功。

---

## 第三次執行 - REFACTOR（程式重構後驗證）

執行指令：
```
py -m unittest discover -s tests -p "test_*.py" -v
```

重構項目：
- 分離 `_turn_left()`, `_turn_right()`, `_forward()` 為獨立方法
- 增加程式碼註解解釋 scent 機制
- 優化坐標計算的可讀性

結果：
```
Ran 13 tests in 0.002s

OK
```

**驗證通過**：重構後所有測試仍通過，邏輯正確性未受影響。

---

## 測試覆蓋範圍

| 面向 | 測試項目 | 數量 |
|------|---------|------|
| 方向旋轉 | L、R、4×R 回原點 | 3 |
| 邊界移動 | 正常移動、邊界越界 LOST | 2 |
| scent 機制 | scent 儲存、scent 防止 LOST、scent 方向隔離 | 3 |
| LOST 行為 | LOST 後忽略後續指令 | 1 |
| 錯誤處理 | 非法指令拋出 ValueError | 1 |
| 解析 & 格式化 | parse_state, format_state with/without LOST | 1 |
| 額外驗證 | 正常移動時不 LOST | 1 |

**總計**：13 個測試，全覆蓋所有指定的測試清單項目。
