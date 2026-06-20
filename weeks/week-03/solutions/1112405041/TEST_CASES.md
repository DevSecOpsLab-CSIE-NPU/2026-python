# TEST_CASES.md

## 測試案例 8 組

### 1. 正常情況 — 旋轉+前進
- 輸入：Robot(0,0,N), world=(5,5), 指令 "RFRF"
- 預期：(1,1,S)
- 實際：(1,1,S)
- PASS
- 對應：test_forward_east, test_forward_south

### 2. 邊界情況 — 北邊越界 LOST
- 輸入：Robot(0,5,N), world=(5,5), 指令 "F"
- 預期：LOST at (0,5,N)
- 實際：LOST at (0,5,N)
- PASS
- 對應：test_forward_out_of_bounds_lost

### 3. 反例 — 小寫指令
- 輸入：Robot(0,0,N), 指令 "f"
- 預期：raise ValueError
- 實際：raise ValueError
- PASS
- 對應：test_lowercase_command_raises

### 4. scent 方向差異 — 同格不同方向
- 輸入：scent=(5,5,N), Robot(5,5,E), 指令 "F"
- 預期：LOST（E 方向不被 N 的 scent 保護）
- 實際：LOST
- PASS
- 對應：test_same_pos_different_dir_not_protected

### 5. LOST 後仍有後續指令
- 輸入：Robot(0,5,N), world=(5,5), 指令 "FRFL"
- 預期：LOST at (0,5,N)，後續指令被忽略
- 實際：LOST at (0,5,N)
- PASS
- 對應：test_lost_robot_stops_execution

### 6. scent 保護第二台機器人
- 輸入：第一台 Robot(0,5,N) → LOST 留下 scent=(0,5,N)；第二台 Robot(0,5,N) 指令 "F"
- 預期：第二台 NOT LOST，位置不變 (0,5,N)
- 實際：NOT LOST，(0,5,N)
- PASS
- 對應：test_second_robot_uses_scent_from_first

### 7. 連續 4 次 R 回原方向
- 輸入：Robot(0,0,N), 指令 "RRRR"
- 預期：方向 N
- 實際：N
- PASS
- 對應：test_four_rights_return_to_start

### 8. scent 只在越界時留下
- 輸入：Robot(0,0,N), world=(5,5), 指令 "F"
- 預期：不留下 scent
- 實際：不留下 scent
- PASS
- 對應：test_scent_not_left_on_safe_move
