"""pygame UI for Robot Lost homework MVP."""

from __future__ import annotations

import sys

import pygame

from robot_core import RobotState, RobotWorld

CELL_SIZE = 60
PADDING = 40
HUD_WIDTH = 280
BG_COLOR = (247, 245, 238)
GRID_COLOR = (186, 180, 168)
ROBOT_COLOR = (45, 98, 150)
SCENT_COLOR = (191, 78, 96)
TEXT_COLOR = (36, 34, 31)


class RobotGame:
    def __init__(self, width: int = 5, height: int = 3) -> None:
        pygame.init()
        pygame.display.set_caption("Robot Lost - Week 03")

        self.world = RobotWorld(width, height)
        self.world.deploy_robot(0, 0, "N")

        self.grid_w = (width + 1) * CELL_SIZE
        self.grid_h = (height + 1) * CELL_SIZE
        screen_w = self.grid_w + PADDING * 2 + HUD_WIDTH
        screen_h = self.grid_h + PADDING * 2

        self.screen = pygame.display.set_mode((screen_w, screen_h))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 22)
        self.small_font = pygame.font.SysFont("consolas", 18)

        self.command_log: list[str] = []
        self.replay_mode = False
        self.replay_index = 0

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    running = self.handle_key(event.key)

            if self.replay_mode and self.world.replay_log:
                self.replay_index = (self.replay_index + 1) % len(self.world.replay_log)

            self.render()
            pygame.display.flip()
            self.clock.tick(8 if self.replay_mode else 30)

        pygame.quit()
        sys.exit(0)

    def handle_key(self, key: int) -> bool:
        if key == pygame.K_ESCAPE:
            return False

        if key == pygame.K_n:
            self.world.deploy_robot(0, 0, "N")
            self.command_log.clear()
            self.replay_mode = False
            self.replay_index = 0
        elif key == pygame.K_c:
            self.world.clear_scents()
            self.command_log.append("CLEAR_SCENT")
        elif key == pygame.K_g:
            self.replay_mode = not self.replay_mode
            self.replay_index = 0
        elif key in (pygame.K_l, pygame.K_r, pygame.K_f):
            command = chr(key).upper()
            self.world.execute_command(command)
            self.command_log.append(command)
            self.replay_mode = False
            self.replay_index = max(0, len(self.world.replay_log) - 1)

        return True

    def render(self) -> None:
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        self.draw_scents()
        self.draw_robot()
        self.draw_hud()

    def draw_grid(self) -> None:
        origin_x, origin_y = PADDING, PADDING
        for x in range(self.world.max_x + 2):
            px = origin_x + x * CELL_SIZE
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (px, origin_y),
                (px, origin_y + self.grid_h),
                width=2,
            )
        for y in range(self.world.max_y + 2):
            py = origin_y + y * CELL_SIZE
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (origin_x, py),
                (origin_x + self.grid_w, py),
                width=2,
            )

    def draw_scents(self) -> None:
        for sx, sy, _ in self.world.scents:
            cx, cy = self.cell_center(sx, sy)
            pygame.draw.circle(self.screen, SCENT_COLOR, (cx, cy), CELL_SIZE // 8)

    def draw_robot(self) -> None:
        state = self.current_view_state()
        cx, cy = self.cell_center(state.x, state.y)

        points = {
            "N": [(cx, cy - 18), (cx - 14, cy + 14), (cx + 14, cy + 14)],
            "E": [(cx + 18, cy), (cx - 14, cy - 14), (cx - 14, cy + 14)],
            "S": [(cx, cy + 18), (cx - 14, cy - 14), (cx + 14, cy - 14)],
            "W": [(cx - 18, cy), (cx + 14, cy - 14), (cx + 14, cy + 14)],
        }
        color = (130, 130, 130) if state.lost else ROBOT_COLOR
        pygame.draw.polygon(self.screen, color, points[state.direction])

    def draw_hud(self) -> None:
        hud_x = PADDING * 2 + self.grid_w
        lines = [
            "Week 03 Robot Lost",
            "",
            "Keys:",
            "L/R/F: step",
            "N: new robot",
            "C: clear scent",
            "G: replay on/off",
            "ESC: exit",
            "",
        ]

        state = self.current_view_state()
        status = "LOST" if state.lost else "ALIVE"
        lines.extend(
            [
                f"Robot: ({state.x}, {state.y})",
                f"Dir: {state.direction}",
                f"State: {status}",
                f"Scents: {len(self.world.scents)}",
                f"Replay: {'ON' if self.replay_mode else 'OFF'}",
                "",
                "Recent commands:",
                "".join(self.command_log[-16:]) or "(none)",
                "",
                "Matrix snapshot:",
            ]
        )

        matrix = self.world.matrix_snapshot(width=10, height=10)
        lines.extend(matrix[:10])

        y = PADDING
        for text in lines:
            font = self.small_font if len(text) > 24 else self.font
            surface = font.render(text, True, TEXT_COLOR)
            self.screen.blit(surface, (hud_x, y))
            y += 24 if font is self.small_font else 28

    def current_view_state(self) -> RobotState:
        if self.replay_mode and self.world.replay_log:
            return self.world.replay_log[self.replay_index]
        assert self.world.robot is not None
        return self.world.robot

    def cell_center(self, x: int, y: int) -> tuple[int, int]:
        cx = PADDING + x * CELL_SIZE + CELL_SIZE // 2
        # pygame Y-axis grows downward, while robot coordinates grow upward.
        cy = PADDING + (self.world.max_y - y) * CELL_SIZE + CELL_SIZE // 2
        return cx, cy


def main() -> None:
    game = RobotGame(width=5, height=3)
    game.run()


if __name__ == "__main__":
    main()
