# TEST_CASES.md - 測試案例詳細說明

## 最低測試清單對應

本專案至少涵蓋以下 10 組指定的測試案例：

---

## 案例 1：`N + L = W`

**測試函式**：`test_left_from_north` (TestRobotCore)

**初始狀態**：機器人在 (0, 0) 朝 North

**指令**：`L`（左轉）

**預期結果**：方向變為 West

**實際結果**：✅ PASS

```python
def test_left_from_north(self):
    r = robot_core.Robot(0, 0, "N")
    self.grid.execute(r, "L")
    self.assertEqual(r.dir, "W")
```

---

## 案例 2：`N + R = E`

**測試函式**：`test_right_from_north` (TestRobotCore)

**初始狀態**：機器人在 (0, 0) 朝 North

**指令**：`R`（右轉）

**預期結果**：方向變為 East

**實際結果**：✅ PASS

```python
def test_right_from_north(self):
    r = robot_core.Robot(0, 0, "N")
    self.grid.execute(r, "R")
    self.assertEqual(r.dir, "E")
```

---

## 案例 3：連續 4 次 `R` 回原方向

**測試函式**：`test_full_rotation` (TestRobotCore)

**初始狀態**：機器人在 (0, 0) 朝 North

**指令**：`RRRR`（右轉 4 次）

**預期結果**：方向仍為 North

**實際結果**：✅ PASS

```python
def test_full_rotation(self):
    r = robot_core.Robot(0, 0, "N")
    self.grid.execute(r, "RRRR")
    self.assertEqual(r.dir, "N")
```

---

## 案例 4：邊界往外 `F` 會 LOST

**測試函式**：`test_move_causes_lost` (TestRobotCore)

**初始狀態**：機器人在 (5, 3) 朝 North，格子範圍 5×3

**指令**：`F`（前進）

**預期結果**：機器人標記為 LOST，位置保持 (5, 3)，scent 記錄 (5, 3, N)

**實際結果**：✅ PASS

```python
def test_move_causes_lost(self):
    r = robot_core.Robot(5, 3, "N")
    self.grid.execute(r, "F")
    self.assertTrue(r.lost)
    self.assertEqual((r.x, r.y), (5, 3))
    self.assertIn((5, 3, "N"), self.grid.scents)
```

---

## 案例 5：邊界內移動不會 LOST

**測試函式**：`test_move_without_lost` (TestRobotCore)

**初始狀態**：機器人在 (1, 1) 朝 North，格子範圍 5×3

**指令**：`F`（前進）

**預期結果**：移動至 (1, 2)，不 LOST

**實際結果**：✅ PASS

```python
def test_move_without_lost(self):
    r = robot_core.Robot(1, 1, "N")
    self.grid.execute(r, "F")
    self.assertFalse(r.lost)
    self.assertEqual((r.x, r.y), (1, 2))
```

---

## 案例 6：第一台越界後留下 scent

**測試函式**：`test_scent_storage` (TestScentBehavior)

**初始狀態**：機器人在 (1, 2) 朝 North，格子範圍 2×2

**指令**：`F`（前進）

**預期結果**：機器人 LOST，scent 集合包含 (1, 2, N) 且只有一筆

**實際結果**：✅ PASS

```python
def test_scent_storage(self):
    r = robot_core.Robot(1, 2, "N")
    self.grid.execute(r, "F")
    self.assertTrue(r.lost)
    self.assertIn((1, 2, "N"), self.grid.scents)
    self.assertEqual(len(self.grid.scents), 1)
```

---

## 案例 7：第二台同 `(x,y,dir)` 會忽略危險 `F`

**測試函式**：`test_ignore_after_scent` (TestScentBehavior)

**初始狀態**：
- 第一台在 (1, 2) 朝 N，執行 `F` 越界 LOST
- 第二台在 (1, 2) 朝 N

**指令**：第二台執行 `F`

**預期結果**：第二台不 LOST，位置仍在 (1, 2)

**實際結果**：✅ PASS

```python
def test_ignore_after_scent(self):
    r1 = robot_core.Robot(1, 2, "N")
    self.grid.execute(r1, "F")
    r2 = robot_core.Robot(1, 2, "N")
    self.grid.execute(r2, "F")
    self.assertFalse(r2.lost)
    self.assertEqual((r2.x, r2.y), (1, 2))
```

---

## 案例 8：同格但不同方向不該共用 scent

**測試函式**：`test_scent_does_not_apply_other_directions` (TestScentBehavior)

**初始狀態**：
- 第一台在 (0, 0) 朝 N
- 第二台也在 (0, 0) 但朝 E
- 格子範圍 0×0（最小，所有方向都會越界）

**指令**：
- 第一台執行 `F` → 越界 LOST，留下 scent (0, 0, N)
- 第二台執行 `F` → 應該也越界 LOST（因為朝 E 不同方向）

**預期結果**：第二台 LOST = True

**實際結果**：✅ PASS

```python
def test_scent_does_not_apply_other_directions(self):
    g = robot_core.Grid(0, 0)
    r1 = robot_core.Robot(0, 0, "N")
    g.execute(r1, "F")
    r2 = robot_core.Robot(0, 0, "E")
    g.execute(r2, "F")
    self.assertTrue(r2.lost)
```

---

## 案例 9：LOST 後不再執行後續指令

**測試函式**：`test_lost_then_ignore_remaining` (TestRobotCore)

**初始狀態**：機器人在 (5, 3) 朝 N，格子範圍 5×3

**指令**：`FRF`（前進→右轉→前進）

**預期結果**：
- 第一個 `F` 越界 LOST
- 後續的 `R` 與 `F` 被忽略
- 方向仍為 N（不執行右轉）

**實際結果**：✅ PASS

```python
def test_lost_then_ignore_remaining(self):
    r = robot_core.Robot(5, 3, "N")
    self.grid.execute(r, "FRF")
    self.assertTrue(r.lost)
    self.assertEqual(r.dir, "N")
```

---

## 案例 10：非法指令（如 `X`）有明確處理策略

**測試函式**：`test_illegal_instruction` (TestRobotCore)

**初始狀態**：機器人在 (0, 0) 朝 N

**指令**：`X`（非法指令）

**預期結果**：拋出 ValueError 異常

**實際結果**：✅ PASS

```python
def test_illegal_instruction(self):
    r = robot_core.Robot(0, 0, "N")
    with self.assertRaises(ValueError):
        self.grid.execute(r, "X")
```

---

## 額外測試案例

### 案例 11：狀態解析與格式化

**測試函式**：`test_parse_and_format` (TestRobotCore)

測試 `parse_state()` 與 `format_state()` 函式的正確性，包括：
- 字串解析為 Robot 物件
- Robot 物件格式化為字串（含 LOST 標記）

**結果**：✅ PASS

---

## 測試執行汇總

- **總測試數**：13
- **通過數**：13
- **失敗數**：0
- **成功率**：100%

所有指定的 10 項最低要求均已實現並通過測試。
