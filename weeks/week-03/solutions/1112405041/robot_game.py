import pygame
import sys
import os
import io
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from robot_core import Robot, RobotWorld, DIR_ORDER

CELL = 40
MARGIN = 60
INFO_H = 120
W = 600
H = 600

pygame.init()
FONT = None
SMALL_FONT = None


def get_font():
    global FONT, SMALL_FONT
    if FONT is None:
        name = "microsoftjhenghei"
        if name not in pygame.font.get_fonts():
            name = "mingliu"
        FONT = pygame.font.SysFont(name, 24)
        SMALL_FONT = pygame.font.SysFont(name, 18)
    return FONT, SMALL_FONT


COLORS = {
    "bg": (30, 30, 30),
    "grid": (60, 60, 60),
    "robot": (46, 204, 113),
    "scent": (231, 76, 60),
    "text": (200, 200, 200),
    "lost": (255, 0, 0),
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

    def export_gif(self, screen, out="assets/replay.gif"):
        if len(self.replay_steps) < 1:
            self.msg = "沒有步驟可匯出"
            return
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
        self.msg = f"replay.gif 已存檔"

    def draw(self, screen):
        font, sfont = get_font()
        screen.fill(COLORS["bg"])
        ox, oy = MARGIN, MARGIN
        for x in range(self.world_w + 1):
            for y in range(self.world_h + 1):
                rx = ox + x * CELL
                ry = oy + (self.world_h - y) * CELL
                rect = pygame.Rect(rx, ry, CELL, CELL)
                pygame.draw.rect(screen, COLORS["grid"], rect, 1)
                if (x, y, "N") in self.world.scents or \
                   (x, y, "E") in self.world.scents or \
                   (x, y, "S") in self.world.scents or \
                   (x, y, "W") in self.world.scents:
                    pygame.draw.circle(screen, COLORS["scent"],
                                       (rx + CELL // 2, ry + CELL // 2), 6)
        if self.robot and not self.robot.lost:
            rx = ox + self.robot.x * CELL
            ry = oy + (self.world_h - self.robot.y) * CELL
            cx, cy = rx + CELL // 2, ry + CELL // 2
            pygame.draw.circle(screen, COLORS["robot"], (cx, cy), CELL // 3)
            dir_idx = DIR_ORDER.index(self.robot.dir)
            angle = 90 - dir_idx * 90
            import math
            ex = cx + int(math.cos(math.radians(angle)) * CELL // 3)
            ey = cy - int(math.sin(math.radians(angle)) * CELL // 3)
            pygame.draw.line(screen, (255, 255, 255), (cx, cy), (ex, ey), 3)
        elif self.robot and self.robot.lost:
            rx = ox + self.robot.x * CELL
            ry = oy + (self.world_h - self.robot.y) * CELL
            pygame.draw.circle(screen, COLORS["lost"], (rx + CELL // 2, ry + CELL // 2), CELL // 3)
            txt = sfont.render("LOST", True, (255, 255, 255))
            screen.blit(txt, (rx + 4, ry + 4))
        info_y = oy + (self.world_h + 1) * CELL + 10
        txt = sfont.render(self.msg, True, COLORS["text"])
        screen.blit(txt, (ox, info_y))
        if self.robot:
            state = sfont.render(f"位置: ({self.robot.x}, {self.robot.y}, {self.robot.dir})", True, COLORS["text"])
            screen.blit(state, (ox, info_y + 25))
            sc = sfont.render(f"scent 數: {len(self.world.scents)}", True, COLORS["text"])
            screen.blit(sc, (ox, info_y + 50))
        txt = sfont.render("指令: " + self.cmd_buffer, True, COLORS["text"])
        screen.blit(txt, (ox, info_y + 75))

    def run(self):
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
            self.draw(screen)
            pygame.display.flip()
            clock.tick(30)


if __name__ == "__main__":
    game = RobotGame(5, 5)
    game.run()
