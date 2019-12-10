import pygame
from settings import WIDHT, HEIGHT


class Player(pygame. sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load('sprites/raketa.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDHT // 2
        self.rect.bottom = HEIGHT - 10


class Bullet(pygame. sprite.Sprite):
    def __init__(self, image=pygame.image.load('sprites/bullet.png')):
        super(Bullet, self).__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 10


class EnemyAircraft(pygame. sprite.Sprite):
    def __init__(self, vel=1):
        super(EnemyAircraft, self).__init__()

        self.image = pygame.image.load('sprites/enimeAircraft.png')
        self.rect = self.image.get_rect()
        self.vel = vel
