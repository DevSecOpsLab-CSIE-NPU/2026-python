# TEST_CASES

## Case 01
- 輸入：state=(1,1,N,False), cmd=L
- 預期結果：方向變 W
- 實際結果：W
- PASS/FAIL：PASS
- 對應測試函式名稱：test_n_plus_l_becomes_w

## Case 02
- 輸入：state=(1,1,N,False), cmd=R
- 預期結果：方向變 E
- 實際結果：E
- PASS/FAIL：PASS
- 對應測試函式名稱：test_n_plus_r_becomes_e

## Case 03
- 輸入：state=(0,0,N,False), cmds=RRRR
- 預期結果：回到 N
- 實際結果：N
- PASS/FAIL：PASS
- 對應測試函式名稱：test_four_right_turns_back_to_origin

## Case 04
- 輸入：world=(5,3), state=(5,3,N,False), cmd=F
- 預期結果：LOST=True，並留下 scent=(5,3,N)
- 實際結果：LOST=True，scent 已加入
- PASS/FAIL：PASS
- 對應測試函式名稱：test_move_out_of_boundary_lost、test_first_robot_leaves_scent_when_lost

## Case 05
- 輸入：world=(5,3), state=(1,1,E,False), cmd=F
- 預期結果：移動到 (2,1,E)，不 LOST
- 實際結果：(2,1,E,False)
- PASS/FAIL：PASS
- 對應測試函式名稱：test_move_inside_boundary_not_lost

## Case 06
- 輸入：第一台先在 (5,3,N) 越界；第二台同 state=(5,3,N), cmd=F
- 預期結果：第二台忽略危險 F，不 LOST
- 實際結果：status=SCENT_BLOCKED，位置不變
- PASS/FAIL：PASS
- 對應測試函式名稱：test_second_robot_ignores_dangerous_forward_at_same_state

## Case 07
- 輸入：已存在 scent=(5,3,N)，第二台 state=(5,3,E), cmd=F
- 預期結果：不同方向不共用 scent，會 LOST
- 實際結果：LOST=True，新增 scent=(5,3,E)
- PASS/FAIL：PASS
- 對應測試函式名稱：test_same_cell_different_direction_not_share_scent

## Case 08
- 輸入：world=(1,1), state=(1,1,N), cmds=FFRFF
- 預期結果：第一個 F 即 LOST，後續不執行
- 實際結果：statuses=[LOST]
- PASS/FAIL：PASS
- 對應測試函式名稱：test_lost_robot_stops_following_commands

## Case 09
- 輸入：state=(1,1,N), cmd=X
- 預期結果：明確丟出 ValueError
- 實際結果：ValueError
- PASS/FAIL：PASS
- 對應測試函式名稱：test_invalid_command_raises

## Case 10
- 輸入：UVA 118 sample
- 預期結果：
  - Robot1 -> (1,1,E)
  - Robot2 -> (3,3,N,LOST)
  - Robot3 -> (2,3,S)
- 實際結果：與預期一致
- PASS/FAIL：PASS
- 對應測試函式名稱：test_uva_sample_robot_1、test_uva_sample_robot_2_and_3
