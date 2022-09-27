import pygame, sys
import function, menu, game, score

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((1280,720),pygame.RESIZABLE)  #cambiar pygame.RESIZABLE por pygame.FULLSCREEN
pygame.display.set_caption("Juego")
window.fill((0,0,0))

run = True
game_over = False
stop = False
reboot = False

while run:

    menu.start(window,stop)

    points = game.game(window,game_over)

    score.scores(window,reboot,points)        
    
    game_over = False
    stop = False
    reboot = False       
    