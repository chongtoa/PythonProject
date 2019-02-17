#enconding:utf-8
#enconding:utf-8
import pygame
from  pygame.locals import *
from sys import exit
from random import  randint

# 定义窗口分别率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# player类，继承pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        pygame.sprite.Sprite.__init__(self)   #父类钩子函数
        self.image = pygame.Surface([10, 10])  # 精灵图片surface
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()     # 精灵图片的大小
        self.rect.topleft = initial_position   # 精灵图片位置
        self.speed = 6

    def update(self):
        self.rect.left += self.speed
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

# 初始化游戏
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 显示窗口大小
pygame.display.set_caption('This is the first pygame-program')

# 建立精灵组
group = pygame.sprite.Group()

# 事件循环
while True:
    clock.tick(10)
    print(len(group.sprites()))

    # 从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 绘制背景
    screen.fill((255, 255, 255))

    # 不断往精灵组中添加精灵
    group.add(Player((randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))))
    group.update()
    group.draw(screen)

    pygame.display.update()
