"""A simple pygame interface for the Robot Lost core logic.

This file provides a minimal playable surface so that human testers can
move the robot around, observe scents, and reset/clear.  It satisfies the
MVP requirements described in HOMEWORK.md.

Controls:
    L / R / F : turn left, turn right, move forward
    N         : spawn a new robot at origin facing north (0,0,N)
    C         : clear all scents on the grid
    G         : replay the recorded moves (see notes below)
    ESC / QUIT: exit the game

Usage:
    python -m pip install pygame
    python robot_game.py

The grid size is hardcoded to 5x3 for demonstration but can be changed
by editing the GRID_WIDTH/GIRD_HEIGHT constants.

For simplicity the replay mechanism just stores snapshots of each step and
plays them back when G is pressed; it does not yet export a GIF file.
"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys
import traceback
from copy import deepcopy

import robot_core

# constants
CELL_SIZE = 40
MARGIN = 20
GRID_WIDTH = 5
GRID_HEIGHT = 3
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE + MARGIN * 2
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + MARGIN * 2

# colors
BG_COLOR = (30, 30, 30)
GRID_COLOR = (200, 200, 200)
ROBOT_COLOR = (200, 50, 50)
SCENT_COLOR = (50, 200, 50)


def draw_grid(surface, grid: robot_core.Grid):
    for x in range(GRID_WIDTH + 1):
        pygame.draw.line(surface, GRID_COLOR,
                         (MARGIN + x * CELL_SIZE, MARGIN),
                         (MARGIN + x * CELL_SIZE, MARGIN + GRID_HEIGHT * CELL_SIZE))
    for y in range(GRID_HEIGHT + 1):
        pygame.draw.line(surface, GRID_COLOR,
                         (MARGIN, MARGIN + y * CELL_SIZE),
                         (MARGIN + GRID_WIDTH * CELL_SIZE, MARGIN + y * CELL_SIZE))
    # draw scents as small dots
    for (sx, sy, sdir) in grid.scents:
        cx = MARGIN + sx * CELL_SIZE + CELL_SIZE // 2
        cy = MARGIN + (GRID_HEIGHT - sy) * CELL_SIZE - CELL_SIZE // 2
        pygame.draw.circle(surface, SCENT_COLOR, (cx, cy), 5)


def draw_robot(surface, robot: robot_core.Robot):
    # convert logical coordinates to screen
    cx = MARGIN + robot.x * CELL_SIZE + CELL_SIZE // 2
    cy = MARGIN + (GRID_HEIGHT - robot.y) * CELL_SIZE - CELL_SIZE // 2
    # draw triangle pointing in robot.dir
    size = CELL_SIZE // 3
    if robot.dir == "N":
        points = [(cx, cy - size), (cx - size, cy + size), (cx + size, cy + size)]
    elif robot.dir == "S":
        points = [(cx, cy + size), (cx - size, cy - size), (cx + size, cy - size)]
    elif robot.dir == "E":
        points = [(cx + size, cy), (cx - size, cy - size), (cx - size, cy + size)]
    elif robot.dir == "W":
        points = [(cx - size, cy), (cx + size, cy - size), (cx + size, cy + size)]
    pygame.draw.polygon(surface, ROBOT_COLOR, points)


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Robot Lost")
        print(f"[INFO] Window created: {WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        clock = pygame.time.Clock()
    except Exception as e:
        print(f"[ERROR] Failed to initialize pygame: {e}")
        traceback.print_exc()
        sys.exit(1)

    grid = robot_core.Grid(GRID_WIDTH, GRID_HEIGHT)
    robot = robot_core.Robot(0, 0, "N")
    history = []  # store snapshots of (robot, scents)

    def record():
        # store deep copy of state for replay
        history.append((deepcopy(robot), deepcopy(grid.scents)))

    record()

    replaying = False
    replay_index = 0

    print("[INFO] Game loop started. Controls: L=left, R=right, F=forward, N=new, C=clear, G=replay, ESC=quit")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("[INFO] Quit event received")
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not replaying:
                key = event.key
                if key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif key == pygame.K_l:
                    grid.execute(robot, "L")
                    record()
                elif key == pygame.K_r:
                    grid.execute(robot, "R")
                    record()
                elif key == pygame.K_f:
                    grid.execute(robot, "F")
                    record()
                elif key == pygame.K_n:
                    robot = robot_core.Robot(0, 0, "N")
                    record()
                elif key == pygame.K_c:
                    grid.scents.clear()
                    record()
                elif key == pygame.K_g:
                    # start replay
                    if history:
                        replaying = True
                        replay_index = 0
        if replaying:
            # show next frame, pause a bit
            robot, grid.scents = deepcopy(history[replay_index])
            replay_index += 1
            if replay_index >= len(history):
                replaying = False

        screen.fill(BG_COLOR)
        draw_grid(screen, grid)
        if not robot.lost:
            draw_robot(screen, robot)
        # display status text
        try:
            font = pygame.font.SysFont(None, 24)
            txt = f"({robot.x},{robot.y},{robot.dir}){' LOST' if robot.lost else ''}" if robot else ""
            screen.blit(font.render(txt, True, (255,255,255)), (MARGIN, WINDOW_HEIGHT - MARGIN))
            pygame.display.flip()
        except Exception as e:
            print(f"[ERROR] Render failed: {e}")
            break
        clock.tick(10)

if __name__ == "__main__":
    print("[INFO] Starting Robot Lost game...")
    try:
        main()
    except Exception as e:
        print(f"[ERROR] Game crashed: {e}")
        traceback.print_exc()
