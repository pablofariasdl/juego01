import pygame, sys
import function

def scores (screen,stop):
    function.draw(screen,"Image/wallpaper_score.png",(0,0))
    while not stop:

        

        for event in pygame.event.get():
            
            #quedo asi pero es any key
            print("Press SPACE to pause")
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    stop = True
            if event.type == pygame.QUIT:
                sys.exit()
    