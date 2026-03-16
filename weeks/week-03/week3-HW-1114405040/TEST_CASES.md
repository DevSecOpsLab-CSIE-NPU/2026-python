# TEST_CASES

以下測資皆使用目前實作的 `robot_core.py` 驗證，實際結果已與程式執行結果對齊。

| # | 類型 | 輸入（地圖 / 初始狀態 / 指令） | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|---|---|---|---|---|---|---|
| 1 | 正常旋轉 | `5x3 / (1,1,N) / L` | `(1,1,W,False)` | `(1,1,W,False)` | PASS | `test_turn_left_from_north_faces_west` |
| 2 | 正常旋轉 | `5x3 / (1,1,N) / R` | `(1,1,E,False)` | `(1,1,E,False)` | PASS | `test_turn_right_from_north_faces_east` |
| 3 | 正常移動 | `5x3 / (0,0,E) / FFRFF` | 最終 `(2,0,S,True)`，並留下 `(2,0,S)` scent | `(2,0,S,True)`，留下 `(2,0,S)` | PASS | `test_forward_inside_boundary_moves_without_loss` |
| 4 | 邊界情況 | `5x3 / (5,3,N) / F` | 機器人 LOST，停在 `(5,3)` | `(5,3,N,True)` | PASS | `test_forward_out_of_boundary_marks_robot_lost` |
| 5 | scent 生效 | 第一台 `5x3 / (5,3,N) / F`，第二台 `5x3 / (5,3,N) / FRF` | 第二台第一個 `F` 被忽略，之後右轉往東掉出地圖 | `(5,3,E,True)` | PASS | `test_scent_allows_following_commands_after_ignored_forward` |
| 6 | 方向差異反例 | 第一台 `5x3 / (5,3,N) / F`，第二台 `5x3 / (5,3,E) / F` | 不同方向不能共用 scent，因此第二台仍會 LOST | `(5,3,E,True)` | PASS | `test_same_cell_different_direction_does_not_share_scent` |
| 7 | UVA 風格案例 | `5x3 / (1,1,E) / RFRFRFRF` | 回到原位 `(1,1,E,False)` | `(1,1,E,False)` | PASS | `test_execute_multiple_commands_matches_uva_sample_style` |
| 8 | LOST 後續命令 | `5x3 / (5,3,N) / FRF` | 第一個 `F` 造成 LOST，後續 `RF` 不再執行 | `(5,3,N,True)` | PASS | `test_lost_robot_stops_processing_remaining_commands` |

## 補充說明

- Case 5 驗證 scent 不是讓機器人無敵，而是只忽略同一格同一方向的危險 `F`。
- Case 6 驗證 scent 必須記錄方向，否則會錯誤保護不相干的移動。
- Case 8 驗證 LOST 之後應立即停止後續命令，不能再轉向或前進。