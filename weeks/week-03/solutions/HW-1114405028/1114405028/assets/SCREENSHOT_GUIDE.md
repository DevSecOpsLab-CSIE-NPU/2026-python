# 如何生成 gameplay.png

此檔案應包含實際遊玩過程中的遊戲視窗截圖，展示以下元素：

## 截圖要求

1. **格子地圖**：清晰可見的網格線，標示邊界
2. **機器人位置**：彩色三角形指示當前位置與朝向
3. **scent 標記**：綠色小點標示機器人掉落過的位置
4. **狀態文字**：螢幕上顯示 (x, y, 方向) 座標與 LOST 狀態

## 生成步驟

### 方法 1：手動截圖（推薦）

1. 在終端執行遊戲：
   ```bash
   py robot_game.py
   ```

2. 在遊戲窗口中進行一些操作，例如：
   - 按 `L/R/F` 移動機器人
   - 移動至邊界邊緣以觸發 LOST
   - 按 `N` 建立新機器人以觀察 scent
   - 按 `C` 清除 scent

3. 當看到三個以上的 scent（或至少一個 LOST 狀態）時，按以下按鍵截屏：
   - **Windows**：`Win + Shift + S` 或截圖工具
   - **截屏後裁剪**至只包含遊戲窗口

4. 將截圖儲存為 `gameplay.png`

### 方法 2：自動截圖腳本（進階）

若要自動化，可修改 `robot_game.py` 的遊戲迴圈，在某個特定時刻調用：

```python
# 在遊戲迴圈中適當位置加入
if some_condition:
    pygame.image.save(screen, "assets/gameplay.png")
    print("Screenshot saved!")
```

### 方法 3：模擬遊玩後截圖

建立一個測試腳本 `take_screenshot.py`：

```python
import pygame
import robot_core
from robot_game import CELL_SIZE, MARGIN, GRID_WIDTH, GRID_HEIGHT, BG_COLOR, draw_grid, draw_robot

pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE + MARGIN * 2,
                                  GRID_HEIGHT * CELL_SIZE + MARGIN * 2))

grid = robot_core.Grid(5, 3)
robot = robot_core.Robot(3, 1, "N")

# 執行一些操作以生成有趣的 scent
grid.execute(robot, "FFFRFFFRFFF")  # 移動並留下 scent

# 繪製
screen.fill(BG_COLOR)
draw_grid(screen, grid)
if not robot.lost:
    draw_robot(screen, robot)

pygame.display.flip()
pygame.image.save(screen, "assets/gameplay.png")
print("Screenshot saved to assets/gameplay.png")
pygame.quit()
```

執行：
```bash
py take_screenshot.py
```

---

## 截圖檢查清單

- [ ] 格子線清晰
- [ ] 機器人三角形可見
- [ ] Scent 綠點可見（至少 2～3 個）
- [ ] 機器人或 LOST 標記可見（若觸發過 LOST）
- [ ] 合理的圖像尺寸（建議 400×400 以上，便於在 README 中內嵌展示）

---

## 提示

- 若遊戲窗口在截圖後消失，這是正常的——pygame 的視窗管理在某些系統上會自動關閉
- 若 scent 顯示不明顯，可調整 `robot_game.py` 中的 `SCENT_COLOR` 或 `draw_grid()` 函式中的圓點半徑

