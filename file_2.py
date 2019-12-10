import os
import pygame
import random
import time
from settings import SIZE, WHITE, HEIGHT, WIDHT, BGCOLOR
from game_objects import Player, Bullet, EnemyAircraft

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello, World!")

player = Player()

enemies = []
exampleEnemy = EnemyAircraft()
enemiesBullets = []
for e in range(3):
    enemies.append(EnemyAircraft())
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

# функция получения названия картинки фона по номеру


def bgCadr(i):
    i = str(i)
    while len(i) < 4:
        i = '0' + i
    return('bg/Видеофон Звёздное небо ' + i+'.jpg')


# функция обновления экрана
def drawWindow():
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


while True:
    clock.tick(120)
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
            if enemyBullet.rect.centery < HEIGHT and enemyBullet.rect.centery > 0:
                delta = random.random()
                enemyBullet.rect.centery += 1 + delta*3
                enemyBullet.rect.bottom += 1 + delta*3
            else:
                # удалил снаряд с индексом, который вылетел за границы
                enemyBullets.pop(enemyBullets.index(enemyBullet))

    # двигаю снаряды игрока и удаляю улетевшие
    for playerBullet in playerBullets:
        if playerBullet.rect.centery < HEIGHT and playerBullet.rect.centery > 0:
            delta = random.random()
            playerBullet.rect.centery -= 20 + delta*3
            playerBullet.rect.bottom -= 20 + delta*3
        else:
            # удалил снаряд с индексом, который вылетел за границы
            playerBullets.pop(playerBullets.index(playerBullet))

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

    # обработка поражения игрока пулями
    for enemy in enemies:

        enemyBullets = enemiesBullets[enemies.index(enemy)]
        enemyBulletsGroup = pygame.sprite.Group(enemyBullets)
        playerBulletsGroup = pygame.sprite.Group(player)
        hits = pygame.sprite.groupcollide(
            enemyBulletsGroup, playerBulletsGroup, True, True)
        for hit in hits:
            if hit:
                time.sleep(2)
                print('Game over')
                os.sys.exit(0)

    # обработка некоторых клавиш (выхода и постоянной стрельбы)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.sys.exit(0)
        if keys[pygame.K_c] and event.type == pygame.KEYUP:
            constantShooting *= -1

    # движение игрока за стрелкой
    if event.type == pygame.MOUSEMOTION:
        [player.rect.centerx, player.rect.centery] = event.pos
        mouseCoords = event.pos

    # движение врагов
    for enemy in enemies:
        if type(enemy) == type(exampleEnemy):
            enemy.rect.centery += enemy.vel
            # обработка столкновения врагов с игроком
            distance = (enemy.rect.centerx - player.rect.centerx)**2 + \
                (enemy.rect.centery - player.rect.centery)**2
            if distance <= 25**2:
                time.sleep(2)
                print('Game over')
                os.sys.exit(0)
    # стрельба врагов
    if enemiesTimerSnaryad == True:
        for enemy in enemies:
            if type(enemy) == type(exampleEnemy):
                enemyBullets = enemiesBullets[enemies.index(enemy)]
                enemyBullets.append(
                    Bullet(pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites/enemyBullet.png'))))
                enemyBullets[len(enemyBullets) -
                             1].rect.centerx = enemy.rect.centerx
                enemyBullets[len(enemyBullets) -
                             1].rect.centery = enemy.rect.centery
        enemiesTimerSnaryad = False

    # стрельба игрока
    if keys[pygame.K_f] or event.type == pygame.MOUSEBUTTONDOWN or constantShooting > 0:
        if playerTimerSnaryad == True:
            playerBullets.append(Bullet())
            playerBullets[len(
                playerBullets) - 1].rect.centerx = mouseCoords[0] - rightleftGun
            playerBullets[len(playerBullets) -
                          1].rect.centery = mouseCoords[1]
            rightleftGun *= -1
            playerTimerSnaryad = False

    drawWindow()
    # проверка счетчика интервала между пулями
    if intervalPlayerSnaryad >= 2:
        playerTimerSnaryad = True
        intervalPlayerSnaryad = 0
    if intervalEnemySnaryad >= 60:
        enemiesTimerSnaryad = True
        intervalEnemySnaryad = 0
