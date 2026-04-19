# TEST_CASES

以下測資皆對應 [tests/test_robot_core.py](tests/test_robot_core.py) 與 [tests/test_robot_scent.py](tests/test_robot_scent.py) 的單元測試。

| # | 類型 | 輸入 | 預期結果 | 實際結果 | PASS/FAIL | 測試函式 |
|---|---|---|---|---|---|---|
| 1 | 正常情況 | `5 5 / 1 1 N / L` | `1 1 W` | `1 1 W` | PASS | `test_turn_left_from_north` |
| 2 | 正常情況 | `5 5 / 1 1 N / R` | `1 1 E` | `1 1 E` | PASS | `test_turn_right_from_north` |
| 3 | 反例 | `5 5 / 1 1 N / RRRR` | 回到 `N` | 回到 `N` | PASS | `test_four_right_turns_restore_direction` |
| 4 | 邊界情況 | `5 5 / 5 5 N / F` | `5 5 N LOST` 並留下 scent | 同預期 | PASS | `test_forward_out_of_bounds_marks_lost` |
| 5 | 邊界內移動 | `5 5 / 2 2 E / F` | `3 2 E` | `3 2 E` | PASS | `test_forward_inside_grid_changes_position` |
| 6 | scent 情況 | `2 2 / 2 2 N / F` 後再重置同位置同方向執行 `FF` | 第二台忽略危險 F，停在原位 | 同預期 | PASS | `test_second_robot_same_position_same_direction_ignores_dangerous_forward` |
| 7 | scent 方向差異 | `2 2 / 2 2 N / F` 後再重置 `2 2 E / F` | 不共用 scent，第二台仍 LOST | 同預期 | PASS | `test_same_position_different_direction_does_not_share_scent` |
| 8 | LOST 後續指令 | `5 5 / 5 5 N / FLR` | 第一個 F 就 LOST，後續 L/R 不執行 | 同預期 | PASS | `test_lost_robot_ignores_remaining_commands` |

補充：非法指令 `X` 會在核心層直接拋出 `ValueError`，對應 `test_invalid_command_raises_value_error`。