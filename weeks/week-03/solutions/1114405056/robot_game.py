from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Set, Tuple

import pygame

from robot_core import Direction, RobotState, RobotWorld, Scent, StepResult

MARGIN = 40
CELL_SIZE = 80
HUD_WIDTH = 360
BACKGROUND_COLOR = (246, 248, 252)
GRID_LINE_COLOR = (180, 186, 196)
ROBOT_COLOR = (43, 120, 228)
LOST_ROBOT_COLOR = (127, 140, 152)
SCENT_COLOR = (213, 81, 81)
TEXT_COLOR = (36, 46, 61)


@dataclass
class ReplayFrame:
    robot: RobotState
    scent: Set[Scent]
    title: str
    message: str


class RobotGame:
    def __init__(self, width: int = 5, height: int = 3) -> None:
        pygame.init()
        self.world = RobotWorld(width, height)
        self.robot = RobotState(0, 0, "N")

        self.width = width
        self.height = height
        self.grid_cols = width + 1
        self.grid_rows = height + 1
        self.grid_width_px = self.grid_cols * CELL_SIZE
        self.grid_height_px = self.grid_rows * CELL_SIZE

        window_width = self.grid_width_px + HUD_WIDTH + MARGIN * 2
        window_height = max(self.grid_height_px + MARGIN * 2, 560)
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Robot Lost - Week 03")

        self.font = pygame.font.SysFont("Arial", 22)
        self.small_font = pygame.font.SysFont("Arial", 18)
        self.clock = pygame.time.Clock()

        self.message = "準備完成：按 L / R / F 操作機器人"
        self.command_log: List[str] = []

        self.replay_frames: List[ReplayFrame] = []
        self.replay_mode = False
        self.replay_index = 0
        self.last_replay_tick = 0
        self.replay_interval_ms = 450

        self.capture_frame("INIT")

    def world_to_screen(self, x: int, y: int) -> Tuple[int, int]:
        px = MARGIN + x * CELL_SIZE + CELL_SIZE // 2
        py = MARGIN + (self.height - y) * CELL_SIZE + CELL_SIZE // 2
        return px, py

    def robot_points(self, center: Tuple[int, int], direction: Direction) -> List[Tuple[int, int]]:
        cx, cy = center
        if direction == "N":
            return [(cx, cy - 19), (cx - 15, cy + 13), (cx + 15, cy + 13)]
        if direction == "E":
            return [(cx + 19, cy), (cx - 13, cy - 15), (cx - 13, cy + 15)]
        if direction == "S":
            return [(cx, cy + 19), (cx - 15, cy - 13), (cx + 15, cy - 13)]
        return [(cx - 19, cy), (cx + 13, cy - 15), (cx + 13, cy + 15)]

    def active_frame(self) -> ReplayFrame:
        if self.replay_mode and self.replay_frames:
            return self.replay_frames[self.replay_index]
        return ReplayFrame(self.robot.copy(), set(self.world.scent), "LIVE", self.message)

    def capture_frame(self, title: str) -> None:
        frame = ReplayFrame(self.robot.copy(), set(self.world.scent), title, self.message)
        self.replay_frames.append(frame)

    def new_robot(self) -> None:
        self.robot = RobotState(0, 0, "N")
        self.command_log.clear()
        self.message = "已部署新機器人，保留 scent"
        self.capture_frame("N")

    def clear_scent(self) -> None:
        self.world.clear_scent()
        self.message = "已清除全部 scent"
        self.capture_frame("C")

    def status_message(self, result: StepResult) -> str:
        if result.status == "ROTATED":
            return f"指令 {result.command}: 旋轉成功 → 朝向 {result.direction}"
        if result.status == "MOVED":
            return f"指令 {result.command}: 移動到 ({result.x}, {result.y})"
        if result.status == "SCENT_IGNORED":
            return f"指令 {result.command}: 觸發 scent，已忽略危險前進"
        if result.status == "LOST":
            return f"指令 {result.command}: 機器人 LOST 於 ({result.x}, {result.y}, {result.direction})"
        if result.status == "IGNORED_LOST":
            return "機器人已 LOST，後續指令忽略"
        return f"狀態: {result.status}"

    def handle_command(self, command: str) -> None:
        try:
            result = self.world.step(self.robot, command)
        except ValueError as error:
            self.message = str(error)
            return

        self.command_log.append(command)
        self.message = self.status_message(result)
        self.capture_frame(command)

    def start_replay(self) -> None:
        if len(self.replay_frames) < 2:
            self.message = "可回放資料不足，請先操作幾步"
            return
        self.replay_mode = True
        self.replay_index = 0
        self.last_replay_tick = pygame.time.get_ticks()
        self.message = "開始回放"

    def update_replay(self) -> None:
        if not self.replay_mode:
            return

        now = pygame.time.get_ticks()
        if now - self.last_replay_tick < self.replay_interval_ms:
            return

        self.last_replay_tick = now
        self.replay_index += 1
        if self.replay_index >= len(self.replay_frames):
            self.replay_index = len(self.replay_frames) - 1
            self.replay_mode = False
            self.message = "回放結束，回到即時模式"

    def save_screenshot(self) -> None:
        output_path = Path(__file__).resolve().parent / "assets" / "gameplay.png"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        pygame.image.save(self.screen, str(output_path))
        self.message = f"已輸出截圖：{output_path.name}"

    def draw_grid(self) -> None:
        for x in range(self.grid_cols):
            for y in range(self.grid_rows):
                rect = pygame.Rect(
                    MARGIN + x * CELL_SIZE,
                    MARGIN + (self.height - y) * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                )
                pygame.draw.rect(self.screen, GRID_LINE_COLOR, rect, width=1)
                coord_text = self.small_font.render(f"{x},{y}", True, (120, 130, 146))
                self.screen.blit(coord_text, (rect.x + 4, rect.y + 4))

    def draw_scents(self, scents: Set[Scent]) -> None:
        direction_offset = {
            "N": (0, -15),
            "E": (15, 0),
            "S": (0, 15),
            "W": (-15, 0),
        }
        for sx, sy, direction in sorted(scents):
            center_x, center_y = self.world_to_screen(sx, sy)
            offset_x, offset_y = direction_offset[direction]
            scent_center = (center_x + offset_x, center_y + offset_y)
            pygame.draw.circle(self.screen, SCENT_COLOR, scent_center, 8)
            label = self.small_font.render(direction, True, (255, 255, 255))
            self.screen.blit(label, label.get_rect(center=scent_center))

    def draw_robot(self, robot: RobotState) -> None:
        center = self.world_to_screen(robot.x, robot.y)
        points = self.robot_points(center, robot.direction)
        color = LOST_ROBOT_COLOR if robot.lost else ROBOT_COLOR
        pygame.draw.polygon(self.screen, color, points)
        if robot.lost:
            pygame.draw.line(self.screen, (220, 30, 30), (center[0] - 20, center[1] - 20), (center[0] + 20, center[1] + 20), 4)
            pygame.draw.line(self.screen, (220, 30, 30), (center[0] - 20, center[1] + 20), (center[0] + 20, center[1] - 20), 4)

    def draw_hud(self, frame: ReplayFrame) -> None:
        panel_left = MARGIN + self.grid_width_px + 24
        panel_top = MARGIN

        mode = "REPLAY" if self.replay_mode else "LIVE"
        robot_state = "LOST" if frame.robot.lost else "ALIVE"
        command_preview = "".join(self.command_log[-24:]) or "-"

        hud_lines = [
            "Week 03: Robot Lost",
            f"Map: (0,0) ~ ({self.width},{self.height})",
            f"Mode: {mode}",
            f"Robot: ({frame.robot.x}, {frame.robot.y}, {frame.robot.direction})",
            f"State: {robot_state}",
            f"Scent count: {len(frame.scent)}",
            f"Replay frames: {len(self.replay_frames)}",
            f"Command log: {command_preview}",
            "",
            "Keys",
            "L / R / F : step command",
            "N : new robot",
            "C : clear scent",
            "P : replay",
            "G : save screenshot",
            "ESC : quit",
            "",
            f"Message: {frame.message}",
        ]

        for index, line in enumerate(hud_lines):
            color = TEXT_COLOR if index < 10 else (58, 76, 99)
            text = self.small_font.render(line, True, color)
            self.screen.blit(text, (panel_left, panel_top + index * 28))

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        frame = self.active_frame()
        self.draw_grid()
        self.draw_scents(frame.scent)
        self.draw_robot(frame.robot)
        self.draw_hud(frame)
        pygame.display.flip()

    def run(self) -> None:
        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_p:
                        self.start_replay()
                    elif self.replay_mode:
                        continue
                    elif event.key == pygame.K_n:
                        self.new_robot()
                    elif event.key == pygame.K_c:
                        self.clear_scent()
                    elif event.key == pygame.K_l:
                        self.handle_command("L")
                    elif event.key == pygame.K_r:
                        self.handle_command("R")
                    elif event.key == pygame.K_f:
                        self.handle_command("F")
                    elif event.key == pygame.K_g:
                        self.draw()
                        self.save_screenshot()

            self.update_replay()
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    RobotGame().run()
