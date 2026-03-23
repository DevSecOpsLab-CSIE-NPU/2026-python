# Robot Lost - 項目說明

## 功能清單

實現了以下互動功能：

- ✅ **格子地圖顯示** - 5x5 網格，坐標標籤清晰
- ✅ **機器人位置與方向** - 彩色圓形 + 箭頭指示
  - 藍色：當前機器人
  - 綠色：其他活躍機器人
  - 紅色：LOST 機器人
- ✅ **Scent 標記** - 黃色圓點表示機器人越界點
- ✅ **鍵盤互動**
  - `L` / `R` / `F`：旋轉/移動當前機器人
  - `N`：創建新機器人（保留 scent）
  - `C`：清除所有 scent
  - `ESC`：退出遊戲
- ✅ **HUD 狀態顯示** - 實時顯示機器人數量、指令記錄、Scent 數量

## 執行方式

### 環境要求
- Python 3.8+
- pygame（自動或手動安裝）

### 安裝依賴

```bash
pip install pygame
```

### 啟動遊戲

```bash
cd weeks/week-03/solutions/1114405054/
python robot_game.py
```

## 測試方式

### 執行單元測試

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 測試結果摘要

- **總測試數**：37
- **通過**：37/37 ✅
- **失敗**：0

### 測試覆蓋面

1. **方向旋轉** (5 tests)
   - N + L = W, N + R = E
   - 連續 4 次 L/R 回原方向
   - 複雜旋轉序列

2. **移動與邊界** (10 tests)
   - 各方向移動 (N/E/S/W)
   - 邊界條件判定
   - 越界 = LOST

3. **Scent 應用** (12 tests)
   - Scent 記錄與查詢
   - 同位置同方向被保護
   - 同位置不同方向無保護
   - 多機器人場景
   - Scent 清除

4. **LOST 狀態** (4 tests)
   - LOST 後停止執行
   - 無效指令處理

5. **複雜場景** (6 tests)
   - 多機器人多 Scent
   - 邊界角落情況

## 資料結構選擇理由

### 1. **Set for Scent: `Set[Tuple[int, int, str]]`**
   - **為什麼**：O(1) 查詢速度，無需遍歷
   - **好處**：在每次移動前檢查 scent 非常快
   - **對比**：List 需要 O(n) 遍歷；Dict 不必要

### 2. **List for Robots: `List[Robot]`**
   - **為什麼**：順序很重要（多機器人場景）
   - **好處**：可按入場順序遍歷；支持索引訪問
   - **對比**：Set 會失去順序；Dict 鍵不明確

### 3. **Direction as String: `'N' | 'E' | 'S' | 'W'`**
   - **為什麼**：可讀性強，易於調試
   - **好處**：無需 Enum；直觀匹配位移表
   - **對比**：整數 Enum 需額外轉換；State Pattern 過度

## 踩到的 Bug 及修正

### Bug #1：方向偏移表的 Y 軸方向
**問題**：初始代碼中 N 向北時 y-1，但地圖坐標應該 y+1
**修正**：將 `'N': (0, -1)` 改為 `'N': (0, 1)`
```python
# 錯誤
DIR_OFFSETS = {
    'N': (0, -1),  # ❌ 這會讓北向變成向下
    ...
}

# 正確
DIR_OFFSETS = {
    'N': (0, 1),   # ✅ 北向增加 y
    ...
}
```

### Bug #2：Scent 點在越界時的位置記錄
**問題**：應記錄 **掉落前的位置**（機器人還未越界時的座標）
**修正**：在 `_move_forward()` 中，於 LOST 前保存舊座標
```python
# 修正邏輯
if (old_x, old_y, robot_dir) in scent:  # 檢查邊界前座標
    return False
else:
    robot.lost = True
    self.scent.add((old_x, old_y, robot_dir))  # ✅ 記錄邊界前座標
```

### Bug #3：測試中的邊界理解
**問題**：測試假設 (5, 5) 地圖中不能越界到 (6, 5) 或 (5, 6)
**修正**：明確邊界為 **[0, width] × [0, height]**，所以 5×5 包含點 (0,0) 到 (5,5)
- 邊界內：`0 <= x <= 5` 且 `0 <= y <= 5`
- 越界：`x < 0 or x > 5 or y < 0 or y > 5`

## 重播方式說明

### 實時重播（遊戲中）
1. 運行 `robot_game.py` 啟動遊戲
2. 所有操作（L/R/F）實時在界面上顯示
3. HUD 下方的 "Commands" 欄顯示已執行的指令序列
4. 按 `C` 可清除 scent 重新開始

### 導出重播截圖
在遊戲中按鍵後，可手動 `print(game.save_screenshot())` 導出當前狀態截圖

### 理想擴展（未來改進）
- [ ] 記錄指令序列到文件，支持重放
- [ ] 生成 animated GIF 顯示執行過程
- [ ] 導出 JSON 日誌用於分析

## 使用範例

### 遊戲示例

```
1. 啟動遊戲
   $ python robot_game.py

2. 看到初始機器人在 (1, 1) 朝 N（北）

3. 按 'R' 兩次 -> 改為朝 S（南）
   HUD 顯示：Commands: RR

4. 按 'F' 三次 -> 移動到 (1, -2)，在 (1, 0) 時越界
   第二個 F 會標記 LOST
   HUD 顯示：Robot LOST at (1, 0, S)
   
5. 按 'N' -> 新機器人在 (1, 1) 朝 N，保留之前的 scent
   
6. 按 'C' -> 清除所有 scent
```

---

**建立於** 2026-03-23
**作者** Student ID: 1114405054
