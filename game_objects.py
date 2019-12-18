import pygame
import random
from settings import WIDHT, HEIGHT
import time
from math import pi


class Player(pygame. sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load('sprites/raketa.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDHT // 2
        self.rect.bottom = HEIGHT - 10


class Bullet(pygame. sprite.Sprite):
    def __init__(self, angle, imageInd, vel):
        super(Bullet, self).__init__()
        self.angle = angle
        self.imageInd = imageInd
        if imageInd == 1:
            self.image = pygame.image.load('sprites/enemyBullet.png')
        elif imageInd == 2:
            self.image = pygame.image.load('sprites/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 10
        self.vel = vel


class EnemyAircraft(pygame. sprite.Sprite):
    def __init__(self, angle, imageInd, vel):
        super(EnemyAircraft, self).__init__()
        self.angle = angle
        self.imageInd = imageInd
        if imageInd == 1:
            self.image = pygame.image.load(
                'sprites/enimeAircraft1.png')
        elif imageInd == 2:
            self.image = pygame.image.load(
                'sprites/enimeAircraft2.png')
        self.rect = self.image.get_rect()
        self.vel = vel
