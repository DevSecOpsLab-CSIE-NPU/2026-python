# TEST_CASES.md

## Robot Lost 測試案例

---

### 案例 1：方向旋轉 - N + L = W

- **輸入**：`Robot(0, 0, 'N', 5, 5)` + 執行 L
- **預期結果**：direction = 'W'
- **實際結果**：direction = 'W'
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_core.py::TestRobotDirection::test_n_plus_l_equals_w`

---

### 案例 2：方向旋轉 - N + R = E

- **輸入**：`Robot(0, 0, 'N', 5, 5)` + 執行 R
- **預期結果**：direction = 'E'
- **實際結果**：direction = 'E'
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_core.py::TestRobotDirection::test_n_plus_r_equals_e`

---

### 案例 3：連續四次旋轉回原方向

- **輸入**：`Robot(0, 0, 'N', 5, 5)` + 執行 RRRR
- **預期結果**：direction = 'N'
- **實際結果**：direction = 'N'
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_core.py::TestRobotDirection::test_four_rights_back_to_original`

---

### 案例 4：邊界內移動安全

- **輸入**：`Robot(3, 3, 'N', 5, 5)` + 執行 F
- **預期結果**：move_forward() = True, lost = False
- **實際結果**：move_forward() = True, lost = False
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_core.py::TestRobotMovement::test_boundary_inside_safe`

---

### 案例 5：邊界外移動會失敗

- **輸入**：`Robot(5, 5, 'N', 5, 5)` + 執行 F
- **預期結果**：move_forward() = False
- **實際結果**：move_forward() = False
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_core.py::TestRobotMovement::test_boundary_outside_lost`

---

### 案例 6：第一台機器人越界留下 scent

- **輸入**：`Robot(5, 5, 'N', 5, 5)` + world.execute_robot(robot, 'F')
- **預期結果**：robot.lost = True, scent = {(5, 5, 'N')}
- **實際結果**：robot.lost = True, scent = {(5, 5, 'N')}
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_scent.py::TestScentMechanism::test_first_robot_leaves_scent`

---

### 案例 7：第二台機器人忽略危險 F

- **輸入**：
  1. Robot1(5, 5, 'N') + 'F' → 留下 scent
  2. Robot2(5, 5, 'N') + 'F'
- **預期結果**：Robot2.lost = False, 位置不變
- **實際結果**：Robot2.lost = False, (5, 5)
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_scent.py::TestScentMechanism::test_second_robot_ignores_dangerous_f`

---

### 案例 8：同位置不同方向不共用 scent

- **輸入**：
  1. Robot1(5, 5, 'N') + 'F' → 留下 scent (5, 5, 'N')
  2. Robot2(5, 5, 'E') + 'F'
- **預期結果**：Robot2.lost = True, 新增 scent (5, 5, 'E')
- **實際結果**：Robot2.lost = True, scent 包含 (5, 5, 'E')
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_scent.py::TestScentMechanism::test_same_position_different_direction_no_shared_scent`

---

### 案例 9：LOST 後停止執行指令

- **輸入**：`Robot(5, 5, 'N', 5, 5)` + world.execute_robot(robot, 'FFFR')
- **預期結果**：lost = True, direction = 'N'（最後一個 R 未執行）
- **實際結果**：lost = True, direction = 'N'
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_scent.py::TestLostBehavior::test_lost_stops_execution`

---

### 案例 10：非法指令拋出例外

- **輸入**：`Robot(0, 0, 'N', 5, 5)` + execute_command('X')
- **預期結果**：拋出 ValueError
- **實際結果**：拋出 ValueError
- **是否通過**：PASS ✓
- **對應測試函式**：`test_robot_core.py::TestRobotExecuteCommand::test_invalid_command_raises`

---

## 總結

| 案例 | 測試重點 | 結果 |
|------|----------|------|
| 1 | 方向旋轉 L | PASS ✓ |
| 2 | 方向旋轉 R | PASS ✓ |
| 3 | 四次旋轉回原點 | PASS ✓ |
| 4 | 邊界內移動 | PASS ✓ |
| 5 | 邊界外移動失敗 | PASS ✓ |
| 6 | 留下 scent | PASS ✓ |
| 7 | 忽略危險 F | PASS ✓ |
| 8 | 不同方向 scent | PASS ✓ |
| 9 | LOST 後停止 | PASS ✓ |
| 10 | 非法指令處理 | PASS ✓ |

**總計：10 組測試案例，全部通過**
