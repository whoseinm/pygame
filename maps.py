import pygame
pygame.init()
sc = pygame.display.set_mode((600, 400))
sc.fill((0,255,255))
earth = pygame.image.load('earth.png')
home = pygame.image.load('home.png')
trees = pygame.image.load('trees.png')
fruits = pygame.image.load('fruit.png')
sun = pygame.image.load('sun.png')

sc.blit(earth, (0,300))
sc.blit(home, (100,100))
sc.blit(trees, (300,150))
sc.blit(fruits, (300,170))
sc.blit(sun, (320,10))

pygame.display.update()a