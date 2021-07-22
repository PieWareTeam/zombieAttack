import pygame
import os
from settings import BG_WIDTH, BG_HEIGHT
from settings import PORTAL_WIDTH, PORTAL_HEIGHT
from settings import MAINCHAR_DEFAULT_HEIGHT, MAINCHAR_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT, ZOMB_DEFAULT_WIDTH
from settings import HELICOPTER_DEFAULT_HEIGHT, HELICOPTER_DEFAULT_WIDTH

#HIER WORDEN ALLE MOGELIJKE AFBEELDINGEN OPGESLAAN IN DICTIONARIES

#player images
FOLDER = "mainchar_ani"

MAINCHARACTERMOVEMENTS = {
    'idleRight': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'idle (1).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'idleLeft': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'idle (1).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft0': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (1).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft1': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (2).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False) ,
    'walkLeft2': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (3).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft3': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (4).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False) ,
    'walkLeft4': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (5).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft5': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (6).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft6': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (7).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft7': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (8).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft8': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (9).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'walkLeft9': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (10).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),

    'walkRight0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (1).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (2).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (3).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (4).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (5).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (6).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (7).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight7': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (8).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight8': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (9).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'walkRight9': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Run (10).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),

    'attackLeft0': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (1).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft1': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (2).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft2': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (3).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft3': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (4).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft4': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (5).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft5': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (6).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft6': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (7).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft7': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (8).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft8': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (9).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),
    'attackLeft9': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (10).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)), True, False),

    'attackRight0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (1).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (2).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (3).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (4).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (5).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (6).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (7).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight7': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (8).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight8': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (9).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'attackRight9': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Attack (10).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),

    'dead0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (1).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (2).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (3).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (4).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (5).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (6).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (7).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead7': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (8).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead8': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (9).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),
    'dead9': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER, 'Dead (10).png')), (MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT)),


}

#zombie images
FOLDER3 = "zombie_m_ani"
FOLDER32 = "zombie_f_ani"

ZOMBIEMOVEMENTS = {
    #male
    'idleRight': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'idle (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'idleLeft': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'idle (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'walkLeft0': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'walkLeft1': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False) ,
    'walkLeft2': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'walkLeft3': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False) ,
    'walkLeft4': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'walkLeft5': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'walkLeft6': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    
    'walkRight0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'walkRight1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'walkRight2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'walkRight3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'walkRight4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'walkRight5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'walkRight6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Run (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    
    'attackLeft0': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'attackLeft1': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'attackLeft2': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'attackLeft3': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'attackLeft4': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'attackLeft5': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'attackLeft6': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    
    'attackRight0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'attackRight1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'attackRight2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'attackRight3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'attackRight4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'attackRight5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'attackRight6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Attack (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),

    'dead0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead7': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (8).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead8': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (9).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead9': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (10).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead10': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (11).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'dead11': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER3, 'Dead (12).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    
    #female
    'fidleRight': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'idle (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fidleLeft': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'idle (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fwalkLeft0': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fwalkLeft1': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False) ,
    'fwalkLeft2': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fwalkLeft3': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False) ,
    'fwalkLeft4': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fwalkLeft5': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fwalkLeft6': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    
    'fwalkRight0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fwalkRight1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fwalkRight2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fwalkRight3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fwalkRight4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fwalkRight5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fwalkRight6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Run (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    
    'fattackLeft0': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fattackLeft1': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fattackLeft2': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fattackLeft3': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fattackLeft4': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fattackLeft5': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    'fattackLeft6': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)), True, False),
    
    'fattackRight0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fattackRight1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fattackRight2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fattackRight3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fattackRight4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fattackRight5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fattackRight6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Attack (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),

    'fdead0': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (1).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead1': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (2).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead2': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (3).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead3': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (4).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead4': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (5).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead5': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (6).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead6': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (7).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead7': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (8).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead8': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (9).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead9': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (10).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead10': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (11).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),
    'fdead11': pygame.transform.scale(pygame.image.load(os.path.join(FOLDER32, 'Dead (12).png')), (ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT)),

    
}

FOLDER4 = 'helicopter'

HELICOPTERMOVEMENTS = {
    'fly0': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_0_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    'fly1': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_1_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    'fly2': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_2_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    'fly3': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_3_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    'fly4': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_4_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    'fly5': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_5_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    'fly6': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_6_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    'fly7': pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(FOLDER4, 'frame_7_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False),
    
}





#extra images zoals backgrounds, portals, ...
#PORTALANIMATIONS = {
    #'portal0': pygame.transform.scale(pygame.image.load(os.path.join('gamefeatures', 'portal (1).png')), (PORTAL_WIDTH, PORTAL_HEIGHT)),
    #'portal1': pygame.transform.scale(pygame.image.load(os.path.join('gamefeatures', 'portal (2).png')), (PORTAL_WIDTH, PORTAL_HEIGHT)),
    #'portal2': pygame.transform.scale(pygame.image.load(os.path.join('gamefeatures', 'portal (3).png')), (PORTAL_WIDTH, PORTAL_HEIGHT)),
#}


#background images
BACKGROUNDANIMATIONS = {
    'bg0': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_0_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
    'bg1': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_1_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
    'bg2': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_2_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
    'bg3': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_3_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
    'bg4': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_4_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
    'bg5': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_5_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
    'bg6': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_6_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
    'bg7': pygame.transform.scale(pygame.image.load(os.path.join('backgrounds', 'frame_7_delay-0.1s.png')), (BG_WIDTH, BG_HEIGHT)),
}
