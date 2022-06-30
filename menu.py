import pygame, sys
import funtion

def menu(screen,position):
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


def inicio (screen,stop):
    screen.fill((255,255,255))
    
    funtion.draw(screen,"Image/titulo.png",(80,80))
    funtion.draw(screen,'Image/start2.png',(400,400))
    funtion.draw(screen,'Image/opciones1.png',(400,480))
    funtion.draw(screen,'Image/salir1.png',(400,560))
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
