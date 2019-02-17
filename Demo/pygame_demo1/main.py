#enconding:utf-8
import pygame
from  pygame.locals import *
from sys import exit

# 定义窗口分别率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# 新增tick
ticks = 0
offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 显示窗口大小

pygame.display.set_caption('This is the first pygame-program')

# 载入背景图片
background = pygame.image.load('resources/images/background.png')

# 载入资源文件
shoot_img = pygame.image.load('resources/images/shoot.png')

# 对资源文件进行剪切
hero1_rect = pygame.Rect(0, 99, 102, 126)
hero2_rect = pygame.Rect(165, 360, 102, 126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
hero_pos = [200, 500]

print(KEYUP)
print(KEYDOWN)

# 事件循环
while True:
    # 绘制背景
    screen.blit(background, (0, 0))

    # 添加飞机
    if ticks % 50 < 25:
        screen.blit(hero1, hero_pos)
    else:
        screen.blit(hero2, hero_pos)
    ticks += 1

    # 更新屏幕
    pygame.display.update()

    # 从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #控制方向
        # print(event.type)
        if event.type == pygame.KEYDOWN:
            print("DOWN:%d" %event.type)
            if event.key in offset:
                print("down")
                offset[event.key] = 3
        elif event.type == pygame.KEYUP:
            if event.key in offset:
                print("UP")
                offset[event.key] = 0

    hero_x = hero_pos[0] + offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
    hero_y = hero_pos[1] + offset[pygame.K_DOWN] - offset[pygame.K_UP]

    if hero_x < 0:
        hero_pos[0] = 0
    elif hero_x > SCREEN_WIDTH - hero1_rect.width:
        hero_pos[0] = SCREEN_WIDTH - hero1_rect.width
    else:
        hero_pos[0] = hero_x

    if hero_y < 0:
        hero_pos[1] = 0
    elif hero_y > SCREEN_HEIGHT - hero1_rect.height:
        hero_pos[1] = SCREEN_HEIGHT - hero1_rect.height
    else:
        hero_pos[1] = hero_x
    # offset_x = offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
    # offset_y = offset[pygame.K_DOWN] - offset[pygame.K_UP]
    # # print("x:%d, y:%d" %(offset_x, offset_y))
    # hero_pos = [hero_pos[0] + offset_x, hero_pos[1] + offset_y]

