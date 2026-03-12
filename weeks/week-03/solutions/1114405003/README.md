# Week 03 Robot Scent (Student 1114405003)

## 功能清單
- 地圖 0..W,0..H 可設定（實作於 `robot_core.py`）
- 機器人位置/方向/LOST 狀態追蹤
- 指令 `L`、`R`、`F`
- 越界 `F` 後設定 scent，並標記 `LOST`
- 同 (x,y,dir) 重覆危險 `F` 會被 scent 擋下
- `Robot.execute()` 非 `L/R/F` 拋 `ValueError`
- `LOST` 後停止後續指令
- 測試覆蓋核心需求（旋轉、越界、scent）

## 執行方式
- Python 3.11（或 3.9+）
- 安裝 `pygame`（若有要做互動可選）：`pip install pygame`
- 目前遊戲檔案 `robot_game.py` 為空，測試重點在核心邏輯。

## 測試方式
```
cd 2026-python/weeks/week-03/solutions/1114405003
python -m unittest discover -s tests -p "test_*.py" -v
```

結果：10 tests OK

### 失敗->成功紀錄（Red->Green）
- Red: 新增 `test_invalid_command_raises`，確認 `X` 拋 `ValueError`。
- Green: `Robot.execute` 加上命令驗證；測試通過。
- Refactor: 確認 `move_forward` 內 scent/LOST 應該先檢查，再用最小原則執行。

## 資料結構選擇理由
1. `set[tuple[int,int,str]]` 讓 scent 查找 O(1)，符合要求。
2. `RobotWorld` 負責全局 scent、邊界判斷，`Robot` 負責單機狀態，單一職責分離。
3. `MOVE_DELTAS`、`LEFT_TURN`、`RIGHT_TURN` 為固定映射，避免長 if/else，容易擴充與測試。

## Bug 與修正
- Bug: `Robot.move_forward` 若越界時 `lost` 設置後仍可能被後續命令繼續執行。
- 修正: `Robot.execute` 每一命令前判斷 `if self.lost: break`，同時 `turn_left/right/move_forward` 內也早退出。

## 截圖
- 已放置 `assets/gameplay.png`（請用真實截圖替換）。

## 重播說明
- 目前沒有實作 replay 機制。
- 可新增 `robot_game.py` 包含 `replay` list，按壓 `G` 輸出 `replay.gif`。
