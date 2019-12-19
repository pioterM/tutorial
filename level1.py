import os
import pygame
import random
import time
from settings import SIZE, WHITE, HEIGHT, WIDHT, BGCOLOR
from game_objects import Player, Bullet, EnemyAircraft
from math import pi, cos, sin
import genPart


def level11(win):
    print("rmervmeivmiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

    player = Player()

    enemies = []
    exampleEnemy = EnemyAircraft(3*pi/2, 1, 1)
    enemiesBullets = []
    for e in range(3):
        enemies.append(EnemyAircraft(3*pi/2, 1, 1))
        enemiesBullets.append([])
    enemies[1].vel = 2

    [enemies[0].rect.centerx, enemies[0].rect.centery] = [WIDHT // 4, -10]
    [enemies[1].rect.centerx, enemies[1].rect.centery] = [WIDHT // 2, -10]
    [enemies[2].rect.centerx, enemies[2].rect.centery] = [WIDHT*3 // 4, -10]

    playerBullets = []
    numberbgCadr = 0
    intervalPlayerSnaryad = 0
    intervalEnemySnaryad = 0
    playerTimerSnaryad = True
    enemiesTimerSnaryad = True
    mouseCoords = []
    clock = pygame.time.Clock()
    rightleftGun = 30
    constantShooting = -1
    global player_live
    player_live = 3
    lastEvent = 0

    # ____________________________________
    def game_over():
        """Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры"""
        go_font = pygame.font.SysFont('monaco', 72)
        red = pygame.Color(255, 0, 0)
        go_surf = go_font.render('Game over', True, red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (125, 200)
        play_surface = pygame.display.set_mode((
            500, 650))
        pygame.display.set_caption('Shooter')
        play_surface.blit(go_surf, go_rect.midtop)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        os.sys.exit()


    # функция получения названия картинки фона по номеру
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play()

    sound1 = pygame.mixer.Sound('music.wav')
    while True:
        clock.tick(45)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYUP:
                if i.key == pygame.K_1:
                    pygame.mixer.music.pause()
                    sound1.play()
                    # pygame.mixer.music.stop()
                elif i.key == pygame.K_2:
                    pygame.mixer.music.unpause()
                    sound1.stop()
                    # pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                elif i.key == pygame.K_3:
                    pygame.mixer.music.unpause()
                    # pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(1)
            # elif i.type == pygame.MOUSEBUTTONUP:
            #     if i.button == 1:
            #         sound1.play()
            #     elif i.button==2:
            #         sound1.stop()
        pygame.time.delay(20)
        #pygame.mixer.music.load('Test.mp3')
        #pygame.mixer.music.play()


        # UPDATE  - -- -- - -- движение врагов
        for enemy in enemies:
            if type(enemy) == type(exampleEnemy):
                enemy.rect.centery += enemy.vel * \
                    (-sin(enemy.angle))
                enemy.rect.centerx += enemy.vel*cos(enemy.angle)
                # обработка столкновения врагов с игроком
                distance = (enemy.rect.centerx - player.rect.centerx)**2 + \
                    (enemy.rect.centery - player.rect.centery)**2
                if distance <= 25**2:
                    time.sleep(0)
                    print('Game over')
                    print(player_live)
                    game_over()
                    # os.sys.exit(0)

        # UPDATE - СОЗДАНИЕ ПУЛЬ  стрельба врагов
        if enemiesTimerSnaryad == True:
            for enemy in enemies:
                if type(enemy) == type(exampleEnemy):
                    enemyBullets = enemiesBullets[enemies.index(
                        enemy)]
                    enemyBullets.append(
                        Bullet(enemy.angle, 1, 3))
                    enemyBullets[len(enemyBullets) -
                                 1].rect.centerx = enemy.rect.centerx
                    enemyBullets[len(enemyBullets) -
                                 1].rect.centery = enemy.rect.centery
            enemiesTimerSnaryad = False

        # обработка поражения врагов пулями
        realEnemies = []
        for enemy in enemies:
            if type(enemy) == type(exampleEnemy):
                realEnemies.append(enemy)
        enemiesGroup = pygame.sprite.Group(realEnemies)
        playerBulletsGroup = pygame.sprite.Group(playerBullets)
        hits = pygame.sprite.groupcollide(
            enemiesGroup, playerBulletsGroup, True, True)
        for hit in hits:
            if hit:
                enemies[enemies.index(hit)] = 0
        genPart.generalPart(player, playerBullets, enemies, enemiesBullets, exampleEnemy,
                            constantShooting, intervalPlayerSnaryad, intervalEnemySnaryad, win, numberbgCadr, playerTimerSnaryad, mouseCoords, lastEvent)
