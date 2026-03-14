# TEST_CASES

## Case 1：左轉測試
- 輸入：
  - 初始狀態：`(1, 1, N)`
  - 指令：`L`
- 預期結果：`(1, 1, W)`，未 LOST
- 實際結果：`(1, 1, W)`，未 LOST
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_turn_left_from_north_to_west`

---

## Case 2：右轉測試
- 輸入：
  - 初始狀態：`(1, 1, N)`
  - 指令：`R`
- 預期結果：`(1, 1, E)`，未 LOST
- 實際結果：`(1, 1, E)`，未 LOST
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_turn_right_from_north_to_east`

---

## Case 3：連續四次右轉
- 輸入：
  - 初始狀態：`(1, 1, N)`
  - 指令：`RRRR`
- 預期結果：方向回到 `N`
- 實際結果：方向回到 `N`
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_turn_right_four_times_back_to_original`

---

## Case 4：地圖內前進
- 輸入：
  - 初始狀態：`(1, 1, N)`
  - 指令：`F`
- 預期結果：`(1, 2, N)`，未 LOST
- 實際結果：`(1, 2, N)`，未 LOST
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_forward_inside_bounds_not_lost`

---

## Case 5：邊界外前進會 LOST
- 輸入：
  - 初始狀態：`(0, 0, S)`
  - 指令：`F`
- 預期結果：機器人 LOST，位置停在 `(0, 0)`
- 實際結果：機器人 LOST，位置停在 `(0, 0)`
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_robot_lost_at_edge`

---

## Case 6：第一台機器人越界後留下 scent
- 輸入：
  - 初始狀態：`(0, 0, S)`
  - 指令：`F`
- 預期結果：`scents` 內新增 `(0, 0, "S")`
- 實際結果：`scents` 內新增 `(0, 0, "S")`
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_first_robot_leaves_scent_after_lost`

---

## Case 7：第二台遇到同位置同方向 scent 會忽略危險 F
- 輸入：
  - 第一台初始狀態：`(0, 0, S)`，指令：`F`
  - 第二台初始狀態：`(0, 0, S)`，指令：`F`
- 預期結果：第二台不 LOST，停在 `(0, 0, S)`
- 實際結果：第二台不 LOST，停在 `(0, 0, S)`
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_scent_prevents_second_robot_lost`

---

## Case 8：同格不同方向不共用 scent
- 輸入：
  - scent：`(0, 0, S)`
  - 初始狀態：`(0, 0, W)`
  - 指令：`F`
- 預期結果：仍然 LOST，因為方向不同
- 實際結果：仍然 LOST，因為方向不同
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_same_position_different_direction_should_not_share_scent`

---

## Case 9：LOST 後不再執行後續指令
- 輸入：
  - 初始狀態：`(0, 0, S)`
  - 指令：`FFRFF`
- 預期結果：第一次 `F` 就 LOST，之後指令不再執行
- 實際結果：第一次 `F` 就 LOST，之後指令不再執行
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_robot_stops_after_lost`

---

## Case 10：非法指令測試
- 輸入：
  - 初始狀態：`(0, 0, N)`
  - 指令：`X`
- 預期結果：拋出 `ValueError`
- 實際結果：拋出 `ValueError`
- PASS/FAIL：PASS
- 對應測試函式名稱：`test_invalid_instruction_should_raise_error`