# 機器人遊戲測試案例

此文件包含至少 8 個自行設計的機器人遊戲測試案例，涵蓋正常情況、邊界情況、反例、scent 方向差異，以及 LOST 後仍有後續指令的情況。

每個測試案例包括：
- **輸入**：初始狀態 + 指令
- **預期輸出**：最終狀態
- **實際輸出**：[測試後填寫]
- **PASS/FAIL**：[填寫]
- **測試函式名稱**：對應的 unittest 函式

## 測試案例 1：正常移動（正常情況）
- **輸入**：網格 10x10，起始 (5,5,N)，指令：F R F
- **預期輸出**：位置 (6,4,E)，方向 E，Lost False，Scents {}
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_normal_movement

## 測試案例 2：邊界移動（邊界情況）
- **輸入**：網格 10x10，起始 (9,9,E)，指令：F
- **預期輸出**：位置 (10,9,E)，方向 E，Lost False，Scents {}
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_boundary_movement

## 測試案例 3：反例 - 錯誤方向映射（反例）
- **輸入**：網格 10x10，起始 (0,0,N)，指令：L F
- **預期輸出**：位置 (-1,0,W)，但因為超出，Lost True，Scents {(0,0,'W')}
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_counterexample_direction

## 測試案例 4：Scent 方向差異（scent 方向差異情況）
- **輸入**：網格 10x10，Scents {(0,0,'N')}，起始 (0,0,E)，指令：F
- **預期輸出**：位置 (1,0,E)，方向 E，Lost False，Scents {(0,0,'N')} (不變，因為不同方向)
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_scent_direction_difference

## 測試案例 5：LOST 後後續指令（LOST 後仍有後續指令的情況）
- **輸入**：網格 10x10，起始 (0,0,W)，指令：F L R F
- **預期輸出**：位置 (0,0,W)，方向 W，Lost True，Scents {(0,0,'W')} (LOST 後忽略 L R F)
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_lost_subsequent_commands

## 測試案例 6：完整轉圈（正常情況）
- **輸入**：網格 10x10，起始 (5,5,N)，指令：R R R R
- **預期輸出**：位置 (5,5,N)，方向 N，Lost False，Scents {}
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_full_circle_turns

## 測試案例 7：多方向超出邊界（邊界情況）
- **輸入**：網格 10x10，起始 (0,10,S)，指令：F
- **預期輸出**：位置 (0,10,S)，方向 S，Lost True，Scents {(0,10,'S')}
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_out_bounds_multiple

## 測試案例 8：非法指令處理（反例）
- **輸入**：網格 10x10，起始 (5,5,N)，指令：X F
- **預期輸出**：忽略 X，然後位置 (5,4,N)，方向 N，Lost False，Scents {} (假設非法指令被忽略)
- **實際輸出**：
- **PASS/FAIL**：
- **測試函式名稱**：test_invalid_command
