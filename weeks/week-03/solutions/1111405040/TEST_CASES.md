# Week 03 測試案例說明

## 概述

- 測試檔：2 份
- 測試函式：12 個
- 覆蓋面向：
  1. 方向旋轉
  2. 越界判定
  3. scent 生效
  4. LOST 後停止
  5. 非法指令處理

---

## 測資清單（至少 8 組）

| 編號 | 輸入（初始狀態 + 指令） | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|------|--------------------------|----------|----------|-----------|--------------|
| 1 | `(1,1,N)` + `L` | 方向變 `W` | 方向變 `W` | PASS | `test_n_plus_l_equals_w` |
| 2 | `(1,1,N)` + `R` | 方向變 `E` | 方向變 `E` | PASS | `test_n_plus_r_equals_e` |
| 3 | `(1,1,N)` + `RRRR` | 方向回 `N` | 方向回 `N` | PASS | `test_four_right_turns_back_to_original_direction` |
| 4 | `(1,1,N)` + `F`（地圖 5x3） | 移動到 `(1,2)`、非 LOST | `(1,2)`、非 LOST | PASS | `test_forward_inside_boundary_not_lost` |
| 5 | `(5,3,N)` + `F`（地圖 5x3） | LOST、位置維持 `(5,3)` | LOST、位置維持 `(5,3)` | PASS | `test_forward_out_of_boundary_will_be_lost` |
| 6 | 第一台 `(5,3,N)` + `F` | 產生 scent `(5,3,N)` | 產生 scent `(5,3,N)` | PASS | `test_first_lost_robot_leaves_scent` |
| 7 | 第二台 `(5,3,N)` + `F`（已有 scent） | 忽略危險 F、不 LOST | 忽略危險 F、不 LOST | PASS | `test_second_robot_same_xyz_direction_ignores_dangerous_forward` |
| 8 | 同格不同方向：`(5,3,E)` + `F`（僅有 scent `(5,3,N)`） | 不可共用 scent，會 LOST | 會 LOST | PASS | `test_same_cell_different_direction_should_not_share_scent` |
| 9 | `(5,3,N)` + `FRFLF` | 第一步 LOST 後停止，方向仍 `N` | LOST 後停止，方向 `N` | PASS | `test_lost_robot_stops_following_commands` |
| 10 | `(1,1,N)` + `X` | 拋出非法指令錯誤 | 拋出 `RobotInstructionError` | PASS | `test_invalid_instruction_x_has_explicit_error` |

---

## 補充測資

| 編號 | 輸入（初始狀態 + 指令） | 預期結果 | 實際結果 | PASS/FAIL | 對應測試函式 |
|------|--------------------------|----------|----------|-----------|--------------|
| 11 | `(0,0,W)` + `F` | LOST 並記錄 scent `(0,0,W)` | LOST 並記錄 scent `(0,0,W)` | PASS | `test_scent_records_position_and_direction` |
| 12 | 已有 scent `(5,3,N)`，第二台 `(5,3,N)` + `FR` | 先忽略 `F`，再 `R` 成 `E`，不 LOST | 方向 `E`，不 LOST | PASS | `test_robot_with_scent_can_continue_next_instruction` |

---

## 測試指令

```bash
cd weeks/week-03/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```
