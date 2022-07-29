import pygame, sys
import function

def name_up(screen,score):
    
    function.draw(screen,"Image/wallpaper_score.png",(0,0))
    function.write_draw (screen,str(score),(520,80))
    control= False
    list_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
                  "R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7",
                  "8","9","0"," "]


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
                 "Image/Letters/0.png"]
    position = [0,0,0]
    ubication = [(80,80),(120,80),(160,80)]
    x=0
    while not control:
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and position[x]<37:
                    position[x]=position[x]+1
        
                if event.key == pygame.K_DOWN and position[x]>=0:
                    position[x]=position[x]-1

                if event.key == pygame.K_LEFT and x>=0:
                    x=x-1
                if event.key == pygame.K_RIGHT and x<2:
                    x=x+1
                if event.key == pygame.K_RETURN:
                    control = True
                function.draw(screen,list_adress[position[0]],ubication[0])
                function.draw(screen,list_adress[position[1]],ubication[1])
                function.draw(screen,list_adress[position[2]],ubication[2])
            if event.type == pygame.QUIT:
                sys.exit()
    sanata=list_letters[position[0]]+list_letters[position[1]]+list_letters[position[2]]
    return(sanata)


def scores (screen,stop):
    score = 3000000
    name=name_up(screen,score)
    function.draw(screen,"Image/wallpaper_score.png",(0,0))

    score_list = [["AAA",999999],["AAA",999999],["AAA",999999],["AAA",999999],
                  ["AAA",999999],["AAA",999999],["AAA",999999],["AAA",999999],
                  ["AAA",999999],["AAA",999999],]
    
    with open("scores.txt") as archivo:
        li1= archivo.readline()
        li2= archivo.readline()
        top=li1.split(" ")
        topu=li2.split(" ")
        x=0
        while x <=9:
            score_list[x][0]=top[x]
            score_list[x][1]=int(topu[x])
            x=x+1

    score_list2 = [["CAP",999999],["SNK",100000],["NAM",10000],["KON",1000],
                  ["AAA",999],["BBB",888],["CCC",777],["DDD",666],
                  ["EEE",555],["FFF",444]]

    x= y =0
    
    while y <= 9:
        if score > score_list[x][1] and x==y:
            score_list2[y][1]= score
            score_list2[y][0]= name
            y= y+1
        else:
            score_list2[y][1]= score_list[x][1]
            score_list2[y][0]= score_list[x][0]
            x = x+1
            y = y+1
    
    name=""
    point=""
    position=(240,100)
    position2=(480,100)
    for dato in score_list2:
        name += dato[0]+" "
        point += str(dato[1])+" "
        function.write_draw (screen,"HIGSCORES",(520,30))
        function.write_draw (screen,dato[0],position)
        function.write_draw (screen,str(dato[1]),position2)
        position=(position[0],position[1]+60)
        position2=(position2[0],position2[1]+60)
    sanata= name +"\n"+point 
    print(sanata)
    

    while not stop:

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    stop = True
            if event.type == pygame.QUIT:
                sys.exit()
    