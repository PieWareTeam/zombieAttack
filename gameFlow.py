import pygame
import random
from settings import BG_WIDTH, BG_HEIGHT, HELICOPTER_UNLOCK_WAVE, BOSSES_ALLOWED, MAINCHAR_DEFAULT_SPEED, MAINCHAR_DEFAULT_REVIVEHEALTH, ZOMB_DEFAULT_SPEED, ZOMB_MAX_SPEED, ZOMB_MAX_HEALTH, ZOMB_DEFAULT_HEALTH, ZOMB_DEFAULT_DAMAGE, ZOMB_MAX_DAMAGE, BEGIN_WAVENUMBER, MAX_WAVE_CAPACITY, SPAWNRANGE, SPAWNRANGE_ADDITION, MAX_SPAWNRANGE, DIFFICULTY_ADDITION, BOSS_SPAWN_WAVE
from  image_lib import MAINCHARACTERMOVEMENTS, ZOMBIEMOVEMENTS, HELICOPTERMOVEMENTS
from characters import Maincharacter, Zombie, Helicopter

#HIER IMPLEMENTEER IK DE SPEL LOGICA ZOALS DE NIEUWE WAVES EN DE PLAYER EN ENEMY CONTROLS EN ANIMATIES


SPAWNED_ENEMIES = list()
SPAWNED_ZOMBIES = list()



def flyingAnimation(flyingMachine, opponent, sender, WIN):
    imageLib = ""
    imageName = ""


    if flyingMachine.id == "helicopter":
        if flyingMachine.shootingcount >= 23:
            flyingMachine.shootingcount = 0
            flyingMachine.endOfFlight(sender)
            for enemy in opponent:
                flyingMachine.dealDamage(enemy)
        flyingMachine.shootingcount += 1
        image_index = flyingMachine.shootingcount // 3
        imageName = f'fly{image_index}'
            
        imageLib = HELICOPTERMOVEMENTS[imageName]
        flyingMachine.fly()
        WIN.blit(flyingMachine.image, (flyingMachine.x, flyingMachine.y))

    if not imageName == "" and not imageLib == "":
        flyingMachine.image = pygame.transform.scale(imageLib, (flyingMachine.width, flyingMachine.height))



def dyingAnimation(character):
    imageLib = ""
    imageName = ""

    if character.id == "main":
        if character.dyingcount >= 49:
            character.isDying = False
            character.dyingcount = 0
        character.dyingcount += 1
        if character.isDying:
            image_index = character.dyingcount // 5
            imageName = f'dead{image_index}'
            
            imageLib = MAINCHARACTERMOVEMENTS[imageName]
        
    

    if character.id == "zombie":
        if character.dyingcount >= 59:
            character.isDying = False
            character.dyingcount = 0
        character.dyingcount += 1
        if character.isDying:
            image_index = character.dyingcount // 5
            if character.male:
                imageName = f'dead{image_index}'
            else:
                imageName = f'fdead{image_index}'
            
            imageLib = ZOMBIEMOVEMENTS[imageName]


    if not imageName == "" and not imageLib == "":
        character.image = pygame.transform.scale(imageLib, (character.width, character.height))



#wandel animatie functie
def walkingAnimation(character):
    imageLib = ""
    if character.id == "main":
        if character.walkingcount >= 49:
            character.walkingcount = 0
        character.walkingcount += 1
        image_index = character.walkingcount // 5
        if character.direction == 'right':
            imageName = f'walkRight{image_index}'
        else:
            imageName = f'walkLeft{image_index}'
        
        imageLib = MAINCHARACTERMOVEMENTS[imageName]
        
     

    if character.id == "zombie":
        if character.walkingcount >= 29:
            character.walkingcount = 0
        character.walkingcount += 1
        image_index = character.walkingcount // 5
        if character.male:
            if character.direction == 'right':
                imageName = f'walkRight{image_index}'
            else:
                imageName = f'walkLeft{image_index}'
        else:
            if character.direction == 'right':
                imageName = f'fwalkRight{image_index}'
            else:
                imageName = f'fwalkLeft{image_index}'
        
        imageLib = ZOMBIEMOVEMENTS[imageName]



    character.image = pygame.transform.scale(imageLib, (character.width, character.height))



