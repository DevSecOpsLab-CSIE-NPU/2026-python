from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import pygame

from robot_core import RobotState, World, execute_commands, grid_snapshot, step_robot

CELL = 64
MARGIN = 24
TITLE_HEIGHT = 56
SIDEBAR_WIDTH = 320
BG = (242, 245, 247)
GRID = (188, 196, 204)
GRID_SOFT = (221, 226, 231)
ROBOT = (36, 112, 214)
ROBOT_LOST = (201, 64, 64)
SCENT = (236, 146, 32)
TEXT = (30, 35, 40)
SUBTEXT = (92, 102, 112)
PANEL = (255, 255, 255)
PANEL_BORDER = (216, 222, 228)
BTN_BG = (236, 240, 244)
BTN_BORDER = (166, 176, 186)
BTN_ACTIVE = (217, 233, 252)
ACCENT = (76, 110, 245)


@dataclass
class Snapshot:
    state: RobotState
    scents: set[Tuple[int, int, str]]
    status: str
    command: str


class RobotGame:
    def __init__(self, width: int = 4, height: int = 3) -> None:
        self.world = World(width=width, height=height)
        self.robot = RobotState(0, 0, "N", False)
        self.history: List[Snapshot] = []
        self.command_buffer = ""
        self.last_status = "READY"

        self.replay_mode = False
        self.replay_index = 0
        self.replay_tick = 0
        self.replay_state = self.robot
        self.replay_scents: set[Tuple[int, int, str]] = set()

        self.record_snapshot(command="-", status="INIT")

    def record_snapshot(self, command: str, status: str) -> None:
        self.history.append(
            Snapshot(
                state=RobotState(self.robot.x, self.robot.y, self.robot.direction, self.robot.lost),
                scents=set(self.world.scents),
                status=status,
                command=command,
            )
        )

    def reset_robot(self) -> None:
        self.robot = RobotState(0, 0, "N", False)
        self.last_status = "NEW_ROBOT"
        self.record_snapshot(command="N", status=self.last_status)

    def clear_scents(self) -> None:
        self.world.scents.clear()
        self.last_status = "CLEAR_SCENT"
        self.record_snapshot(command="C", status=self.last_status)

    def apply_command(self, command: str) -> None:
        self.replay_mode = False
        result = step_robot(self.world, self.robot, command)
        self.robot = result.state
        self.last_status = result.status
        self.command_buffer += command
        self.record_snapshot(command=command, status=result.status)

    def replay_start(self) -> None:
        if not self.history:
            return
        self.replay_mode = True
        self.replay_index = 0
        self.replay_tick = 0
        first = self.history[0]
        self.replay_state = first.state
        self.replay_scents = set(first.scents)

    def update_replay(self) -> None:
        if not self.replay_mode:
            return
        self.replay_tick += 1
        if self.replay_tick < 20:
            return
        self.replay_tick = 0
        self.replay_index += 1
        if self.replay_index >= len(self.history):
            self.replay_mode = False
            return
        frame = self.history[self.replay_index]
        self.replay_state = frame.state
        self.replay_scents = set(frame.scents)


def get_layout(game: RobotGame) -> Dict[str, pygame.Rect]:
    board_w = (game.world.width + 1) * CELL
    board_h = (game.world.height + 1) * CELL

    board_rect = pygame.Rect(MARGIN, MARGIN + TITLE_HEIGHT, board_w, board_h)
    sidebar_rect = pygame.Rect(board_rect.right + 20, board_rect.y, SIDEBAR_WIDTH, board_h)
    status_rect = pygame.Rect(sidebar_rect.x, sidebar_rect.y, sidebar_rect.width, 206)
    event_rect = pygame.Rect(sidebar_rect.x, status_rect.bottom + 14, sidebar_rect.width, 108)
    control_rect = pygame.Rect(sidebar_rect.x, event_rect.bottom + 14, sidebar_rect.width, 176)
    return {
        "board": board_rect,
        "sidebar": sidebar_rect,
        "status": status_rect,
        "event": event_rect,
        "control": control_rect,
    }


BUTTON_LABELS = {
    "L": "左轉",
    "R": "右轉",
    "F": "前進",
    "N": "新機器人",
    "C": "清除標記",
    "P": "回放",
    "S": "離開",
}


def build_buttons(game: RobotGame) -> Dict[str, pygame.Rect]:
    layout = get_layout(game)
    control_rect = layout["control"]
    base_x = control_rect.x + 18
    base_y = control_rect.y + 42
    w, h, gap_x, gap_y = 64, 38, 10, 10

    keys = ["L", "R", "F", "N", "C", "P", "S"]
    rects: Dict[str, pygame.Rect] = {}
    for i, key in enumerate(keys):
        row = i // 4
        col = i % 4
        rects[key] = pygame.Rect(
            base_x + col * (w + gap_x),
            base_y + row * (h + gap_y),
            w,
            h,
        )
    return rects


def get_font(size: int, bold: bool = False) -> pygame.font.Font:
    candidates = ["microsoftjhengheiui", "microsoftjhenghei", "segoeui", "arial"]
    for name in candidates:
        font = pygame.font.SysFont(name, size, bold=bold)
        if font:
            return font
    return pygame.font.Font(None, size)


