import pygame
from random import*
pygame.init()
clock=pygame.time.Clock()
sc=pygame.display.set_mode((500,400))
pl=pygame.image.load('pl.png')
t=pygame.image.load('tr.png')
win=pygame.image.load('win.png')
finish=pygame.image.load('finish.png')
r_f=pygame.Rect(360,60,28,242)
x1=x2=x3=0
winner=0
while winner==0:
    sc.blit(pl,(0,0))
    sc.blit(finish,r_f)
    r_t1=pygame.Rect(x1,60,64,60)
    r_t2=pygame.Rect(x2,150,64,60)
    r_t3=pygame.Rect(x3,235,64,60)
    sc.blit(t,r_t1)
    sc.blit(t,r_t2)
    sc.blit(t,r_t3)
    x1=x1+randint(0,3)
    x2=x2+randint(0,3)
    x3=x3+randint(0,3)
    if r_t1.colliderect(r_f):
        winner=1
        sc.blit(win,(250,50))
    if r_t2.colliderect(r_f):
        winner=1
        sc.blit(win,(250,140))
    if r_t3.colliderect(r_f):
        winner=1
        sc.blit(win,(250,220))
    pygame.display.update()
    clock.tick(60)