#attack animatie functie
def attackAnimation(character, opponent, WIN=""):
    imageLib = ""
    if character.id == "main":
        if character.attackingcount >= 39:
            character.attackingcount = 0
            for enemy in opponent:
                character.dealDamage(enemy)
        character.attackingcount += 1
        image_index = character.attackingcount // 4
        if character.direction == 'right':
            imageName = f'attackRight{image_index}'
        else:
            imageName = f'attackLeft{image_index}'
        
        imageLib = MAINCHARACTERMOVEMENTS[imageName]
        
     

    if character.id == "zombie":
        if character.attackingcount >= 41:
            character.attackingcount = 0
            character.dealDamage(opponent)
        character.attackingcount += 1
        image_index = character.attackingcount // 6
        if character.male:
            if character.direction == 'right':
                imageName = f'attackRight{image_index}'
            else:
                imageName = f'attackLeft{image_index}'
        else:
            if character.direction == 'right':
                imageName = f'fattackRight{image_index}'
            else:
                imageName = f'fattackLeft{image_index}'
        
        imageLib = ZOMBIEMOVEMENTS[imageName]
    

    


    character.image = pygame.transform.scale(imageLib, (character.width, character.height))



#de player controls
def maincharacterControls(pressed_down_keys, maincharacter, zombieList, WIN):
    isWalking, isAttacking = False, False

    if maincharacter.isDying:
        dyingAnimation(maincharacter)
    elif not maincharacter.alive:
        maincharacter.image = MAINCHARACTERMOVEMENTS['dead9']
    else:
        #automatisch healen
        maincharacter.revive(WIN, maincharacter.revive_amount)
        
        #bepaal juiste image wanneer je stilstaat
        if maincharacter.direction == 'right':
            idle = pygame.transform.scale(MAINCHARACTERMOVEMENTS['idleRight'], (maincharacter.width, maincharacter.height))
        else:
            idle = pygame.transform.scale(MAINCHARACTERMOVEMENTS['idleLeft'], (maincharacter.width, maincharacter.height))
        
        #acties:
        
        #helicopter backup oproepen
        if pressed_down_keys[pygame.K_h]:
            maincharacter.callHelicopter()
        if maincharacter.spawnedhelicopter:
            flyingAnimation(maincharacter.spawnedhelicopter[0], zombieList, maincharacter, WIN)


        #aanvallen
        if pressed_down_keys[pygame.K_w] or pressed_down_keys[pygame.K_UP]: #attack
            isAttacking = True
        
        if isAttacking:
            attackAnimation(maincharacter, zombieList)
            

        #wandelen
        if not isAttacking:
            if pressed_down_keys[pygame.K_a] or pressed_down_keys[pygame.K_LEFT]: #left
                if not maincharacter.x <= 0:
                    maincharacter.direction = "left"
                    isWalking = True
            
            if pressed_down_keys[pygame.K_d] or pressed_down_keys[pygame.K_RIGHT]: #right
                if not (maincharacter.x + maincharacter.width) >= BG_WIDTH:
                    maincharacter.direction = "right"
                    isWalking = True
        
            if isWalking:
                maincharacter.walk()
                walkingAnimation(maincharacter)

            #springen
            if pressed_down_keys[pygame.K_SPACE]: #jump
                pass
    

        #maak player idle
        if not isWalking and not isAttacking:
            maincharacter.image = idle
            maincharacter.walkingcount = 0
            maincharacter.attackingcount = 0

    WIN.blit(maincharacter.image, (maincharacter.x, maincharacter.y))



#de zombie controls
def zombieControls(maincharacter, zombiecharacter, WIN):
    isWalking, isAttacking = False, False

    if zombiecharacter.isDying:
        dyingAnimation(zombiecharacter)
    elif not zombiecharacter.alive:
        if zombiecharacter.male:
            zombiecharacter.image = pygame.transform.scale(ZOMBIEMOVEMENTS['dead11'], (zombiecharacter.width, zombiecharacter.height))
        else:
            zombiecharacter.image = pygame.transform.scale(ZOMBIEMOVEMENTS['fdead11'], (zombiecharacter.width, zombiecharacter.height))
    else:
        #bepaal in welke richting de zombie loopt
        if maincharacter.middle <= zombiecharacter.middle:
            zombiecharacter.direction = 'left'
        else:
            zombiecharacter.direction = "right"


        #aanval logica
        if abs(maincharacter.middle - zombiecharacter.middle) <= zombiecharacter.attackrange: #attack
            isAttacking = True

        if isAttacking:
            attackAnimation(zombiecharacter, maincharacter)
            maincharacter.underAttack()
            zombiecharacter.walkingcount = 0
        else:
            maincharacter.isUnderAttack = False
            

        #wandelen
        if not isAttacking:
            zombiecharacter.walk()
            isWalking = True

            if isWalking:
                walkingAnimation(zombiecharacter)
                zombiecharacter.attackingcount = 0
        


    WIN.blit(zombiecharacter.image, (zombiecharacter.x, zombiecharacter.y))


