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
    def __init__(self, imageInd, vel=1):
        super(EnemyAircraft, self).__init__()
        self.imageInd = imageInd
        if imageInd == 1:
            self.image = pygame.image.load(
                'sprites/enimeAircraft1.png')
        elif imageInd == 2:
            self.image = pygame.image.load(
                'sprites/enimeAircraft2.png')
        self.rect = self.image.get_rect()
        self.vel = vel
