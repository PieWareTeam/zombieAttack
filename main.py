import pygame
import os
import sys
from characters import Maincharacter, Zombie
from background import Background
from image_lib import BACKGROUNDANIMATIONS
from gameFlow import maincharacterControls, zombieControls, Waves
pygame.init()

FPS = 60
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
BACKGROUND = Background()


#func die background animeert
def backGroundAni(bg):
    if bg.change_image_count >= 63:
        bg.change_image_count = 0
    bg.change_image_count += 1
    image_index = bg.change_image_count // 8
    WIN.blit(BACKGROUNDANIMATIONS[f'bg{image_index}'], (0, 0))


#func die scherm beschrijft
def defineScreen(pressed_down_keys, maincharacter, livingzombies):
    backGroundAni(BACKGROUND)

    #roep zombie controls op
    for zombie in livingzombies:
        zombieControls(maincharacter, zombie, WIN)

    #roep maincharacter controls op
    maincharacterControls(pressed_down_keys, maincharacter, livingzombies, WIN)
    
    #update scherm
    pygame.display.update()


def startNewWave(wave, firstwave=False):
    wave.increaseDifficulty(firstwave)
    wave.spawnZombies()


def mainFunc():
    #maak players character
    maincharacter = Maincharacter()

    #start eertse wave
    wave = Waves(maincharacter)
    startNewWave(wave, True)
    livingzombies = wave.livingzombies

    clock = pygame.time.Clock()
    run = True
    
    
    #de gameloop die FPS variable keer refreshed per seconde
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pressed_down_keys = pygame.key.get_pressed()

        #start nieuwe wave
        wave.removeDeadZombies()
        if len(wave.livingzombies) == 0:
            startNewWave(wave)
            livingzombies = wave.livingzombies
        
        defineScreen(pressed_down_keys, maincharacter, livingzombies)

    pygame.quit()


if __name__ == "__main__":
    mainFunc()
