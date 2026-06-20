import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
import sys
sys.path.insert(0, os.path.dirname(__file__))
from app import BigTwoApp

app = BigTwoApp()
app.render()
pygame.image.save(app.screen, os.path.join(os.path.dirname(__file__), "gameplay.png"))
print("Screenshot saved to gameplay.png")
pygame.quit()
