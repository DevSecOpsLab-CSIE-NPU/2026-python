# AI_USAGE - Robot Lost

## 我問 AI 的問題

1. `scent` 應該記錄什麼欄位才不會誤判？
2. `robot_core.py` 要怎麼設計才容易測試、又不依賴 pygame？
3. 如何拆出最少但完整的單元測試，覆蓋旋轉、越界、scent 三大重點？
4. 回放機制如果不輸出 gif，還有哪些等效做法？

## 採用的建議與原因

- 採用 `set[(x, y, dir)]` 儲存 scent。
	- 原因：同格不同方向不能共用警告，這樣最精準。
- 採用 `RobotState` + 純函式 (`step_robot`, `run_commands`) 的 core 設計。
	- 原因：可以直接用 unittest 驗證，不受 UI 影響。
- 採用雙測試檔分工：
	- `test_robot_core.py` 主要測旋轉/邊界/錯誤處理。
	- `test_robot_scent.py` 主要測 scent 與整合案例。

## 拒絕的建議與原因

- 建議內容：把 scent 簡化為 `set[(x, y)]`。
- 拒絕原因：會誤把不同方向的危險點當成同一個，與題意不符。

## AI 建議不完整、我自行修正的一例

- 不完整處：一版建議在遇到 scent 時直接 `break` 指令迴圈。
- 問題：這會讓機器人提早停止，違反「忽略該指令後繼續下一個指令」。
- 我的修正：在 scent 命中時改成 `continue`，且只在真正掉落時才 `LOST` 並中止。
