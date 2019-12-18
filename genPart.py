import os
import pygame
import random
import time
from settings import SIZE, WHITE, HEIGHT, WIDHT, BGCOLOR
from game_objects import Player, Bullet, EnemyAircraft
from math import pi, cos, sin

global pause
pause = False


def pausedddd():
    global pause
    keys = pygame.key.get_pressed()
    while pause:
        for event in events:
            if event.type == pygame.QUIT:
                os.sys.exit()
            if keys[pygame.K_e]:
                os.sys.exit()
        go_font = pygame.font.SysFont('monaco', 72)
        red = pygame.Color(255, 0, 0)
        go_surf = go_font.render(' Paused', True, red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (125, 200)
        play_surface = pygame.display.set_mode((
            500, 650))
        pygame.display.set_caption('Shooter')
        play_surface.blit(go_surf, go_rect.midtop)
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pause = False
        pygame.display.update()

# функция обновления экрана


def drawWindow(win, bgCadr, numberbgCadr, playerBullets, enemies, enemiesBullets, exampleEnemy, player):
    bg = pygame.image.load(bgCadr(numberbgCadr))
    win.blit(bg, (0, 0))
    for playerBullet in playerBullets:
        win.blit(playerBullet.image, playerBullet.rect)
    for enemy in enemies:
        enemyBullets = enemiesBullets[enemies.index(enemy)]
        for enemyBullet in enemyBullets:
            win.blit(enemyBullet.image, enemyBullet.rect)
        if type(enemy) == type(exampleEnemy):
            win.blit(enemy.image, enemy.rect)
    win.blit(player.image, player.rect)
    pygame.display.update()


def bgCadr(i):
    i = str(i)
    while len(i) < 4:
        i = '0' + i
    return('bg/Видеофон Звёздное небо ' + i+'.jpg')

# ___________________________________________


def generalPart(player, playerBullets, enemies, enemiesBullets, exampleEnemy, constantShooting, intervalPlayerSnaryad, intervalEnemySnaryad, win, numberbgCadr, playerTimerSnaryad, mouseCoords, lastEvent):

    intervalPlayerSnaryad += 1
    intervalEnemySnaryad += 1

    # счетчик для анимированного фона
    if numberbgCadr < 7325:
        numberbgCadr += 1
    else:
        numberbgCadr = 0

    # двигаю снаряды врагов и удаляю улетевшие
    for enemy in enemies:
        enemyBullets = enemiesBullets[enemies.index(enemy)]
        for enemyBullet in enemyBullets:
            if enemyBullet.rect.centery < HEIGHT and enemyBullet.rect.centery >= 0 and type(enemy) == type(exampleEnemy):
                enemyBullet.rect.centery += (enemy.vel + enemyBullet.vel) * \
                    (-round(sin(enemyBullet.angle), 3))
                # enemyBullet.rect.bottom += enemyBullet.vel*(-sin(enemy.Bullet.angle*pi/180)) + delta*3
                enemyBullet.rect.centerx += (enemy.vel + enemyBullet.vel) * \
                    (round(cos(enemyBullet.angle), 3))
            else:
                # удалил снаряд с индексом, который вылетел за границы
                enemyBullets.pop(enemyBullets.index(enemyBullet))

    # двигаю снаряды игрока и удаляю улетевшие
    for playerBullet in playerBullets:
        if playerBullet.rect.centery < HEIGHT and playerBullet.rect.centery > 0:
            delta = round(random.random())
            playerBullet.rect.centery -= playerBullet.vel + delta*3
            playerBullet.rect.bottom -= playerBullet.vel + delta*3
        else:
            # удалил снаряд с индексом, который вылетел за границы
            playerBullets.pop(playerBullets.index(playerBullet))

    # обработка некоторых клавиш (выхода и постоянной стрельбы)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            os.sys.exit()
        if keys[pygame.K_e]:
            os.sys.exit(0)
        if keys[pygame.K_c] and event.type == pygame.KEYUP:
            constantShooting *= -1
    if len(events) > 0:
        lastEvent = event
    # движение игрока за стрелкой
    if lastEvent.type == pygame.MOUSEMOTION and type(lastEvent) != type(int(3)):
        [player.rect.centerx, player.rect.centery] = lastEvent.pos
        mouseCoords = lastEvent.pos
    if keys[pygame.K_o]:
        pause = True
        pausedddd()

    # обработка поражения игрока пулями
    for enemy in enemies:
        enemyBullets = enemiesBullets[enemies.index(enemy)]
        enemyBulletsGroup = pygame.sprite.Group(enemyBullets)
        playerBulletsGroup = pygame.sprite.Group(player)
        hits = pygame.sprite.groupcollide(
            enemyBulletsGroup, playerBulletsGroup, True, True)
        for hit in hits:
            if hit:
                enemyBullets.pop(enemyBullets.index(hit))
                # уничтожение пули

                player_live -= 1
                if player_live < 0:
                    time.sleep(0)
                    print('Game over')
                    print(player_live)
                    game_over()
    # стрельба игрока
    if lastEvent.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_f] or constantShooting > 0:
        if playerTimerSnaryad == True and len(playerBullets) > 0:
            playerBullets.append(Bullet(pi/2, 2, 20))
            playerBullets[len(
                playerBullets) - 1].rect.centerx = mouseCoords[0] - rightleftGun
            playerBullets[len(playerBullets) -
                          1].rect.centery = mouseCoords[1]
            rightleftGun *= -1
            playerTimerSnaryad = False

    # проверка счетчика интервала между пулями
    if intervalPlayerSnaryad >= 2:
        playerTimerSnaryad = True
        intervalPlayerSnaryad = 0
    if intervalEnemySnaryad >= 60:
        enemiesTimerSnaryad = True
        intervalEnemySnaryad = 0

    drawWindow(win, bgCadr, numberbgCadr,
               playerBullets, enemies, enemiesBullets, exampleEnemy, player)
