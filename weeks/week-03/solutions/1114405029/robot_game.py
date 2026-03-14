import os
import sys
import pygame
import imageio

sys.path.append(os.path.dirname(__file__))

from robot_core import Robot, execute_instruction

# ===== 地圖設定 =====
MAP_W = 5
MAP_H = 5
MARGIN = 20
BOTTOM_PANEL_HEIGHT = 150
SIDE_PANEL_MIN_WIDTH = 320

# 固定視窗大小
WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 680

# ===== 顏色 =====
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (210, 210, 210)
RED = (230, 50, 50)
GREEN = (70, 180, 90)
BLUE = (70, 130, 255)
YELLOW = (255, 220, 70)
LIGHT_BLUE = (235, 245, 255)

# ===== 初始化 =====
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Robot Lost")
clock = pygame.time.Clock()

font = pygame.font.SysFont("microsoftjhenghei", 28)
small_font = pygame.font.SysFont("microsoftjhenghei", 22)
tiny_font = pygame.font.SysFont("microsoftjhenghei", 20)
scent_font = pygame.font.SysFont("arial", 20, bold=True)

# ===== 載入圖片 =====
BASE_DIR = os.path.dirname(__file__)
ROBOT_IMAGE_PATH = os.path.join(BASE_DIR, "assets", "robot.png")
robot_img_original = pygame.image.load(ROBOT_IMAGE_PATH)

# ===== 狀態 =====
robot = Robot(0, 0, "N")
scents = set()

replay_frames = []
replay_mode = False
replay_index = 0
replay_last_time = 0
REPLAY_INTERVAL_MS = 500

# 使用者按鍵紀錄
command_history = ""


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


replay_frames.append(make_snapshot(robot, scents))


def get_layout():
    """
    固定視窗下的版面配置
    """
    status_top = WINDOW_HEIGHT - BOTTOM_PANEL_HEIGHT
    usable_height = status_top - MARGIN * 2
    usable_width = WINDOW_WIDTH - MARGIN * 3 - SIDE_PANEL_MIN_WIDTH

    grid_size = min(usable_height, usable_width)
    grid_size = max(grid_size, 360)

    cell_size = grid_size // (MAP_W + 1)
    cell_size = max(cell_size, 45)

    grid_width = cell_size * (MAP_W + 1)
    grid_height = cell_size * (MAP_H + 1)

    grid_left = MARGIN
    grid_top = MARGIN

    side_x = grid_left + grid_width + MARGIN
    side_y = MARGIN
    side_w = WINDOW_WIDTH - side_x - MARGIN
    side_h = status_top - MARGIN * 2

    return {
        "cell_size": cell_size,
        "grid_left": grid_left,
        "grid_top": grid_top,
        "grid_width": grid_width,
        "grid_height": grid_height,
        "side_x": side_x,
        "side_y": side_y,
        "side_w": side_w,
        "side_h": side_h,
        "status_top": status_top,
    }


def grid_to_screen(x, y):
    layout = get_layout()
    cell_size = layout["cell_size"]
    sx = layout["grid_left"] + x * cell_size + cell_size // 2
    sy = layout["grid_top"] + (MAP_H - y) * cell_size + cell_size // 2
    return sx, sy


def draw_grid():
    layout = get_layout()
    cell_size = layout["cell_size"]

    for x in range(MAP_W + 1):
        for y in range(MAP_H + 1):
            sx, sy = grid_to_screen(x, y)
            rect = pygame.Rect(
                sx - cell_size // 2,
                sy - cell_size // 2,
                cell_size,
                cell_size
            )
            pygame.draw.rect(screen, GRAY, rect, 1)

            coord_text = small_font.render(f"{x},{y}", True, BLACK)
            text_rect = coord_text.get_rect(center=(sx, sy))
            screen.blit(coord_text, text_rect)


