# TEST_CASES - Robot Lost

## Case 1 - N + L = W
- 輸入：state=(0,0,N), command=L
- 預期結果：方向變 W
- 實際結果：W
- PASS/FAIL：PASS
- 對應測試函式：`test_turn_left_from_north`

## Case 2 - N + R = E
- 輸入：state=(0,0,N), command=R
- 預期結果：方向變 E
- 實際結果：E
- PASS/FAIL：PASS
- 對應測試函式：`test_turn_right_from_north`

## Case 3 - 連續 4 次 R 回原方向
- 輸入：初始方向 N，連續執行 RRRR
- 預期結果：方向回到 N
- 實際結果：N
- PASS/FAIL：PASS
- 對應測試函式：`test_turn_right_four_times_back_to_origin`

## Case 4 - 邊界往外 F 會 LOST
- 輸入：地圖 5x3，state=(5,3,N), command=F
- 預期結果：LOST=True，event=LOST
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_forward_off_boundary_becomes_lost`

## Case 5 - 邊界內 F 不會 LOST
- 輸入：地圖 5x3，state=(1,1,E), command=F
- 預期結果：位置到 (2,1,E)，LOST=False
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_forward_inside_boundary_not_lost`

## Case 6 - 第一台越界留下 scent
- 輸入：地圖 5x3，state=(5,3,N), command=F
- 預期結果：scent 內含 (5,3,N)
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_first_lost_robot_leaves_scent`

## Case 7 - 第二台同 (x,y,dir) 忽略危險 F
- 輸入：先建立 scent=(5,3,N)，再用 state=(5,3,N), command=F
- 預期結果：不 LOST，位置不變，event=IGNORED_BY_SCENT
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_second_robot_same_position_direction_ignores_dangerous_forward`

## Case 8 - 同格不同方向不共用 scent
- 輸入：已存在 scent=(5,3,N)，執行 state=(5,3,E), command=F
- 預期結果：仍會 LOST，新增 scent=(5,3,E)
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_same_position_different_direction_does_not_share_scent`

## Case 9 - LOST 後停止後續指令
- 輸入：state=(5,3,N), commands=FFR
- 預期結果：第一步 LOST 後停止，事件數量為 1
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_lost_robot_ignores_followup_commands`

## Case 10 - 非法指令 X 的處理策略
- 輸入：state=(0,0,N), command=X
- 預期結果：丟出 ValueError
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_invalid_command_raises`

## Case 11 - 經典三台機器人整合案例
- 輸入：
  - 地圖：5 3
  - r1: 1 1 E / RFRFRFRF
  - r2: 3 2 N / FRRFLLFFRRFLL
  - r3: 0 3 W / LLFFFLFLFL
- 預期結果：
  - r1 -> 1 1 E
  - r2 -> 3 3 N LOST
  - r3 -> 2 3 S
- 實際結果：符合預期
- PASS/FAIL：PASS
- 對應測試函式：`test_classic_sample_case`
