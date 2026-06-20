import pygame
import sys
import os
import math
sys.path.insert(0, os.path.dirname(__file__))
from robot_core import Robot, RobotWorld, DIR_ORDER

CELL = 80
MARGIN = 40
W = 600
H = 680

FONT = None
SMALL_FONT = None


def get_font():
    global FONT, SMALL_FONT
    if FONT is None:
        names = ["microsoftjhenghei", "mingliu", "notosanscjk", "notosanscjkjp", "simhei", "simsun", None]
        for name in names:
            if name is None or name in pygame.font.get_fonts():
                break
        try:
            FONT = pygame.font.SysFont(name, 28)
            SMALL_FONT = pygame.font.SysFont(name, 20)
        except:
            FONT = pygame.font.Font(None, 28)
            SMALL_FONT = pygame.font.Font(None, 20)
    return FONT, SMALL_FONT


COLORS = {
    "bg": (40, 40, 50),
    "grid": (100, 100, 120),
    "cell_bg": (55, 55, 70),
    "robot": (46, 204, 113),
    "scent": (231, 76, 60),
    "text": (220, 220, 220),
    "lost": (255, 80, 80),
    "button": (52, 152, 219),
}


class RobotGame:
    def __init__(self, world_w=5, world_h=5):
        self.world_w = world_w
        self.world_h = world_h
        self.world = RobotWorld(world_w, world_h)
        self.robot = None
        self.cmd_buffer = ""
        self.msg = "按 N 新增機器人 | L/R/F 控制 | C 清除 scent | ESC 離開"
        self.history = []
        self.replay_steps = []

    def new_robot(self):
        self.robot = Robot(0, 0, "N", world=(self.world_w, self.world_h), world_ref=self.world)
        self.world.add_robot(self.robot)
        self.msg = f"新機器人 at (0, 0, N)"
        self.cmd_buffer = ""
        self.replay_steps = []

    def run_cmd(self, cmd):
        if not self.robot or self.robot.lost:
            self.msg = "機器人已 LOST，按 N 新增"
            return
        self.replay_steps.append((self.robot.x, self.robot.y, self.robot.dir, cmd))
        try:
            self.robot.execute(cmd)
            self.msg = f"執行 {cmd} → ({self.robot.x}, {self.robot.y}, {self.robot.dir})"
            if self.robot.lost:
                self.msg += " LOST"
        except ValueError:
            self.msg = f"無效指令: {cmd}"

    def clear_scents(self):
        self.world.scents.clear()
        self.msg = "scent 已清除"

    def export_gif(self, screen, out="replay.gif"):
        try:
            from PIL import Image
        except ImportError:
            self.msg = "匯出 GIF 需要 Pillow 套件：pip install Pillow"
            return
        if len(self.replay_steps) < 1:
            self.msg = "沒有步驟可匯出"
            return
        try:
            frames = []
            replay = RobotGame(self.world_w, self.world_h)
            replay.new_robot()
            replay.robot.x = self.replay_steps[0][0]
            replay.robot.y = self.replay_steps[0][1]
            replay.robot.dir = self.replay_steps[0][2]
            replay.replay_steps = []
            buf = pygame.Surface((W, H))
            replay.draw(buf)
            frames.append(Image.frombytes("RGB", (W, H), pygame.image.tobytes(buf, "RGB")))
            for sx, sy, sdir, cmd in self.replay_steps:
                if replay.robot.lost:
                    break
                replay.robot.x, replay.robot.y, replay.robot.dir = sx, sy, sdir
                replay.run_cmd(cmd)
                replay.draw(buf)
                frames.append(Image.frombytes("RGB", (W, H), pygame.image.tobytes(buf, "RGB")))
            out_path = os.path.join(os.path.dirname(__file__), out)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=300, loop=0)
            self.msg = "replay.gif 已存檔"
        except Exception as e:
            self.msg = f"GIF 匯出失敗：{e}"

    def draw(self, screen):
        font, sfont = get_font()
        screen.fill(COLORS["bg"])
        ox, oy = MARGIN, MARGIN
        cell_count = self.world_w + 1
        for x in range(cell_count):
            for y in range(cell_count):
                rx = ox + x * CELL
                ry = oy + (self.world_h - y) * CELL
                rect = pygame.Rect(rx, ry, CELL, CELL)
                if x < cell_count - 1 and y < cell_count - 1:
                    pygame.draw.rect(screen, COLORS["cell_bg"], rect)
                pygame.draw.rect(screen, COLORS["grid"], rect, 2)
                for d in ("N", "E", "S", "W"):
                    if (x, y, d) in self.world.scents:
                        pygame.draw.circle(screen, COLORS["scent"],
                                           (rx + CELL // 2, ry + CELL // 2), 10)
                        break
        if self.robot:
            rx = ox + self.robot.x * CELL
            ry = oy + (self.world_h - self.robot.y) * CELL
            cx, cy = rx + CELL // 2, ry + CELL // 2
            if self.robot.lost:
                pygame.draw.circle(screen, COLORS["lost"], (cx, cy), CELL // 2 - 4)
                txt = sfont.render("LOST", True, (255, 255, 255))
                screen.blit(txt, (rx + 8, ry + 8))
            else:
                pygame.draw.circle(screen, COLORS["robot"], (cx, cy), CELL // 2 - 4)
                dir_idx = DIR_ORDER.index(self.robot.dir)
                angle = 90 - dir_idx * 90
                ex = cx + int(math.cos(math.radians(angle)) * CELL // 3)
                ey = cy - int(math.sin(math.radians(angle)) * CELL // 3)
                pygame.draw.line(screen, (255, 255, 255), (cx, cy), (ex, ey), 4)
        info_y = oy + (self.world_h + 1) * CELL + 15
        txt = sfont.render(self.msg, True, COLORS["text"])
        screen.blit(txt, (ox, info_y))
        if self.robot:
            state = sfont.render(f"位置：({self.robot.x}, {self.robot.y}, {self.robot.dir})", True, COLORS["text"])
            screen.blit(state, (ox, info_y + 30))
            sc = sfont.render(f"scent 數：{len(self.world.scents)}", True, COLORS["text"])
            screen.blit(sc, (ox, info_y + 55))
        txt = sfont.render(f"指令鍵 N/L/R/F/C/G/ESC | 緩衝：{self.cmd_buffer}", True, COLORS["text"])
        screen.blit(txt, (ox, info_y + 80))

    def run(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("Robot Lost")
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_n:
                        self.new_robot()
                    elif event.key == pygame.K_c:
                        self.clear_scents()
                    elif event.key == pygame.K_l:
                        self.run_cmd("L")
                    elif event.key == pygame.K_r:
                        self.run_cmd("R")
                    elif event.key == pygame.K_f:
                        self.run_cmd("F")
                    elif event.key == pygame.K_g:
                        self.export_gif(screen)
            try:
                self.draw(screen)
                pygame.display.flip()
            except Exception as e:
                print(f"繪圖錯誤：{e}")
            clock.tick(30)


if __name__ == "__main__":
    g = RobotGame(5, 5)
    g.run()
