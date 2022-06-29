import pygame, sys

def game (screen,stop):
    while not stop:

        screen.fill((255,255,0))
        pygame.display.flip()

        for event in pygame.event.get():
            
            #quedo asi pero es any key
            print("Press SPACE to pause")
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop = True
            if event.type == pygame.QUIT:
                sys.exit()