import pygame
from random import*
pygame.init()
clock=pygame.time.Clock()
sc=pygame.display.set_mode((400,400))
bg= pygame.image.load("sea.jpg")
rk= pygame.image.load("rk.png")
r_rk=pygame.Rect(200,200,60,60)
while 1:
    sc.blit(bg,(0,0))
    sc.blit(rk,r_rk)
    pygame.display.update()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.exit()
        if i.type==pygame.MOUSEBUTTONDOWN and i.button==1:
            x,y=pos
            if r_rk.collidepoint(x,y):
                clock.tick(60)