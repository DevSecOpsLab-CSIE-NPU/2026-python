import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
import sys
sys.path.insert(0, os.path.dirname(__file__))
from robot_game import RobotGame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 600))

game = RobotGame(5, 5)
game.new_robot()
for cmd in ["R", "F", "F", "R", "F", "L", "F"]:
    game.run_cmd(cmd)
game.draw(screen)
out = os.path.join(os.path.dirname(__file__), "assets", "gameplay.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
pygame.image.save(screen, out)
print("Screenshot saved to assets/gameplay.png")

game.export_gif(screen, "assets/replay.gif")
pygame.quit()