def draw_card(surface: pygame.Surface, rect: pygame.Rect) -> None:
    pygame.draw.rect(surface, PANEL, rect, border_radius=16)
    pygame.draw.rect(surface, PANEL_BORDER, rect, width=1, border_radius=16)


def draw_text(surface: pygame.Surface, font: pygame.font.Font, text: str, color: tuple[int, int, int], pos: tuple[int, int]) -> None:
    img = font.render(text, True, color)
    surface.blit(img, pos)


def _board_inner_rect(game: RobotGame) -> pygame.Rect:
    return get_layout(game)["board"].inflate(-14, -14)


def _to_screen(game: RobotGame, x: int, y: int) -> Tuple[int, int]:
    inner = _board_inner_rect(game)
    sx = inner.x + x * CELL + CELL // 2
    sy = inner.y + (game.world.height - y) * CELL + CELL // 2
    return sx, sy


def draw_robot(surface: pygame.Surface, game: RobotGame, state: RobotState) -> None:
    cx, cy = _to_screen(game, state.x, state.y)
    half = CELL // 3
    color = ROBOT_LOST if state.lost else ROBOT

    if state.direction == "N":
        points = [(cx, cy - half), (cx - half, cy + half), (cx + half, cy + half)]
    elif state.direction == "E":
        points = [(cx + half, cy), (cx - half, cy - half), (cx - half, cy + half)]
    elif state.direction == "S":
        points = [(cx, cy + half), (cx - half, cy - half), (cx + half, cy - half)]
    else:
        points = [(cx - half, cy), (cx + half, cy - half), (cx + half, cy + half)]

    pygame.draw.polygon(surface, color, points)


