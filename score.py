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
        z=[0,1,2]
        for a in z:
            function.draw(screen,function.list_adress[position[a]],ubication[a])
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP and position[x]<37) :
                    position[x]+=1
        
                if (event.key == pygame.K_DOWN and position[x]>=0 and x!=0) or (event.key == pygame.K_DOWN and position[x]>0 and x==0):
                    position[x]-=1

                if event.key == pygame.K_LEFT and x>=0:
                    x-=1
                if event.key == pygame.K_RIGHT and x<3:
                    x+=1
                    if x==3:
                        function.draw(screen, function.list_adressb[36],(200,80))
                if event.key == pygame.K_RETURN and (position[x]==36 or position[x]==-1):
                    control = True
            print(position[x])
            if event.type == pygame.QUIT:
                sys.exit()
        for a in z:
            if position[int(a)]!=36 and position[int(a)]!=-1:
                if int(a) == x:
                    function.draw(screen, function.list_adressb[position[int(a)]],ubication[int(a)])
                else:
                    function.draw(screen, function.list_adress[position[int(a)]],ubication[int(a)])
            
        
    name=function.list_letters[position[0]]+function.list_letters[position[1]]+function.list_letters[position[2]]
    return(name)


def scores (screen,stop,points):
    score = points
    name=name_up(screen,score)
    function.draw(screen,"Image/wallpaper_score.png",(0,0))

    score_list = [["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9]]
    
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
    score_list2 = [["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9],["A",9]]
    x= y =0
    
    while y <= 9:
        if score > score_list[x][1] and x==y:
            score_list2[y][1]= score
            score_list2[y][0]= name
            y+= 1
        else:
            score_list2[y][1]= score_list[x][1]
            score_list2[y][0]= score_list[x][0]
            x +=1
            y +=1

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
    f = open('scores.txt','w')
    f.write(sanata)
    f.close()   

    while not stop:

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    stop = True
            if event.type == pygame.QUIT:
                sys.exit()
    