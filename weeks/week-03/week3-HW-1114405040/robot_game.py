from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

try:
    import pygame
except ModuleNotFoundError as exc:
    raise SystemExit(
        "pygame 未安裝。請先在虛擬環境中執行: python -m pip install pygame-ce pillow"
    ) from exc

from PIL import Image

from robot_core import Robot, World, execute_command


WINDOW_WIDTH = 1120
WINDOW_HEIGHT = 760
GRID_ORIGIN = (40, 40)
CELL_SIZE = 56
GRID_COLOR = (40, 74, 94)
BACKGROUND = (247, 240, 224)
PANEL = (27, 59, 79)
ACCENT = (228, 120, 55)
SUCCESS = (55, 139, 95)
WARNING = (176, 58, 46)
SCENT_COLOR = (212, 174, 56)
ROBOT_COLOR = (34, 99, 132)
TEXT_LIGHT = (249, 247, 242)
TEXT_DARK = (26, 34, 41)
UI_FONT = "microsoftjhengheiui"


@dataclass(slots=True)
class FrameState:
    x: int
    y: int
    direction: str
    lost: bool
    scents: set[tuple[int, int, str]]
    action: str
    message: str


@dataclass(slots=True)
class RobotGame:
    world: World = field(default_factory=lambda: World(9, 9))
    robot: Robot = field(default_factory=lambda: Robot(5, 5, "N"))
    history: list[FrameState] = field(default_factory=list)
    command_buffer: list[str] = field(default_factory=list)
    status_message: str = "準備開始，使用 L / R / F 控制機器人。"

    def __post_init__(self) -> None:
        self.record_frame("INIT", self.status_message)

    def reset_robot(self) -> None:
        self.robot = Robot(5, 5, "N")
        self.command_buffer.clear()
        self.status_message = "新機器人已建立，保留既有 scent。"
        self.record_frame("NEW_ROBOT", self.status_message)

    def clear_scents(self) -> None:
        self.world.clear_scents()
        self.status_message = "所有 scent 已清除。"
        self.record_frame("CLEAR_SCENT", self.status_message)

    def apply_command(self, command: str) -> str:
        action = execute_command(self.world, self.robot, command)
        self.command_buffer.append(command)
        self.status_message = self.describe_action(command, action)
        self.record_frame(action, self.status_message)
        return action

    def describe_action(self, command: str, action: str) -> str:
        if action == "TURN_LEFT":
            return f"指令 {command}: 左轉，朝向 {self.robot.direction}。"
        if action == "TURN_RIGHT":
            return f"指令 {command}: 右轉，朝向 {self.robot.direction}。"
        if action == "MOVE":
            return f"指令 {command}: 前進到 ({self.robot.x}, {self.robot.y})。"
        if action == "SCENT_BLOCKED":
            return "前方有 scent，危險移動已忽略。"
        if action == "LOST":
            return f"機器人在 ({self.robot.x}, {self.robot.y}) 面向 {self.robot.direction} 掉出地圖。"
        return "未知動作。"

    def record_frame(self, action: str, message: str) -> None:
        self.history.append(
            FrameState(
                x=self.robot.x,
                y=self.robot.y,
                direction=self.robot.direction,
                lost=self.robot.lost,
                scents=set(self.world.scent_marks),
                action=action,
                message=message,
            )
        )

    def build_matrix(self, state: FrameState | None = None) -> list[str]:
        state = state or self.history[-1]
        grid = [["." for _ in range(self.world.width + 1)] for _ in range(self.world.height + 1)]
        for scent_x, scent_y, _direction in state.scents:
            grid[self.world.height - scent_y][scent_x] = "S"
        symbol = "X" if state.lost else state.direction
        grid[self.world.height - state.y][state.x] = symbol
        return [" ".join(row) for row in grid]

    def export_replay_gif(self, output_path: str | Path, size: tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT)) -> Path:
        output = Path(output_path)
        surface = pygame.Surface(size)
        frames: list[Image.Image] = []
        for frame_state in self.history:
            self.render(surface, frame_state)
            rgba_bytes = pygame.image.tobytes(surface, "RGBA")
            image = Image.frombytes("RGBA", size, rgba_bytes)
            frames.append(image.convert("P", palette=Image.ADAPTIVE))
        frames[0].save(
            output,
            save_all=True,
            append_images=frames[1:],
            duration=480,
            loop=0,
        )
        return output

    def save_screenshot(self, output_path: str | Path, size: tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT)) -> Path:
        output = Path(output_path)
        surface = pygame.Surface(size)
        self.render(surface)
        pygame.image.save(surface, output)
        return output

    def render(self, surface: pygame.Surface, state: FrameState | None = None) -> None:
        state = state or self.history[-1]
        surface.fill(BACKGROUND)
        self.draw_grid(surface, state)
        self.draw_side_panel(surface, state)

    def draw_grid(self, surface: pygame.Surface, state: FrameState) -> None:
        origin_x, origin_y = GRID_ORIGIN
        width_px = (self.world.width + 1) * CELL_SIZE
        height_px = (self.world.height + 1) * CELL_SIZE
        grid_rect = pygame.Rect(origin_x, origin_y, width_px, height_px)
        pygame.draw.rect(surface, (255, 252, 247), grid_rect, border_radius=20)
        pygame.draw.rect(surface, GRID_COLOR, grid_rect, 3, border_radius=20)

        for column in range(self.world.width + 2):
            start_x = origin_x + column * CELL_SIZE
            pygame.draw.line(surface, GRID_COLOR, (start_x, origin_y), (start_x, origin_y + height_px), 1)
        for row in range(self.world.height + 2):
            start_y = origin_y + row * CELL_SIZE
            pygame.draw.line(surface, GRID_COLOR, (origin_x, start_y), (origin_x + width_px, start_y), 1)

        font = pygame.font.SysFont(UI_FONT, 20)
        for x_value in range(self.world.width + 1):
            label = font.render(str(x_value), True, TEXT_DARK)
            surface.blit(label, (origin_x + x_value * CELL_SIZE + 18, origin_y + height_px + 8))
        for y_value in range(self.world.height + 1):
            label = font.render(str(y_value), True, TEXT_DARK)
            surface.blit(label, (origin_x - 26, origin_y + (self.world.height - y_value) * CELL_SIZE + 18))

        for scent_x, scent_y, _direction in state.scents:
            center = self.cell_center(scent_x, scent_y)
            pygame.draw.circle(surface, SCENT_COLOR, center, 8)
            pygame.draw.circle(surface, PANEL, center, 8, 2)

        self.draw_robot(surface, state)

    def draw_robot(self, surface: pygame.Surface, state: FrameState) -> None:
        center_x, center_y = self.cell_center(state.x, state.y)
        points = {
            "N": [(center_x, center_y - 18), (center_x - 14, center_y + 15), (center_x + 14, center_y + 15)],
            "E": [(center_x + 18, center_y), (center_x - 15, center_y - 14), (center_x - 15, center_y + 14)],
            "S": [(center_x, center_y + 18), (center_x - 14, center_y - 15), (center_x + 14, center_y - 15)],
            "W": [(center_x - 18, center_y), (center_x + 15, center_y - 14), (center_x + 15, center_y + 14)],
        }
        color = WARNING if state.lost else ROBOT_COLOR
        pygame.draw.polygon(surface, color, points[state.direction])
        pygame.draw.circle(surface, PANEL, (center_x, center_y), 20, 2)

    def draw_side_panel(self, surface: pygame.Surface, state: FrameState) -> None:
        panel_rect = pygame.Rect(650, 40, 430, 670)
        pygame.draw.rect(surface, PANEL, panel_rect, border_radius=28)
        title_font = pygame.font.SysFont(UI_FONT, 32, bold=True)
        body_font = pygame.font.SysFont("consolas", 20)
        text_font = pygame.font.SysFont(UI_FONT, 22)

        surface.blit(title_font.render("Robot Lost 控制面板", True, TEXT_LIGHT), (680, 68))
        info_lines = [
            f"位置: ({state.x}, {state.y})",
            f"方向: {state.direction}",
            f"狀態: {'LOST' if state.lost else 'ALIVE'}",
            f"指令串: {''.join(self.command_buffer) or '-'}",
            f"scent 數量: {len(state.scents)}",
            f"最近動作: {state.action}",
        ]
        for index, line in enumerate(info_lines):
            surface.blit(text_font.render(line, True, TEXT_LIGHT), (680, 122 + index * 34))

        box_rect = pygame.Rect(675, 340, 380, 86)
        pygame.draw.rect(surface, (243, 225, 199), box_rect, border_radius=16)
        wrapped_lines = wrap_text(state.message, 24)
        for index, line in enumerate(wrapped_lines[:3]):
            surface.blit(text_font.render(line, True, TEXT_DARK), (692, 357 + index * 24))

        helper_lines = [
            "操作鍵: L / R / F",
            "N: 新機器人   C: 清除 scent",
            "G: 匯出 replay.gif   P: screenshot",
            "ESC: 離開",
            "10x10 matrix:",
        ]
        for index, line in enumerate(helper_lines):
            surface.blit(text_font.render(line, True, TEXT_LIGHT), (680, 448 + index * 30))

        for index, row in enumerate(self.build_matrix(state)):
            surface.blit(body_font.render(row, True, TEXT_LIGHT), (680, 606 + index * 18))

    def cell_center(self, x_value: int, y_value: int) -> tuple[int, int]:
        origin_x, origin_y = GRID_ORIGIN
        return (
            origin_x + x_value * CELL_SIZE + CELL_SIZE // 2,
            origin_y + (self.world.height - y_value) * CELL_SIZE + CELL_SIZE // 2,
        )


