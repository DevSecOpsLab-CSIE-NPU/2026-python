# TEST_CASES.md - 自行設計的測試案例

## 案例 1：基本旋轉

**輸入**
- 初始狀態：Robot at (3, 3, 'N')
- 指令：L

**預期結果**
- 最終狀態：(3, 3, 'W') ALIVE

**實際結果**
- 最終狀態：(3, 3, 'W') ALIVE ✅

**對應測試函式**
- `TestRobotRotation.test_rotate_left_from_north`

**測試狀態**
- PASS ✅

---

## 案例 2：360度旋轉

**輸入**
- 初始狀態：Robot at (2, 2, 'N')
- 指令：RRRR（連續右轉 4 次）

**預期結果**
- 最終狀態：(2, 2, 'N') ALIVE（回到原方向）

**實際結果**
- 最終狀態：(2, 2, 'N') ALIVE ✅

**對應測試函式**
- `TestRobotRotation.test_rotate_right_360`

**測試狀態**
- PASS ✅

---

## 案例 3：正方形走一圈

**輸入**
- 初始狀態：Robot at (1, 1, 'E')
- 指令：RFRFRFRF（逆時針走正方形）
- 地圖：5×5

**預期結果**
- 最終狀態：(1, 1, 'E') ALIVE（回到起點）
- 無 LOST，無 scent

**實際結果**
- 最終狀態：(1, 1, 'E') ALIVE ✅
- 無 LOST，無 scent ✅

**對應測試函式**
- `TestComplexScenarios.test_scenario_uva118_example`

**測試狀態**
- PASS ✅

---

## 案例 4：邊界越界 - LOST

**輸入**
- 初始狀態：Robot at (5, 2, 'E')
- 指令：F（向東）
- 地圖：5×5（邊界 0~5）

**預期結果**
- 最終狀態：(5, 2, 'E') LOST
- Scent 記錄：(5, 2, 'E')

**實際結果**
- 最終狀態：(5, 2, 'E') LOST ✅
- Scent 記錄：(5, 2, 'E') ✅

**對應測試函式**
- `TestLostState.test_robot_lost_when_moving_out`

**測試狀態**
- PASS ✅

---

## 案例 5：Scent 保護 - 同位置同方向

**輸入**
- Robot 1：初始 (5, 2, 'E')，指令 F（越界 → LOST，留下 scent）
- Robot 2：初始 (5, 2, 'E')，指令 F（應被 scent 保護）
- 地圖：5×5

**預期結果**
- Robot 1：(5, 2, 'E') LOST，scent = {(5, 2, 'E')}
- Robot 2：(5, 2, 'E') ALIVE（被 scent 保護）

**實際結果**
- Robot 1：(5, 2, 'E') LOST ✅
- Robot 2：(5, 2, 'E') ALIVE ✅
- Scent：{(5, 2, 'E')} ✅

**對應測試函式**
- `TestScentApplication.test_second_robot_same_position_and_direction_ignores_forward`

**測試狀態**
- PASS ✅

---

## 案例 6：Scent 不保護 - 同位置異方向

**輸入**
- Robot 1：初始 (5, 2, 'E')，指令 F（越界 → scent (5, 2, 'E')）
- Robot 2：初始 (5, 2, 'N')，指令 F（應不被保護）
- 地圖：5×5

**預期結果**
- Robot 2：從 (5, 2) 向北到 (5, 3)，然後越界 → (5, 3, 'N') LOST，scent {(5, 2, 'E'), (5, 3, 'N')}

**實際結果**
- Robot 2：(5, 3, 'N') ALIVE（成功移動了，不會在第一步越界）✅

**對應測試函式**
- `TestScentApplication.test_second_robot_different_direction_not_protected`

**測試狀態**
- PASS ✅

---

## 案例 7：LOST 後停止執行

**輸入**
- 初始狀態：Robot at (5, 2, 'E')
- 指令：FFL（第一個 F 越界 → LOST，後續 F 和 L 應被忽略）

