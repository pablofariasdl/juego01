import pygame, sys
import funtion

def menu(screen,position):
    screen.fill((255,255,255))
    funtion.draw(screen,'image/titulo.png',(80,80))
    if position == 0:
        funtion.draw(screen,'Image/start2.png',(400,400))
        funtion.draw(screen,'Image/opciones1.png',(400,480))
        funtion.draw(screen,'Image/salir1.png',(400,560))
    elif position == 1:
        funtion.draw(screen,'Image/start1.png',(400,400))
        funtion.draw(screen,'Image/opciones2.png',(400,480))
        funtion.draw(screen,'Image/salir1.png',(400,560))
    elif position == 2:
        funtion.draw(screen,'Image/start1.png',(400,400))
        funtion.draw(screen,'Image/opciones1.png',(400,480))
        funtion.draw(screen,'Image/salir2.png',(400,560))
    pygame.display.flip()

def menu2 (screen,position):
    screen.fill((255,255,255))
    if position == 0:
        funtion.draw(screen,'Image/controles2.png',(400,160))
        funtion.draw(screen,'Image/sonido1.png',(400,320))
        funtion.draw(screen,'Image/volver1.png',(400,480))
    elif position == 1:
        funtion.draw(screen,'Image/controles1.png',(400,160))
        funtion.draw(screen,'Image/sonido2.png',(400,320))
        funtion.draw(screen,'Image/volver1.png',(400,480))
    elif position == 2:
        funtion.draw(screen,'Image/controles1.png',(400,160))
        funtion.draw(screen,'Image/sonido1.png',(400,320))
        funtion.draw(screen,'Image/volver2.png',(400,480))
    pygame.display.flip()

def inicio (screen,stop):
    
    position = 0  #  <  >
    while not stop:
        menu(screen,position)
        for event in pygame.event.get():
            print("Press RETURN to select")
            if event.type == pygame.KEYDOWN:
                if position >= 0 and position <= 2:
                    if event.key == pygame.K_DOWN and position < 2:
                        position = position +1
                    if event.key == pygame.K_UP and position > 0:
                        position = position -1
                print(position)
                

                if event.key == pygame.K_RETURN:
                    if position == 0:
                        stop = True
                    if position == 1:
                        comeback = False
                        position2 = 0
                        while not comeback:
                            menu2(screen,position2)
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if position2 >= 0 and position2 <= 2:
                                        if event.key == pygame.K_DOWN and position2 < 2:
                                            position2 = position2 +1
                                        if event.key == pygame.K_UP and position2 > 0:
                                            position2 = position2 -1
                                    print(position2)
                                    
                                    
                                    if event.key == pygame.K_RETURN:
                                        if position2 == 0:
                                            print(position2)
                                        if position2 == 1:
                                            print(position2)
                                        if position2 == 2:
                                            comeback = True
                                if event.type == pygame.QUIT:
                                    sys.exit()            
                                                        
                    if position == 2:
                        sys.exit()
                
            if event.type == pygame.QUIT:
                sys.exit()
