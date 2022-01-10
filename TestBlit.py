import pygame
import sys
import pygame.freetype
from pygame.locals import *


pygame.init()
Background=pygame.image.load("Background/1080p.png")
Background.set_alpha(25)
screen=pygame.display.set_mode((1080,1920),FULLSCREEN)
#screen.set_alpha(0)
pygame.display.set_caption("Test")
clock=pygame.time.Clock()
i=1
def showText(a):
    Font=pygame.font.Font("FontLib/setup/苹方黑体-准-简.ttf",32)
    Font.set_bold(1)
    screen.blit(Font.render(str(i),True,(255,255,255)),(600,600))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(Background,(0,0))
    showText(i)
    i+=1
    clock.tick(30)
    pygame.display.update()
