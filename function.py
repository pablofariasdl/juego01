import sys,pygame

def draw(screen,adress,position):
    image = pygame.image.load(adress)
    screen.blit(image,position)
    pygame.display.flip()

def menu (screen,adress,ubication,amount):
    position = 0
    
    loop = True

    while loop:
        x=0
        while x < amount:
            draw(screen,adress[position][x],ubication[x])
            x=x+1

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if position >= 0 and position <= 2:
                    if event.key == pygame.K_DOWN and position < 2:
                        position = position +1
                    if event.key == pygame.K_UP and position > 0:
                        position = position -1
                if event.key == pygame.K_RETURN:
                    return position
            if event.type == pygame.QUIT:
                sys.exit()
