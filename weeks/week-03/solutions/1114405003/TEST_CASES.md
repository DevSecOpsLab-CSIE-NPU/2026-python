# TEST_CASES

1. 初始 (0,0,N), 指令 `L` => (0,0,W,False)  [test_n_left_is_w] PASS
2. 初始 (0,0,N), 指令 `R` => (0,0,E,False)  [test_n_right_is_e] PASS
3. 初始 (0,0,N), 指令 `RRRR` => (0,0,N,False)  [test_4_right_returns_to_n] PASS
4. 初始 (0,0,N), 指令 `F` (在邊界內) => (0,1,N,False)  [test_forward_within_boundary_not_lost] PASS
5. 初始 (0,0,N), 地圖 (0,0), 指令 `F` => (0,0,N,True) LOST  [test_forward_beyond_boundary_lost] PASS
6. 地圖 (1,1), 第一台(0,1,N), `F` => LOST, scent=(0,1,N)  [test_scent_added_when_lost] PASS
7. 地圖 (1,1), 第一台(0,1,N), `F`, 第二台同狀態`F` => 不 LOST  [test_scent_prevents_second_robot_loss_same_state] PASS
8. 地圖 (1,1), 第一台(0,1,N), `F`, 第二台(0,1,E), `F` => (1,1,E,False)  [test_no_scent_share_different_direction] PASS
9. 初始 (0,0,N), 指令 `X` => ValueError  [test_invalid_command_raises] PASS
10. LOST後命令中斷: 地圖(0,0), 指令 `FRF` => (0,0,N,True)  [test_lost_stops_following_commands] PASS
