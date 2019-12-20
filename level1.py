import os
import pygame
import random
import time
from settings import SIZE, WHITE, HEIGHT, WIDHT, BGCOLOR
from game_objects import Player, Bullet, EnemyAircraft, Heart, Coin
from math import pi, cos, sin


def level11(win, money):
    print("rmervmeivmiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

# __________________________БЛОК ПЕРЕМЕННЫХ начинается___________________________
    player = Player()
    coins = []
    exampleCoin = Coin(1, 1)
    exampleCoin.image = pygame.transform.scale(
        exampleCoin.image, (25, 25))
    exampleCoin.rect.center = [20, 20]
    event = 0
    enemies = []
    exampleEnemy = EnemyAircraft(270, 1, 10)
    enemiesBullets = []
    for e in range(3):
        enemies.append(EnemyAircraft(270, 1, 1))
        enemiesBullets.append([])
    enemies[1].vel = 2

    [enemies[0].rect.centerx, enemies[0].rect.centery] = [WIDHT // 4, -10]
    [enemies[1].rect.centerx, enemies[1].rect.centery] = [WIDHT // 2, -10]
    [enemies[2].rect.centerx, enemies[2].rect.centery] = [WIDHT*3 // 4, -10]

    playerBullets = []
    numberbgCadr = 0
    intervalPlayerSnaryad = 0
    intervalEnemySnaryad = 0
    intervalCoin = 0
    intervalCoin2 = 0
    intervalPause12 = 0
    intervalPause23 = 0
    global numberCoinImg
    numberCoinImg = 1
    global numberCoinImg2
    numberCoinImg2 = 1
    playerTimerSnaryad = True
    enemiesTimerSnaryad = True
    mouseCoords = []
    clock = pygame.time.Clock()
    rightleftGun = 30
    constantShooting = -1
    global player_live
    player_live = 3
    hearts = []
    for staff2 in range(player_live):
        hearts.append(Heart(staff2))
        hearts[staff2].centerx = WIDHT - 25 - staff2*35
        hearts[staff2].centery = 25
    pause = False
    restart = False
    allEnemiesZero = False

    font_name = pygame.font.match_font('Comic Sans MS')

# __________________________БЛОК ПЕРЕМЕННЫХ закончился___________________________

# __________________________БЛОК ФУНКЦИЙ начинается___________________________

    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def game_over():
        """Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры"""
        play_surface = pygame.display.set_mode((500, 650))
        bg = pygame.image.load('sprites/gameover_bg.jpg')
        play_surface.blit(bg, (0, 0))
        pygame.display.set_caption('Shooter')
        draw_text(play_surface, str('Game over'),
                  72, WIDHT//2, HEIGHT//2 - 200)
        play_surface.blit(exampleCoin.image, exampleCoin.rect)
        draw_text(play_surface, str(money), 20, 60, 11)
        draw_text(play_surface, str(money),
                  50, WIDHT//2, HEIGHT//2 - 50)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        os.sys.exit()

    # функция получения названия картинки фона по номеру

    def winner():
        play_surface = pygame.display.set_mode((
            500, 650))
        pygame.display.set_caption('Shooter')
        bg = pygame.image.load('sprites/winner_bg.jpg')
        play_surface.blit(bg, (0, 0))
        draw_text(play_surface, str('You win!'),
                  72, WIDHT//2, HEIGHT//2 - 200)
        play_surface.blit(exampleCoin.image, exampleCoin.rect)
        draw_text(play_surface, str(money), 20, 60, 11)
        draw_text(play_surface, str(money),
                  50, WIDHT//2, HEIGHT//2 - 50)
        draw_text(play_surface, str(
            'press \'Esc\' to exit...'), 10, WIDHT//2, HEIGHT - 40)
        pygame.display.flip()
        winner = True
        while winner:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.sys.exit()
                if keys[pygame.K_ESCAPE]:
                    winner = False
        pygame.quit()
        os.sys.exit()

    def bgCadr(i):
        i = str(i)
        while len(i) < 4:
            i = '0' + i
        return('bg/Видеофон Звёздное небо ' + i+'.jpg')

    def pausedddd():
        nonlocal pause
        nonlocal restart
        play_surface = pygame.display.set_mode((
            500, 650))
        pygame.display.set_caption('Shooter')
        bg = pygame.image.load('sprites/pause_bg.jpg')
        play_surface.blit(bg, (0, 0))
        while pause or not restart:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os.sys.exit()
                if keys[pygame.K_r]:
                    restart = True

                if keys[pygame.K_p]:
                    pause = False
                    break

            draw_text(play_surface, str('Pause...'),
                      72, WIDHT//2, HEIGHT//2 - 200)
            play_surface.blit(exampleCoin.image, exampleCoin.rect)
            draw_text(play_surface, str(money), 20, 60, 11)
            draw_text(play_surface, str(money),
                      50, WIDHT//2, HEIGHT//2 - 50)
            draw_text(play_surface, str(
                'press \'R\' to restart game...'), 10, WIDHT//2, HEIGHT - 40)
            for staff2 in range(player_live):
                win.blit(hearts[staff2].image, hearts[staff2].rect)
            pygame.display.flip()
            pygame.display.update()

    # функция обновления экрана

    def drawWindow(win):
        bg = pygame.image.load(bgCadr(numberbgCadr))
        win.blit(bg, (0, 0))
        for playerBullet in playerBullets:
            win.blit(playerBullet.image, playerBullet.rect)
        for coin in coins:
            if coin.imageInd == 1:
                coin.image = pygame.image.load(
                    'sprites/coin'+str(coin.imageInd)+'/coin'+str(numberCoinImg)+'.png')
            elif coin.imageInd == 2:
                coin.image = pygame.image.load(
                    'sprites/coin'+str(coin.imageInd)+'/coin'+str(numberCoinImg2)+'.png')
            win.blit(coin.image, coin.rect)
        for enemy in enemies:
            enemyBullets = enemiesBullets[enemies.index(enemy)]
            for enemyBullet in enemyBullets:
                win.blit(enemyBullet.image, enemyBullet.rect)
            if type(enemy) == type(exampleEnemy):
                win.blit(enemy.image, enemy.rect)
        win.blit(player.image, player.rect)
        for staff2 in range(player_live):
            win.blit(hearts[staff2].image, hearts[staff2].rect)

        draw_text(win, str(money), 20, 60, 11)
        win.blit(exampleCoin.image, exampleCoin.rect)
        pygame.display.update()

    # двигаю снаряды врагов и удаляю улетевшие
    def movingEnemiesBullets():
        for enemy in enemies:
            enemyBullets = enemiesBullets[enemies.index(enemy)]
            for enemyBullet in enemyBullets:
                if inWindow(enemyBullet) == 1:
                    enemyBullet.rect.centery += enemyBullet.vel * \
                        (-round(sin(enemyBullet.angle*pi/180), 3))
                    enemyBullet.rect.centerx += enemyBullet.vel * \
                        (round(cos(enemyBullet.angle*pi/180), 3))
                else:
                    enemyBullets.pop(enemyBullets.index(enemyBullet))

    # двигаю снаряды игрока и удаляю улетевшие
    def movingPlayerBullets():
        for playerBullet in playerBullets:
            if inWindow(playerBullet) == 1:
                delta = round(random.random())
                playerBullet.rect.centery -= playerBullet.vel + delta*3
                playerBullet.rect.bottom -= playerBullet.vel + delta*3
            else:
                playerBullets.pop(playerBullets.index(playerBullet))

    # обработка поражения врагов пулями
    def defeatOfEnemies():
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
                if allEnemiesZero == False:
                    imageInd = 1
                    coins.append(Coin(numberCoinImg, imageInd))
                    coins[len(coins)-1].rect.center = enemies[enemies.index(
                        hit)].rect.center
                    coins[len(coins)-1].image = pygame.image.load(
                        'sprites/coin'+str(imageInd)+'/coin'+str(numberCoinImg)+'.png')
                elif allEnemiesZero == True and iteration3 == False:
                    imageInd = 2
                    coins.append(Coin(numberCoinImg, imageInd))
                    coins[len(coins)-1].rect.center = enemies[enemies.index(
                        hit)].rect.center
                    coins[len(coins)-1].image = pygame.image.load(
                        'sprites/coin'+str(imageInd)+'/coin'+str(numberCoinImg)+'.png')

                enemies[enemies.index(hit)] = 0

    def takeCoins():
        nonlocal money
        for coin in coins:
            distance = (coin.rect.centerx - player.rect.centerx)**2 + \
                (coin.rect.centery - player.rect.centery)**2
            if distance <= 25**2:
                if coin.imageInd == 1:
                    coins.pop(coins.index(coin))
                    money += 1
                elif coin.imageInd == 2:
                    coins.pop(coins.index(coin))
                    money += 2

            # обработка поражения игрока пулями

    def defeatOfPlayer():
        global player_live
        for enemy in enemies:
            enemyBullets = enemiesBullets[enemies.index(enemy)]
            for enemyBullet in enemyBullets:
                # обработка столкновения врагов с игроком
                distance = (enemyBullet.rect.centerx - player.rect.centerx)**2 + \
                    (enemyBullet.rect.centery - player.rect.centery)**2
                if distance <= 25**2:
                    enemyBullets.pop(enemyBullets.index(enemyBullet))
                    # уничтожение пули
                    player_live -= 1
                    if player_live <= 0:
                        time.sleep(0)
                        print('Game over')
                        print(player_live)
                        game_over()

    def inWindow(sprite):
        if sprite.rect.left > WIDHT or sprite.rect.right < 0 or sprite.rect.top > HEIGHT or sprite.rect.bottom < 0:
            return(0)
        else:
            return(1)

           # __________________________БЛОК ФУНКЦИЙ закончился________________________

           # __________________________ОСНОВНОЙ БЛОК начинается___________________________

           # __________________________итерация 1_________________________________
    i = 1
    while not allEnemiesZero:
        clock.tick(45)
        intervalPlayerSnaryad += 1
        intervalEnemySnaryad += 1
        intervalCoin += 1

        # счетчик для анимированного фона
        if numberbgCadr < 7325:
            numberbgCadr += 1
        else:
            numberbgCadr = 0

        movingEnemiesBullets()

        movingPlayerBullets()

        takeCoins()

        defeatOfEnemies()

        defeatOfPlayer()

        # обработка некоторых клавиш (выхода и постоянной стрельбы)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                os.sys.exit()
            if keys[pygame.K_e]:
                os.sys.exit(0)
            if keys[pygame.K_c]:
                constantShooting *= -1
            if keys[pygame.K_p]:
                pause = True
                pausedddd()

        # движение игрока за стрелкой
        if event.type == pygame.MOUSEMOTION:
            [player.rect.centerx, player.rect.centery] = event.pos
            mouseCoords = event.pos

        # движение врагов
        staff1 = 0
        for enemy in enemies:
            if type(enemy) == type(exampleEnemy):
                if inWindow(enemy) == 1:
                    enemy.rect.centery += enemy.vel * \
                        (-sin(enemy.angle*pi/180))
                    enemy.rect.centerx += enemy.vel * \
                        cos(enemy.angle*pi/180)
                    # обработка столкновения врагов с игроком
                    distance = (enemy.rect.centerx - player.rect.centerx)**2 + \
                        (enemy.rect.centery - player.rect.centery)**2
                    if distance <= 30**2:
                        time.sleep(0)
                        print('Game over')
                        print(player_live)
                        game_over()
                else:
                    enemy = 0
                    staff1 += 1
            else:
                staff1 += 1
        if staff1 == 3:
            allEnemiesZero = True

        # UPDATE - СОЗДАНИЕ ПУЛЬ  стрельба врагов
        if enemiesTimerSnaryad == True:
            for enemy in enemies:
                if type(enemy) == type(exampleEnemy):
                    enemyBullets = enemiesBullets[enemies.index(
                        enemy)]
                    enemyBullets.append(
                        Bullet(enemy.angle, 1, 6))
                    enemyBullets[len(enemyBullets) -
                                 1].rect.centerx = enemy.rect.centerx
                    enemyBullets[len(enemyBullets) -
                                 1].rect.centery = enemy.rect.centery
            enemiesTimerSnaryad = False

        # стрельба игрока
        if keys[pygame.K_f] or event.type == pygame.MOUSEBUTTONDOWN or constantShooting > 0:
            if playerTimerSnaryad == True:
                playerBullets.append(Bullet(90, 2, 20))
                playerBullets[len(
                    playerBullets) - 1].rect.centerx = mouseCoords[0] - rightleftGun
                playerBullets[len(playerBullets) -
                              1].rect.centery = mouseCoords[1]
                rightleftGun *= -1
                playerTimerSnaryad = False

        drawWindow(win)
        # проверка счетчика интервала между пулями
        if intervalPlayerSnaryad >= 5:
            playerTimerSnaryad = True
            intervalPlayerSnaryad = 0
        if intervalEnemySnaryad >= 30:
            enemiesTimerSnaryad = True
            intervalEnemySnaryad = 0
        if intervalCoin >= 5 and numberCoinImg < 6:
            numberCoinImg += 1
            intervalCoin = 0
        elif numberCoinImg >= 6:
            numberCoinImg = 1

        #allEnemiesZero = True

    # __________________итерация 2_________________________________________
    allEnemiesZero = True
    intervalEnemySnaryad = 9
    enemiesTimerSnaryad = True
    iteration3 = False
    enemy1Count = 0
    enemy2Count = 0
    """

    """
    #
    """
    enemies = []
    enemiesBullets = []
    for e in range(3):
        enemies.append(EnemyAircraft(270, 1, 1))
        enemiesBullets.append([])
    enemies[1].vel = 2

    [enemies[0].rect.centerx, enemies[0].rect.centery] = [WIDHT // 4, -10]
    [enemies[1].rect.centerx, enemies[1].rect.centery] = [WIDHT // 2, -10]
    [enemies[2].rect.centerx, enemies[2].rect.centery] = [WIDHT*3 // 4, -10]
    enemiesBullets = []
    for e in range(3):
        enemies.append(EnemyAircraft(270, 1, 1))
        enemiesBullets.append([])
    enemies[1].vel = 2

    [enemies[0].rect.centerx, enemies[0].rect.centery] = [WIDHT // 4, -10]
    [enemies[1].rect.centerx, enemies[1].rect.centery] = [WIDHT // 2, -10]
    [enemies[2].rect.centerx, enemies[2].rect.centery] = [WIDHT*3 // 4, -10]
    """
    exampleEnemy = EnemyAircraft(270, 1, 1)
    enemies = []
    enemiesBullets = []

    while intervalPause12 <= 100:
        intervalPause12 += 1
        intervalCoin += 1
        takeCoins()
        # обработка некоторых клавиш (выхода и постоянной стрельбы)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                os.sys.exit()
            if keys[pygame.K_e]:
                os.sys.exit(0)
            if keys[pygame.K_c]:
                constantShooting *= -1
            if keys[pygame.K_p]:
                pause = True
                pausedddd()

        # движение игрока за стрелкой
        if event.type == pygame.MOUSEMOTION:
            [player.rect.centerx, player.rect.centery] = event.pos
            mouseCoords = event.pos

        movingPlayerBullets()
        if intervalCoin >= 5 and numberCoinImg < 6:
            numberCoinImg += 1
            intervalCoin = 0
        elif numberCoinImg >= 6:
            numberCoinImg = 1
        drawWindow(win)

    enemies.append(EnemyAircraft(0, 2, 10, 2))
    enemiesBullets.append([])
    [enemies[0].rect.centerx, enemies[0].rect.centery] = [0, WIDHT//2]

    enemies.append(EnemyAircraft(-90, 2, 10, 1.3, 10))
    enemies[len(enemies)-1].image_copy = enemies[len(enemies)-1].image
    enemiesBullets.append([])
    [enemies[len(enemies)-1].rect.centerx,
     enemies[len(enemies)-1].rect.centery] = [WIDHT//3, 0]
    #
    #
    # здесь должен быть код с созданием врагов второй итерации
    #
    # playerBullets = []
    #
    while not iteration3:
        clock.tick(45)
        intervalPlayerSnaryad += 1
        intervalEnemySnaryad += 1
        intervalCoin2 += 1
        intervalCoin += 1

        # счетчик для анимированного фона
        if numberbgCadr < 7325:
            numberbgCadr += 1
        else:
            numberbgCadr = 0

        movingEnemiesBullets()

        movingPlayerBullets()

        takeCoins()
        defeatOfEnemies()

        defeatOfPlayer()

        """
        staff1 = 0
        for enemy in enemies:
            if type(enemy) == type(exampleEnemy):
                enemy.rect.centery += enemy.vel * \
                    (-sin(enemy.angle*pi/180))
                enemy.rect.centerx += enemy.vel * \
                    cos(enemy.angle*pi/180)
                # обработка столкновения врагов с игроком
                distance = (enemy.rect.centerx - player.rect.centerx)**2 + \
                    (enemy.rect.centery - player.rect.centery)**2
                if distance <= 30**2:
                    time.sleep(0)
                    print('Game over')
                    print(player_live)
                    game_over()
            else:
                staff1 += 1
        if staff1 == 3:
            allEnemiesZero = True
        """
        for enemy in enemies:
            if type(enemy) == type(exampleEnemy):
                if enemies.index(enemy) == 0:
                    enemy.rect.centery += enemy.vel * \
                        (-round(sin(enemy.angle*pi/180), 3))
                    enemy.rect.centerx += enemy.vel * \
                        (round(cos(enemy.angle*pi/180), 3))
                    enemy.rotate()
                    distance = (enemy.rect.centerx - player.rect.centerx)**2 + \
                        (enemy.rect.centery - player.rect.centery)**2
                    if inWindow(enemy) == 0:
                        enemies[0] = EnemyAircraft(0, 2, 10, 2)
                        [enemies[0].rect.centerx, enemies[0].rect.centery] = [
                            0, WIDHT//2]
                        enemy1Count += 1
                    if enemy1Count == 3:
                        enemies[0] = 0
                elif enemies.index(enemy) == 1:
                    enemy.rect.centery += enemy.vel * \
                        (-round(sin(enemy.angle*pi/180), 3))
                    enemy.rect.centerx += enemy.vel * \
                        (round(cos(enemy.angle*pi/180), 3))
                    enemy.rotate()
                    distance = (enemy.rect.centerx - player.rect.centerx)**2 + \
                        (enemy.rect.centery - player.rect.centery)**2
                    if inWindow(enemy) == 0:
                        enemies[len(
                            enemies)-1] = EnemyAircraft(-90, 2, 10, 1.3, 10)
                        enemies[len(
                            enemies)-1].image_copy = enemies[len(enemies)-1].image
                        [enemies[len(enemies)-1].rect.centerx,
                         enemies[len(enemies)-1].rect.centery] = [WIDHT//4, 0]
                        enemy2Count += 1
                    if enemy2Count == 3:
                        enemies[1] = 0

                if distance <= 30**2:
                    time.sleep(0)
                    print('Game over')
                    print(player_live)
                    game_over()

        #
        #
        #
        #
        #
        #
        # здесь будет функция с движением игроков второй итерации
        #
        #

        # обработка некоторых клавиш (выхода и постоянной стрельбы)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                os.sys.exit()
            if keys[pygame.K_e]:
                os.sys.exit(0)
            if keys[pygame.K_c]:
                constantShooting *= -1
            if keys[pygame.K_p]:
                pause = True
                pausedddd()

        # движение игрока за стрелкой
        if event.type == pygame.MOUSEMOTION:
            [player.rect.centerx, player.rect.centery] = event.pos
            mouseCoords = event.pos

        # UPDATE - СОЗДАНИЕ ПУЛЬ  стрельба врагов
        if enemiesTimerSnaryad == True:
            for enemy in enemies:
                if type(enemy) == type(exampleEnemy):
                    enemyBullets = enemiesBullets[enemies.index(
                        enemy)]
                    enemyBullets.append(
                        Bullet(enemy.angle, 1, 15))
                    enemyBullets[len(enemyBullets) -
                                 1].rect.centerx = enemy.rect.centerx
                    enemyBullets[len(enemyBullets) -
                                 1].rect.centery = enemy.rect.centery
            enemiesTimerSnaryad = False
        # стрельба игрока
        if keys[pygame.K_f] or event.type == pygame.MOUSEBUTTONDOWN or constantShooting > 0:
            if playerTimerSnaryad == True:
                playerBullets.append(Bullet(pi/2, 2, 20))
                playerBullets[len(
                    playerBullets) - 1].rect.centerx = mouseCoords[0] - rightleftGun
                playerBullets[len(playerBullets) -
                              1].rect.centery = mouseCoords[1]
                rightleftGun *= -1
                playerTimerSnaryad = False

        drawWindow(win)
        # проверка счетчика интервала между пулями
        if intervalPlayerSnaryad >= 7:
            playerTimerSnaryad = True
            intervalPlayerSnaryad = 0
        if intervalEnemySnaryad >= 3:
            enemiesTimerSnaryad = True
            intervalEnemySnaryad = 0
        if intervalCoin >= 5 and numberCoinImg < 6:
            numberCoinImg += 1
            intervalCoin = 0
        elif numberCoinImg >= 6:
            numberCoinImg = 1

        if intervalCoin2 >= 20 and numberCoinImg2 < 6:
            numberCoinImg2 += 1
            intervalCoin2 = 0
        elif numberCoinImg2 >= 6:
            numberCoinImg2 = 1

        if (enemy1Count >= 3 or enemies[0] == 0) and (enemy2Count >= 3 or enemies[1] == 0):
            iteration3 = True

    enemies = []
    enemiesBullets = []
    while intervalPause23 <= 100:
        intervalPause23 += 1
        intervalCoin += 1
        takeCoins()
        # обработка некоторых клавиш (выхода и постоянной стрельбы)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                os.sys.exit()
            if keys[pygame.K_e]:
                os.sys.exit(0)
            if keys[pygame.K_c]:
                constantShooting *= -1
            if keys[pygame.K_p]:
                pause = True
                pausedddd()

        # движение игрока за стрелкой
        if event.type == pygame.MOUSEMOTION:
            [player.rect.centerx, player.rect.centery] = event.pos
            mouseCoords = event.pos

        movingPlayerBullets()
        if intervalCoin >= 5 and numberCoinImg < 6:
            numberCoinImg += 1
            intervalCoin = 0
        elif numberCoinImg >= 6:
            numberCoinImg = 1
        drawWindow(win)

    winner()
