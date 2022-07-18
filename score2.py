import pygame, sys

def scores (screen,stop):
    while not stop:

        screen.fill((0,255,255))
        pygame.display.flip()

        for event in pygame.event.get():
            
            #quedo asi pero es any key
            print("Press SPACE to pause")
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    stop = True
            if event.type == pygame.QUIT:
                sys.exit()