"""
機器人遊戲 Pygame 可視化界面
支持交互式遊玩
"""
import pygame
import sys
from enum import Enum
from robot_core import Robot, RobotGame

# ==================== 常數定義 ====================
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
GRID_SIZE = 50  # 每個格子的像素大小
MARGIN = 50

class GameMode(Enum):
    """遊戲模式"""
    PLAYING = "playing"
    NEW_ROBOT = "new_robot"
    INPUT_POSITION = "input_position"
    INPUT_DIRECTION = "input_direction"
    INPUT_COMMANDS = "input_commands"


class RobotGameUI:
    """
    Pygame 遊戲界面
    """
    
    def __init__(self, map_width=5, map_height=5):
        """
        初始化遊戲 UI
        
        參數：
        - map_width, map_height: 遊戲地圖大小
        """
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("機器人遊戲 - Scent Navigation")
        
        self.game = RobotGame(map_width, map_height)
        self.map_width = map_width
        self.map_height = map_height
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        
        # 當前模式和輸入狀態
        self.mode = GameMode.PLAYING
        self.command_input = ""  # 儲存使用者輸入的指令
        self.robot_positions = []  # 儲存所有機器人的位置歷史（用於回放）
        
        # 顏色定義
        self.COLOR_BG = (240, 240, 240)
        self.COLOR_GRID = (200, 200, 200)
        self.COLOR_BORDER = (0, 0, 0)
        self.COLOR_ROBOT = (0, 100, 255)
        self.COLOR_LOST_ROBOT = (255, 0, 0)
        self.COLOR_SCENT = (255, 200, 0)
        self.COLOR_TEXT = (0, 0, 0)
        self.COLOR_HUD_BG = (200, 220, 255)
        
        # 字體
        self.font_small = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_large = pygame.font.Font(None, 48)
        
        # 建立初始機器人
        self._create_initial_robot()
    
    def _create_initial_robot(self):
        """建立初始機器人"""
        # 預設位置：左下角 (0, 0)
        x = 0
        y = 0
        direction = 'N'
        
        # 確保位置在地圖範圍內
        x = max(0, min(x, self.map_width - 1))
        y = max(0, min(y, self.map_height - 1))
        
        initial_robot = self.game.create_new_robot(x, y, direction)
    
    def get_grid_coords(self, grid_x, grid_y):
        """將格子座標轉換為像素座標"""
        pixel_x = MARGIN + grid_x * GRID_SIZE + GRID_SIZE // 2
        pixel_y = WINDOW_HEIGHT - MARGIN - grid_y * GRID_SIZE - GRID_SIZE // 2
        return pixel_x, pixel_y
    
    def draw_grid(self):
        """繪製背景格子"""
        self.window.fill(self.COLOR_BG)
        
        # 繪製垂直線
        for x in range(self.map_width + 2):
            start_x = MARGIN + x * GRID_SIZE
            pygame.draw.line(
                self.window,
                self.COLOR_GRID,
                (start_x, MARGIN),
                (start_x, WINDOW_HEIGHT - MARGIN),
                1
            )
        
        # 繪製水平線
        for y in range(self.map_height + 2):
            start_y = MARGIN + y * GRID_SIZE
            pygame.draw.line(
                self.window,
                self.COLOR_GRID,
                (MARGIN, start_y),
                (WINDOW_WIDTH - MARGIN, start_y),
                1
            )
        
        # 繪製邊界
        pygame.draw.rect(
            self.window,
            self.COLOR_BORDER,
            (MARGIN, MARGIN, 
             (self.map_width + 1) * GRID_SIZE,
             (self.map_height + 1) * GRID_SIZE),
            2
        )
        
        # 繪製座標標籤
        for x in range(self.map_width + 1):
            label = self.font_small.render(str(x), True, self.COLOR_TEXT)
            label_x = MARGIN + x * GRID_SIZE + GRID_SIZE // 2 - label.get_width() // 2
            self.window.blit(label, (label_x, MARGIN - 25))
        
        for y in range(self.map_height + 1):
            label = self.font_small.render(str(y), True, self.COLOR_TEXT)
            label_y = WINDOW_HEIGHT - MARGIN - y * GRID_SIZE - GRID_SIZE // 2 - label.get_height() // 2
            self.window.blit(label, (MARGIN - 30, label_y))
    
    def draw_scents(self):
        """繪製 scent 標記"""
        for x, y, direction in self.game.scents:
            pixel_x, pixel_y = self.get_grid_coords(x, y)
            pygame.draw.circle(self.window, self.COLOR_SCENT, (pixel_x, pixel_y), 5)
    
    def draw_robots(self):
        """繪製機器人"""
        direction_arrows = {
            'N': '↑',
            'E': '→',
            'S': '↓',
            'W': '←',
        }
        
        for idx, robot in enumerate(self.game.robots):
            pixel_x, pixel_y = self.get_grid_coords(robot.x, robot.y)
            
            # 繪製機器人圓形
            color = self.COLOR_LOST_ROBOT if robot.lost else self.COLOR_ROBOT
            pygame.draw.circle(self.window, color, (pixel_x, pixel_y), 15)
            
            # 繪製方向箭頭
            arrow = direction_arrows.get(robot.direction, '?')
            arrow_text = self.font_medium.render(arrow, True, (255, 255, 255))
            arrow_x = pixel_x - arrow_text.get_width() // 2
            arrow_y = pixel_y - arrow_text.get_height() // 2
            self.window.blit(arrow_text, (arrow_x, arrow_y))
            
            # 繪製機器人標籤（ID）
            robot_id_text = self.font_small.render(f"R{idx}", True, self.COLOR_TEXT)
            self.window.blit(robot_id_text, (pixel_x - robot_id_text.get_width() // 2, pixel_y + 25))
    
    def draw_hud(self):
        """繪製頭部顯示信息（HUD）"""
        hud_y = 10
        hud_items = [
            f"地圖: {self.map_width}x{self.map_height}",
            f"機器人數: {len(self.game.robots)}",
            f"Scent數: {len(self.game.scents)}",
        ]
        
        if self.game.robots:
            current = self.game.get_current_robot()
            if current:
                hud_items.append(f"當前機器人: ({current.x}, {current.y}, {current.direction}) " + 
                               ("LOST" if current.lost else "活躍"))
        
        for idx, item in enumerate(hud_items):
            text = self.font_small.render(item, True, self.COLOR_TEXT)
            self.window.blit(text, (10, hud_y + idx * 25))
        
        # 繪製操作提示
        hints = [
            "L/R/F: 指令   N: 新機器人",
            "C: 清除Scent   ESC: 離開",
        ]
        
        hint_y = WINDOW_HEIGHT - 60
        for idx, hint in enumerate(hints):
            text = self.font_small.render(hint, True, self.COLOR_TEXT)
            self.window.blit(text, (10, hint_y + idx * 25))
    
    def handle_command(self, command):
        """處理指令"""
        current_robot = self.game.get_current_robot()
        if current_robot:
            try:
                current_robot.execute_command(command, self.game)
                self.command_input += command
                
                # 如果機器人 LOST 或輸入了 10 個指令，提示完成
                if current_robot.lost or len(self.command_input) % 10 == 0:
                    pass  # 可在此加入額外邏輯
                
            except ValueError as e:
                print(f"錯誤: {e}")
    
    def create_new_robot(self):
        """建立新機器人的交互流程"""
        print("建立新機器人...")
        print("輸入位置 (例: 2 3):")
        
        try:
            # 簡單的控制台輸入方式
            pos_input = input().strip().split()
            if len(pos_input) != 2:
                print("無效的位置格式")
                return
            
            x, y = int(pos_input[0]), int(pos_input[1])
            
            print("輸入方向 (N/E/S/W):")
            direction = input().strip().upper()
            
            if direction not in ['N', 'E', 'S', 'W']:
                print("無效的方向")
                return
            
            robot = self.game.create_new_robot(x, y, direction)
            self.command_input = ""
            print(f"新機器人建立: ({x}, {y}, {direction})")
            
        except ValueError:
            print("輸入錯誤")
    
    def handle_events(self):
        """處理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key).upper()
                
                # 遊戲指令
                if key in ['L', 'R', 'F']:
                    self.handle_command(key)
                
                elif key == 'N':
                    # 建立新機器人
                    self.create_new_robot()
                
                elif key == 'C':
                    # 清除 scent
                    self.game.clear_scents()
                    print("已清除所有 Scent")
                
                elif key == 'ESCAPE':
                    self.running = False
                
                elif key == 'SPACE':
                    # 切換到下一台機器人
                    self.game.switch_to_next_robot()
                    self.command_input = ""
    
    def update(self):
        """更新遊戲狀態"""
        pass
    
    def draw(self):
        """繪製所有元素"""
        self.draw_grid()
        self.draw_scents()
        self.draw_robots()
        self.draw_hud()
        
        pygame.display.flip()
    
    def run(self):
        """主遊戲迴圈"""
        print("=" * 50)
        print("機器人遊戲啟動！")
        print("=" * 50)
        print("按鍵說明:")
        print("  L: 左轉 (turn left)")
        print("  R: 右轉 (turn right)")
        print("  F: 前進 (move forward)")
        print("  N: 新機器人 (new robot)")
        print("  SPACE: 切換機器人 (switch robot)")
        print("  C: 清除Scent (clear scents)")
        print("  ESC: 離開 (exit)")
        print("=" * 50)
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()
        print("遊戲結束")


def main():
    """主函數"""
    # 可輸入地圖大小
    print("歡迎使用機器人遊戲！")
    print("輸入地圖大小 (預設: 5 5):")
    
    try:
        size_input = input().strip()
        if size_input:
            width, height = map(int, size_input.split())
        else:
            width, height = 5, 5
    except ValueError:
        width, height = 5, 5
    
    ui = RobotGameUI(width, height)
    ui.run()


if __name__ == '__main__':
    main()
