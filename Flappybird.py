import Random
import sys
import pygame
from pygame.locals import *


#Global Variables
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}

#PLAYER = ''
#BACKGROUND = ''
#PIPE = ''

def WelcomeScreen():
    '''
    Shows welcome images on the screen
    '''
playerx=int((SCREENWIDTH / 5))
playery=int((SCREENHEIGHT - GAME_SPRITES ['player'].get_height())/2)
messagex=int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/12)
messagey=int(SCREENHEIGHT*0.13)
basex=0

while True:
    for event in pygame.event.get():
        #if user clicks on cross button, close the game
        if event.type== QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
            return
        else:
            SCREEN.blit(GAME_SPRITES['background'], ((0,0)))
            SCREEN.blit(GAME_SPRITES['player'],([playerx,playery]))
            SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
            SCREEN.blit(GAME_SPRITES['base'], (basex,GROUNDY))

    pygame.display.update()
    FPSCLOCK.tick(FPS)
    
    def mainGame():
        score = 0
    playerx = int(SCREENWIDTH /5)
    playery= int(SCREENWIDTH /2)
    basex = 0

    #creating 2 pipes for blitting on the screen

    newpipe1= getRandomPipe()
    newpipe2= getRandomPipe()

    #my list of upper pipes

    UpperPipes = [
        {"x": SCREENWIDTH + 200, "y": newpipe1[0]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2),"y": newpipe2[1]["y"]},
    ]
#my list of lower pipes
    lowerpipes=[
        {"x": SCREENWITDH +200,"y": newpipe1[1]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH /2),"y": newpipe2[1]["y"]},
    ]
    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = -8
    playerFlapAccv = -8 #velocity while flapping
    playerFlapped= False #It is only true when the bird is flapping
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key== K_ESCAPE):
                pygame.QUIT()
        sys.exit()
        if event.type == KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
            if player >0:
                playerVelY=playerFlapAccv
                playerFlapped=True
                GAME_SOUNDS['wing'].play()
        CrashTest = iscollide(playerx,playery,UpperPipes,lowerpipes) #This function will return if the player or the bird is crashed
        if CrashTet:
            True
        PlayerMidPos=palyerx + GAME_SPRITES ['player'].get_width()/2

        for pipe in upperpipes:
            PipeMidPos=pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if PipeMidPos <= PlayerMidPos < PipeMidPos +4:
                score += 1
                print ("Your Score Is: ,")(score)
                GAME_SOUNDS['point'].play()

        if player < playerMaxVelY and not PlayerFlapped:
            playerVely += playerAccy 
        if playerFlapped:
            playerFlapped=False
            playerheight = GAME_SPRITES ['player'].get_height()
            playery = playery + min (playerVelY, GROUNDY_PlayerY - playerheight)
        # move pipes in the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes): upperPipe ['x'] += pipeVelX
        lowerpipe['x'] += pipeVelX