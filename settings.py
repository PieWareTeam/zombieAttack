import pygame
import os
pygame.init()

#BACKROUND SETTINGS
infoObject = pygame.display.Info()
BG_WIDTH, BG_HEIGHT = infoObject.current_w, infoObject.current_h


#PORTAL SETTINGS
PORTAL_WIDTH, PORTAL_HEIGHT = 200, 200


#WAVE SETTINGS
BEGIN_WAVENUMBER = 1
MAX_WAVE_CAPACITY = 50

BOSSES_ALLOWED = False
BOSS_SPAWN_WAVE = 8
HELICOPTER_UNLOCK_WAVE = 8

SPAWNRANGE = BG_WIDTH * BEGIN_WAVENUMBER
SPAWNRANGE_ADDITION = BG_WIDTH//4
MAX_SPAWNRANGE = BG_WIDTH * 15

#hoeveel sterker de vijanden worden per wave
DIFFICULTY_ADDITION = 1


#PLAYER EN ENEMY SETTINGS

#Maincharacter default values
MAINCHAR_DEFAULT_WIDTH = 100
MAINCHAR_DEFAULT_HEIGHT = 100
MAINCHAR_DEFAULT_HEALTH = 150
MAINCHAR_DEFAULT_REVIVEHEALTH = MAINCHAR_DEFAULT_HEALTH / 10
MAINCHAR_DEFAULT_DAMAGE = 8
MAINCHAR_DEFAULT_SPEED = 5
MAINCHAR_DEFAULT_ATTACKRANGE = 55

MAINCHAR_DEFAULT_DIRECTION = "right"

MAINCHAR_DEFAULT_HELICOPTERS = 0

MAINCHAR_DEFAULT_POSX = 0
MAINCHAR_DEFAULT_POSY = BG_HEIGHT - MAINCHAR_DEFAULT_HEIGHT



#zombie default values
ZOMB_BOSS = False
ZOMB_MALE = False
ZOMB_DEFAULT_DIRECTION = "left"

ZOMB_DEFAULT_WIDTH = 100
ZOMB_DEFAULT_HEIGHT = 100
ZOMB_DEFAULT_HEALTH = 30
ZOMB_MAX_HEALTH = ZOMB_DEFAULT_HEALTH * 2
ZOMB_DEFAULT_DAMAGE = 2
ZOMB_MAX_DAMAGE = ZOMB_DEFAULT_DAMAGE + 2
ZOMB_DEFAULT_SPEED = 2
ZOMB_MAX_SPEED = MAINCHAR_DEFAULT_SPEED - 1
ZOMB_DEFAULT_ATTACKRANGE = 50

ZOMB_DEFAULT_POSX =  BG_WIDTH
ZOMB_DEFAULT_POSY = BG_HEIGHT - ZOMB_DEFAULT_HEIGHT

ZOMB_BOSS_WIDTH = 200
ZOMB_BOSS_HEIGHT = 200
ZOMB_BOSS_HEALTH = 300
ZOMB_BOSS_DAMAGE = 30
ZOMB_BOSS_SPEED = 1
ZOMB_BOSS_ATTACKRANGE = 50

ZOMB_BOSS_POSX =  BG_WIDTH
ZOMB_BOSS_POSY = BG_HEIGHT - ZOMB_BOSS_HEIGHT


#helicopter settings
HELICOPTER_DEFAULT_WIDTH = 200
HELICOPTER_DEFAULT_HEIGHT = 200

HELICOPTER_DEFAULT_DAMAGE = 130
HELICOPTER_DEFAULT_ATTACKRANGE = 350
HELICOPTER_DEFAULT_SPEED = 10

HELICOPTER_DEFAULT_POSX = 0 - HELICOPTER_DEFAULT_WIDTH
HELICOPTER_DEFAULT_POSY = BG_HEIGHT - HELICOPTER_DEFAULT_HEIGHT * 1.5


#mech settings

#Mech1
MECH_DEFAULT_WIDTH = 200
MECH_DEFAULT_HEIGHT = 200
MECH_DEFAULT_HEALTH = 1000
MECH_DEFAULT_DAMAGE = 10
MECH_DEFAULT_SPEED = MAINCHAR_DEFAULT_SPEED
