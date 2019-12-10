import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((350, 200))

pygame.time.wait(3000)
pygame.quit()
