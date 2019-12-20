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
    def __init__(self, angle, imageInd, vel, rot_speed=0, render_rot=0):
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
        self.rot_speed = rot_speed
        self.image_copy = self.image.copy()
        self.last_update = pygame.time.get_ticks()
        self.render_rot = render_rot

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.render_rot:
            self.last_update = now
            self.angle = (self.angle + self.rot_speed) % 360
            new_image = pygame.transform.rotate(
                self.image_copy, self.angle)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


class Heart(pygame. sprite.Sprite):
    def __init__(self, staff2):
        super(Heart, self).__init__()
        self.image = pygame.image.load('sprites/heart.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDHT - 25 - staff2*35, 25)


class Coin(pygame. sprite.Sprite):
    def __init__(self, numberCoinImg, imageInd=1):
        super(Coin, self).__init__()
        self.numberCoinImg = numberCoinImg
        self.image = pygame.image.load(
            'sprites/coin'+str(imageInd)+'/coin'+str(numberCoinImg)+'.png')
        self.rect = self.image.get_rect()
        self.imageInd = imageInd