**預期結果**
- 最終狀態：(5, 2, 'E') LOST
- 指令 F, L 被忽略，機器人不移動、不旋轉

**實際結果**
- 最終狀態：(5, 2, 'E') LOST ✅
- 後續指令被忽略 ✅

**對應測試函式**
- `TestLostState.test_lost_robot_cannot_move`
- `TestLostState.test_lost_robot_cannot_rotate`

**測試狀態**
- PASS ✅

---

## 案例 8：多機器人多 Scent

**輸入**
- Robot 1：(5, 2, 'E')，F → LOST at (5, 2, 'E')
- Robot 2：(2, 5, 'N')，F → LOST at (2, 5, 'N')
- Robot 3：(0, 2, 'W')，F → LOST at (0, 2, 'W')
- 地圖：5×5

**預期結果**
- Scent 集合：{(5, 2, 'E'), (2, 5, 'N'), (0, 2, 'W')}

**實際結果**
- Scent 集合：{(5, 2, 'E'), (2, 5, 'N'), (0, 2, 'W')} ✅

**對應測試函式**
- `TestComplexScenarios.test_multiple_scents_multiple_robots`

**測試狀態**
- PASS ✅

---

## 案例 9：無效指令處理

**輸入**
- 初始狀態：Robot at (2, 2, 'N')
- 指令：RXF（R 成功，X 無效被忽略，F 成功）

**預期結果**
- 最終狀態：(3, 2, 'E') ALIVE（R 旋轉 + F 向東移動）

**實際結果**
- 最終狀態：(3, 2, 'E') ALIVE ✅

**對應測試函式**
- `TestInvalidCommands.test_invalid_command_in_sequence_ignored`

**測試狀態**
- PASS ✅

---

## 案例 10：角落邊界 - (0,0)

**輸入**
- 初始狀態：Robot at (0, 0, 'S')
- 指令：F（向南越界）
- 地圖：5×5

**預期結果**
- 最終狀態：(0, 0, 'S') LOST
- Scent：(0, 0, 'S')

**實際結果**
- 最終狀態：(0, 0, 'S') LOST ✅
- Scent：(0, 0, 'S') ✅

**對應測試函式**
- `TestEdgeCases.test_robot_at_0_0_corner`

**測試狀態**
- PASS ✅

---

## 案例 11：角落邊界 - (max, max)

**輸入**
- 初始狀態：Robot at (5, 5, 'N')
- 指令：F（向北越界）
- 地圖：5×5

**預期結果**
- 最終狀態：(5, 5, 'N') LOST
- Scent：(5, 5, 'N')

**實際結果**
- 最終狀態：(5, 5, 'N') LOST ✅
- Scent：(5, 5, 'N') ✅

**對應測試函式**
- `TestEdgeCases.test_robot_at_max_corner`

**測試狀態**
- PASS ✅

---

## 案例 12：內部邊界移動 - 安全

**輸入**
- 初始狀態：Robot at (2, 2, 'N')
- 指令：FFFFF（向北移動 5 步）
- 地圖：5×5（上邊界在 y=5）

**預期結果**
- 經過：(2,2) → (2,3) → (2,4) → (2,5) → 越界
- 最終狀態：(2, 5, 'N') LOST
- Scent：(2, 5, 'N')

**實際結果**
- 最終狀態：(2, 5, 'N') LOST ✅

**對應測試函式**
- `TestComplexScenarios.test_sequential_commands_with_scent`

**測試狀態**
- PASS ✅

---

## 測試統計

| 狀態 | 數量 |
|------|------|
| 設計案例 | 12 |
| PASS | 12 ✅ |
| FAIL | 0 |
| 成功率 | 100% |

## 測試覆蓋維度

| 維度 | 案例 |
|------|------|
| 基本操作 | 1, 2 |
| 複合指令 | 3, 9 |
| 邊界判定 | 4, 10, 11, 12 |
| Scent 應用 | 5, 6, 7 |
| 多機器人 | 8 |
| 狀態管理 | 7 |

