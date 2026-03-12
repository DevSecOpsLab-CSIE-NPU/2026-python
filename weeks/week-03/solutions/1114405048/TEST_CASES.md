# TEST_CASES

## Case 1：基本旋轉（N + L）

- 輸入：`(0,0,N)` + `L`
- 預期結果：方向 `W`
- 實際結果：方向 `W`
- PASS/FAIL：PASS
- 對應測試：`test_n_plus_l_equals_w`

## Case 2：基本旋轉（N + R）

- 輸入：`(0,0,N)` + `R`
- 預期結果：方向 `E`
- 實際結果：方向 `E`
- PASS/FAIL：PASS
- 對應測試：`test_n_plus_r_equals_e`

## Case 3：四次右轉回原方向

- 輸入：`(0,0,N)` + `RRRR`
- 預期結果：方向 `N`
- 實際結果：方向 `N`
- PASS/FAIL：PASS
- 對應測試：`test_four_right_turns_back_to_original`

## Case 4：邊界外前進會 LOST

- 輸入：`(0,3,N)` + `F`，地圖 `5x3`
- 預期結果：`LOST=True`，留下 scent `(0,3,N)`
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試：`test_forward_outside_boundary_becomes_lost`

## Case 5：邊界內移動不 LOST

- 輸入：`(0,0,N)` + `FFRFF`，地圖 `5x3`
- 預期結果：`(2,2,E,False)`
- 實際結果：`(2,2,E,False)`
- PASS/FAIL：PASS
- 對應測試：`test_forward_inside_boundary_not_lost`

## Case 6：第一台越界留下 scent

- 輸入：`(3,3,N)` + `F`，地圖 `5x3`
- 預期結果：scent 包含 `(3,3,N)`
- 實際結果：scent 包含 `(3,3,N)`
- PASS/FAIL：PASS
- 對應測試：`test_first_robot_leaves_scent`

## Case 7：第二台同格同方向忽略危險 F

- 輸入：已有 scent `(3,3,N)`，機器人 `(3,3,N)` + `F`
- 預期結果：不移動、不 LOST，仍在 `(3,3,N,False)`
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試：`test_second_robot_ignores_dangerous_forward_with_same_scent`

## Case 8：同格不同方向不共用 scent

- 輸入：已有 scent `(3,3,N)`，機器人 `(3,3,E)` + `F`
- 預期結果：可前進到 `(4,3,E)`
- 實際結果：`(4,3,E)`
- PASS/FAIL：PASS
- 對應測試：`test_same_cell_different_direction_does_not_share_scent`

## Case 9：LOST 後不執行後續指令

- 輸入：`(0,3,N)` + `FRFRF`，地圖 `5x3`
- 預期結果：第一次 `F` 後 LOST，後續忽略
- 實際結果：停在 `(0,3,N,True)`
- PASS/FAIL：PASS
- 對應測試：`test_lost_robot_stops_following_commands`

## Case 10：非法指令策略

- 輸入：`(0,0,N)` + `FXR`
- 預期結果：預設策略丟出 `ValueError`
- 實際結果：丟出 `ValueError`
- PASS/FAIL：PASS
- 對應測試：`test_invalid_command_raises_value_error`
