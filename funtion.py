import sys,pygame

def draw(screen,adress,position):
    image = pygame.image.load(adress)
    screen.blit(image, position)

def menu(screen,position):
    if position == 0:
        draw(screen,'Image/start2.png',(400,400))
        draw(screen,'Image/opciones1.png',(400,480))
        draw(screen,'Image/salir1.png',(400,560))
    elif position == 1:
        draw(screen,'Image/start1.png',(400,400))
        draw(screen,'Image/opciones2.png',(400,480))
        draw(screen,'Image/salir1.png',(400,560))
    elif position == 2:
        draw(screen,'Image/start1.png',(400,400))
        draw(screen,'Image/opciones1.png',(400,480))
        draw(screen,'Image/salir2.png',(400,560))
    pygame.display.flip()

def inicio (screen,stop):
    screen.fill((255,255,255))
    
    draw(screen,"Image/titulo.png",(80,80))
    draw(screen,'Image/start2.png',(400,400))
    draw(screen,'Image/opciones1.png',(400,480))
    draw(screen,'Image/salir1.png',(400,560))
    pygame.display.flip()

    position = 0  #  <  >
    while not stop:
    
        for event in pygame.event.get():
            print("Press RETURN to select")
            if event.type == pygame.KEYDOWN:
                if position >= 0 and position <= 2:
                    if event.key == pygame.K_DOWN and position < 2:
                        position = position +1
                    if event.key == pygame.K_UP and position > 0:
                        position = position -1
                print(position)
                menu(screen,position)

                if event.key == pygame.K_RETURN:
                    if position == 0:
                        stop = True
                    if position == 1:
                        print("entrar a opciones")
                    if position == 2:
                        sys.exit()
                
            if event.type == pygame.QUIT:
                sys.exit()



def scores (screen,stop):
    while not stop:

        screen.fill((0,255,255))
        pygame.display.flip()

        for event in pygame.event.get():
            
            #quedo asi pero es any key
            print("Press SPACE to pause")
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = True
            if event.type == pygame.QUIT:
                sys.exit()
    
    