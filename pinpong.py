import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")
clock = pygame.time.Clock()


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = 20
        self.rect.bottom = HEIGHT / 2
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -10
        if keystate[pygame.K_s]:
            self.speedy = 10
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 20
        self.rect.bottom = HEIGHT / 2
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT /2
        self.speedx = random.randint(-6,6)
        self.speedy = random.randint(-6, 4)


    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH+10:
            pygame.quit()
        if self.rect.left < 0:
            pygame.quit()
        if self.rect.top < HEIGHT-3:
            self.speedy=-self.speedy
        if self.rect.bottom > 10:
            self.speedy=-self.speedy



all_sprites = pygame.sprite.Group()
Mob = pygame.sprite.Group()
Players=pygame.sprite.Group()
player1 = Player1()
player2 = Player2()
ball=Ball()
Mob.add(ball)
Players.add(player1,player2)
all_sprites.add(player1,player2,ball)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    hits_p1 = pygame.sprite.spritecollide(player1, Mob, False)
    hits_p2 = pygame.sprite.spritecollide(player2, Mob, False)
    if hits_p1:
     ball.speedx = random.randint(3,6)
     ball.speedy = random.randint(2,4)
    if hits_p2:
     ball.speedx= -random.randint(3,6)
     ball.speedy = -random.randint(2,4)
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
