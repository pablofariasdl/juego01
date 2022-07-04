import sys,pygame

def draw(screen,adress,position):
    image = pygame.image.load(adress)
    screen.blit(image,position)
    pygame.display.flip()


    