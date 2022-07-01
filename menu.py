import pygame, sys
import function

def menu (screen,adress,ubication,stop):
    
    position = 0  #  <  >
    screen.fill((255,255,255))
    pygame.display.flip()
    while not stop:
        function.draw(screen,adress[position][0],ubication[0])
        function.draw(screen,adress[position][1],ubication[1])
        function.draw(screen,adress[position][2],ubication[2])
        pygame.display.flip()    

        for event in pygame.event.get():

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
                        sanata = True
                        print("hacer un start pero el otro :0")
                    if position == 2:
                        sys.exit()
                
            if event.type == pygame.QUIT:
                sys.exit()

def start (screen,stop):
    adress_menu1 = [['Image/start2.png','Image/options1.png','Image/exit1.png'],
                ['Image/start1.png','Image/options2.png','Image/exit1.png'],
                ['Image/start1.png','Image/options1.png','Image/exit2.png']]

    ubication_menu1 = [(400,400),(400,480),(400,560)]

    menu (screen,adress_menu1,ubication_menu1,stop)
    