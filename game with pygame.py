import pygame
pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((50,50))
sh = pygame.image.load('dovre.png')
koff = pygame.image.load('off.png')
kon = pygame.image.load('on.png')
loff = pygame.image.load('lamp_off.png')
lon = pygame.image.load('lamp_on.png')
key=koff
lamp=loff
k=0
r_key=pygame.Rect(170,0,50,0)

while 1:
    sc.blit(sh,(500,371))
    sc.blit(key,r_key)
    sc.blit(lamp,(221,211))
    pygame.display.update()
    clock.tick(60)

for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            x,y=i.pos
            if r_key.collidepoint(x,y) and i.button==1:
                if k==0:
                    key=kon
                    lamp=lon
                    k=1
                else:
                    key=koff
                    lamp=loff
                    k=0