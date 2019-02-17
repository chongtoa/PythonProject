#enconding:utf-8
import pygame,sys
from math import *

pygame.init()
screen = pygame.display.set_mode((1500, 900), 0 ,32)
missile = pygame.image.load('red.png').convert_alpha()
x1, y1 = 100, 600
velocity = 800
time = 1/1000
clock = pygame.time.Clock()
old_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(300)
    x, y = pygame.mouse.get_pos()
    distance = sqrt(pow(x1 - x, 2) + pow(y1 - y, 2))
    section = velocity * time
    sina = (y1 - y)/distance
    cosa = (x1 - x)/distance
    angle = atan2(y - y1, x - x1)
    x1, y1 = (x1 + section * cosa, y1 - section * sina)
    d_angle = degrees(angle)
    screen.blit(missile, (x1 - missile.get_width(), y1-missile.get_height()/2))
    dis_angle = d_angle - old_angle
    pygame.display.update()