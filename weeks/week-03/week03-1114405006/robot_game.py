from __future__ import annotations

from pathlib import Path

try:
    import pygame
except ImportError as exc:  # pragma: no cover - runtime guard
    raise SystemExit("pygame is required. Install it with: python -m pip install pygame") from exc

from robot_core import RobotSimulator


WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 780
GRID_SIZE = 11
MARGIN = 48
PANEL_WIDTH = 320
CELL_SIZE = 50
GRID_PIXEL = CELL_SIZE * GRID_SIZE

BG = (18, 24, 38)
GRID_BG = (28, 36, 56)
GRID_LINE = (78, 93, 122)
ACCENT = (255, 194, 77)
ROBOT = (89, 202, 255)
ROBOT_EDGE = (233, 247, 255)
TEXT = (238, 242, 247)
MUTED = (171, 183, 204)
SENT = (255, 126, 95)
LOSS = (255, 87, 87)
PANEL = (14, 18, 30)


pygame.init()
title_font = pygame.font.SysFont("arial", 30, bold=True)
body_font = pygame.font.SysFont("arial", 22)
small_font = pygame.font.SysFont("arial", 16)


def create_simulator() -> RobotSimulator:
    simulator = RobotSimulator(GRID_SIZE - 1, GRID_SIZE - 1)
    simulator.deploy(1, 1, "N")
    return simulator


def draw_text(surface: pygame.Surface, font: pygame.font.Font, text: str, x: int, y: int, color=TEXT) -> None:
    rendered = font.render(text, True, color)
    surface.blit(rendered, (x, y))


def grid_to_screen(x: int, y: int) -> tuple[int, int]:
    screen_x = MARGIN + x * CELL_SIZE
    screen_y = MARGIN + (GRID_SIZE - 1 - y) * CELL_SIZE
    return screen_x, screen_y


def draw_grid(surface: pygame.Surface) -> None:
    grid_rect = pygame.Rect(MARGIN, MARGIN, GRID_PIXEL, GRID_PIXEL)
    pygame.draw.rect(surface, GRID_BG, grid_rect, border_radius=18)

    for index in range(GRID_SIZE):
        pygame.draw.line(
            surface,
            GRID_LINE,
            (MARGIN + index * CELL_SIZE, MARGIN),
            (MARGIN + index * CELL_SIZE, MARGIN + GRID_PIXEL),
            1,
        )
        pygame.draw.line(
            surface,
            GRID_LINE,
            (MARGIN, MARGIN + index * CELL_SIZE),
            (MARGIN + GRID_PIXEL, MARGIN + index * CELL_SIZE),
            1,
        )

    for x in range(GRID_SIZE):
        draw_text(surface, small_font, str(x), MARGIN + x * CELL_SIZE + 18, MARGIN + GRID_PIXEL + 6, MUTED)
    for y in range(GRID_SIZE):
        draw_text(surface, small_font, str(y), MARGIN - 26, MARGIN + (GRID_SIZE - 1 - y) * CELL_SIZE + 16, MUTED)


def direction_triangle(center_x: int, center_y: int, direction: str) -> list[tuple[int, int]]:
    tip_offset = {
        "N": (0, -18),
        "E": (18, 0),
        "S": (0, 18),
        "W": (-18, 0),
    }[direction]
    left_offset = {
        "N": (-14, 12),
        "E": (-12, -14),
        "S": (14, -12),
        "W": (12, 14),
    }[direction]
    right_offset = {
        "N": (14, 12),
        "E": (-12, 14),
        "S": (-14, -12),
        "W": (12, -14),
    }[direction]
    return [
        (center_x + tip_offset[0], center_y + tip_offset[1]),
        (center_x + left_offset[0], center_y + left_offset[1]),
        (center_x + right_offset[0], center_y + right_offset[1]),
    ]


def draw_scent(surface: pygame.Surface, simulator: RobotSimulator) -> None:
    for x, y, direction in simulator.scent:
        top_left_x, top_left_y = grid_to_screen(x, y)
        center_x = top_left_x + CELL_SIZE // 2
        center_y = top_left_y + CELL_SIZE // 2
        pygame.draw.circle(surface, SENT, (center_x, center_y), 7)
        draw_text(surface, small_font, direction, center_x - 4, center_y - 10, SENT)


