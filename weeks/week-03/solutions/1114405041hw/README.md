# Week 03 Homework - Robot Lost (pygame MVP)

## 功能清單

- 視覺化格子地圖 (0,0) 到 (W,H)
- 顯示機器人位置與朝向 (N/E/S/W)
- 顯示 `scent` 標記點
- 鍵盤逐步執行 `L/R/F`
- `N` 重置新機器人 (保留 scent)
- `C` 清除 scent
- `G` 啟動回放模式 (使用事件歷史)
- 結束遊戲時輸出 `assets/replay.txt`
- 額外提供 `matrix_snapshot()` 便於觀察 10x10/任意尺寸狀態

## 檔案結構

```text
1114405041/
├── robot_core.py
├── robot_game.py
├── assets/
│   ├── gameplay.png
│   ├── replay.gif
│   └── replay.txt
├── tests/
│   ├── test_robot_core.py
│   └── test_robot_scent.py
├── AI_USAGE.md
├── README.md
├── TEST_CASES.md
└── TEST_LOG.md
```

## 執行方式

Python 版本建議：3.10+（Python 3.14 需使用 `pygame-ce`）

```bash
# Python 3.14 請使用 pygame-ce（官方 pygame 無 3.14 預編譯版）
pip install pygame-ce

# Python 3.10–3.12 也可用官方版
# pip install pygame

python robot_game.py
```

## 操作方式

- `L`：左轉
- `R`：右轉
- `F`：前進
- `N`：新機器人
- `C`：清除 scent
- `G`：回放歷史步驟
- `ESC`：離開

## 測試方式

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

目前測試覆蓋：

- 方向旋轉
- 越界 LOST
- scent 忽略危險步驟
- 非法指令處理
- 經典範例行為驗證

## 資料結構選擇理由

1. `RobotState` (dataclass)：把 `x, y, direction, lost` 封裝成不可變狀態，便於測試與回放。
2. `set[(x, y, dir)]` for scent：查詢 O(1)，可精準區分同座標不同方向。
3. `list[history]`：記錄每一步狀態與事件，用於回放模式與 replay log。

## 我踩到的一個 bug 與修正

- 問題：第二台機器人遇到 scent 時，原本寫成直接 `break`，導致後續指令沒執行。
- 修正：改為 `continue` 忽略當下危險 `F`，並繼續執行下一個指令。

## 遊玩截圖

![gameplay](assets/gameplay.png)

## 重播方式說明

- 進入遊戲後按 `G` 會啟動事件回放模式，逐步重現已執行操作。
- 關閉程式時會輸出 `assets/replay.txt`，可作為文字版回放紀錄。
- `assets/replay.gif` 目前提供佔位檔案，之後可替換成實際錄製版本。
