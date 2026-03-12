# TEST_CASES

## 案例 1：一般移動
- 輸入：Robot(1,1,N), commands=FFRFF
- 預期： (3,3,E), ALIVE
- 實際： (3,3,E), ALIVE
- 結果： PASS
- 對應測試函式： `test_move_inside_boundary_not_lost`

## 案例 2：左轉規則
- 輸入：direction N, command L
- 預期： W
- 實際： W
- 結果： PASS
- 對應測試函式： `test_rotate_left_from_north`

## 案例 3：右轉規則
- 輸入：direction N, command R
- 預期： E
- 實際： E
- 結果： PASS
- 對應測試函式： `test_rotate_right_from_north`

## 案例 4：連續右轉四次
- 輸入：direction N, commands=RRRR
- 預期： N
- 實際： N
- 結果： PASS
- 對應測試函式： `test_four_right_turns_back_to_original_direction`

## 案例 5：越界後 LOST
- 輸入：Robot(5,3,N), commands=F
- 預期： LOST，並留下 scent (5,3,N)
- 實際： LOST，並留下 scent (5,3,N)
- 結果： PASS
- 對應測試函式： `test_forward_out_of_boundary_causes_lost`

## 案例 6：scent 阻擋重複掉落
- 輸入：第一台 Robot(5,3,N):F，第二台 Robot(5,3,N):F
- 預期：第二台停在 (5,3,N)，且 ALIVE
- 實際：第二台停在 (5,3,N)，且 ALIVE
- 結果： PASS
- 對應測試函式： `test_second_robot_same_position_and_direction_ignores_dangerous_forward`

## 案例 7：同格不同方向
- 輸入：已有 scent (5,3,N)，robot 在 (5,3,E) 執行 F
- 預期：仍會 LOST（方向不同不共用 scent）
- 實際： LOST
- 結果： PASS
- 對應測試函式： `test_same_position_different_direction_does_not_share_scent`

## 案例 8：LOST 後應停止
- 輸入：Robot(5,3,N), commands=FRF
- 預期：第一個 F 後 LOST，後續指令被忽略
- 實際：第一個 F 後 LOST，後續指令被忽略
- 結果： PASS
- 對應測試函式： `test_execute_stops_after_lost`

## 案例 9：非法指令
- 輸入：Robot(0,0,N), command X
- 預期：拋出 ValueError
- 實際：拋出 ValueError
- 結果： PASS
- 對應測試函式： `test_invalid_command_raises_value_error`
