import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
import sys
sys.path.insert(0, os.path.dirname(__file__))
from robot_game import RobotGame, W, H

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((W, H))

game = RobotGame(5, 5)
game.new_robot()
for cmd in ["F", "F", "F", "F", "F", "F"]:
    game.run_cmd(cmd)
game.new_robot()
for cmd in ["R", "F", "F"]:
    game.run_cmd(cmd)
game.draw(screen)
out = os.path.join(os.path.dirname(__file__), "gameplay.png")
pygame.image.save(screen, out)
print("Screenshot saved to gameplay.png")

game.export_gif(screen, "replay.gif")
pygame.quit()
