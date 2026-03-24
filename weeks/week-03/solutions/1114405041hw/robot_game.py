"""Week 03 Robot Lost pygame MVP.

Controls:
- L / R / F: execute one command
- N: deploy new robot at (0,0,N), keep scents
- C: clear scents
- G: replay from recorded history
- ESC: quit
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import pygame
except ImportError:
    print("pygame 未安裝，請先執行: pip install pygame")
    sys.exit(1)

from robot_core import RobotState, matrix_snapshot, new_robot, run_commands, step_robot

WORLD_W = 5
WORLD_H = 3
CELL = 90
MARGIN = 40
HUD_HEIGHT = 120
SCREEN_W = MARGIN * 2 + (WORLD_W + 1) * CELL
SCREEN_H = MARGIN * 2 + (WORLD_H + 1) * CELL + HUD_HEIGHT

BG_COLOR = (246, 244, 236)
GRID_COLOR = (130, 126, 112)
ROBOT_COLOR = (32, 94, 175)
SCENT_COLOR = (210, 60, 60)
TEXT_COLOR = (38, 38, 38)
ACCENT = (60, 150, 90)


def to_screen(x: int, y: int) -> tuple[int, int]:
    sx = MARGIN + x * CELL + CELL // 2
    sy = MARGIN + (WORLD_H - y) * CELL + CELL // 2
    return sx, sy


def draw_grid(screen: pygame.Surface) -> None:
    for x in range(WORLD_W + 2):
        px = MARGIN + x * CELL
        pygame.draw.line(screen, GRID_COLOR, (px, MARGIN), (px, MARGIN + (WORLD_H + 1) * CELL), 2)
    for y in range(WORLD_H + 2):
        py = MARGIN + y * CELL
        pygame.draw.line(screen, GRID_COLOR, (MARGIN, py), (MARGIN + (WORLD_W + 1) * CELL, py), 2)


def draw_scents(screen: pygame.Surface, scents: set[tuple[int, int, str]]) -> None:
    for x, y, _ in scents:
        sx, sy = to_screen(x, y)
        pygame.draw.circle(screen, SCENT_COLOR, (sx, sy), 8)


def draw_robot(screen: pygame.Surface, state: RobotState) -> None:
    sx, sy = to_screen(state.x, state.y)
    size = 28

    if state.direction == "N":
        points = [(sx, sy - size), (sx - size // 2, sy + size // 2), (sx + size // 2, sy + size // 2)]
    elif state.direction == "E":
        points = [(sx + size, sy), (sx - size // 2, sy - size // 2), (sx - size // 2, sy + size // 2)]
    elif state.direction == "S":
        points = [(sx, sy + size), (sx - size // 2, sy - size // 2), (sx + size // 2, sy - size // 2)]
    else:
        points = [(sx - size, sy), (sx + size // 2, sy - size // 2), (sx + size // 2, sy + size // 2)]

    color = (90, 90, 90) if state.lost else ROBOT_COLOR
    pygame.draw.polygon(screen, color, points)


def draw_hud(
    screen: pygame.Surface,
    font: pygame.font.Font,
    small_font: pygame.font.Font,
    state: RobotState,
    scents: set[tuple[int, int, str]],
    last_event: str,
) -> None:
    base_y = MARGIN + (WORLD_H + 1) * CELL + 16
    status = f"Robot: ({state.x}, {state.y}) {state.direction} | LOST={state.lost}"
    event = f"Last Event: {last_event}"
    scent_count = f"Scent count: {len(scents)}"
    control = "Keys: L/R/F step | N new robot | C clear scent | G replay | ESC quit"

    screen.blit(font.render(status, True, TEXT_COLOR), (MARGIN, base_y))
    screen.blit(font.render(event, True, ACCENT), (MARGIN, base_y + 30))
    screen.blit(font.render(scent_count, True, TEXT_COLOR), (MARGIN, base_y + 60))
    screen.blit(small_font.render(control, True, TEXT_COLOR), (MARGIN, base_y + 88))


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Week 03 - Robot Lost MVP")
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("consolas", 22)
    small_font = pygame.font.SysFont("consolas", 18)

    robot = new_robot(0, 0, "N")
    scents: set[tuple[int, int, str]] = set()
    history: list[tuple[RobotState, set[tuple[int, int, str]], str]] = []
    last_event = "READY"
    replay_mode = False
    replay_index = 0

    def record(event: str) -> None:
        history.append((robot, set(scents), event))

    record("INIT")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_n:
                    robot = new_robot(0, 0, "N")
                    last_event = "NEW_ROBOT"
                    record(last_event)
                elif event.key == pygame.K_c:
                    scents.clear()
                    last_event = "CLEAR_SCENT"
                    record(last_event)
                elif event.key == pygame.K_l:
                    robot, last_event = step_robot(robot, "L", WORLD_W, WORLD_H, scents)
                    record(last_event)
                elif event.key == pygame.K_r:
                    robot, last_event = step_robot(robot, "R", WORLD_W, WORLD_H, scents)
                    record(last_event)
                elif event.key == pygame.K_f:
                    robot, last_event = step_robot(robot, "F", WORLD_W, WORLD_H, scents)
                    record(last_event)
                elif event.key == pygame.K_g and history:
                    replay_mode = True
                    replay_index = 0

        if replay_mode and history:
            replay_robot, replay_scents, replay_event = history[replay_index]
            robot = replay_robot
            scents = set(replay_scents)
            last_event = f"REPLAY:{replay_event}"
            replay_index += 1
            if replay_index >= len(history):
                replay_mode = False

        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_scents(screen, scents)
        draw_robot(screen, robot)
        draw_hud(screen, font, small_font, robot, scents, last_event)

        pygame.display.flip()
        clock.tick(8 if replay_mode else 30)

    # Export plain replay log for report/reference.
    output_dir = Path(__file__).parent / "assets"
    output_dir.mkdir(parents=True, exist_ok=True)
    replay_txt = output_dir / "replay.txt"
    snapshot = matrix_snapshot(robot, WORLD_W, WORLD_H, scents)
    with replay_txt.open("w", encoding="utf-8") as f:
        f.write("Robot Lost Replay Log\n")
        for i, (r, s, evt) in enumerate(history, start=1):
            f.write(f"{i:03d}: ({r.x},{r.y},{r.direction},lost={r.lost}) event={evt} scents={len(s)}\n")
        f.write("\nFinal Matrix:\n")
        for row in snapshot:
            f.write(row + "\n")

    pygame.quit()


if __name__ == "__main__":
    main()