#code die waves zal regelen
class Waves:
    def __init__(self, maincharacter, wavenumber=BEGIN_WAVENUMBER, bosses_allowed=BOSSES_ALLOWED, bossspawnwave=BOSS_SPAWN_WAVE, helicopterunlockwave=HELICOPTER_UNLOCK_WAVE, difficultyaddition=DIFFICULTY_ADDITION, maxwavecapacity=MAX_WAVE_CAPACITY, spawnrange=SPAWNRANGE, maxspawnrange=MAX_SPAWNRANGE, spawnrangeaddition=SPAWNRANGE_ADDITION):
        self.wavenumber = wavenumber
        
        self.enemiesalive = False
        self.livingzombies = list()
        
        self.min_damage = ZOMB_DEFAULT_DAMAGE
        self.max_damage = ZOMB_MAX_DAMAGE
        self.min_health = ZOMB_DEFAULT_HEALTH
        self.max_health = ZOMB_MAX_HEALTH
        self.min_speed = ZOMB_DEFAULT_SPEED
        self.max_speed = ZOMB_MAX_SPEED
        self.maxwavecapacity = maxwavecapacity
        
        self.helicopterunlockwave = helicopterunlockwave

        self.maincharacter = maincharacter

        self.difficultyaddition = difficultyaddition
        self.maxspawnrange = maxspawnrange
        self.spanwrangeaddition = spawnrangeaddition
        
        self.wavecapacity = 2 * self.wavenumber
        
        
        self.spawnrange = spawnrange
        self.bosses_allowed = bosses_allowed
        self.bosspawnwave = bossspawnwave
        if bosses_allowed:
            self.bosspawnwave = self.wavenumber
        
        self.increaseDifficulty(True)
        self.spawnZombies()


    def increaseWavenumber(self, number):
        self.wavenumber += number

    def spawnZombies(self):
        for i in range(1, self.wavecapacity):
            #pick zombie gender
            gender = False
            num1 = random.randint(1,10)
            if num1 % 2:
                gender = True

            #pick damage
            damage = random.randint(self.min_damage, self.max_damage)
            
            #pick health
            health = random.randint(self.min_health, self.max_health)

            #pick speed
            speed = random.randint(self.min_speed, self.max_speed)

            #pick spawnpoint
            x = random.randint(BG_WIDTH, self.spawnrange)

            #pick boss or normal
            boss = False
            if self.bosses_allowed:
                num2 = random.randint(1, 100)
                if num2 % 25 == 0:
                    boss = True
            
            #maak de zombie
            zombie = Zombie(boss, gender, speed, health, damage, x)
            self.livingzombies.append(zombie)
        


    def removeDeadZombies(self):
        self.livingzombies = [x for x in self.livingzombies if x.alive]
    
    def increaseDifficulty(self, firstwave=False):
        if not firstwave:
            #verhoog wave nummer
            self.increaseWavenumber(1)
        #maak zombies sterker
        self.max_health += self.difficultyaddition
        self.min_health += self.difficultyaddition
        self.max_damage += self.difficultyaddition
        self.min_damage += self.difficultyaddition
        #vergroot wavecapacity
        self.wavecapacity = self.wavenumber + 2
        if self.wavecapacity >= self.maxwavecapacity:
                self.wavecapacity = self.maxwavecapacity
        #vergroot spawn oppervlakte
        self.spawnrange += self.spanwrangeaddition
        if self.spawnrange >= self.maxspawnrange:
            self.spawnrange = self.maxspawnrange
        #kijk of bosses mogen spawnen vanaf deze wave
        if self.wavenumber >= self.bosspawnwave:
            self.bosses_allowed = True
        #kijk of player helicopters mag oproepen
        if self.wavenumber >= self.helicopterunlockwave:
            self.maincharacter.helicopters += 1
        