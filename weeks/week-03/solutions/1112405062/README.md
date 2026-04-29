# Week 03 回家作業 - Robot Lost

## 功能清單

- [x] 2D 格子地圖顯示
- [x] 機器人位置與方向顯示（箭頭三角形）
- [x] scent 標記顯示（橙色圓點）
- [x] 鍵盤輸入指令（L/R/F）執行
- [x] 隨機生成新機器人（N 鍵）
- [x] 清除所有 scent（C 鍵）
- [x] 截圖保存（需手動觸發）
- [x] 機器人狀態顯示（位置、方向、LOST）
- [x] 指令緩衝區顯示
- [x] 邊界檢測與越界處理
- [x] scent 機制（阻止後續機器人掉落）
- [x] 字串矩陣視圖（可選顯示）

---

## 執行方式

### Python 版本
- Python 3.14+

### 安裝依賴
```bash
pip install pygame
```

### 啟動遊戲
```bash
python robot_game.py [world_width] [world_height]
# 例如：python robot_game.py 5 3
```

### 測試執行
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 測試結果摘要

- **測試檔案**：2 個（test_robot_core.py, test_robot_scent.py）
- **測試函式**：29 個
- **全部通過**：✓

### 覆蓋範圍
- 方向旋轉測試：6 個
- 移動與越界測試：6 個
- scent 機制測試：7 個
- LOST 行為測試：2 個
- 完整場景測試：3 個
- 其他輔助測試：5 個

---

## 資料結構選擇理由

### 1. 方向表示：索引 + 列表
```python
DIRS = ['N', 'E', 'S', 'W']
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]
```
- **理由**：用整數索引 (0-3) 取代字串，計算左/右轉只需 `±1 % 4`
- **優點**：比 if-elif 判斷更簡潔，效能更好

### 2. 機器人狀態：類別屬性
```python
class Robot:
    def __init__(self, x, y, direction, world_width, world_height):
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False
```
- **理由**：將狀態封裝在類別中，每個機器人有獨立狀態
- **優點**：易於管理多個機器人，狀態清晰

### 3. scent 儲存：Set[Tuple[int, int, str]]
```python
self.scents: Set[Tuple[int, int, str]] = set()
```
- **理由**：需要記錄 (x, y, direction) 三個資訊來區分不同方向的危險
- **優點**：O(1) 查詢速度，自動去重

---

## 踩到的 Bug 與修正

### Bug：scent 未記錄方向

**問題描述**：
一開始 scent 只存 (x, y)：
```python
self.scents: Set[Tuple[int, int]] = set()
```

導致同位置不同方向的危險無法區分：
- Robot A 向北在 (5,5) 掉落
- Robot B 向東仍在 (5,5)，不應受影響

**修正方式**：
```python
self.scents: Set[Tuple[int, int, str]] = set()
# 存儲 (5, 5, 'N') 和 (5, 5, 'E') 是不同的危險點
```

**教訓**：仔細閱讀題目規格，題目說「掉落前最後位置 + 當前方向」已經明確說明了方向。

---

## 遊玩截圖

![gameplay](assets/gameplay.png)

---

## 重播方式

### 截圖
1. 在遊戲中按 `G` 鍵可截圖保存
2. 截圖會保存為 `assets/replay.png`

### 手動重播
1. 每次操作會記錄到 history 列表
2. 可在程式碼中存取 `game.history` 查看操作歷史

---

## 檔案結構

```
week-03/solutions/1112405062/
├── robot_core.py              # 核心邏輯（可獨立測試）
├── robot_game.py              # pygame 遊戲主程式
├── assets/
│   └── gameplay.png          # 遊玩截圖
├── tests/
│   ├── test_robot_core.py    # 核心邏輯測試
│   └── test_robot_scent.py   # scent 機制測試
├── TEST_CASES.md             # 測試案例
├── TEST_LOG.md               # 測試執行紀錄
├── AI_USAGE.md               # AI 使用記錄
└── README.md                 # 本文件
```
