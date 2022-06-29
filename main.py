import pygame, sys
import funtion, game

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((1280,720),pygame.RESIZABLE)  #cambiar pygame.RESIZABLE por pygame.FULLSCREEN
pygame.display.set_caption("Juego")
window.fill((0,0,0))

run = True
game_over = False
start = False
reboot = False

while run:

    funtion.inicio(window,start)

    game.game(window,game_over)

    funtion.scores(window,reboot)        
    
    game_over = False
    start = False
    reboot = False    