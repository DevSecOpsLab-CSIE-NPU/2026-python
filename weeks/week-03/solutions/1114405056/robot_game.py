from __future__ import annotations

from typing import List, Set, Tuple

try:
    import pygame
except ImportError as exc:  # pragma: no cover - runtime dependency
    raise SystemExit("pygame is required. Install with: pip install pygame") from exc

from robot_core import RobotState, ScentMark, apply_command

GRID_W = 5
GRID_H = 3
CELL_SIZE = 120
MARGIN = 40
HUD_WIDTH = 320
WINDOW_W = MARGIN * 2 + CELL_SIZE * (GRID_W + 1) + HUD_WIDTH
WINDOW_H = MARGIN * 2 + CELL_SIZE * (GRID_H + 1)
BG_COLOR = (245, 241, 232)
GRID_COLOR = (49, 54, 63)
SCENT_COLOR = (201, 124, 50)
ROBOT_COLOR = (32, 96, 168)
LOST_COLOR = (172, 47, 47)
TEXT_COLOR = (36, 36, 36)


def world_to_screen(x: int, y: int) -> tuple[int, int]:
    # world 座標 y 向上增加；螢幕座標 y 向下增加，需做反轉轉換
    px = MARGIN + x * CELL_SIZE
    py = MARGIN + (GRID_H - y) * CELL_SIZE
    return px, py


def draw_grid(screen: pygame.Surface) -> None:
    for x in range(GRID_W + 2):
        px = MARGIN + x * CELL_SIZE
        pygame.draw.line(screen, GRID_COLOR, (px, MARGIN), (px, MARGIN + CELL_SIZE * (GRID_H + 1)), 2)
    for y in range(GRID_H + 2):
        py = MARGIN + y * CELL_SIZE
        pygame.draw.line(screen, GRID_COLOR, (MARGIN, py), (MARGIN + CELL_SIZE * (GRID_W + 1), py), 2)


def draw_scents(screen: pygame.Surface, scents: Set[ScentMark], font: pygame.font.Font) -> None:
    # scent 以小方塊 + 方向字母標示，方便觀察危險前進點
    for x, y, direction in scents:
        px, py = world_to_screen(x, y)
        marker = pygame.Rect(px + CELL_SIZE // 2 - 8, py + CELL_SIZE // 2 - 8, 16, 16)
        pygame.draw.rect(screen, SCENT_COLOR, marker)
        text = font.render(direction, True, TEXT_COLOR)
        screen.blit(text, (px + CELL_SIZE // 2 - 6, py + CELL_SIZE // 2 + 10))


def draw_robot(screen: pygame.Surface, state: RobotState) -> None:
    px, py = world_to_screen(state.x, state.y)
    center = (px + CELL_SIZE // 2, py + CELL_SIZE // 2)
    pygame.draw.circle(screen, LOST_COLOR if state.lost else ROBOT_COLOR, center, 26)

    dx, dy = {
        "N": (0, -24),
        "E": (24, 0),
        "S": (0, 24),
        "W": (-24, 0),
    }[state.direction]
    # 白線表示目前朝向
    pygame.draw.line(screen, (255, 255, 255), center, (center[0] + dx, center[1] + dy), 4)


def draw_hud(
    screen: pygame.Surface,
    font: pygame.font.Font,
    state: RobotState,
    scents: Set[ScentMark],
    replaying: bool,
) -> None:
    left = MARGIN + CELL_SIZE * (GRID_W + 1) + 24
    lines = [
        "Week 03 - Robot Lost",
        "",
        f"State: ({state.x}, {state.y}, {state.direction})",
        f"Lost: {state.lost}",
        f"Scent marks: {len(scents)}",
        f"Replay: {'ON' if replaying else 'OFF'}",
        "",
        "Controls:",
        "L/R/F: step command",
        "N: new robot",
        "C: clear scent",
        "P: replay moves",
        "ESC: quit",
    ]
    for idx, line in enumerate(lines):
        text = font.render(line, True, TEXT_COLOR)
        screen.blit(text, (left, MARGIN + idx * 28))


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("Robot Lost MVP")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 22)

    scents: Set[ScentMark] = set()
    state = RobotState(0, 0, "N", False)
    history: List[RobotState] = [state]
    replaying = False
    replay_index = 0
    replay_tick = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                if event.key == pygame.K_n:
                    # 建立新機器人，但保留既有 scent
                    state = RobotState(0, 0, "N", False)
                    history = [state]
                    replaying = False
                    continue

                if event.key == pygame.K_c:
                    # 清除所有 scent 記錄
                    scents.clear()
                    continue

                if event.key == pygame.K_p:
                    # 進入回放模式，從歷史第 0 步開始播放
                    replaying = len(history) > 1
                    replay_index = 0
                    replay_tick = pygame.time.get_ticks()
                    continue

                key_to_command = {
                    pygame.K_l: "L",
                    pygame.K_r: "R",
                    pygame.K_f: "F",
                }
                command = key_to_command.get(event.key)
                if command is not None and not replaying:
                    # 回放中不接受新指令，避免狀態被覆蓋
                    state = apply_command(state, command, GRID_W, GRID_H, scents)
                    history.append(state)

        draw_state = state
        if replaying:
            now = pygame.time.get_ticks()
            if now - replay_tick > 350:
                # 固定時間間隔播放下一個歷史狀態
                replay_tick = now
                replay_index += 1
                if replay_index >= len(history):
                    replaying = False
                    replay_index = len(history) - 1
            draw_state = history[replay_index]

        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_scents(screen, scents, font)
        draw_robot(screen, draw_state)
        draw_hud(screen, font, draw_state, scents, replaying)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
