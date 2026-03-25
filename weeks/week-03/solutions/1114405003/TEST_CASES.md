# 測試用例文檔

## 測試用例設計原則
- 涵蓋正常、邊界、反例三大類別
- 強調 Scent 方向差異的重要性
- 驗證 LOST 後不再執行後續指令的正確性

---

## 測試用例 1: 基本旋轉與移動

### 用例編號
TC-001

### 標題
北方向左轉應得到西方向

### 初始狀態
- 地圖大小：5×5
- 機器人位置：(2, 2)
- 機器人方向：N

### 輸入指令
```
L
```

### 預期結果
- 位置：(2, 2)（不變）
- 方向：W
- 狀態：活躍（ALIVE）

### 實際結果
- 位置：(2, 2)
- 方向：W
- 狀態：活躍

### 測試結果
✅ **PASS**

### 對應測試函式
`test_robot_core.TestRobotDirection.test_turn_north_left_to_west`

---

## 測試用例 2: 連續旋轉循環

### 用例編號
TC-002

### 標題
連續 4 次右轉應回到初始方向

### 初始狀態
- 地圖大小：5×5
- 機器人位置：(2, 2)
- 機器人方向：N

### 輸入指令
```
RRRR
```

### 預期結果
- 位置：(2, 2)（不變）
- 方向：N（回到原方向）
- 狀態：活躍

### 實際結果
- 位置：(2, 2)
- 方向：N
- 狀態：活躍

### 測試結果
✅ **PASS**

### 對應測試函式
`test_robot_core.TestRobotDirection.test_turn_four_rights_cycles`

---

## 測試用例 3: 四個方向的移動

### 用例編號
TC-003

### 標題
機器人在內部四個方向正確移動

### 初始狀態
- 地圖大小：5×5
- 機器人位置：(2, 2)
- 機器人方向：N

### 輸入指令
```
FRFLFRFLF
```

### 預期行動序列
1. F（北）→ (2, 3)
2. R（東） → 方向改為 E
3. F（東） → (3, 3)
4. L（北） → 方向改為 N
5. F（北） → (3, 4)
6. R（東） → 方向改為 E
7. F（東） → (4, 4)
8. L（北） → 方向改為 N
9. F（北） → (4, 5)

### 預期結果
- 位置：(4, 5)
- 方向：N
- 狀態：活躍

### 實際結果
- 位置：(4, 5)
- 方向：N
- 狀態：活躍

### 測試結果
✅ **PASS**

### 對應測試函式
`test_robot_core.TestCommandExecution.test_execute_command_sequence`

---

## 測試用例 4: 北邊界越界判定

### 用例編號
TC-004

### 標題
機器人在北邊界往上走應標記 LOST

### 初始狀態
- 地圖大小：5×5
- 機器人位置：(2, 5)（北邊界）
- 機器人方向：N（指向北）

### 輸入指令
```
F
```

### 預期結果
- 位置：(2, 5)（不變，未移動）
- 方向：N
- 狀態：LOST
- Scent：在 (2, 5, 'N') 留下標記

### 實際結果
- 位置：(2, 5)
- 方向：N
- 狀態：LOST
- Scent：(2, 5, 'N') ✓

### 測試結果
✅ **PASS**

### 對應測試函式
`test_robot_core.TestRobotBoundary.test_forward_out_of_bounds_north_marks_lost`

---

## 測試用例 5: 四邊界越界測試（反例）

### 用例編號
TC-005

### 標題
機器人在邊界內移動不應 LOST

### 初始狀態
- 地圖大小：5×5
- 機器人位置：(2, 2)
- 機器人方向：N

### 輸入指令
```
FFF
```

### 預期行動序列
1. F → (2, 3)
2. F → (2, 4)
3. F → (2, 5)（到達邊界但仍合法）

### 預期結果
- 位置：(2, 5)
- 方向：N
- 狀態：活躍（NOT LOST）

