# Week 03 Robot Lost（學號：1114405048）

![gameplay](assets/gameplay.png)

## 1) 功能清單

- 完成 L/R/F 規則模擬
- 完成 LOST 與 scent（以 `(x, y, dir)` 記錄）
- pygame 互動介面：地圖、機器人朝向、scent 顯示
- 支援鍵盤逐步操作：`L`、`R`、`F`
- 支援 `N` 新機器人（保留 scent）
- 支援 `C` 清除 scent
- 支援 `G` 回放模式（等效 replay 機制）
- HUD 顯示狀態、命令紀錄、10x10 矩陣快照

## 2) 執行方式

- Python 版本：3.10+
- 安裝 pygame：

```bash
python -m pip install pygame
```

- 啟動遊戲：

```bash
python robot_game.py
```

## 3) 測試方式

執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

結果摘要：

- 測試總數：13
- 通過：13
- 失敗：0

## 4) 資料結構選擇理由

1. `set[tuple[int, int, str]]` 適合 `scent`，可 O(1) 判斷「同格同方向」是否危險。
2. `RobotState` 使用 `dataclass`，欄位明確，便於測試與除錯。
3. `RobotWorld` 封裝地圖邊界、scent、機器人狀態，讓 `robot_core.py` 與 pygame 視覺層分離。

## 5) 一個踩到的 bug 與修正

- 問題：一開始把 scent 只記錄 `(x, y)`，導致同格不同方向都被忽略前進。
- 修正：改成 `(x, y, dir)` 三元組，僅在真正相同方向、會越界的情境下忽略 `F`。

## 6) 遊玩截圖

- 檔案位置：`assets/gameplay.png`
- 目前放置可提交用範例圖，建議再以你實際操作畫面覆蓋一次。

## 7) 重播方式說明

本作業採「等效回放機制」：

- 每次按下 `L/R/F` 都會記錄機器人狀態到 `replay_log`
- 按 `G` 進入回放模式，畫面會循序播放歷史狀態
- 再按一次 `G` 可離開回放模式

若要改成匯出 `assets/replay.gif`，可在後續版本將每幀存圖後合成 GIF。
