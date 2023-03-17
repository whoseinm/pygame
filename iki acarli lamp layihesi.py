import pygame
pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((500,400))
sh = pygame.image.load('sh.png')
koff = pygame.image.load('koff.png')
kon = pygame.image.load('kon.png')
loff = pygame.image.load('loff.png')
lon = pygame.image.load('lon.png')
key1=koff
key2=koff
lamp=loff
k1=0
k2=0
r_key1=pygame.Rect(110,0,170,90)
r_key2=pygame.Rect(110,270,170,90)
while 1:
    sc.blit(sh,(0,0))
    sc.blit(key1,r_key1)
    sc.blit(key2,r_key2)
    sc.blit(lamp,(380,60))
    pygame.display.update()
    clock.tick(60)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            x,y=i.pos
            if i.button==1:
                if r_key1.collidepoint(x,y):
                    if k1==0:
                        k1=1
                        key1=kon
                    else:
                        k1=0
                        key1=koff
                if r_key2.collidepoint(x,y):
                    if k2==0:
                        k2=1
                        key2=kon
                    else:
                        k2=0
                        key2=koff
        if k1==1 and k2==1:
            lamp=lon
        else:
            lamp=loff

