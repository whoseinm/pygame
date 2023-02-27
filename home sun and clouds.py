
import pygame
pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((600, 400))
torpaq = pygame.image.load('torpaq.png')
bulud = pygame.image.load('bulud.png')
ev = pygame.image.load('ev.png')
agac = pygame.image.load('ağac.png')
meyve = pygame.image.load('meyvə.png')
gunes = pygame.image.load('günəş.png')
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    sc.blit(torpaq, (0,300))
    sc.blit(ev, (100,90))
    sc.blit(bulud, (50,100))
    sc.blit(agac, (320,170))
    sc.blit(meyve, (320,180))
    sc.blit(gunes, (320,0))
    pygame.display.update()
    clock.tick()