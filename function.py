import sys,pygame

list_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
                  "R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7",
                  "8","9"," "]
list_adress=["Image/Letters/A.png","Image/Letters/B.png","Image/Letters/C.png",
                 "Image/Letters/D.png","Image/Letters/E.png","Image/Letters/F.png",
                 "Image/Letters/G.png","Image/Letters/H.png","Image/Letters/I.png",
                 "Image/Letters/J.png","Image/Letters/K.png","Image/Letters/L.png",
                 "Image/Letters/M.png","Image/Letters/N.png","Image/Letters/O.png",
                 "Image/Letters/P.png","Image/Letters/Q.png","Image/Letters/R.png",
                 "Image/Letters/S.png","Image/Letters/T.png","Image/Letters/U.png",
                 "Image/Letters/V.png","Image/Letters/W.png","Image/Letters/X.png",
                 "Image/Letters/Y.png","Image/Letters/Z.png","Image/Letters/0.png",
                 "Image/Letters/1.png","Image/Letters/2.png","Image/Letters/3.png",
                 "Image/Letters/4.png","Image/Letters/5.png","Image/Letters/6.png",
                 "Image/Letters/7.png","Image/Letters/8.png","Image/Letters/9.png",
                 "Image/Letters/00.png"]

list_adressb=["Image/Letters/A2.png","Image/Letters/B2.png","Image/Letters/C2.png",
                  "Image/Letters/D2.png","Image/Letters/E2.png","Image/Letters/F2.png",
                  "Image/Letters/G2.png","Image/Letters/H2.png","Image/Letters/I2.png",
                  "Image/Letters/J2.png","Image/Letters/K2.png","Image/Letters/L2.png",
                  "Image/Letters/M2.png","Image/Letters/N2.png","Image/Letters/O2.png",
                  "Image/Letters/P2.png","Image/Letters/Q2.png","Image/Letters/R2.png",
                  "Image/Letters/S2.png","Image/Letters/T2.png","Image/Letters/U2.png",
                  "Image/Letters/V2.png","Image/Letters/W2.png","Image/Letters/X2.png",
                  "Image/Letters/Y2.png","Image/Letters/Z2.png","Image/Letters/0b.png",
                  "Image/Letters/1b.png","Image/Letters/2b.png","Image/Letters/3b.png",
                  "Image/Letters/4b.png","Image/Letters/5b.png","Image/Letters/6b.png",
                  "Image/Letters/7b.png","Image/Letters/8b.png","Image/Letters/9b.png",
                  "Image/Letters/00A.png"]

def draw(screen,adress,position):
    image = pygame.image.load(adress)
    screen.blit(image,position)
    pygame.display.flip()

def write_draw(screen,sentence,ubication):
    text = sentence

    
    text_adress=[]
    x=y=0
    position=ubication
    while x <len(text):
        if text[x] == list_letters[y]:
            data=[list_adress[y]]
            text_adress=text_adress+data
            position = (position[0]+40,position[1])
            draw(screen,text_adress[x],position)  
            x=x+1
            y=0
        else:
            y=y+1

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

