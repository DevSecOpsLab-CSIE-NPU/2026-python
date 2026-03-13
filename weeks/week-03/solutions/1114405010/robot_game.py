"""Pygame UI for Week 03 Robot Lost with dark dashboard layout."""

import pygame

from robot_core import RobotState, execute_commands

CELL_SIZE = 50
GRID_W = 9
GRID_H = 9
MATRIX_SIZE = 10
WINDOW_W = 700
WINDOW_H = 980
GRID_LEFT = 30
GRID_TOP = 30
GRID_SIZE_PX = CELL_SIZE * MATRIX_SIZE
PANEL_LEFT = 30
PANEL_TOP = 550
PANEL_WIDTH = 640
PANEL_HEIGHT = 400


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        pygame.display.set_caption("Week 03 - Robot Lost")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("microsoftjhenghei", 30)
        self.text_font = pygame.font.SysFont("microsoftjhenghei", 18)
        self.matrix_font = pygame.font.SysFont("consolas", 16)

        self.scents = set()
        self.robot = RobotState(0, 0, "N")
        self.robot_index = 1
        self.latest_event = "就緒"
        self.command_log: list[str] = []
        self.replay_count = 0
        self.last_snapshot = self.build_matrix_snapshot()

    def reset_robot(self) -> None:
        self.robot = RobotState(0, 0, "N")
        self.robot_index += 1
        self.latest_event = "新機器人建立"
        self.command_log.clear()

    def clear_scents(self) -> None:
        self.scents.clear()
        self.latest_event = "已清除 scent"

    def run_step(self, command: str) -> None:
        execute_commands(self.robot, [command], GRID_W, GRID_H, self.scents)
        self.command_log.append(command)
        if self.robot.lost:
            self.latest_event = "機器人 LOST"
        else:
            self.latest_event = f"執行指令 {command}"
        self.last_snapshot = self.build_matrix_snapshot()

    def build_matrix_snapshot(self) -> list[str]:
        """Build a 10x10 string matrix snapshot."""
        matrix = [["." for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

        for sx, sy, _ in self.scents:
            if 0 <= sx < MATRIX_SIZE and 0 <= sy < MATRIX_SIZE:
                matrix[MATRIX_SIZE - 1 - sy][sx] = "s"

        if 0 <= self.robot.x < MATRIX_SIZE and 0 <= self.robot.y < MATRIX_SIZE:
            marker = "X" if self.robot.lost else "R"
            matrix[MATRIX_SIZE - 1 - self.robot.y][self.robot.x] = marker

        return ["".join(row) for row in matrix]

    def print_snapshot(self) -> None:
        print("\n10x10 矩陣快照")
        for line in self.last_snapshot:
            print(line)
        scents_sorted = sorted(self.scents)
        print(f"容器 world.scents 觀察: {scents_sorted}\n")

    def draw_grid(self) -> None:
        # Frame
        pygame.draw.rect(
            self.screen,
            (66, 80, 101),
            (GRID_LEFT, GRID_TOP, GRID_SIZE_PX, GRID_SIZE_PX),
            width=2,
        )

        # Grid lines
        for i in range(MATRIX_SIZE + 1):
            x = GRID_LEFT + i * CELL_SIZE
            y = GRID_TOP + i * CELL_SIZE
            pygame.draw.line(self.screen, (66, 80, 101), (x, GRID_TOP), (x, GRID_TOP + GRID_SIZE_PX), 1)
            pygame.draw.line(self.screen, (66, 80, 101), (GRID_LEFT, y), (GRID_LEFT + GRID_SIZE_PX, y), 1)

        # Scents
        for sx, sy, _ in self.scents:
            px = GRID_LEFT + sx * CELL_SIZE + CELL_SIZE // 2
            py = GRID_TOP + (GRID_H - sy) * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(self.screen, (243, 184, 87), (px, py), 8)

        # Robot triangle
        cx = GRID_LEFT + self.robot.x * CELL_SIZE + CELL_SIZE // 2
        cy = GRID_TOP + (GRID_H - self.robot.y) * CELL_SIZE + CELL_SIZE // 2
        size = 24
        if self.robot.direction == "N":
            points = [(cx, cy - size), (cx - size, cy + size), (cx + size, cy + size)]
        elif self.robot.direction == "E":
            points = [(cx + size, cy), (cx - size, cy - size), (cx - size, cy + size)]
        elif self.robot.direction == "S":
            points = [(cx, cy + size), (cx - size, cy - size), (cx + size, cy - size)]
        else:
            points = [(cx - size, cy), (cx + size, cy - size), (cx + size, cy + size)]

        robot_color = (86, 213, 174) if not self.robot.lost else (223, 96, 96)
        pygame.draw.polygon(self.screen, robot_color, points)

    def draw_panel(self) -> None:
        def draw_wrapped(text: str, font: pygame.font.Font, x: int, y: int, max_width: int, color: tuple[int, int, int], line_gap: int) -> int:
            words = text.split(" ")
            line = ""
            for word in words:
                candidate = word if not line else f"{line} {word}"
                if font.size(candidate)[0] <= max_width:
                    line = candidate
                else:
                    if line:
                        surf = font.render(line, True, color)
                        self.screen.blit(surf, (x, y))
                        y += line_gap
                    line = word
            if line:
                surf = font.render(line, True, color)
                self.screen.blit(surf, (x, y))
                y += line_gap
            return y

        panel_rect = pygame.Rect(PANEL_LEFT, PANEL_TOP, PANEL_WIDTH, PANEL_HEIGHT)
        pygame.draw.rect(self.screen, (31, 43, 58), panel_rect, border_radius=16)

        status_word = "LOST" if self.robot.lost else "存活"
        lines = [
            f"機器人 #{self.robot_index} : ({self.robot.x}, {self.robot.y}) {self.robot.direction} {status_word}",
            f"最新事件：{self.latest_event}",
            f"Scent 數量：{len(self.scents)}",
            f"回放影格數：{self.replay_count}",
            f"指令紀錄：{''.join(self.command_log[-16:])}",
            f"容器 world.scents（ set ）觀察：{sorted(self.scents)}",
            "操作：L/R/F｜N 新機器人｜C 清除 scent｜G 匯出 GIF｜ESC 離開",
            "10x10 矩陣快照 ( R=機器人, s=scent, .=空格 )",
        ]

        content_left = PANEL_LEFT + 16
        content_right = PANEL_LEFT + PANEL_WIDTH - 16
        content_width = content_right - content_left
        content_bottom = PANEL_TOP + PANEL_HEIGHT - 14

        y = PANEL_TOP + 16
        for line in lines:
            if y >= content_bottom:
                break
            y = draw_wrapped(line, self.text_font, content_left, y, content_width, (215, 223, 232), 24)

        if y + 6 < content_bottom:
            y += 6

        row_height = 18
        remaining_rows = max(0, (content_bottom - y) // row_height)
        matrix_to_draw = self.last_snapshot[:remaining_rows]

        for matrix_line in matrix_to_draw:
            surf = self.matrix_font.render(matrix_line, True, (215, 223, 232))
            self.screen.blit(surf, (content_left, y))
            y += row_height

        if remaining_rows < len(self.last_snapshot) and y < content_bottom:
            more = self.matrix_font.render("...", True, (215, 223, 232))
            self.screen.blit(more, (content_left, y))

    def draw(self) -> None:
        self.screen.fill((10, 18, 30))
        self.draw_grid()
        self.draw_panel()

        pygame.display.flip()

    def loop(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_l:
                        self.run_step("L")
                    elif event.key == pygame.K_r:
                        self.run_step("R")
                    elif event.key == pygame.K_f:
                        self.run_step("F")
                    elif event.key == pygame.K_n:
                        self.reset_robot()
                        self.last_snapshot = self.build_matrix_snapshot()
                    elif event.key == pygame.K_c:
                        self.clear_scents()
                        self.last_snapshot = self.build_matrix_snapshot()
                    elif event.key == pygame.K_g:
                        self.latest_event = "GIF 匯出尚未實作"
                        self.replay_count = len(self.command_log)
                    elif event.key == pygame.K_m:
                        self.last_snapshot = self.build_matrix_snapshot()
                        self.print_snapshot()

            self.draw()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    Game().loop()