def wrap_text(text: str, chunk_size: int) -> list[str]:
    words = text.split()
    if not words:
        return [text]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        if len(current) + len(word) + 1 <= chunk_size:
            current = f"{current} {word}"
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def replay_actions(game: RobotGame, commands: Iterable[str]) -> None:
    for command in commands:
        game.apply_command(command)
        if game.robot.lost:
            break


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Week 03 Robot Lost - 1114405040")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    game = RobotGame()
    output_dir = Path(__file__).resolve().parent / "assets"
    output_dir.mkdir(exist_ok=True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_l:
                    game.apply_command("L")
                elif event.key == pygame.K_r:
                    game.apply_command("R")
                elif event.key == pygame.K_f:
                    game.apply_command("F")
                elif event.key == pygame.K_n:
                    game.reset_robot()
                elif event.key == pygame.K_c:
                    game.clear_scents()
                elif event.key == pygame.K_g:
                    gif_path = game.export_replay_gif(output_dir / "replay.gif")
                    game.status_message = f"已輸出回放: {gif_path.name}"
                    game.record_frame("EXPORT_GIF", game.status_message)
                elif event.key == pygame.K_p:
                    screenshot_path = game.save_screenshot(output_dir / "gameplay.png")
                    game.status_message = f"已輸出畫面: {screenshot_path.name}"
                    game.record_frame("SCREENSHOT", game.status_message)

        game.render(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()