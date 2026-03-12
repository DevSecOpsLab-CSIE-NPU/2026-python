# Week 03 測試執行日誌

## 執行環境

- Python 版本：3.10
- 測試框架：unittest
- 測試目錄：`weeks/week-03/solutions/1111405040/tests/`
- 測試指令：

```bash
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

---

## 第一次執行（Red，失敗）

### 執行結果摘要

- 測試總數：2（測試模組）
- 通過數：0
- 失敗數：2（import error）

### 錯誤重點

- `ModuleNotFoundError: No module named 'robot_core'`
- 兩個測試模組 `test_robot_core`、`test_robot_scent` 均無法載入。

### 從失敗到下一步的修改

1. 建立 `robot_core.py`，補上 `RobotWorld`、`RobotState`、LOST/scent 規則。
2. 補上非法指令例外 `RobotInstructionError`，讓 `X` 有明確處理策略。

---

## 第二次執行（Green，部分通過）

### 執行結果摘要

- 測試總數：12
- 通過數：11
- 失敗數：1

### 失敗重點

- `test_robot_with_scent_can_continue_next_instruction` 預期值不正確。
- 測試用的指令 `FRF` 在最後一步會向東越界，應該 LOST。

### 調整內容

- 將該測試指令修正為 `FR`，專注驗證「忽略危險 F 後仍可繼續下一步」。

---

## 第三次執行（Green，全通過）

### 執行結果摘要

- 測試總數：12
- 通過數：12
- 失敗數：0

### 結果

- 旋轉規則、越界判定、scent 行為、LOST 停止、非法指令處理皆通過。

---

## Refactor 紀錄

在功能正確後做以下整理，並再次確認測試全綠：

1. 將方向旋轉與位移規則集中為常數表（`LEFT_TURN`, `RIGHT_TURN`, `MOVE_STEP`）。
2. 將狀態驗證集中於 `validate_state()`。
3. 保持 `robot_core.py` 不依賴 pygame，讓測試可單獨執行。
