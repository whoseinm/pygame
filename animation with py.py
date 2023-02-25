 import pygame
 pygame.init()
 cl = pygame.time.Clock()
 sc = pygame.display.set_mode((500,375))
 bg = pygame.image.load("bg.png")
 ball = pygame.image.load("ball.png")
 xb = 0
 yb = 320
 while 1:
        sc.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        xb+=3
        sc.blit(ball,(xb,yb))
        pygame.display.update()
        pygame.clock.tick(60)