# AI_USAGE

1) 問: scent 應該記錄方向嗎？
   - 答: 是，因為相同座標但不同方向的下一步風險不同，應區分。
   - 採用: 在 scent key 建立 `(x,y,direction)`。

2) 問: LOST 後是否還執行餘下命令？
   - 答: 不應執行，因為規格要求機器人只執行到掉落為止。
   - 採用: `Robot.execute` 開頭檢查 `if self.lost: break`。

3) 問: 如何寫回放 / replay？
   - 答: 建議儲存每一步狀態到 list，然後輸出 GIF/逐幀顯示。
   - 自修: 本版本先聚焦核心邏輯與測試，`robot_game.py` 仍可以進一步實作。

4) 拒絕建議: 不可直接 copy 現成競賽題解。
   - 原因: 課程要求「AI 產生建議後須自行驗證與理解」。

5) AI 建議不完整例:
   - 原建議僅說「用 set 儲存 scent」而沒說「方向要納入」，我補上方向維度並新增測試 `test_no_scent_share_different_direction`。