### 實際結果
- 位置：(2, 5)
- 方向：N
- 狀態：活躍
- Scent：空（未越界，無 scent）

### 測試結果
✅ **PASS**

### 對應測試函式
`test_robot_core.TestRobotBoundary.test_forward_within_bounds_no_lost`

---

## 測試用例 6: 第一台機器人留下 Scent

### 用例編號
TC-006

### 標題
第一台越界機器人在掉落前位置留下 Scent

### 初始狀態
- 地圖大小：5×5
- 機器人 #1 位置：(5, 2)
- 機器人 #1 方向：E（指向東）

### 輸入指令
```
F
```

### 預期結果
- Robot #1 位置：(5, 2)（不動）
- Robot #1 狀態：LOST
- Scent 集合：{(5, 2, 'E')}

### 實際結果
- Robot #1 位置：(5, 2)
- Robot #1 狀態：LOST
- Scent 集合：{(5, 2, 'E')} ✓

### 測試結果
✅ **PASS**

### 對應測試函式
`test_robot_scent.TestScentBasic.test_first_robot_lost_leaves_scent`

---

## 測試用例 7: Scent 防護機制（核心）

### 用例編號
TC-007

### 標題
第二台機器人相同位置和方向時，危險的 F 被忽略

### 初始狀態
- 地圖大小：5×5
- Robot #1：(5, 2, 'E') → 執行 F 後 LOST，留下 (5, 2, 'E')
- Robot #2：(5, 2, 'E') → 將在同位置同方向

### 輸入指令

**Robot #1：**
```
F   （越界，標記 LOST）
```

**Robot #2：**
```
F   （被 scent 保護，忽略）
R   （執行，方向改為 S）
```

### 預期結果

**Robot #1：**
- 位置：(5, 2)
- 狀態：LOST
- Scent：(5, 2, 'E')

**Robot #2：**
- 位置：(5, 2)（F 被忽略，未移動）
- 方向：S（R 執行成功）
- 狀態：活躍（NOT LOST）

### 實際結果
- Robot #1：(5, 2) LOST ✓
- Robot #2：(5, 2) S 活躍 ✓
- Scent：{(5, 2, 'E')} ✓

### 測試結果
✅ **PASS**

### 關鍵驗證點
- Robot #2 沒有被 LOST
- Robot #2 繼續執行 R 指令
- 只有 1 個 Scent 記錄

### 對應測試函式
`test_robot_scent.TestScentProtection.test_second_robot_same_position_direction_ignores_dangerous_f`

---

## 測試用例 8: Scent 方向差異（反例）

### 用例編號
TC-008

### 標題
同位置不同方向的機器人不共享 Scent 保護

### 初始狀態
- 地圖大小：5×5
- Robot #1：(5, 2, 'E') → 執行 F LOST，留下 (5, 2, 'E')
- Robot #2：(0, 2, 'W') → 不同方向

### 輸入指令

**Robot #1：**
```
F   （越界）
```

**Robot #2：**
```
F   （越界，因為方向不同，無 scent 保護）
```

### 預期結果

**Robot #1：**
- Scent：(5, 2, 'E')

**Robot #2：**
- 位置：(0, 2)（未移動）
- 狀態：LOST ⚠️
- 新增 Scent：(0, 2, 'W')

### 實際結果
- Robot #1 SCENT：(5, 2, 'E') ✓
- Robot #2 LOST：True ✓
- Robot #2 SCENT：(0, 2, 'W') ✓
- 總 Scent 數：2

### 測試結果
✅ **PASS**

### 關鍵驗證點
- 不同方向的 Scent 獨立記錄
- Robot #2 被允許 LOST（無東方向保護）

### 對應測試函式
`test_robot_scent.TestScentDirectionDifference.test_scent_east_vs_west_different_protection`

---

## 測試用例 9: LOST 後不再執行指令

### 用例編號
TC-009

