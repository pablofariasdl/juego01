import pygame, sys
import function

def scores (screen,stop):
    function.draw(screen,"Image/wallpaper_score.png",(0,0))

    score = 3000000
    
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
            score_list2[y][0]= "ZZZ"
            y= y+1
        else:
            score_list2[y][1]= score_list[x][1]
            score_list2[y][0]= score_list[x][0]
            x = x+1
            y = y+1
    
    name=""
    point=""
    for dato in score_list2:
        name += dato[0]+" "
        point += str(dato[1])+" "
    sanata= name +"\n"+point 
    print(sanata)

    while not stop:

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    stop = True
            if event.type == pygame.QUIT:
                sys.exit()
    