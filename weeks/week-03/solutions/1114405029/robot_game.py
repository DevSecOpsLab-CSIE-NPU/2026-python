import os
import sys
import pygame

sys.path.append(os.path.dirname(__file__))

from robot_core import Robot, execute_instruction

# ===== 地圖設定 =====
MAP_W = 5
MAP_H = 5
CELL_SIZE = 80
MARGIN = 60

WINDOW_WIDTH = (MAP_W + 1) * CELL_SIZE + MARGIN * 2
WINDOW_HEIGHT = (MAP_H + 1) * CELL_SIZE + MARGIN * 2 + 120

# ===== 顏色 =====
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (210, 210, 210)
RED = (230, 50, 50)
GREEN = (70, 180, 90)
BLUE = (70, 130, 255)
YELLOW = (255, 220, 70)

# ===== 初始化 =====
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Robot Lost")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
small_font = pygame.font.SysFont(None, 22)

# ===== 載入圖片 =====
BASE_DIR = os.path.dirname(__file__)
ROBOT_IMAGE_PATH = os.path.join(BASE_DIR, "assets", "robot.png")
robot_img = pygame.image.load(ROBOT_IMAGE_PATH)
robot_img = pygame.transform.scale(robot_img, (60, 60))

# ===== 狀態 =====
robot = Robot(0, 0, "N")
scents = set()

# replay_frames 會記錄每一步操作後的狀態
replay_frames = []
replay_mode = False
replay_index = 0
replay_last_time = 0
REPLAY_INTERVAL_MS = 500


def make_snapshot(current_robot, current_scents):
    return {
        "x": current_robot.x,
        "y": current_robot.y,
        "direction": current_robot.direction,
        "lost": current_robot.lost,
        "scents": set(current_scents),
    }


def load_snapshot(snapshot):
    global robot, scents
    robot = Robot(snapshot["x"], snapshot["y"], snapshot["direction"], snapshot["lost"])
    scents = set(snapshot["scents"])


# 一開始先記錄初始狀態
replay_frames.append(make_snapshot(robot, scents))


def grid_to_screen(x, y):
    sx = MARGIN + x * CELL_SIZE
    sy = WINDOW_HEIGHT - 120 - MARGIN - y * CELL_SIZE
    return sx, sy


def draw_grid():
    for x in range(MAP_W + 1):
        for y in range(MAP_H + 1):
            sx, sy = grid_to_screen(x, y)
            rect = pygame.Rect(
                sx - CELL_SIZE // 2,
                sy - CELL_SIZE // 2,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, GRAY, rect, 1)

            coord_text = small_font.render(f"{x},{y}", True, BLACK)
            screen.blit(coord_text, (sx - 20, sy - 10))


def draw_scents():
    """
    將 scent 畫得更明顯：
    - 格子右上角
    - 大紅點
    - 黃色外框
    - 中間標示方向
    """
    for x, y, direction in scents:
        sx, sy = grid_to_screen(x, y)

        scent_pos = (sx + 22, sy - 22)

        # 黃色外圈
        pygame.draw.circle(screen, YELLOW, scent_pos, 14)

        # 紅色主體
        pygame.draw.circle(screen, RED, scent_pos, 11)

        # 黑色邊框
        pygame.draw.circle(screen, BLACK, scent_pos, 11, 2)

        # 方向字母
        d_text = small_font.render(direction, True, WHITE)
        screen.blit(d_text, (scent_pos[0] - 6, scent_pos[1] - 8))


def draw_robot(current_robot):
    # 如果機器人已經 LOST，就不要再畫出來
    if current_robot.lost:
        return

    sx, sy = grid_to_screen(current_robot.x, current_robot.y)

    if current_robot.direction == "N":
        angle = 0
    elif current_robot.direction == "E":
        angle = -90
    elif current_robot.direction == "S":
        angle = 180
    else:  # W
        angle = 90

    rotated_img = pygame.transform.rotate(robot_img, angle)
    rect = rotated_img.get_rect(center=(sx, sy))
    screen.blit(rotated_img, rect)


def draw_status(current_robot):
    status = f"Robot: ({current_robot.x}, {current_robot.y}) {current_robot.direction} | LOST: {current_robot.lost}"
    status_img = font.render(status, True, BLACK)
    screen.blit(status_img, (20, WINDOW_HEIGHT - 95))

    hint = "L=left  R=right  F=forward  N=new robot  C=clear scent  P=replay  ESC=quit"
    hint_img = small_font.render(hint, True, BLACK)
    screen.blit(hint_img, (20, WINDOW_HEIGHT - 55))

    scent_text = small_font.render(f"Scent count: {len(scents)}", True, GREEN)
    screen.blit(scent_text, (WINDOW_WIDTH - 170, WINDOW_HEIGHT - 95))

    if replay_mode:
        replay_text = small_font.render("REPLAY MODE", True, BLUE)
        screen.blit(replay_text, (WINDOW_WIDTH - 170, WINDOW_HEIGHT - 55))


def record_frame():
    replay_frames.append(make_snapshot(robot, scents))


def start_replay():
    global replay_mode, replay_index, replay_last_time

    if len(replay_frames) <= 1:
        return

    replay_mode = True
    replay_index = 0
    replay_last_time = pygame.time.get_ticks()
    load_snapshot(replay_frames[0])


def update_replay():
    global replay_mode, replay_index, replay_last_time

    if not replay_mode:
        return

    now = pygame.time.get_ticks()
    if now - replay_last_time >= REPLAY_INTERVAL_MS:
        replay_index += 1
        replay_last_time = now

        if replay_index >= len(replay_frames):
            replay_mode = False
            replay_index = len(replay_frames) - 1
            return

        load_snapshot(replay_frames[replay_index])


def main():
    global robot, scents, replay_mode

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # replay 中只允許結束，不做新操作
                if replay_mode:
                    continue

                elif event.key == pygame.K_l:
                    execute_instruction(robot, "L", MAP_W, MAP_H, scents)
                    record_frame()

                elif event.key == pygame.K_r:
                    execute_instruction(robot, "R", MAP_W, MAP_H, scents)
                    record_frame()

                elif event.key == pygame.K_f:
                    execute_instruction(robot, "F", MAP_W, MAP_H, scents)
                    record_frame()

                elif event.key == pygame.K_n:
                    robot = Robot(0, 0, "N")
                    record_frame()

                elif event.key == pygame.K_c:
                    scents.clear()
                    record_frame()

                elif event.key == pygame.K_p:
                    start_replay()

        update_replay()

        screen.fill(WHITE)
        draw_grid()
        draw_scents()
        draw_robot(robot)
        draw_status(robot)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()