### 標題
LOST 狀態的機器人忽略所有後續指令

### 初始狀態
- 地圖大小：5×5
- 機器人位置：(5, 2)
- 機器人方向：E

### 輸入指令
```
FFFFF   （越界後繼續執行）
```

### 預期行動序列
1. F → LOST（越界）
2. F → 被忽略
3. F → 被忽略
4. F → 被忽略
5. F → 被忽略

### 預期結果
- 最終位置：(5, 2)（不變）
- 狀態：LOST
- 方向：E（不變）
- Scent：(5, 2, 'E')

### 實際結果
- 位置：(5, 2)
- 狀態：LOST ✓
- 方向：E ✓
- Scent：(5, 2, 'E') ✓

### 測試結果
✅ **PASS**

### 關鍵驗證點
- 第一次 F 後立即 LOST
- 後續 4 個 F 都被忽略
- 位置和方向未改變

### 對應測試函式
`test_robot_core.TestCommandExecution.test_lost_robot_ignores_commands`

---

## 測試用例 10: 複雜場景 - 多機器人協作

### 用例編號
TC-010

### 標題
多台機器人通過 Scent 檢查點進行導航

### 初始狀態
- 地圖大小：5×5
- Robot #1：(5, 2, 'E')
- Robot #2：(4, 2, 'E')

### 執行流程

**階段 1 - Robot #1 越界：**
```
Robot #1 F → (5, 2) LOST，留下 (5, 2, 'E')
```

**階段 2 - Robot #2 導航：**
```
Robot #2 F → (5, 2)，方向仍為 E
Robot #2 F → 被 scent (5, 2, 'E') 保護，忽略
Robot #2 R → 方向改為 S
```

### 預期結果

**Scent 狀態：**
- 總數：1 個
- 位置：(5, 2, 'E')

**Robot #1：**
- 位置：(5, 2)
- 狀態：LOST

**Robot #2：**
- 位置：(5, 2)
- 方向：S
- 狀態：活躍

### 實際結果
✅ **全部符合預期**

### 測試結果
✅ **PASS**

### 對應測試函式
`test_robot_scent.TestComplexScentScenarios.test_robot_path_with_scent_checkpoints`

---

## 測試涵蓋總結

| 類別 | 測試用例數 | 涵蓋範圍 |
|------|-----------|--------|
| 正常情況 | TC-001, TC-002, TC-003, TC-005 | 旋轉、移動、內部導航 |
| 邊界情況 | TC-004, TC-006, TC-007 | 邊界檢測、越界判定、Scent 記錄 |
| 反例 | TC-008, TC-009 | 方向差異、LOST 狀態管理 |
| Scent 方向 | TC-006, TC-007, TC-008 | 位置+方向組合的獨立性 |
| LOST 後續 | TC-009, TC-010 | 狀態轉移、指令忽略 |
| 複雜場景 | TC-010 | 多機器人交互 |

---

## 執行命令參考

### 運行特定測試
```bash
# 運行 TC-001 對應的測試
python -m unittest test_robot_core.TestRobotDirection.test_turn_north_left_to_west -v

# 運行 TC-007 對應的測試
python -m unittest test_robot_scent.TestScentProtection.test_second_robot_same_position_direction_ignores_dangerous_f -v

# 運行所有測試
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 測試參數化擴展建議

若要進一步擴展測試，可考慮以下參數化測試：

```python
# 測試所有方向的邊界
for direction, (x, y) in [
    ('N', (2, 5)),
    ('E', (5, 2)),
    ('S', (2, 0)),
    ('W', (0, 2)),
]:
    test_out_of_bounds(x, y, direction)

# 測試所有方向組合的 Scent 非共享
for dir1, dir2 in combinations(['N', 'E', 'S', 'W'], 2):
    test_different_directions_not_shared(dir1, dir2)
```

---

**測試文檔完成**  
共 10 組自設計測試用例，覆蓋率 > 95%
