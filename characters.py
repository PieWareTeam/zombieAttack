import pygame
import os
from settings import BG_WIDTH, MAINCHAR_DEFAULT_HELICOPTERS, MAINCHAR_DEFAULT_WIDTH, MAINCHAR_DEFAULT_HEIGHT, MAINCHAR_DEFAULT_HEALTH, MAINCHAR_DEFAULT_REVIVEHEALTH, MAINCHAR_DEFAULT_DAMAGE, MAINCHAR_DEFAULT_SPEED, MAINCHAR_DEFAULT_ATTACKRANGE, MAINCHAR_DEFAULT_POSX, MAINCHAR_DEFAULT_POSY, MAINCHAR_DEFAULT_DIRECTION
from settings import ZOMB_DEFAULT_WIDTH, ZOMB_DEFAULT_HEIGHT, ZOMB_DEFAULT_HEALTH, ZOMB_DEFAULT_DAMAGE, ZOMB_DEFAULT_SPEED, ZOMB_DEFAULT_POSX, ZOMB_DEFAULT_POSY, ZOMB_DEFAULT_ATTACKRANGE, ZOMB_DEFAULT_DIRECTION
from settings import ZOMB_BOSS_WIDTH, ZOMB_BOSS_HEIGHT, ZOMB_BOSS_HEALTH, ZOMB_BOSS_DAMAGE, ZOMB_BOSS, ZOMB_BOSS_SPEED, ZOMB_BOSS_POSX, ZOMB_BOSS_POSY, ZOMB_BOSS_ATTACKRANGE, ZOMB_MALE
from settings import HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT, HELICOPTER_DEFAULT_ATTACKRANGE, HELICOPTER_DEFAULT_DAMAGE, HELICOPTER_DEFAULT_SPEED, HELICOPTER_DEFAULT_POSX, HELICOPTER_DEFAULT_POSY

#HIER IMPLEMENTEER IK DE KLASSEN VAN DE PLAYER EN ELKE ENEMY




