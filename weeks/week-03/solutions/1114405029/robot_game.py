import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from robot_core import RobotWorld, Robot

WIDTH = 1000
HEIGHT = 700

CELL_SIZE = 80
MAP_W, MAP_H = 5, 5

MAP_OFFSET_X = 40
MAP_OFFSET_Y = HEIGHT - 120

UI_X = 600


class RobotGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("機器人懸崖挑戰")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("microsoftjhenghei", 20, bold=True)

        self.world = RobotWorld(MAP_W, MAP_H)
        self.reset_robot()

        self.load_assets()

    # -------------------------
    def load_assets(self):
        self.img_platform = pygame.transform.scale(
            pygame.image.load("assets/platform.png").convert_alpha(),
            (CELL_SIZE, CELL_SIZE)
        )

        self.img_scent = pygame.transform.scale(
            pygame.image.load("assets/scent.png").convert_alpha(),
            (CELL_SIZE, CELL_SIZE)
        )

        raw_robot = pygame.image.load("assets/robot.png").convert_alpha()
        self.robot_sprites = self.split_robot_images(raw_robot)

    # -------------------------
    def split_robot_images(self, sheet):
        w, h = sheet.get_size()
        single_w = w // 4

        dirs = ['N', 'W', 'S', 'E']
        sprites = {}

        size = CELL_SIZE

        for i, d in enumerate(dirs):
            rect = pygame.Rect(i * single_w, 0, single_w, h)
            sub = sheet.subsurface(rect).copy()

            crop = sub.get_bounding_rect()
            img = sub.subsurface(crop)

            sprites[d] = pygame.transform.scale(img, (size, size))

        return sprites

    # -------------------------
    def reset_robot(self):
        self.robot = Robot(0, 0, 'N', self.world)
        self.history = []

    # -------------------------
    def grid_to_screen(self, x, y):
        return (
            MAP_OFFSET_X + x * CELL_SIZE,
            MAP_OFFSET_Y - y * CELL_SIZE
        )

    # -------------------------
    def draw_center(self, img, x, y):
        px, py = self.grid_to_screen(x, y)
        cx = px + CELL_SIZE // 2
        cy = py + CELL_SIZE // 2

        rect = img.get_rect(center=(cx, cy))
        self.screen.blit(img, rect)

    # -------------------------
    def draw_map(self):
        for x in range(MAP_W + 1):
            for y in range(MAP_H + 1):
                px, py = self.grid_to_screen(x, y)
                self.screen.blit(self.img_platform, (px, py))
                pygame.draw.rect(self.screen, (60, 60, 70), (px, py, CELL_SIZE, CELL_SIZE), 2)

    # -------------------------
    def draw_matrix(self):
        matrix = [["." for _ in range(10)] for _ in range(10)]

        for x, y, d in self.world.scents:
            if 0 <= x < 10 and 0 <= y < 10:
                matrix[y][x] = "S"

        if not self.robot.lost:
            matrix[self.robot.y][self.robot.x] = "R"

        for i, row in enumerate(matrix[::-1]):
            text = "".join(row)
            txt = self.font.render(text, True, (200, 200, 200))
            self.screen.blit(txt, (UI_X, 410 + i * 20))

    # -------------------------
    def draw_ui(self):
        x = UI_X

        self.screen.blit(self.font.render("【遊戲資訊】", True, (255,255,255)), (x, 30))
        self.screen.blit(self.font.render(f"座標: ({self.robot.x},{self.robot.y})", True, (255,255,255)), (x, 70))
        display_dir_map = {
                'N': 'S',
                'S': 'N',
                'E': 'W',
                'W': 'E'
            }

        display_dir = display_dir_map.get(self.robot.orientation, self.robot.orientation)

        self.screen.blit(self.font.render(f"方向: {display_dir}", True, (255,255,255)), (x, 100))

        if self.robot.lost:
                status = "狀態: 已墜落"
                color = (255, 80, 80)
        else:
                status = "狀態: 運作中"
                color = (80, 255, 120)

        self.screen.blit(self.font.render(status, True, color), (x, 130))

        lines = [
            "",
            "【操作方式】",
            "L：左轉",
            "R：右轉",
            "F：前進",
            "N：新機器人",
            "C：清除氣味",
            "ESC：離開",
            "G：產生回放 GIF" # ✅ 幫你在 UI 說明裡加了一行
        ]

        for i, line in enumerate(lines):
            self.screen.blit(self.font.render(line, True, (180,180,180)), (x, 160 + i * 25))

        self.screen.blit(self.font.render("【10x10 狀態】", True, (255,255,255)), (x, 380))
        self.draw_matrix()

    # -------------------------
    def draw(self):
        self.screen.fill((15, 15, 20))

        self.draw_map()

        for x, y, _ in self.world.scents:
            self.draw_center(self.img_scent, x, y)

        if not self.robot.lost:
            img = self.robot_sprites[self.robot.orientation]
            self.draw_center(img, self.robot.x, self.robot.y)

        self.draw_ui()
        pygame.display.flip()

    # -------------------------
    def execute(self, cmd):
        try:
            if cmd == 'F':
                # ✅ 反轉前進（但只執行一次動作）
                reverse_map = {
                    'N': 'S',
                    'S': 'N',
                    'E': 'W',
                    'W': 'E'
                }

                original = self.robot.orientation
                self.robot.orientation = reverse_map[original]

                if hasattr(self.robot, 'execute_command'):
                    self.robot.execute_command('F')
                else:
                    self.robot.execute('F')

                self.robot.orientation = original

            else:
                if hasattr(self.robot, 'execute_command'):
                    self.robot.execute_command(cmd)
                else:
                    self.robot.execute(cmd)

        except Exception as e:
            print("[警告] 防崩潰：", e)
            self.robot.lost = True  # ❗不關程式

        self.history.append(cmd)

    # -------------------------
    # ✅ 新增：自動產生 GIF 的邏輯
    def replay_and_save_gif(self):
        try:
            from PIL import Image
        except ImportError:
            print("\n[錯誤] 尚未安裝 Pillow！請先在終端機輸入: pip install Pillow\n")
            return

        if not self.history:
            print("目前沒有任何操作紀錄，無法產生 GIF！")
            return

        print("\n開始產生 replay.gif，請不要關閉視窗...")
        saved_history = list(self.history)
        
        # 退回原點準備錄影
        self.robot = Robot(0, 0, 'N', self.world)
        self.history = []
        frames = []
        
        # 錄下起始畫面
        self.draw()
        frame_str = pygame.image.tostring(self.screen, "RGBA")
        frames.append(Image.frombytes("RGBA", (WIDTH, HEIGHT), frame_str))

        # 逐步重播並錄影
        for cmd in saved_history:
            self.execute(cmd)
            self.draw()
            frame_str = pygame.image.tostring(self.screen, "RGBA")
            frames.append(Image.frombytes("RGBA", (WIDTH, HEIGHT), frame_str))
            
            # 讓畫面稍微停頓，讓玩家看得到重播過程
            pygame.time.delay(400)
            pygame.display.flip()

        # 輸出成 GIF 到 assets 資料夾
        frames[0].save(
            "assets/replay.gif",
            save_all=True,
            append_images=frames[1:],
            duration=400, # 每一格停留 0.4 秒
            loop=0
        )
        
        # 復原歷史紀錄
        self.history = saved_history
        print("✅ 成功！已輸出檔案至 assets/replay.gif\n")

    # -------------------------
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_n:
                        self.reset_robot()

                    if event.key == pygame.K_c:
                        self.world.scents.clear()

                    # ✅ 綁定 G 鍵觸發 GIF 產生
                    if event.key == pygame.K_g:
                        self.replay_and_save_gif()

                    if not self.robot.lost:
                        if event.key == pygame.K_l:
                            self.execute('L')
                        elif event.key == pygame.K_r:
                            self.execute('R')
                        elif event.key == pygame.K_f:
                            self.execute('F')

            self.draw()
            self.clock.tick(30)


if __name__ == "__main__":
    RobotGame().run()