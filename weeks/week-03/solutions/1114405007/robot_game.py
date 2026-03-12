"""Robot Lost 的 pygame 互動版（MVP）。

操作方式：
- L/R/F：左轉、右轉、前進
- N：生成新機器人（保留 scent）
- C：清除 scent
- P：重播歷史
- ESC：離開
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

import pygame

from robot_core import Robot, RobotWorld

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
MARGIN = 50
HUD_HEIGHT = 120
BG_COLOR = (240, 244, 248)
GRID_COLOR = (150, 160, 170)
ROBOT_COLOR = (30, 120, 220)
SCENT_COLOR = (220, 90, 70)
TEXT_COLOR = (30, 30, 30)
BTN_BG = (232, 237, 242)
BTN_BORDER = (90, 100, 110)
BTN_TEXT = (20, 30, 40)


@dataclass
class Snapshot:
    """每一幀的狀態快照，用於回放。"""

    x: int
    y: int
    direction: str
    lost: bool
    scents: set[tuple[int, int, str]]


class RobotGame:
    def __init__(self, width: int = 5, height: int = 3) -> None:
        pygame.init()
        pygame.display.set_caption("Week 03 - Robot Lost MVP")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 22)
        self.small_font = pygame.font.SysFont("consolas", 18)

        self.world = RobotWorld(width, height)
        self.robot = Robot(0, 0, "N")
        self.history: list[Snapshot] = []
        self.replay_mode = False
        self.replay_index = 0
        self.last_action = "Ready"
        self.last_key = "None"
        self.buttons = self._build_buttons()

        # 一開始先記錄初始狀態，確保回放可從第 0 幀開始。
        self._record_snapshot()

    @property
    def cell_size(self) -> int:
        usable_w = WINDOW_WIDTH - MARGIN * 2
        usable_h = WINDOW_HEIGHT - MARGIN * 2 - HUD_HEIGHT
        return min(usable_w // (self.world.width + 1), usable_h // (self.world.height + 1))

    def to_screen(self, x: int, y: int) -> tuple[int, int]:
        # 邏輯座標（左下原點）轉為螢幕座標（左上原點）。
        px = MARGIN + x * self.cell_size
        py = WINDOW_HEIGHT - HUD_HEIGHT - MARGIN - y * self.cell_size
        return px, py

    def spawn_new_robot(self) -> None:
        self.robot = Robot(0, 0, "N")
        self.last_action = "Spawned new robot"
        self._record_snapshot()

    def clear_scents(self) -> None:
        self.world.scents.clear()
        self.last_action = "Cleared scents"
        self._record_snapshot()

    def process_command(self, command: str) -> None:
        # 若已 LOST，僅更新提示，不再變更狀態。
        if self.robot.lost:
            self.last_action = "Robot LOST, press N for a new robot"
            return
        self.world.step(self.robot, command)
        self.last_action = f"Command {command}"
        self._record_snapshot()

    def _record_snapshot(self) -> None:
        # 使用 set(self.world.scents) 複製集合，避免後續修改污染歷史。
        self.history.append(
            Snapshot(
                x=self.robot.x,
                y=self.robot.y,
                direction=self.robot.direction,
                lost=self.robot.lost,
                scents=set(self.world.scents),
            )
        )

    def _build_buttons(self) -> list[tuple[str, pygame.Rect]]:
        # 建立固定位置的操作按鈕列。
        labels = ["L", "R", "F", "N", "C", "P"]
        width = 62
        height = 36
        gap = 10
        start_x = WINDOW_WIDTH - (len(labels) * width + (len(labels) - 1) * gap) - 20
        y = WINDOW_HEIGHT - HUD_HEIGHT + 8
        buttons: list[tuple[str, pygame.Rect]] = []
        for i, label in enumerate(labels):
            x = start_x + i * (width + gap)
            buttons.append((label, pygame.Rect(x, y, width, height)))
        return buttons

    def draw_buttons(self) -> None:
        for label, rect in self.buttons:
            pygame.draw.rect(self.screen, BTN_BG, rect, border_radius=8)
            pygame.draw.rect(self.screen, BTN_BORDER, rect, width=2, border_radius=8)
            text = self.small_font.render(label, True, BTN_TEXT)
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    def handle_mouse_click(self, pos: tuple[int, int]) -> None:
        # 點擊按鈕時，把操作映射到既有命令流程。
        for label, rect in self.buttons:
            if not rect.collidepoint(pos):
                continue

            self.last_key = f"mouse:{label}"
            if label in ("L", "R", "F"):
                self.process_command(label)
                return
            if label == "N":
                self.spawn_new_robot()
                return
            if label == "C":
                self.clear_scents()
                return
            if label == "P" and self.history:
                self.replay_mode = True
                self.replay_index = 0
                self.last_action = "Replay started"
                return

    def draw_grid(self) -> None:
        # 畫出 (0,0) 到 (W,H) 的格子地圖。
        for x in range(self.world.width + 1):
            for y in range(self.world.height + 1):
                px, py = self.to_screen(x, y)
                rect = pygame.Rect(px - self.cell_size // 2, py - self.cell_size // 2, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, GRID_COLOR, rect, width=1)

    def draw_scents(self, scents: set[tuple[int, int, str]]) -> None:
        for sx, sy, _ in scents:
            px, py = self.to_screen(sx, sy)
            pygame.draw.circle(self.screen, SCENT_COLOR, (px, py), max(3, self.cell_size // 8))

    def draw_robot(self, x: int, y: int, direction: str, lost: bool) -> None:
        # 以三角形表示朝向。
        px, py = self.to_screen(x, y)
        r = max(8, self.cell_size // 3)

        if direction == "N":
            points = [(px, py - r), (px - r, py + r), (px + r, py + r)]
        elif direction == "E":
            points = [(px + r, py), (px - r, py - r), (px - r, py + r)]
        elif direction == "S":
            points = [(px, py + r), (px - r, py - r), (px + r, py - r)]
        else:
            points = [(px - r, py), (px + r, py - r), (px + r, py + r)]

        color = (120, 120, 120) if lost else ROBOT_COLOR
        pygame.draw.polygon(self.screen, color, points)

    def draw_hud(self, x: int, y: int, direction: str, lost: bool, scents_count: int, mode_text: str) -> None:
        focus_text = "FOCUSED" if pygame.key.get_focused() else "NOT FOCUSED"
        lines = [
            f"Robot: ({x}, {y}, {direction})  Status: {'LOST' if lost else 'ALIVE'}",
            f"Scents: {scents_count}",
            "Keys: L/R/F or A/D/W or Left/Right/Up or Space | Mouse buttons: L R F N C P | ESC",
            f"{mode_text} | {focus_text} | Last key: {self.last_key} | {self.last_action}",
        ]
        base_y = WINDOW_HEIGHT - HUD_HEIGHT + 10
        for i, text in enumerate(lines):
            font = self.font if i < 2 else self.small_font
            surf = font.render(text, True, TEXT_COLOR)
            self.screen.blit(surf, (20, base_y + i * 26))

    def draw(self) -> None:
        self.screen.fill(BG_COLOR)
        self.draw_grid()

        if self.replay_mode and self.history:
            # 回放模式顯示歷史快照。
            snap = self.history[self.replay_index]
            self.draw_scents(snap.scents)
            self.draw_robot(snap.x, snap.y, snap.direction, snap.lost)
            mode_text = f"REPLAY MODE: frame {self.replay_index + 1}/{len(self.history)}"
            self.draw_hud(snap.x, snap.y, snap.direction, snap.lost, len(snap.scents), mode_text)
        else:
            # 即時模式顯示目前世界狀態。
            self.draw_scents(self.world.scents)
            self.draw_robot(self.robot.x, self.robot.y, self.robot.direction, self.robot.lost)
            self.draw_hud(self.robot.x, self.robot.y, self.robot.direction, self.robot.lost, len(self.world.scents), "LIVE MODE")

        self.draw_buttons()

        pygame.display.flip()

    def update_replay(self) -> None:
        if not self.replay_mode:
            return
        # 逐幀播放，播完即回到即時模式。
        self.replay_index += 1
        if self.replay_index >= len(self.history):
            self.replay_mode = False
            self.replay_index = 0

    def run(self) -> None:
        # 長按鍵盤可連續觸發，改善操作手感。
        pygame.key.set_repeat(220, 120)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    self.last_key = f"{key_name} ({event.unicode!r})"

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)

                    if self.replay_mode:
                        continue

                    # 同時支援 keycode 與 unicode，避免輸入法造成判定落差。
                    letter = (event.unicode or "").lower()

                    if event.key in (pygame.K_l, pygame.K_a, pygame.K_LEFT) or letter in ("l", "a"):
                        self.process_command("L")
                    elif event.key in (pygame.K_r, pygame.K_d, pygame.K_RIGHT) or letter in ("r", "d"):
                        self.process_command("R")
                    elif event.key in (pygame.K_f, pygame.K_w, pygame.K_UP, pygame.K_SPACE) or letter in ("f", "w"):
                        self.process_command("F")
                    elif event.key == pygame.K_n or letter == "n":
                        self.spawn_new_robot()
                    elif event.key == pygame.K_c or letter == "c":
                        self.clear_scents()
                    elif (event.key == pygame.K_p or letter == "p") and self.history:
                        self.replay_mode = True
                        self.replay_index = 0
                        self.last_action = "Replay started"
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.replay_mode:
                        continue
                    self.handle_mouse_click(event.pos)

            self.update_replay()
            self.draw()
            self.clock.tick(8 if self.replay_mode else 30)


def main() -> None:
    game = RobotGame(width=5, height=3)
    game.run()


if __name__ == "__main__":
    main()
