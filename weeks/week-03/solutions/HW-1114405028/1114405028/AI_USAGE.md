# AI_USAGE.md - AI 協助記錄

根據作業規則「可以使用 AI 協助拆解規格、產生雛形、建議測試案例」，此檔案記錄 AI 的使用情況。

---

## 我問 AI 的問題

### 問題 1：Python dataclass 如何實作機器人狀態？

**背景**：需要一個簡單的資料結構來存儲機器人的 x, y, dir, lost 四個屬性。

**AI 建議**：使用 Python 內建的 `dataclasses.dataclass` 修飾符。

**採用原因**：
- 程式碼簡潔明了
- 自動產生 `__init__`, `__eq__` 等常用方法
- 提高可讀性且符合 Python 風格指南

**實作結果**：
```python
from dataclasses import dataclass

@dataclass
class Robot:
    x: int
    y: int
    dir: str
    lost: bool = False
```

---

### 問題 2：如何用 set 記錄 scent？

**背景**：scent 需要儲存多筆 (x, y, dir) 記錄，並快速查詢是否存在某筆記錄。

**AI 建議**：使用 `set[tuple[int, int, str]]`。

**採用原因**：
- Set 的成員檢查是 O(1) 時間複雜度，比 list 高效
- Tuple 是 immutable，適合用作 set 的元素
- 自動去重（不用擔心重複記錄）
- 語意明確：「位置集合」

**實作結果**：
```python
self.scents: set[tuple[int, int, str]] = set()

# 檢查 scent 是否存在
if (robot.x, robot.y, robot.dir) in self.scents:
    return

# 新增 scent
self.scents.add((robot.x, robot.y, robot.dir))
```

---

### 問題 3：方向轉換的索引循環如何實作？

**背景**：N/E/S/W 四個方向需要支援 L（左轉-1） 和 R（右轉+1），且循環回到起點。

**AI 建議**：使用列表索引與模運算。

**採用原因**：
- 簡單直觀，易於維護
- 支援自然的循環邏輯

**實作結果**：
```python
directions = ["N", "E", "S", "W"]

def _turn_left(self, robot: Robot) -> None:
    idx = directions.index(robot.dir)
    robot.dir = directions[(idx - 1) % 4]

def _turn_right(self, robot: Robot) -> None:
    idx = directions.index(robot.dir)
    robot.dir = directions[(idx + 1) % 4]
```

---

### 問題 4：pytest vs unittest 應該用哪一個？

**背景**：作業規格没有強制指定測試框架。

**AI 建議**：使用 Python 內建 `unittest`。

**採用原因**：
- 無需額外安裝
- 學生環境通常預裝
- 作業規格中範例使用 `unittest`
- 對初學者友善

**實作結果**：用 `unittest.TestCase` 編寫所有測試。

---

### 問題 5：pygame 如何顯示簡單的格子與機器人？

**背景**：需要一個最小化的 pygame MVP 來滿足「互動視覺呈現」要求。

**AI 建議**：使用 `pygame.draw.line()` 畫線、`pygame.draw.polygon()` 畫三角形。

**採用原因**：
- 不需要複雜的圖像資源
- 程式碼輕量化
- 足以驗證邏輯正確性

**實作結果**：`robot_game.py` 中使用基礎 draw 函式。

---

## 我採用的建議與原因

### ✅ 採用：dataclass 改進程式結構

**原因**：提高程式可讀性，減少重複程式碼。

### ✅ 採用：set 作為 scent 集合

**原因**：效能與語意上都優於 list。

### ✅ 採用：模運算實作循環方向

**原因**：簡潔且容易維護。

### ✅ 採用：pygame 基礎繪圖函式

**原因**：符合 MVP 精神，快速實現需求。

---

## 我拒絕的建議與原因

### ❌ 拒絕：使用 numpy 陣列表示格子狀態

**原因**：
- 題目已提供核心資料結構（set + tuple）
- 加入 numpy 會增加掌握難度
- 此專案規模不需要 numpy 的最佳化

### ❌ 拒絕：使用 pygame sprite 與 group

**原因**：
- MVP 階段不需要複雜的渲染系統
- 簡單的迴圈繪圖已足夠
- 專注於核心邏輯驗證而非視覺華麗度

### ❌ 拒絕：using type hints everywhere

**原因**：
- 學習重點在邏輯設計，不在 Python 進階型別系統
- 適度使用（如 `Grid`, `Robot`）即可
- 完全型別化會使初學者分心

---

## AI 建議不完整、自行修正的案例

### 案例 1：scent 方向隔離測試

**AI 初版建議**：
```python
def test_scent_does_not_apply_other_directions(self):
    r1 = robot_core.Robot(1, 2, "N")
    self.grid.execute(r1, "F")
    r2 = robot_core.Robot(1, 2, "E")
    self.grid.execute(r2, "F")
    self.assertTrue(r2.lost)
```

**問題**：
在 2×2 格子中，位置 (1, 2) 朝 E 前進會到 (2, 2)，仍在範圍內，測試失敗。

**自行修正**：
```python
def test_scent_does_not_apply_other_directions(self):
    g = robot_core.Grid(0, 0)  # 最小格子
    r1 = robot_core.Robot(0, 0, "N")
    g.execute(r1, "F")
    r2 = robot_core.Robot(0, 0, "E")
    g.execute(r2, "F")
    self.assertTrue(r2.lost)
```

改用 0×0 格子確保任何方向都會越界，驗證 scent 方向隔離是否正確生效。

### 案例 2：pygame 窗口無響應

**AI 初版建議**：直接呼叫 `pygame.init()` 和 `display.set_mode()`。

**問題**：
在某些 Windows 環境中無法正常顯示窗口或立即關閉。

**自行修正**：
- 加入 `os.environ['PYGAME_HIDE_SUPPORT_PROMPT']` 抑制歡迎訊息
- 加入異常捕捉與診斷輸出
- 加入印刷語句追蹤程式流程

```python
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    pygame.init()
    print(f"[INFO] Window created: {WINDOW_WIDTH}x{WINDOW_HEIGHT}")
except Exception as e:
    print(f"[ERROR] Failed to initialize pygame: {e}")
    traceback.print_exc()
    sys.exit(1)
```

---

## 總結

- **AI 協助程度**：10%～20%（主要用於快速確認最佳實踐）
- **自主實作程度**：80%～90%（核心邏輯、測試設計、bug 修復）
- **關鍵心得**：AI 的建議是出發點，理解並驗證建議內容、根據實際情況調整，才是真正的學習。

