import pygame, sys
import function

def menu (screen,adress,ubication,amount):
    position = 0
    
    
    loop = True

    while loop:

        function.draw(screen,adress[position][0],ubication[0])
        function.draw(screen,adress[position][1],ubication[1])
        function.draw(screen,adress[position][2],ubication[2])

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if position >= 0 and position <= 2:
                    if event.key == pygame.K_DOWN and position < 2:
                        position = position +1
                    if event.key == pygame.K_UP and position > 0:
                        position = position -1
                print(position)
                if event.key == pygame.K_RETURN:
                    return position
            if event.type == pygame.QUIT:
                sys.exit()

def start (screen,stop): 

    adress_menu1 = [['Image/start2.png','Image/options1.png','Image/exit1.png'],
                ['Image/start1.png','Image/options2.png','Image/exit1.png'],
                ['Image/start1.png','Image/options1.png','Image/exit2.png']]

    ubication_menu1 = [(400,400),(400,480),(400,560)]

    adress_menu2= [['Image/controls2.png','Image/sound1.png','Image/return1.png'],
                ['Image/controls1.png','Image/sound2.png','Image/return1.png'],
                ['Image/controls1.png','Image/sound1.png','Image/return2.png']]

    ubication_menu2 = [(400,120),(400,280),(400,440)]
    
    position  = 0  #  <  >
    position2 = 0
    while not stop:
        
            function.draw(screen,"Image/wallpaper_menu.png",(0,0))
            function.draw(screen,"Image/title.png",(80,80))   
            position = menu (screen,adress_menu1,ubication_menu1,3)
            if position == 0:
                stop = True
            if position == 1:
                sanata2 = False
                while not sanata2:
                
                    function.draw(screen,"Image/wallpaper_menu2.png",(0,0))
                    position2 = menu (screen,adress_menu2,ubication_menu2,3)
                    
                    sanata = False
                    while not sanata:
                    
                        if position2 == 0:
                            function.draw(screen,"Image/wallpaper_controls.png",(0,0))
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RETURN:
                                        sanata = True
                                if event.type == pygame.QUIT:
                                    sys.exit()                
                        if position2 == 1:
                            function.draw(screen,"Image/wallpaper_sound.png",(0,0))
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_LEFT:
                                        print("hay q sumar")
                                    if event.key == pygame.K_RIGHT:
                                        print ("hay q restar")
                                    if event.key == pygame.K_RETURN:
                                        sanata = True
                                if event.type == pygame.QUIT:
                                    sys.exit()

                        if position2 == 2:
                            sanata = True
                            sanata2 = True
            if position == 2:
                sys.exit()
    