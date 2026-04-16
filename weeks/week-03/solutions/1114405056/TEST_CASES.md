# TEST_CASES

> 地圖預設為 `(0,0)` 到 `(5,3)`。

| Case | 輸入（初始狀態 + 指令） | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|---|---|---|---|---|---|
| 1 | `(0,0,N)` + `L` | 方向變 `W` | 方向為 `W` | PASS | `test_n_plus_l_equals_w` |
| 2 | `(0,0,N)` + `R` | 方向變 `E` | 方向為 `E` | PASS | `test_n_plus_r_equals_e` |
| 3 | `(0,0,N)` + `RRRR` | 回到 `N` | 方向為 `N` | PASS | `test_four_r_returns_original_direction` |
| 4 | `(5,3,N)` + `F` | 越界後 `LOST` | `LOST`，停在 `(5,3)` | PASS | `test_forward_outside_boundary_marks_lost` |
| 5 | `(0,0,N)` + `F` | 移動到 `(0,1)`，未 LOST | 到 `(0,1)`，`ALIVE` | PASS | `test_forward_inside_boundary_not_lost` |
| 6 | 第一台 `(5,3,N)` + `F` | 留下 scent `(5,3,N)` | scent 成功新增 | PASS | `test_first_robot_lost_leaves_scent` |
| 7 | 第二台 `(5,3,N)` + `F` | 忽略危險 `F`，不 LOST | 狀態 `SCENT_IGNORED`，位置不變 | PASS | `test_second_robot_same_state_ignores_dangerous_forward` |
| 8 | `(5,3,E)` + `F`（已有 `(5,3,N)` scent） | 不應共用 scent，應 LOST | 狀態 `LOST` | PASS | `test_same_cell_different_direction_does_not_share_scent` |
| 9 | `(5,3,N)` + `FRF` | 第一個 `F` LOST，後續不執行 | 只執行 1 步，仍在 `(5,3,N)` | PASS | `test_lost_robot_stops_following_commands` |
| 10 | `(0,0,N)` + `X` | 非法指令應明確處理 | 拋出 `ValueError` | PASS | `test_invalid_command_raises_value_error` |
