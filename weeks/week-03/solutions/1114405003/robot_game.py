import os
import sys
import pygame
import time
from robot_core import RobotWorld

# 2D grid settings
CELL_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 10
WINDOW_MARGIN = 80
FPS = 60


def draw_grid(screen, grid_w, grid_h, margin):
    for x in range(grid_w + 1):
        pygame.draw.line(screen, (200, 200, 200), (margin + x * CELL_SIZE, margin),
                         (margin + x * CELL_SIZE, margin + grid_h * CELL_SIZE), 1)
    for y in range(grid_h + 1):
        pygame.draw.line(screen, (200, 200, 200), (margin, margin + y * CELL_SIZE),
                         (margin + grid_w * CELL_SIZE, margin + y * CELL_SIZE), 1)


def draw_scent(screen, scents, margin):
    for x, y, d in scents:
        cx = margin + x * CELL_SIZE + CELL_SIZE // 2
        cy = margin + (GRID_HEIGHT - y - 1) * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, (255, 0, 0), (cx, cy), CELL_SIZE // 6)


def draw_robot(screen, robot, margin):
    x, y, direction, lost = robot.state()
    if lost:
        color = (169, 169, 169)
    else:
        color = (0, 128, 255)
    cx = margin + x * CELL_SIZE + CELL_SIZE // 2
    cy = margin + (GRID_HEIGHT - y - 1) * CELL_SIZE + CELL_SIZE // 2
    half = CELL_SIZE // 3

    if direction == 'N':
        pts = [(cx, cy - half), (cx - half, cy + half), (cx + half, cy + half)]
    elif direction == 'S':
        pts = [(cx, cy + half), (cx - half, cy - half), (cx + half, cy - half)]
    elif direction == 'E':
        pts = [(cx + half, cy), (cx - half, cy - half), (cx - half, cy + half)]
    elif direction == 'W':
        pts = [(cx - half, cy), (cx + half, cy - half), (cx + half, cy + half)]
    else:
        pts = [(cx, cy)]

    pygame.draw.polygon(screen, color, pts)
    if lost:
        pygame.draw.circle(screen, (255, 0, 0), (cx, cy), 4)


def render_state(screen, world, robot, history):
    screen.fill((30, 30, 30))

    draw_grid(screen, GRID_WIDTH, GRID_HEIGHT, WINDOW_MARGIN)
    draw_scent(screen, world.scents, WINDOW_MARGIN)
    if robot is not None:
        draw_robot(screen, robot, WINDOW_MARGIN)

    font = pygame.font.SysFont('Consolas', 18)
    info_lines = [
        f"Position: {robot.x},{robot.y}  Dir: {robot.direction}" if robot else "No robot",
        f"LOST: {robot.lost if robot else 'N/A'}",
        f"Scent count: {len(world.scents)}",
        "Controls: L/R/F = move, N = new robot, C = clear scent, G = replay, ESC = quit",
        f"History: {len(history)} steps",
    ]
    for i, line in enumerate(info_lines):
        lbl = font.render(line, True, (220, 220, 220))
        screen.blit(lbl, (10, 10 + i * 22))

    pygame.display.flip()


def cycle_robot_states(screen, world_snapshot, robot_snapshot, history):
    # replay history in animation
    if not history:
        return
    for state in history:
        world = state['world']
        robot = state['robot']
        screen.fill((30, 30, 30))
        draw_grid(screen, GRID_WIDTH, GRID_HEIGHT, WINDOW_MARGIN)
        draw_scent(screen, world.scents, WINDOW_MARGIN)
        draw_robot(screen, robot, WINDOW_MARGIN)
        font = pygame.font.SysFont('Consolas', 18)
        label = font.render(f"Replay step {state['index']+1}/{len(history)}", True, (255, 255, 0))
        screen.blit(label, (10, 10))
        pygame.display.flip()
        pygame.time.delay(200)


def save_replay_gif(history):
    try:
        import imageio
    except ImportError:
        print("imageio not installed; cannot export GIF")
        return

    frames = []
    os.makedirs('assets', exist_ok=True)
    for state in history:
        world = state['world']
        robot = state['robot']
        surface = pygame.Surface((WINDOW_MARGIN * 2 + GRID_WIDTH * CELL_SIZE,
                                  WINDOW_MARGIN * 2 + GRID_HEIGHT * CELL_SIZE))
        surface.fill((30, 30, 30))
        draw_grid(surface, GRID_WIDTH, GRID_HEIGHT, WINDOW_MARGIN)
        draw_scent(surface, world.scents, WINDOW_MARGIN)
        draw_robot(surface, robot, WINDOW_MARGIN)
        data = pygame.image.tostring(surface, 'RGB')
        image = pygame.image.fromstring(data, surface.get_size(), 'RGB')
        arr = pygame.surfarray.array3d(image)
        arr = arr.transpose([1, 0, 2])
        frames.append(arr)

    out_path = os.path.join('assets', 'replay.gif')
    imageio.mimsave(out_path, frames, fps=5)
    print(f"Saved replay GIF: {out_path}")


def main():
    pygame.init()
    screen_w = WINDOW_MARGIN * 2 + CELL_SIZE * GRID_WIDTH
    screen_h = WINDOW_MARGIN * 2 + CELL_SIZE * GRID_HEIGHT
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption('Robot Scent Simulator')

    clock = pygame.time.Clock()
    world = RobotWorld(GRID_WIDTH - 1, GRID_HEIGHT - 1)
    robot = world.create_robot(0, 0, 'N')

    history = []

    def push_history(step):
        # snapshot
        history.append({
            'world': RobotWorld(world.max_x, world.max_y),
            'robot': world.create_robot(robot.x, robot.y, robot.direction) if robot else None,
            'index': len(history),
        })
        history[-1]['world'].scents = set(world.scents)
        if robot:
            history[-1]['robot'].x = robot.x
            history[-1]['robot'].y = robot.y
            history[-1]['robot'].direction = robot.direction
            history[-1]['robot'].lost = robot.lost

    push_history(0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                if event.key == pygame.K_l:
                    if robot and not robot.lost:
                        robot.turn_left()
                        push_history(1)
                elif event.key == pygame.K_r:
                    if robot and not robot.lost:
                        robot.turn_right()
                        push_history(1)
                elif event.key == pygame.K_f:
                    if robot and not robot.lost:
                        robot.move_forward()
                        push_history(1)
                elif event.key == pygame.K_n:
                    robot = world.create_robot(0, 0, 'N')
                    push_history(1)
                elif event.key == pygame.K_c:
                    world.scents.clear()
                    push_history(1)
                elif event.key == pygame.K_g:
                    cycle_robot_states(screen, world, robot, history)
                    save_replay_gif(history)

        render_state(screen, world, robot, history)
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
