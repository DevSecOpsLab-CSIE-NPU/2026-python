import pygame
import sys
import os
from collections import deque
import imageio

# 初始化 pygame
pygame.init()

# 常數
CELL_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 10
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + 100  # 額外空間給按鈕或文字

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 方向映射
DIRECTIONS = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

TURN_LEFT = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
TURN_RIGHT = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.lost = False

    def turn_left(self):
        self.direction = TURN_LEFT[self.direction]

    def turn_right(self):
        self.direction = TURN_RIGHT[self.direction]

    def move_forward(self, grid_width, grid_height, scents):
        if self.lost:
            return
        dx, dy = DIRECTIONS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x < 0 or new_x > grid_width or new_y < 0 or new_y > grid_height:
            # 檢查 scent
            if (self.x, self.y, self.direction) not in scents:
                self.lost = True
                scents.add((self.x, self.y, self.direction))
            # 如果有 scent，不移動
        else:
            self.x = new_x
            self.y = new_y

def draw_grid(screen, grid_width, grid_height):
    for x in range(grid_width + 1):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, grid_height * CELL_SIZE))
    for y in range(grid_height + 1):
        pygame.draw.line(screen, BLACK, (0, y * CELL_SIZE), (grid_width * CELL_SIZE, y * CELL_SIZE))

def draw_robot(screen, robot):
    if robot.lost:
        color = RED
    else:
        color = BLUE
    center_x = robot.x * CELL_SIZE + CELL_SIZE // 2
    center_y = robot.y * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, color, (center_x, center_y), CELL_SIZE // 4)
    # 畫箭頭表示方向
    if robot.direction == 'N':
        pygame.draw.polygon(screen, color, [(center_x, center_y - 10), (center_x - 5, center_y + 5), (center_x + 5, center_y + 5)])
    elif robot.direction == 'S':
        pygame.draw.polygon(screen, color, [(center_x, center_y + 10), (center_x - 5, center_y - 5), (center_x + 5, center_y - 5)])
    elif robot.direction == 'E':
        pygame.draw.polygon(screen, color, [(center_x + 10, center_y), (center_x - 5, center_y - 5), (center_x - 5, center_y + 5)])
    elif robot.direction == 'W':
        pygame.draw.polygon(screen, color, [(center_x - 10, center_y), (center_x + 5, center_y - 5), (center_x + 5, center_y + 5)])

def draw_scents(screen, scents):
    for x, y, dir in scents:
        center_x = x * CELL_SIZE + CELL_SIZE // 2
        center_y = y * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, GREEN, (center_x, center_y), 5)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Robot Game")
    clock = pygame.time.Clock()

    robot = Robot(0, 0, 'N')
    scents = set()
    replay_frames = []

    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen, GRID_WIDTH, GRID_HEIGHT)
        draw_scents(screen, scents)
        draw_robot(screen, robot)

        # 顯示文字
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Position: ({robot.x}, {robot.y}) Direction: {robot.direction} Lost: {robot.lost}", True, BLACK)
        screen.blit(text, (10, GRID_HEIGHT * CELL_SIZE + 10))

        pygame.display.flip()

        # 捕捉幀給回放
        frame = pygame.surfarray.array3d(screen)
        frame = frame.transpose([1, 0, 2])  # 轉換為 imageio 格式
        replay_frames.append(frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_l:
                    robot.turn_left()
                elif event.key == pygame.K_r:
                    robot.turn_right()
                elif event.key == pygame.K_f:
                    robot.move_forward(GRID_WIDTH, GRID_HEIGHT, scents)
                elif event.key == pygame.K_n:
                    robot = Robot(0, 0, 'N')  # 新機器人
                elif event.key == pygame.K_c:
                    scents.clear()
                elif event.key == pygame.K_g:
                    # 生成 GIF
                    if replay_frames:
                        imageio.mimsave('replay.gif', replay_frames, fps=10)
                        print("Replay GIF saved as replay.gif")

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
