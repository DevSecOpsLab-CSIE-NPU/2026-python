# Week 03 Homework - Robot Lost（1114405056 - 尤靖崵）

![gameplay](assets/gameplay.png)

## 1. 功能清單

- 完整支援 `L / R / F` 指令規則
- 機器人越界時會標記 `LOST`，並在最後安全點留下 `scent`
- 後續機器人在相同 `(x, y, dir)` 會忽略危險 `F`，繼續執行下一步
- pygame 介面顯示地圖、機器人朝向、scent 標記與 HUD 狀態
- 支援操作鍵：`L`、`R`、`F`、`N`、`C`、`P`、`G`、`ESC`
- 提供回放機制（`P`）：依序播放整段操作歷程

## 2. 執行方式

- Python 版本：`3.9+`
- 安裝套件：

```bash
python -m pip install pygame
```

- 啟動遊戲：

```bash
python robot_game.py
```

## 3. 測試方式

- 在本資料夾執行：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

- 目前測試結果：`17/17` 通過

## 4. 資料結構選擇理由

1. `RobotState`（dataclass）
   - 將 `x, y, direction, lost` 集中為單一狀態物件，便於測試與回放快照。
2. `set[tuple[int, int, str]]` 作為 `scent`
   - 以 `(x, y, dir)` 當 key，可 O(1) 查詢危險邊界，且方向可精準區分。
3. `list[ReplayFrame]` 保留操作時間序列
   - 每次指令後拍快照，回放時只要按索引逐幀顯示即可。
4. `dict` 位移表（`MOVE_VECTOR`）
   - 方向轉位移一對一，簡化 `F` 的邏輯與可讀性。

## 5. 我踩到的一個 bug 與修正

- 問題：`scent` 若只存 `(x, y)` 會導致同位置不同方向也被錯誤保護。
- 修正：改為存 `(x, y, dir)`，並在測試加入「同格不同方向不共用 scent」案例，確認行為正確。

## 6. 遊玩截圖

- 截圖檔：`assets/gameplay.png`
- 可在遊戲中按 `G` 直接輸出最新畫面。

## 7. 重播方式說明

- 本作業採「內建回放機制」而非匯出 GIF。
- 先進行一段操作後按 `P`，系統會逐幀重播歷程。
- 回放結束會自動回到即時操作模式。