def draw_game(surface: pygame.Surface, game: RobotGame, font: pygame.font.Font) -> None:
    surface.fill(BG)

    title_font = get_font(24, bold=True)
    value_font = get_font(20, bold=True)
    body_font = get_font(17)
    small_font = get_font(14)
    mono_font = get_font(16)

    layout = get_layout(game)
    board_rect = layout["board"]
    info_rect = layout["status"]
    event_rect = layout["event"]
    control_rect = layout["control"]

    draw_text(surface, title_font, "Robot Lost", TEXT, (MARGIN, MARGIN - 2))
    draw_text(surface, small_font, "Week 03 規則模擬與視覺化", SUBTEXT, (MARGIN, MARGIN + 30))

    pygame.draw.rect(surface, PANEL, board_rect, border_radius=18)
    pygame.draw.rect(surface, PANEL_BORDER, board_rect, width=1, border_radius=18)
    inner_board = _board_inner_rect(game)
    pygame.draw.rect(surface, (250, 251, 252), inner_board, border_radius=12)
    pygame.draw.rect(surface, GRID, inner_board, width=2, border_radius=12)

    for x in range(game.world.width + 1):
        px = inner_board.x + x * CELL
        pygame.draw.line(surface, GRID_SOFT, (px, inner_board.y), (px, inner_board.bottom), width=1)

    for y in range(game.world.height + 1):
        py = inner_board.y + y * CELL
        pygame.draw.line(surface, GRID_SOFT, (inner_board.x, py), (inner_board.right, py), width=1)

    scents = game.replay_scents if game.replay_mode else game.world.scents
    state = game.replay_state if game.replay_mode else game.robot

    for x in range(game.world.width + 1):
        label = small_font.render(str(x), True, SUBTEXT)
        lx = inner_board.x + x * CELL + (CELL - label.get_width()) // 2
        surface.blit(label, (lx, inner_board.bottom + 8))

    for y in range(game.world.height + 1):
        label = small_font.render(str(game.world.height - y), True, SUBTEXT)
        ly = inner_board.y + y * CELL + (CELL - label.get_height()) // 2
        surface.blit(label, (inner_board.x - 18, ly))

    for sx, sy, _ in scents:
        px, py = _to_screen(game, sx, sy)
        pygame.draw.circle(surface, SCENT, (px, py), 6)
        pygame.draw.circle(surface, (255, 242, 224), (px, py), 12, width=2)

    draw_robot(surface, game, state)

    draw_card(surface, info_rect)
    draw_card(surface, event_rect)
    draw_card(surface, control_rect)

    draw_text(surface, small_font, "目前狀態", SUBTEXT, (info_rect.x + 14, info_rect.y + 14))
    draw_text(surface, value_font, f"({state.x}, {state.y})", TEXT, (info_rect.x + 14, info_rect.y + 34))
    draw_text(surface, body_font, f"方向 {state.direction}", TEXT, (info_rect.x + 14, info_rect.y + 66))

    badge_rect = pygame.Rect(info_rect.x + 14, info_rect.y + 92, 78, 28)
    badge_color = ROBOT_LOST if state.lost else ACCENT
    pygame.draw.rect(surface, badge_color, badge_rect, border_radius=14)
    draw_text(
        surface,
        small_font,
        "LOST" if state.lost else "ALIVE",
        (255, 255, 255),
        (badge_rect.x + 16, badge_rect.y + 5),
    )

    draw_text(surface, small_font, f"scent 數量 {len(scents)}", SUBTEXT, (info_rect.x + 14, info_rect.y + 128))
    draw_text(surface, small_font, f"歷史步數 {len(game.history) - 1}", SUBTEXT, (info_rect.x + 14, info_rect.y + 150))
    mode_text = "回放中" if game.replay_mode else "手動控制"
    draw_text(surface, small_font, f"模式 {mode_text}", SUBTEXT, (info_rect.x + 14, info_rect.y + 172))

    draw_text(surface, small_font, "事件紀錄", SUBTEXT, (event_rect.x + 14, event_rect.y + 14))
    draw_text(surface, small_font, "上次事件", SUBTEXT, (event_rect.x + 14, event_rect.y + 38))
    draw_text(surface, get_font(15, bold=True), game.last_status, TEXT, (event_rect.x + 94, event_rect.y + 36))
    draw_text(surface, small_font, "最近指令", SUBTEXT, (event_rect.x + 14, event_rect.y + 70))
    command_preview = game.command_buffer[-14:] if game.command_buffer else "-"
    draw_text(surface, mono_font, command_preview, TEXT, (event_rect.x + 94, event_rect.y + 68))

    snapshot_lines = grid_snapshot(game.world, state, max_size=6)
    draw_text(surface, small_font, "控制按鈕", SUBTEXT, (control_rect.x + 14, control_rect.y + 14))

    buttons = build_buttons(game)
    for key, rect in buttons.items():
        active = key in {"L", "R", "F"}
        pygame.draw.rect(surface, BTN_ACTIVE if active else BTN_BG, rect, border_radius=10)
        pygame.draw.rect(surface, BTN_BORDER, rect, width=1, border_radius=10)
        key_text = small_font.render(key, True, TEXT)
        desc_text = get_font(10).render(BUTTON_LABELS[key], True, SUBTEXT)
        surface.blit(key_text, (rect.x + (rect.width - key_text.get_width()) // 2, rect.y + 4))
        surface.blit(desc_text, (rect.x + (rect.width - desc_text.get_width()) // 2, rect.y + 20))

    draw_text(surface, small_font, "矩陣預覽", SUBTEXT, (control_rect.x + 14, control_rect.y + 132))
    for i, line in enumerate(snapshot_lines[:3]):
        draw_text(surface, mono_font, line, TEXT, (control_rect.x + 14, control_rect.y + 150 + i * 16))


def save_gameplay_screenshot(game: RobotGame, target_path: Path) -> None:
    pygame.init()
    pygame.font.init()
    layout = get_layout(game)
    width = layout["sidebar"].right + MARGIN
    height = max(layout["board"].bottom, layout["control"].bottom) + MARGIN
    surface = pygame.Surface((width, height))
    font = get_font(22)
    draw_game(surface, game, font)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    pygame.image.save(surface, str(target_path))
    pygame.quit()


def generate_demo_capture(output_path: Path) -> None:
    game = RobotGame(width=4, height=3)
    commands = "RFRFRFRFFFFLF"
    for c in commands:
        game.apply_command(c)
        if game.robot.lost:
            break
    game.reset_robot()
    for c in "RFF":
        game.apply_command(c)
    save_gameplay_screenshot(game, output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Robot Lost pygame 模擬器")
    parser.add_argument("--capture", action="store_true", help="產生 demo 截圖後結束")
    parser.add_argument(
        "--capture-path",
        default="assets/gameplay.png",
        help="截圖輸出路徑",
    )
    args = parser.parse_args()

    if args.capture:
        generate_demo_capture(Path(args.capture_path))
        print(f"saved: {args.capture_path}")
        return

    pygame.init()
    pygame.font.init()

    game = RobotGame(width=4, height=3)
    layout = get_layout(game)
    screen_w = layout["sidebar"].right + MARGIN
    screen_h = max(layout["board"].bottom, layout["control"].bottom) + MARGIN
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("Robot Lost - Week 03")

    clock = pygame.time.Clock()
    font = get_font(22)

    running = True
    while running:
        buttons = build_buttons(game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_l, pygame.K_LEFT, pygame.K_a):
                    game.apply_command("L")
                elif event.key in (pygame.K_r, pygame.K_RIGHT, pygame.K_d):
                    game.apply_command("R")
                elif event.key in (pygame.K_f, pygame.K_UP, pygame.K_w):
                    game.apply_command("F")
                elif event.key == pygame.K_n:
                    game.reset_robot()
                elif event.key == pygame.K_c:
                    game.clear_scents()
                elif event.key == pygame.K_p:
                    game.replay_start()
                elif event.key == pygame.K_s:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for key, rect in buttons.items():
                    if rect.collidepoint(mx, my):
                        if key in ("L", "R", "F"):
                            game.apply_command(key)
                        elif key == "N":
                            game.reset_robot()
                        elif key == "C":
                            game.clear_scents()
                        elif key == "P":
                            game.replay_start()
                        elif key == "S":
                            running = False
                        break

        game.update_replay()
        draw_game(screen, game, font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
