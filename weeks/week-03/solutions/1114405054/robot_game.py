"""
Robot Lost - Pygame Visualization
使用 pygame 實現互動式遊戲界面

功能：
- 顯示格子地圖
- 顯示機器人位置和方向
- 顯示 scent 標記
- 鍵盤控制：L/R/F 移動，N 新機器人，C 清除 scent，ESC 離開
- 狀態 HUD（機器人狀態、指令記錄）
"""

import sys
import os
from typing import List, Tuple

# 嘗試導入 pygame，如果失敗則給出裝置提示
try:
    import pygame
    from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_l, K_r, K_f, K_n, K_c
except ImportError:
    print("pygame 未安裝。請執行:")
    print("  pip install pygame")
    sys.exit(1)

# 加入上級目錄以導入 robot_core
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from robot_core import RobotSimulator, Robot


class RobotGameVisualizer:
    """Pygame 遊戲可視化器"""
    
    # 顏色定義
    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)
    COLOR_GRAY = (200, 200, 200)
    COLOR_DARK_GRAY = (100, 100, 100)
    COLOR_BLUE = (0, 100, 255)
    COLOR_RED = (255, 0, 0)
    COLOR_GREEN = (0, 200, 0)
    COLOR_YELLOW = (255, 255, 0)
    COLOR_PURPLE = (200, 0, 200)
    
    def __init__(self, width: int = 5, height: int = 5, grid_size: int = 60):
        """
        初始化視覺化器
        
        Args:
            width: 模擬世界寬度
            height: 模擬世界高度
            grid_size: 每格的像素大小
        """
        self.world_width = width
        self.world_height = height
        self.grid_size = grid_size
        self.margin = 50
        
        # 計算視窗大小
        self.window_width = width * grid_size + 2 * self.margin
        self.window_height = height * grid_size + 2 * self.margin + 100  # 額外空間給 HUD
        
        # 初始化 pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Robot Lost - Pygame Visualization")
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.Font(None, 24)
        self.font_large = pygame.font.Font(None, 32)
        
        # 模擬器
        self.simulator = RobotSimulator(width, height)
        
        # 遊戲狀態
        self.current_robot: Robot = None
        self.command_history: str = ""
        self.running = True
        self.game_log: List[str] = []
    
    def world_to_screen(self, x: int, y: int) -> Tuple[int, int]:
        """將世界座標轉換為屏幕座標"""
        screen_x = self.margin + x * self.grid_size
        screen_y = self.window_height - self.margin - (y + 1) * self.grid_size
        return (screen_x, screen_y)
    
    def draw_grid(self):
        """繪製格子背景"""
        # 背景
        self.screen.fill(self.COLOR_WHITE)
        
        # 垂直線
        for x in range(self.world_width + 1):
            screen_x = self.margin + x * self.grid_size
            start = (screen_x, self.margin)
            end = (screen_x, self.window_height - self.margin - 100)
            pygame.draw.line(self.screen, self.COLOR_GRAY, start, end, 1)
        
        # 水平線
        for y in range(self.world_height + 1):
            screen_y = self.window_height - self.margin - 100 - y * self.grid_size
            start = (self.margin, screen_y)
            end = (self.window_width - self.margin, screen_y)
            pygame.draw.line(self.screen, self.COLOR_GRAY, start, end, 1)
        
        # 邊界標籤 (x軸)
        for x in range(self.world_width + 1):
            screen_x = self.margin + x * self.grid_size
            text = self.font_small.render(str(x), True, self.COLOR_BLACK)
            self.screen.blit(text, (screen_x - 10, self.window_height - self.margin - 100 + 10))
        
        # 邊界標籤 (y軸)
        for y in range(self.world_height + 1):
            screen_y = self.window_height - self.margin - 100 - y * self.grid_size
            text = self.font_small.render(str(y), True, self.COLOR_BLACK)
            self.screen.blit(text, (self.margin - 40, screen_y - 10))
    
    def draw_scent(self):
        """繪製 scent 標記"""
        for x, y, direction in self.simulator.get_scent():
            screen_x, screen_y = self.world_to_screen(x, y)
            # 在格子中心附近畫個小圓點
            center = (screen_x + self.grid_size // 2, screen_y + self.grid_size // 2)
            pygame.draw.circle(self.screen, self.COLOR_YELLOW, center, 5)
    
    def draw_robot(self, robot: Robot):
        """繪製單個機器人"""
        screen_x, screen_y = self.world_to_screen(robot.x, robot.y)
        center = (screen_x + self.grid_size // 2, screen_y + self.grid_size // 2)
        
        # 機器人顏色
        if robot.lost:
            color = self.COLOR_RED
        elif robot == self.current_robot:
            color = self.COLOR_BLUE
        else:
            color = self.COLOR_GREEN
        
        # 繪製機器人圓形
        pygame.draw.circle(self.screen, color, center, self.grid_size // 3)
        
        # 繪製方向指示器（箭頭）
        direction_offset = {
            'N': (0, -15),
            'E': (15, 0),
            'S': (0, 15),
            'W': (-15, 0)
        }
        dx, dy = direction_offset[robot.direction]
        end_pos = (center[0] + dx, center[1] + dy)
        pygame.draw.line(self.screen, self.COLOR_BLACK, center, end_pos, 2)
    
    def draw_robots(self):
        """繪製所有機器人"""
        for robot in self.simulator.robots:
            self.draw_robot(robot)
    
    def draw_hud(self):
        """繪製 HUD（狀態資訊）"""
        hud_y = self.window_height - 100
        
        # 標題
        title = self.font_large.render("Robot Lost - Pygame Game", True, self.COLOR_BLACK)
        self.screen.blit(title, (self.margin, hud_y))
        
        # 控制說明
        controls = [
            "Controls: L/R/F (rotate/move) | N (new robot) | C (clear scent) | ESC (exit)",
            f"Current Robot: {self.current_robot if self.current_robot else 'None'} | Commands: {self.command_history}",
            f"Total Robots: {len(self.simulator.robots)} | Scents: {len(self.simulator.get_scent())} | Log: {len(self.game_log)} events"
        ]
        
        for i, text in enumerate(controls):
            rendered = self.font_small.render(text, True, self.COLOR_BLACK)
            self.screen.blit(rendered, (self.margin, hud_y + 30 + i * 22))
    
    def add_robot_at_cursor(self, x: int = None, y: int = None, direction: str = 'N'):
        """添加新機器人"""
        if x is None:
            x = 1
        if y is None:
            y = 1
        robot = self.simulator.add_robot(x, y, direction)
        self.current_robot = robot
        self.command_history = ""
        self.game_log.append(f"New robot at ({x}, {y}) facing {direction}")
    
    def handle_input(self):
        """處理輸入事件"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_n:
                    self.add_robot_at_cursor()
                elif event.key == K_c:
                    self.simulator.clear_scent()
                    self.game_log.append("Scent cleared")
                elif self.current_robot and not self.current_robot.lost:
                    if event.key == K_l:
                        try:
                            self.simulator.execute_command(self.current_robot, 'L')
                            self.command_history += 'L'
                            self.game_log.append(f"Robot L -> {self.current_robot.direction}")
                        except ValueError:
                            pass
                    elif event.key == K_r:
                        try:
                            self.simulator.execute_command(self.current_robot, 'R')
                            self.command_history += 'R'
                            self.game_log.append(f"Robot R -> {self.current_robot.direction}")
                        except ValueError:
                            pass
                    elif event.key == K_f:
                        try:
                            self.simulator.execute_command(self.current_robot, 'F')
                            self.command_history += 'F'
                            if self.current_robot.lost:
                                self.game_log.append(f"Robot LOST at {self.current_robot.get_position()}")
                            else:
                                self.game_log.append(f"Robot moved to {self.current_robot.get_position()}")
                        except ValueError:
                            pass
    
    def run(self):
        """主遊戲循環"""
        # 創建第一個機器人
        self.add_robot_at_cursor()
        
        while self.running:
            self.handle_input()
            
            # 繪製所有元素
            self.draw_grid()
            self.draw_scent()
            self.draw_robots()
            self.draw_hud()
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
    
    def save_screenshot(self, path: str = "gameplay.png"):
        """保存屏幕截圖"""
        pygame.image.save(self.screen, path)
        self.game_log.append(f"Screenshot saved to {path}")


def main():
    """主程式入口"""
    game = RobotGameVisualizer(width=5, height=5, grid_size=60)
    game.run()


if __name__ == '__main__':
    main()
