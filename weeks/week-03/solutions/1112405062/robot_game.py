"""
Robot Game - pygame 視覺化機器人模擬遊戲
"""

import pygame
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from robot_core import Robot, RobotWorld, parse_robot_line


pygame.init()

CELL_SIZE = 40
WINDOW_PADDING = 60
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BLUE = (50, 100, 200)
RED = (200, 50, 50)
GREEN = (50, 180, 80)
ORANGE = (255, 150, 0)
YELLOW = (255, 255, 0)

FONT_NAME = "Arial"


class RobotGame:
    """機器人遊戲主類別"""

    def __init__(self, world_width: int, world_height: int):
        self.world_width = world_width
        self.world_height = world_height
        self.world = RobotWorld(world_width, world_height)
        self.robot: Optional[Robot] = None
        self.command_buffer = ""
        self.current_command_idx = 0
        self.history = []
        self.show_matrix = False

        self.screen_width = world_width * CELL_SIZE + WINDOW_PADDING * 2
        self.screen_height = world_height * CELL_SIZE + WINDOW_PADDING * 2 + 100

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Robot Lost - 機器人模擬遊戲")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(FONT_NAME, 18)
        self.font_large = pygame.font.SysFont(FONT_NAME, 24)
        self.font_small = pygame.font.SysFont(FONT_NAME, 14)

    def spawn_robot(self, x: int, y: int, direction: str):
        """生成新機器人"""
        self.robot = Robot(x, y, direction, self.world_width, self.world_height)
        self.command_buffer = ""
        self.current_command_idx = 0

    def spawn_random_robot(self):
        """隨機生成機器人"""
        import random

        x = random.randint(0, self.world_width)
        y = random.randint(0, self.world_height)
        direction = random.choice(["N", "E", "S", "W"])
        self.spawn_robot(x, y, direction)
        self.history.append(f"Spawn: ({x}, {y}, {direction})")

    def execute_command(self, cmd: str) -> bool:
        """執行單一指令"""
        if self.robot is None or self.robot.lost:
            return False

        self.history.append(f"Command: {cmd}")

        if cmd == "F":
            if not self.robot.move_forward():
                if self.world.has_scent(
                    self.robot.x, self.robot.y, self.robot.direction
                ):
                    self.history.append("Ignored (has scent)")
                    return True
                else:
                    self.robot.lost = True
                    self.world.add_scent(self.robot)
                    self.history.append("LOST!")
                    return False
        elif cmd == "L":
            self.robot.turn_left()
        elif cmd == "R":
            self.robot.turn_right()

        return True

    def execute_next_command(self) -> bool:
        """執行下一個緩衝區中的指令"""
        if self.command_buffer and self.current_command_idx < len(self.command_buffer):
            cmd = self.command_buffer[self.current_command_idx]
            self.current_command_idx += 1
            return self.execute_command(cmd)
        return False

    def clear_scent(self):
        """清除所有氣味"""
        self.world.scents.clear()
        self.history.append("Scent cleared")

    def draw_grid(self):
        """繪製網格"""
        for x in range(self.world_width + 1):
            for y in range(self.world_height + 1):
                rect = pygame.Rect(
                    WINDOW_PADDING + x * CELL_SIZE,
                    WINDOW_PADDING + (self.world_height - y) * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                )
                pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_coordinate(self):
        """繪製座標軸"""
        for x in range(self.world_width + 1):
            text = self.font_small.render(str(x), True, GRAY)
            self.screen.blit(
                text,
                (
                    WINDOW_PADDING + x * CELL_SIZE + CELL_SIZE // 2 - 5,
                    WINDOW_PADDING + self.world_height * CELL_SIZE + 5,
                ),
            )

        for y in range(self.world_height + 1):
            text = self.font_small.render(str(y), True, GRAY)
            self.screen.blit(
                text,
                (
                    WINDOW_PADDING - 20,
                    WINDOW_PADDING
                    + (self.world_height - y) * CELL_SIZE
                    + CELL_SIZE // 2
                    - 5,
                ),
            )

    def draw_scent(self):
        """繪製氣味標記"""
        for x, y, direction in self.world.scents:
            center_x = WINDOW_PADDING + x * CELL_SIZE + CELL_SIZE // 2
            center_y = (
                WINDOW_PADDING + (self.world_height - y) * CELL_SIZE + CELL_SIZE // 2
            )
            pygame.draw.circle(self.screen, ORANGE, (center_x, center_y), 5)

    def draw_robot(self):
        """繪製機器人"""
        if self.robot is None:
            return

        x, y = self.robot.x, self.robot.y
        center_x = WINDOW_PADDING + x * CELL_SIZE + CELL_SIZE // 2
        center_y = WINDOW_PADDING + (self.world_height - y) * CELL_SIZE + CELL_SIZE // 2
        size = CELL_SIZE // 3

        points = []
        if self.robot.direction == "N":
            points = [
                (center_x, center_y + size),
                (center_x - size, center_y - size),
                (center_x + size, center_y - size),
            ]
        elif self.robot.direction == "S":
            points = [
                (center_x, center_y - size),
                (center_x - size, center_y + size),
                (center_x + size, center_y + size),
            ]
        elif self.robot.direction == "E":
            points = [
                (center_x - size, center_y),
                (center_x + size, center_y - size),
                (center_x + size, center_y + size),
            ]
        elif self.robot.direction == "W":
            points = [
                (center_x + size, center_y),
                (center_x - size, center_y - size),
                (center_x - size, center_y + size),
            ]

        color = RED if self.robot.lost else GREEN
        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, BLACK, points, 2)

    def draw_info(self):
        """繪製資訊面板"""
        panel_y = WINDOW_PADDING + self.world_height * CELL_SIZE + 20

        if self.robot:
            state_text = f"Position: ({self.robot.x}, {self.robot.y}) Direction: {self.robot.direction}"
            if self.robot.lost:
                state_text += " LOST"
            text = self.font.render(state_text, True, BLACK)
            self.screen.blit(text, (WINDOW_PADDING, panel_y))

            cmd_text = f"Commands: {self.command_buffer[: self.current_command_idx]}[{self.command_buffer[self.current_command_idx :]}]"
            text = self.font.render(cmd_text, True, BLUE)
            self.screen.blit(text, (WINDOW_PADDING, panel_y + 25))

        scent_text = f"Scent count: {len(self.world.scents)}"
        text = self.font.render(scent_text, True, ORANGE)
        self.screen.blit(text, (WINDOW_PADDING + 400, panel_y))

    def draw_controls(self):
        """繪製控制說明"""
        panel_y = self.screen_height - 35
        controls = (
            "L: Left  R: Right  F: Forward  N: New Robot  C: Clear Scent  ESC: Quit"
        )
        text = self.font_small.render(controls, True, GRAY)
        self.screen.blit(text, (WINDOW_PADDING, panel_y))

    def draw_matrix(self):
        """繪製字串矩陣視圖"""
        if not self.show_matrix:
            return

        matrix_y = WINDOW_PADDING + self.world_height * CELL_SIZE + 70
        matrix_str = ""

        for y in range(self.world_height, -1, -1):
            row = ""
            for x in range(self.world_width + 1):
                if (
                    self.robot
                    and self.robot.x == x
                    and self.robot.y == y
                    and not self.robot.lost
                ):
                    row += self.robot.direction + " "
                elif any(s[0] == x and s[1] == y for s in self.world.scents):
                    row += "* "
                else:
                    row += ". "
            matrix_str += row + "\n"

        lines = matrix_str.strip().split("\n")
        for i, line in enumerate(lines):
            text = self.font_small.render(line, True, BLACK)
            self.screen.blit(text, (WINDOW_PADDING, matrix_y + i * 15))

    def screenshot(self, filepath: str):
        """截圖"""
        pygame.image.save(self.screen, filepath)

    def run(self):
        """遊戲主迴圈"""
        running = True
        waiting_for_spawn = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    elif event.key == pygame.K_l:
                        if waiting_for_spawn and self.robot is None:
                            direction = "W"
                            self.spawn_robot(0, 0, direction)
                            waiting_for_spawn = False
                        elif not waiting_for_spawn:
                            self.execute_command("L")

                    elif event.key == pygame.K_r:
                        if waiting_for_spawn and self.robot is None:
                            direction = "E"
                            self.spawn_robot(0, 0, direction)
                            waiting_for_spawn = False
                        elif not waiting_for_spawn:
                            self.execute_command("R")

                    elif event.key == pygame.K_f:
                        if waiting_for_spawn and self.robot is None:
                            direction = "N"
                            self.spawn_robot(0, 0, direction)
                            waiting_for_spawn = False
                        elif not waiting_for_spawn:
                            self.execute_command("F")

                    elif event.key == pygame.K_n:
                        waiting_for_spawn = False
                        self.spawn_random_robot()

                    elif event.key == pygame.K_c:
                        self.clear_scent()

                    elif event.key == pygame.K_g:
                        self.screenshot("assets/replay.png")
                        self.history.append("Screenshot saved!")

                    elif event.key in [
                        pygame.K_1,
                        pygame.K_2,
                        pygame.K_3,
                        pygame.K_4,
                        pygame.K_5,
                    ]:
                        if self.robot is None:
                            robot_num = event.key - pygame.K_1
                            self.spawn_robot(robot_num, 0, "N")
                            waiting_for_spawn = False

            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_coordinate()
            self.draw_scent()
            self.draw_robot()
            self.draw_info()
            self.draw_controls()
            self.draw_matrix()

            if waiting_for_spawn:
                hint = self.font_large.render("Press L/R/F to spawn robot", True, BLUE)
                self.screen.blit(hint, (WINDOW_PADDING, 20))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


def main():
    """主程式"""
    world_w, world_h = 5, 3
    if len(sys.argv) > 2:
        world_w, world_h = int(sys.argv[1]), int(sys.argv[2])

    game = RobotGame(world_w, world_h)
    game.run()


if __name__ == "__main__":
    main()
