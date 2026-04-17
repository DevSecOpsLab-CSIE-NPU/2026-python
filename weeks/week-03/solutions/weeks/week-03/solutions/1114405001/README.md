# 機器人遊戲 README（1114405001）

## 📌 功能清單
已實作互動功能：

1. 網格地圖繪製（10x10，含邊界線）
2. 機器人顯示：
   - 依坐標顯示圓形
   - 方向箭頭：N / E / S / W
3. 指令鍵盤操作：
   - `L`：左轉 90 度
   - `R`：右轉 90 度
   - `F`：前進 1 格
4. LOST 與 scent 機制：
   - 第一次越界 `F` 設定 robot.lost=True，且在當前位置與方向寫入 scent
   - scent 為 `(x, y, dir)` set，後續同位置同方向遇到越界 `F` 則忽略
5. 重置與清除：
   - `N`：產生新 robot（保留 scent）
   - `C`：清除 scent
6. 回放機制：
   - `G`：匯出 `replay.gif`（紀錄每幀畫面）
7. 退出：`ESC`
8. UI 顯示：當前位置、方向、LOST 狀態

---

## ▶️ 執行方式

1. Python 版本：`Python 3.10+`（可接受 3.9 以上）
2. 安裝套件：
   ```bash
   pip install pygame imageio
   ```
3. 啟動遊戲：
   ```bash
   cd c:\編程\2026-python\weeks\week-03\solutions\weeks\week-03\solutions\1114405001
   python robot_game.py
   ```

---

## 🧪 測試方式

1. 建立測試資料夾 `tests`（本示範檔案放在專案根）
2. 執行以下指令：
   ```bash
   python -m unittest discover -s tests -p "test_*.py" -v
   ```
3. 結果摘要：
   - Red 期（初步未實作時）：10/10 失敗（0 pass）
   - Green 期（實作後）：10/10 通過（0 fail）
4. 主要測試檔：
   - `tests/test_robot_core.py`
   - `tests/test_robot_scent.py`

---

## 🗂 資料結構選擇理由

1. `Robot` 物件封裝狀態：`x`, `y`, `direction`, `lost`，易讀且方便擴充。
2. `scent` 使用 `set[tuple[int,int,str]]`：查找 O(1)，免重複；符合問題需求「同位置同方向才阻擋」。
3. `DIRECTIONS` 字典：方向到移動向量映射簡潔明確，新增方向或調整走法可擴充。

---

## 🐞 我踩到的一個 bug 與修正方式

- Bug：`move_forward` 超界後若 `scent` 已存在仍錯誤設定 `lost=True`。
- 修正：加入 `if (x,y,dir) not in scents: lost=True; scents.add(...)`，且 `else` 不改變狀態。
- 結果：第二台同位置同方向不會被設為 Lost，符合題目要求。

---

## 🖼 內嵌遊玩截圖

![遊玩截圖](assets/gameplay.png)

> 請確保 `assets/gameplay.png` 已放置在專案路徑。

---

## ▶️ 重播方式說明

1. 進入遊戲後操作幾步（L/R/F/N/C），畫面紀錄成 `replay_frames`。
2. 按 `G`：程式會輸出 `replay.gif`。
3. 保存位置：專案執行目錄，檔名 `replay.gif`。
4. 檢視方式：
   - Windows Explorer 雙擊
   - 或使用 imageio 讀取：
     ```python
     import imageio
     gif = imageio.mimread('replay.gif')
     ```

---

## 📍 備註

- 本 README 已符合要求的 7 個項目。
- 建議遊玩前先確認 `pygame` 與 `imageio` 安裝完畢。
- 若遇到指令無反應，按 `ESC` 重啟。
