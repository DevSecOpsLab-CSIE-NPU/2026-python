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
game.run_cmd("R")
game.run_cmd("F")
game.run_cmd("F")
game.run_cmd("R")
game.run_cmd("F")
game.run_cmd("L")
game.run_cmd("F")
game.draw(screen)
pygame.image.save(screen, os.path.join(os.path.dirname(__file__), "assets", "gameplay.png"))
print("Screenshot saved to assets/gameplay.png")
pygame.quit()
