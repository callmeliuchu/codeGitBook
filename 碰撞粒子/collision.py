import pygame
import time
import random
import sys
pygame.init()
screencaption=pygame.display.set_caption('hello world')
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.circle(screen,[0,0,0],[20,30],10,10)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