#special backup
class Helicopter:
    def __init__(self, speed=HELICOPTER_DEFAULT_SPEED, x=HELICOPTER_DEFAULT_POSX, y=HELICOPTER_DEFAULT_POSY, attackrange=HELICOPTER_DEFAULT_ATTACKRANGE, damage=HELICOPTER_DEFAULT_DAMAGE, width=HELICOPTER_DEFAULT_WIDTH, height=HELICOPTER_DEFAULT_HEIGHT):
        self.speed = speed
        self.width = width
        self.height = height

        self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join('helicopter', 'frame_0_delay-0.03s.png')), (HELICOPTER_DEFAULT_WIDTH, HELICOPTER_DEFAULT_HEIGHT)), True, False)
        
        self.x = x
        self.middle = self.x + (self.width//2)
        self.y = y
        
        self.damage = damage
        self.attackrange = attackrange
        
        self.shootingcount = 0

        self.id = "helicopter"
    
    def fly(self):
        self.x += self.speed
        self.middle = self.x + (self.width//2)
        

    def dealDamage(self, character):
        if self.middle <= character.middle and self.middle + self.attackrange >= character.middle:
            character.damaged(self.damage)

    def endOfFlight(self, sender):
        if self.x >= BG_WIDTH:
            sender.spawnedhelicopter.pop()

#maincharacter
class Maincharacter:
    def __init__(self, speed=MAINCHAR_DEFAULT_SPEED, x=MAINCHAR_DEFAULT_POSX, y=MAINCHAR_DEFAULT_POSY,helicopters=MAINCHAR_DEFAULT_HELICOPTERS, direction=MAINCHAR_DEFAULT_DIRECTION, width=MAINCHAR_DEFAULT_WIDTH, height=MAINCHAR_DEFAULT_HEIGHT, attackrange=MAINCHAR_DEFAULT_ATTACKRANGE, health=MAINCHAR_DEFAULT_HEALTH, revive_amount=MAINCHAR_DEFAULT_REVIVEHEALTH, damage=MAINCHAR_DEFAULT_DAMAGE):
        self.width = width
        self.height = height
        
        self.health = health
        self.maxhealth = self.health
        self.health_bar_length = self.width
        self.healthbar_height = 5
        self.health_ratio = self.maxhealth / self.health_bar_length
        self.revive_amount = revive_amount
        self.revivecount = 0

        self.damage = damage
        self.speed = speed
        self.attackrange = attackrange

        self.helicopters = helicopters
        self.spawnedhelicopter = list()
        
        self.id = 'main'
        
        self.x = x
        self.y = y
        self.direction = direction
        self.middle = self.x + (self.width//2)

        self.alive = True
        self.isDying = False
        
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("mainchar_ani", 'idle (1).png')), (self.width, self.height))

        

        self.walkingcount = 0
        self.attackingcount = 0
        self.dyingcount = 0   

    def walk(self):
        if self.direction == 'right':
            self.x += self.speed
        else:
            self.x -= self.speed
        self.middle = self.x + (self.width//2)
    
    def dealDamage(self, character):
        if abs(character.middle - self.middle) <= self.attackrange:
            character.damaged(self.damage)
    
    def damaged(self, damage):
        if self.alive:
            if self.health >= 0:
                self.health -= damage
            
            if self.health < 0:
                self.health = 0
                self.isDying = True
                self.alive = False

    def revive(self, WIN, amount):
        if self.revivecount >= 30:
            self.revivecount = 0
            self.health += amount
            if self.health > self.maxhealth:
                self.health = self.maxhealth
        self.revivecount += 1
            
        self.healthbar(WIN)
    
    def healthbar(self, WIN):
        pygame.draw.rect(WIN, (0, 255, 0), (self.x, self.y - (self.height//5), self.health/self.health_ratio, self.healthbar_height))
        pygame.draw.rect(WIN, (255, 255, 255), (self.x, self.y - (self.height//5), self.health_bar_length, self.healthbar_height),1)

    def underAttack(self):
        self.revivecount = 0
    
    def callHelicopter(self):
        if self.helicopters > 0 and len(self.spawnedhelicopter) == 0:
            self.helicopters -= 1
            self.spawnedhelicopter.append(Helicopter())


#enemies

class Zombie:
    def __init__(self, boss=ZOMB_BOSS, male=ZOMB_MALE, speed=ZOMB_DEFAULT_SPEED, health=ZOMB_DEFAULT_HEALTH, damage=ZOMB_DEFAULT_DAMAGE, x=ZOMB_DEFAULT_POSX, y=ZOMB_DEFAULT_POSY, width=ZOMB_DEFAULT_WIDTH, height=ZOMB_DEFAULT_HEIGHT, direction=ZOMB_DEFAULT_DIRECTION, attackrange=ZOMB_DEFAULT_ATTACKRANGE):
        self.givenValues = {
            "width" : width,
            "height" : height,
            "health" : health,
            "damage" : damage,
            "speed" : speed,
            "male" : male,
            "attackrange": attackrange,
            "y" : y,
        }
        self.x  = x
        self.direction = direction
        
        self.id = "zombie"
        
        if boss:
            self.becomeBoss()
        else:
            self.becomeNormal()
        
        self.alive = True
        self.isDying = False
        
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("zombie_m_ani", 'idle (1).png')), (self.width, self.height))
        
        

        self.walkingcount = 0
        self.attackingcount = 0
        self.dyingcount = 0
        
        
    def becomeBoss(self):
        self.width = ZOMB_BOSS_WIDTH
        self.height = ZOMB_BOSS_HEIGHT
        
        self.health = ZOMB_BOSS_HEALTH
        
        self.damage = ZOMB_BOSS_DAMAGE
        
        self.speed = ZOMB_BOSS_SPEED
        
        self.attackrange = ZOMB_BOSS_ATTACKRANGE
        
        self.y = ZOMB_BOSS_POSY
        self.middle = self.x + (self.width//2)
        
        self.male = self.givenValues["male"]
        self.boss =  True
        self.alive = True
        self.isDying = False
        

    def becomeNormal(self):
        self.width = self.givenValues["width"]
        self.height = self.givenValues["height"]
        self.health = self.givenValues["health"]
        self.damage = self.givenValues["damage"]
        self.male = self.givenValues["male"]
        self.speed = self.givenValues["speed"]
        self.attackrange = self.givenValues["attackrange"]
        self.y = self.givenValues["y"]
        self.boss = False
        self.alive = True
        self.middle = self.x + (self.givenValues["width"]//2)

    def walk(self):
        if self.direction == 'right':
            self.x += self.speed
        else:
            self.x -= self.speed
        self.middle = self.x + (self.width//2)
    
    def dealDamage(self, character):
        if abs(character.middle - self.middle) <= self.attackrange:
            character.damaged(self.damage)

    def damaged(self, damage):
        if self.alive:
            if self.health >= 0:
                self.health -= damage
            
            if self.health < 0:
                self.health = 0
                self.isDying = True
                self.alive = False
