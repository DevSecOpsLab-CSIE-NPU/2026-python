"""
Auto-generate a screenshot of the game with some interesting state.
Run this to automatically create assets/gameplay.png
"""
import os
import sys

# 抑制 pygame 歡迎訊息
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# 檢查並安裝 pygame（若需要）
try:
    import pygame
except ImportError:
    print("[INFO] pygame not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

# 新增路徑以匯入 robot_core
sys.path.insert(0, os.path.dirname(__file__))
import robot_core

# 常數設定
CELL_SIZE = 40
MARGIN = 20
GRID_WIDTH = 5
GRID_HEIGHT = 3
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE + MARGIN * 2
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + MARGIN * 2

# 顏色
BG_COLOR = (30, 30, 30)
GRID_COLOR = (200, 200, 200)
ROBOT_COLOR = (200, 50, 50)
SCENT_COLOR = (50, 200, 50)


def draw_grid(surface, grid):
    # 繪製網格線（垂直）
    for x in range(GRID_WIDTH + 1):
        pygame.draw.line(surface, GRID_COLOR,
                         (MARGIN + x * CELL_SIZE, MARGIN),
                         (MARGIN + x * CELL_SIZE, MARGIN + GRID_HEIGHT * CELL_SIZE))
    # 繪製網格線（水平）
    for y in range(GRID_HEIGHT + 1):
        pygame.draw.line(surface, GRID_COLOR,
                         (MARGIN, MARGIN + y * CELL_SIZE),
                         (MARGIN + GRID_WIDTH * CELL_SIZE, MARGIN + y * CELL_SIZE))
    # 繪製 scent（綠點）
    for (sx, sy, sdir) in grid.scents:
        cx = MARGIN + sx * CELL_SIZE + CELL_SIZE // 2
        cy = MARGIN + (GRID_HEIGHT - sy) * CELL_SIZE - CELL_SIZE // 2
        pygame.draw.circle(surface, SCENT_COLOR, (cx, cy), 5)


def draw_robot(surface, robot):
    # 轉換邏輯座標到螢幕座標
    cx = MARGIN + robot.x * CELL_SIZE + CELL_SIZE // 2
    cy = MARGIN + (GRID_HEIGHT - robot.y) * CELL_SIZE - CELL_SIZE // 2
    
    # 繪製三角形指向機器人方向
    size = CELL_SIZE // 3
    if robot.dir == "N":
        points = [(cx, cy - size), (cx - size, cy + size), (cx + size, cy + size)]
    elif robot.dir == "S":
        points = [(cx, cy + size), (cx - size, cy - size), (cx + size, cy - size)]
    elif robot.dir == "E":
        points = [(cx + size, cy), (cx - size, cy - size), (cx - size, cy + size)]
    elif robot.dir == "W":
        points = [(cx - size, cy), (cx + size, cy - size), (cx + size, cy + size)]
    
    pygame.draw.polygon(surface, ROBOT_COLOR, points)


def main():
    print("[INFO] Initializing pygame...")
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Robot Lost - Screenshot Generation")
    
    # 建立格子與機器人
    grid = robot_core.Grid(GRID_WIDTH, GRID_HEIGHT)
    robot = robot_core.Robot(0, 0, "N")
    
    # 執行一連串操作以形成有趣的遊戲狀態
    print("[INFO] Executing demo commands...")
    
    # 第一台機器人：移動並觸發 LOST
    grid.execute(robot, "FFFRFFFRFFFRFFFR")  # 繞邊界移動多次
    
    # 第二台機器人：在 scent 旁邊移動
    robot2 = robot_core.Robot(3, 0, "N")
    grid.execute(robot2, "FFFFRFFF")
    
    # 清空，建立第三台以展示多個 scent
    robot3 = robot_core.Robot(5, 1, "W")
    grid.execute(robot3, "FFF")
    
    # 最後的機器人在中央
    robot_final = robot_core.Robot(2, 1, "N")
    
    # 繪製遊戲畫面
    screen.fill(BG_COLOR)
    draw_grid(screen, grid)
    if not robot_final.lost:
        draw_robot(screen, robot_final)
    
    # 繪製狀態文字
    font = pygame.font.SysFont(None, 24)
    status_text = f"({robot_final.x},{robot_final.y},{robot_final.dir})"
    text_surface = font.render(status_text, True, (255, 255, 255))
    screen.blit(text_surface, (MARGIN, WINDOW_HEIGHT - MARGIN - 20))
    
    # 控制說明
    info_text = "Controls: L/R/F, N=new, C=clear, G=replay, ESC=quit"
    info_surface = font.render(info_text, True, (200, 200, 200))
    screen.blit(info_surface, (MARGIN, 5))
    
    pygame.display.flip()
    
    # 儲存截圖
    output_path = os.path.join(os.path.dirname(__file__), "assets", "gameplay.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    pygame.image.save(screen, output_path)
    print(f"[SUCCESS] Screenshot saved to: {output_path}")
    print(f"[INFO] Scents recorded: {len(grid.scents)}")
    
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
