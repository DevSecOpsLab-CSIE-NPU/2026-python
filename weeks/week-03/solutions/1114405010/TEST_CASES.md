# TEST_CASES

| 編號 | 輸入（初始狀態 + 指令） | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|---|---|---|---|---|---|
| 1 | (0,0,N), `L` | 方向變 W | W | PASS | test_turn_left_from_north |
| 2 | (0,0,N), `R` | 方向變 E | E | PASS | test_turn_right_from_north |
| 3 | (0,0,N), `RRRR` | 回到 N | N | PASS | test_four_right_turns_back_to_origin |
| 4 | (5,3,N), `F` | LOST 並留 scent | LOST, scent 含 (5,3,N) | PASS | test_lost_at_boundary_and_leave_scent |
| 5 | (0,0,N), `F` | 移動到 (0,1), 非 LOST | (0,1), 非 LOST | PASS | test_forward_inside_boundary_not_lost |
| 6 | (5,3,N), `F` 且 scent 已有 (5,3,N) | 忽略 F, 非 LOST | 位置維持 (5,3), 非 LOST | PASS | test_second_robot_ignores_dangerous_forward |
| 7 | (5,3,N), `F` 且 scent 只有 (5,3,E) | LOST（方向不同不保護） | LOST | PASS | test_same_cell_different_direction_not_protected |
| 8 | (5,3,N), `FFRFF` | LOST 後停止執行 | 在第一次越界後停止，維持 (5,3,N) LOST | PASS | test_lost_robot_stops_following_commands |
