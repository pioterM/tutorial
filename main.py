import os
import pygame
import random
import time
import level1
from settings import SIZE, WHITE, HEIGHT, WIDHT, BGCOLOR
from game_objects import Player, Bullet, EnemyAircraft


os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
game_over = False
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Shooter")

# _________________________________________________________________
level1.level11(win)
# ______________________________________________________________________