def draw_scents():
    layout = get_layout()
    cell_size = layout["cell_size"]

    for x, y, direction in scents:
        sx, sy = grid_to_screen(x, y)
        scent_pos = (sx + cell_size // 4, sy - cell_size // 4)

        outer_r = max(10, cell_size // 6 + 2)
        inner_r = max(8, cell_size // 7 + 2)

        pygame.draw.circle(screen, YELLOW, scent_pos, outer_r)
        pygame.draw.circle(screen, RED, scent_pos, inner_r)
        pygame.draw.circle(screen, BLACK, scent_pos, inner_r, 2)

        d_text = scent_font.render(direction, True, BLACK)
        text_rect = d_text.get_rect(center=scent_pos)
        screen.blit(d_text, text_rect)


def draw_robot(current_robot):
    if current_robot.lost:
        return

    layout = get_layout()
    cell_size = layout["cell_size"]

    sx, sy = grid_to_screen(current_robot.x, current_robot.y)

    if current_robot.direction == "N":
        angle = 0
    elif current_robot.direction == "E":
        angle = -90
    elif current_robot.direction == "S":
        angle = 180
    else:
        angle = 90

    robot_size = max(36, int(cell_size * 0.75))
    robot_img = pygame.transform.scale(robot_img_original, (robot_size, robot_size))
    rotated_img = pygame.transform.rotate(robot_img, angle)
    rect = rotated_img.get_rect(center=(sx, sy))
    screen.blit(rotated_img, rect)


def get_grid_snapshot(current_robot, current_scents, width=10, height=10):
    grid = [["." for _ in range(width)] for _ in range(height)]

    for x, y, direction in current_scents:
        if 0 <= x < width and 0 <= y < height:
            grid[height - 1 - y][x] = "S"

    if 0 <= current_robot.x < width and 0 <= current_robot.y < height:
        if current_robot.lost:
            grid[height - 1 - current_robot.y][current_robot.x] = "X"
        else:
            grid[height - 1 - current_robot.y][current_robot.x] = current_robot.direction

    return grid


def draw_side_panel(current_robot):
    layout = get_layout()
    panel_x = layout["side_x"]
    panel_y = layout["side_y"]
    panel_w = layout["side_w"]
    panel_h = layout["side_h"]

    pygame.draw.rect(screen, LIGHT_BLUE, (panel_x, panel_y, panel_w, panel_h))
    pygame.draw.rect(screen, BLACK, (panel_x, panel_y, panel_w, panel_h), 2)

    title = font.render("10x10 字串矩陣", True, BLACK)
    screen.blit(title, (panel_x + 15, panel_y + 15))

    snapshot = get_grid_snapshot(current_robot, scents, 10, 10)

    start_y = panel_y + 60
    for i, row in enumerate(snapshot):
        row_text = " ".join(row)
        img = tiny_font.render(row_text, True, BLACK)
        screen.blit(img, (panel_x + 15, start_y + i * 24))

    scent_title = small_font.render("scent 容器內容：", True, BLACK)
    screen.blit(scent_title, (panel_x + 15, start_y + 10 * 24 + 20))

    scent_list = sorted(list(scents))
    if not scent_list:
        empty_text = tiny_font.render("[]", True, BLACK)
        screen.blit(empty_text, (panel_x + 15, start_y + 10 * 24 + 50))
    else:
        for idx, item in enumerate(scent_list[:8]):
            line = tiny_font.render(str(item), True, BLACK)
            screen.blit(line, (panel_x + 15, start_y + 10 * 24 + 50 + idx * 24))

    legend_y = panel_y + panel_h - 120
    legends = [
        ". = 空格",
        "S = scent",
        "N/E/S/W = 機器人方向",
        "X = LOST 位置",
    ]
    for i, text in enumerate(legends):
        img = tiny_font.render(text, True, BLACK)
        screen.blit(img, (panel_x + 15, legend_y + i * 24))


def draw_status(current_robot):
    layout = get_layout()
    base_y = layout["status_top"] + 10

    status_text = (
        f"位置: ({current_robot.x}, {current_robot.y})   "
        f"方向: {current_robot.direction}   "
        f"狀態: {'LOST' if current_robot.lost else '正常'}"
    )
    status_img = font.render(status_text, True, BLACK)
    screen.blit(status_img, (20, base_y))

    hint_line_1 = "操作: L左轉  R右轉  F前進  N新機器人"
    hint_line_2 = "      C清除scent  P重播  G輸出GIF  ESC離開"

    hint_img_1 = small_font.render(hint_line_1, True, BLACK)
    hint_img_2 = small_font.render(hint_line_2, True, BLACK)
    screen.blit(hint_img_1, (20, base_y + 38))
    screen.blit(hint_img_2, (20, base_y + 66))

    history_show = command_history[-30:] if command_history else "（尚無）"
    history_text = small_font.render(f"指令紀錄: {history_show}", True, BLUE)
    screen.blit(history_text, (20, base_y + 98))

    scent_text = small_font.render(f"scent 數量: {len(scents)}", True, GREEN)
    screen.blit(scent_text, (WINDOW_WIDTH - 250, base_y))

    if replay_mode:
        replay_text = small_font.render("重播模式中", True, BLUE)
        screen.blit(replay_text, (WINDOW_WIDTH - 250, base_y + 34))


def record_frame():
    replay_frames.append(make_snapshot(robot, scents))


def add_command_history(command):
    global command_history
    command_history += command


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
            load_snapshot(replay_frames[-1])
            return

        load_snapshot(replay_frames[replay_index])


def render_current_frame(current_robot):
    screen.fill(WHITE)
    draw_grid()
    draw_scents()
    draw_robot(current_robot)
    draw_status(current_robot)
    draw_side_panel(current_robot)


def export_replay_gif():
    global robot, scents

    if len(replay_frames) <= 1:
        print("沒有足夠的重播畫面可輸出 GIF")
        return

    saved_robot = make_snapshot(robot, scents)
    frames = []

    for snapshot in replay_frames:
        load_snapshot(snapshot)
        render_current_frame(robot)
        pygame.display.flip()

        frame = pygame.surfarray.array3d(screen)
        frame = frame.swapaxes(0, 1)
        frames.append(frame)

    gif_path = os.path.join(BASE_DIR, "assets", "replay.gif")
    imageio.mimsave(gif_path, frames, duration=0.5)

    load_snapshot(saved_robot)
    print("GIF 已儲存：", gif_path)


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

                if replay_mode:
                    continue

                elif event.key == pygame.K_l:
                    execute_instruction(robot, "L", MAP_W, MAP_H, scents)
                    add_command_history("L")
                    record_frame()

                elif event.key == pygame.K_r:
                    execute_instruction(robot, "R", MAP_W, MAP_H, scents)
                    add_command_history("R")
                    record_frame()

                elif event.key == pygame.K_f:
                    execute_instruction(robot, "F", MAP_W, MAP_H, scents)
                    add_command_history("F")
                    record_frame()

                elif event.key == pygame.K_n:
                    robot = Robot(0, 0, "N")
                    add_command_history("N")
                    record_frame()

                elif event.key == pygame.K_c:
                    scents.clear()
                    add_command_history("C")
                    record_frame()

                elif event.key == pygame.K_p:
                    add_command_history("P")
                    start_replay()

                elif event.key == pygame.K_g:
                    add_command_history("G")
                    export_replay_gif()

        update_replay()

        render_current_frame(robot)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()