def draw_robot(surface: pygame.Surface, simulator: RobotSimulator) -> None:
    if simulator.state.lost:
        return

    top_left_x, top_left_y = grid_to_screen(simulator.state.x, simulator.state.y)
    center_x = top_left_x + CELL_SIZE // 2
    center_y = top_left_y + CELL_SIZE // 2
    triangle = direction_triangle(center_x, center_y, simulator.state.direction)
    pygame.draw.polygon(surface, ROBOT, triangle)
    pygame.draw.polygon(surface, ROBOT_EDGE, triangle, 2)


def draw_hud(surface: pygame.Surface, simulator: RobotSimulator) -> None:
    panel_x = MARGIN + GRID_PIXEL + 28
    pygame.draw.rect(surface, PANEL, pygame.Rect(panel_x, MARGIN, PANEL_WIDTH - 40, GRID_PIXEL), border_radius=18)

    draw_text(surface, title_font, "Robot Lost", panel_x + 18, MARGIN + 18, ACCENT)
    draw_text(surface, body_font, f"狀態：{simulator.format_state()}", panel_x + 18, MARGIN + 76)
    draw_text(surface, body_font, f"地圖：0..{simulator.width} x 0..{simulator.height}", panel_x + 18, MARGIN + 116)
    draw_text(surface, body_font, f"scent 數量：{len(simulator.scent)}", panel_x + 18, MARGIN + 156)
    draw_text(surface, body_font, "操作：L / R / F", panel_x + 18, MARGIN + 216)
    draw_text(surface, body_font, "N 新機器人", panel_x + 18, MARGIN + 256)
    draw_text(surface, body_font, "C 清除 scent", panel_x + 18, MARGIN + 296)
    draw_text(surface, body_font, "G 匯出 replay.gif", panel_x + 18, MARGIN + 336)
    draw_text(surface, body_font, "ESC 離開", panel_x + 18, MARGIN + 376)

    status_color = LOSS if simulator.state.lost else MUTED
    draw_text(surface, body_font, "最新狀態", panel_x + 18, MARGIN + 438, ACCENT)
    draw_text(surface, small_font, simulator.format_state(), panel_x + 18, MARGIN + 470, status_color)

    y = MARGIN + 522
    for index, line in enumerate(simulator.grid_lines(10)):
        draw_text(surface, small_font, line, panel_x + 18, y + index * 18, MUTED)


def render_frame(simulator: RobotSimulator) -> pygame.Surface:
    surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    surface.fill(BG)
    draw_grid(surface)
    draw_scent(surface, simulator)
    draw_robot(surface, simulator)
    draw_hud(surface, simulator)
    return surface


def export_replay_gif(simulator: RobotSimulator, output_path: Path) -> str:
    try:
        from PIL import Image
    except ImportError:
        return "Pillow not installed; replay.gif was not exported."

    frames = []
    for snapshot in simulator.snapshot_history:
        temp_simulator = RobotSimulator(simulator.width, simulator.height)
        temp_simulator.scent = set(simulator.scent)
        temp_simulator.state = snapshot
        frames.append(pygame.image.tostring(render_frame(temp_simulator), "RGB"))

    if not frames:
        return "No frames available for replay export."

    images = [Image.frombytes("RGB", (WINDOW_WIDTH, WINDOW_HEIGHT), frame) for frame in frames]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=220,
        loop=0,
    )
    return f"Replay exported to {output_path}"


def main() -> int:
    pygame.display.set_caption("Robot Lost - Week 03")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    simulator = create_simulator()
    message = "按 L / R / F 開始操作，N 重置，C 清除 scent，G 匯出 replay.gif"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_n:
                    simulator.deploy(1, 1, "N")
                    message = "已重置新機器人"
                elif event.key == pygame.K_c:
                    simulator.clear_scent()
                    message = "已清除 scent"
                elif event.key == pygame.K_g:
                    message = export_replay_gif(simulator, Path(__file__).with_name("assets").joinpath("replay.gif"))
                elif event.key in (pygame.K_l, pygame.K_r, pygame.K_f):
                    if not simulator.state.lost:
                        command = {pygame.K_l: "L", pygame.K_r: "R", pygame.K_f: "F"}[event.key]
                        simulator.apply_command(command)
                        message = f"已執行 {command}"
                    else:
                        message = "機器人已 LOST，請按 N 重置"

        frame = render_frame(simulator)
        screen.blit(frame, (0, 0))
        draw_text(screen, small_font, message, MARGIN, WINDOW_HEIGHT - 28, ACCENT)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())