import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()  # инициализируем модуль pygame
win = pygame.display.set_mode((500, 500))  # создаем окно

pygame.display.set_caption("Cubes Game")  # заголовок окна

walkRight = [pygame.image.load('sprites/pygame_right_1.png'), pygame.image.load('sprites/pygame_right_2.png'), pygame.image.load('sprites/pygame_right_3.png'),
             pygame.image.load('sprites/pygame_right_4.png'), pygame.image.load('sprites/pygame_right_5.png'), pygame.image.load('sprites/pygame_right_6.png')]

walkLeft = [pygame.image.load('sprites/pygame_left_1.png'), pygame.image.load('sprites/pygame_left_2.png'), pygame.image.load('sprites/pygame_left_3.png'),
            pygame.image.load('sprites/pygame_left_4.png'), pygame.image.load('sprites/pygame_left_5.png'), pygame.image.load('sprites/pygame_left_6.png')]

bg = pygame.image.load('sprites/pygame_bg.jpg')
playerStand = pygame.image.load('sprites/pygame_idle.png')

clock = pygame.time.Clock()

x = 400
y = 422
widht = 60
height = 71
speed = 7

isJump = False
jumpHeight = 10
jumpCount = jumpHeight

left = False
right = False
animCount = 0
lastMove = "right"
timerSnaryad = True
numberbgCadr = 0


class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing  # направление
        self.vel = 8 * facing  # скорость

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount

    # на win загрузили фоновую картунку bg
    win.blit(bg, (0, 0))

    # 30 кадров в секунду
    if animCount + 1 >= 30:
        animCount = 0

    for bullet in bullets:
        bullet.draw(win)

    # при каждой отрисовке окна проверяем, какие кнопки у нас нажаты и в соответствии с этим
    # начинаем проигрывать анимацию игрока
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    # обновление окна, по сути всё отображается именно благодаря запуску этой функции
    pygame.display.update()


# создание цикла для работы игры
run = True
bullets = []

while run:
    clock.tick(30)

    numberbgCadr += 1

    for event in pygame.event.get():  # функция pygame.event.get получает на вход массив произошедших событий
        # event - объект события https://younglinux.info/pygame/key
        if event.type == pygame.QUIT:  # кнопка "закрыть", крестик
            run = False  # тогда из цикла выходим, программа завершается

    for bullet in bullets:  # двигаю снаряды и удаляю улетевшие
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            # удалил снаряд с индексом, который вылетел за границы
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:  # стреляет
        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        # задали максимальное количество снарядов на экране - 5
        if len(bullets) < 10 and timerSnaryad == True:
            bullets.append(
                snaryad(round(x + widht // 2), round(y + height // 2), 5, (255, 0, 0), facing))
            timerSnaryad = False

    if keys[pygame.K_LEFT] and 5 < x:  # бежит влево
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 500 - 5 - widht:  # бежит вправо
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:  # стоит
        right = False
        left = False
        animCount = 0
    if not(isJump):  # если сейчас не прыгаю, проверю на нажатие space
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            isJump = True
    else:  # прыгаем
        if jumpCount >= 0:
            y -= (jumpCount ** 2)/2
            jumpCount -= 1
        else:
            if jumpCount >= -jumpHeight:
                y += (jumpCount ** 2)/2
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = jumpHeight
    drawWindow()
    timerSnaryad = True

pygame.quit()
