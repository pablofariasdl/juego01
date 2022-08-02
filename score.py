import pygame, sys
import function

def name_up(screen,score):
    
    function.draw(screen,"Image/wallpaper_score.png",(0,0))
    function.write_draw (screen,str(score),(520,80))
    control= False
    
    position = [0,0,0]
    ubication = [(80,80),(120,80),(160,80)]
    x=0
    
    while not control:

        

        function.draw(screen,function.list_adress[position[0]],ubication[0])
        function.draw(screen,function.list_adress[position[1]],ubication[1])
        function.draw(screen,function.list_adress[position[2]],ubication[2])
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
                function.draw(screen, function.list_adress[position[0]],ubication[0])
                function.draw(screen, function.list_adress[position[1]],ubication[1])
                function.draw(screen, function.list_adress[position[2]],ubication[2])
            if event.type == pygame.QUIT:
                sys.exit()
        function.draw(screen,function.list_adressb[position[0]],ubication[0])
        function.draw(screen,function.list_adressb[position[1]],ubication[1])
        function.draw(screen,function.list_adressb[position[2]],ubication[2])
        
    sanata=function.list_letters[position[0]]+function.list_letters[position[1]]+function.list_letters[position[2]]
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
        function.write_draw (screen,"HIGSCORES",(320,30))
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
    