#import pprint
import pygame
pygame.init()

Screen_Hight = 1000
Screen_width = 1800
screen = pygame.display.set_mode((Screen_width,Screen_Hight))

class movable(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,top,back,width,height):
        super().__init__(top,back,width,height)
        self.tx = back
        self.ty = top
    health = 4
    invulnrabilityc = 0
    hidden = False
    
    def move_ip(self,deltaX:float,deltaY:float):
        self.tx = self.tx+deltaX
        self.ty = self.ty+deltaY
        selfAsRect = super()
        selfAsRect.move_ip(round(self.tx)-selfAsRect.x,round(self.ty)-selfAsRect.y)
        print("moved to "+str(self.tx)+","+str(self.ty))


jcool = 0
ymom = 0
dcool = 0
xmom = 0
slashc = 0
sldammage = 1
level = 0
max_soul = 100
soul_gain = 1
invulnrability = 0
soul = 100
jumps = 0
s1f = True
soulc = 0
xposition = 900
yposition = 500
player = pygame.Rect(xposition,yposition,50,50)
enemy1 = movable(900,800,50,100)
enemy2 = movable(2300,390,50,100)
#map instanciacion
floort = pygame.Rect(0,980,3000,20)
backboard = pygame.Rect(0,0,50,1100)
roof = pygame.Rect(0,0,2000,50)
fwall = pygame.Rect(3000,200,50,1400)
invis_secret = pygame.Rect(3000,-300,500,600)
invis_sfloort = pygame.Rect(3000,200,500,50)
bwall = pygame.Rect(2000,-600,50,800)
plat1 = pygame.Rect(2000,800,150,50)
tplat1 = pygame.Rect(2000,795,150,5)
plat2 = pygame.Rect(2200,500,150,50)
tplat2 = pygame.Rect(2200,495,150,5)
plat3 = pygame.Rect(2400,200,150,50)
tplat3 = pygame.Rect(2400,195,150,5)
plat4 = pygame.Rect(2600,-100,150,50)
tplat4 = pygame.Rect(2600,-105,150,5)
floort2 = pygame.Rect(3000,-300,3000,50)
fiwall = pygame.Rect(6000,-1400,50,1100)
soulbar = pygame.Rect(30,50,100,20)
secret = pygame.Rect(3200,0,50,50)
slash = movable(0,0,20,40)
ifloort = pygame.Rect(0,1000,2000,50)
ibackwall = pygame.Rect(0,0,50,1000)
objects = [ibackwall]
tobjects = [ifloort]
enemies = []
noncols = []

run = True



while run:
    if soul<1:
        run = False
    

    screen.fill((255,255,255))

    pygame.draw.circle(screen,(255,0,0),player.center,40)

    if level == 1:
        if not floort in tobjects:
            objects.append[backboard,roof,fwall,bwall,plat1,plat2,plat3,plat4,fiwall]
            tobjects.append[floort,tplat1,tplat2,tplat3,tplat4,floort2,invis_sfloort]
            enemies.append[enemy1,enemy2]
        
        pygame.draw.rect(screen,(0,0,0),floort)
        pygame.draw.rect(screen,(0,0,0),backboard)
        pygame.draw.rect(screen,(0,0,0),roof)
        pygame.draw.rect(screen,(0,0,0),fwall)
        pygame.draw.rect(screen,(0,0,0),bwall)
        pygame.draw.rect(screen,(0,0,0),plat1)
        pygame.draw.rect(screen,(0,0,0),tplat1)
        pygame.draw.rect(screen,(0,0,0),plat2)
        pygame.draw.rect(screen,(0,0,0),tplat2)
        pygame.draw.rect(screen,(0,0,0),plat3)
        pygame.draw.rect(screen,(0,0,0),tplat3)
        pygame.draw.rect(screen,(0,0,0),plat4)
        pygame.draw.rect(screen,(0,0,0),tplat4)
        pygame.draw.rect(screen,(0,0,0),floort2)
        pygame.draw.rect(screen,(0,0,0),fiwall)
        pygame.draw.rect(screen,(200,200,200),soulbar,soul)
        pygame.draw.rect(screen,(20,20,20),invis_secret)
        pygame.draw.rect(screen,(20,20,20),invis_sfloort)
        if s1f == True:
            pygame.draw.rect(screen,(150,150,150),secret)
        if slashc > 150:
            slash.hidden = False
            if facing == 1:
                slash.x=player.right+15
            else:
                slash.x=player.left-30
            slash.y = yposition
            pygame.draw.rect(screen,(0,0,0),slash)
        else:
            slash.hidden = True
    
#        objects.clear
#        tobjects.clear
#        enemies.clear
    elif level == 0:
        pygame.draw.rect(screen,(0,0,0),ifloort)
        pygame.draw.rect(screen,(0,0,0),ibackwall)



    # Check if we're on the screen
    if player.x<0:
        player.x = Screen_width - 10
    if player.x>Screen_width:
        player.x = 10
    if player.y>Screen_Hight:
        player.y = 10
    if player.y<0:
        player.y = Screen_Hight - 10
    
    
    def col():
        i = 0
        colliding = False
        while i < len(objects) and colliding == False:
            if player.colliderect(objects[i]) == True:
                colliding = True
            i=1 + i
        return colliding
    
    
    def bcol():
        n = 0
        bottomcol = False
        while n < len(objects) and bottomcol == False:
            if player.top < objects[n].bottom + 10:
                bottomcol = True
        return bottomcol
        

        
    def colt():
        d = 0
        collided = False
        while d < len(tobjects) and collided == False:
            if player.colliderect(tobjects[d]) == True:
                collided = True
            d=1 + d

        return collided

    def moveObjsX(objectsList,x):
        l=0
        if col() == False:
            while l < len(objectsList):
                objectsList[l].move_ip(x,0)
                l+=1
        else:
            l = 0
            while l < len(objectsList):
                objectsList[l].move_ip(-x,0)
                l+=1

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        #xposition=xposition-.1
        moveObjsX(objects + tobjects + enemies + noncols,1)
        facing = 0

    if key[pygame.K_d] == True:
        #xposition=xposition+.1
        moveObjsX(objects + tobjects + enemies + noncols,-1)
        facing = 1
    if key[pygame.K_e] == True and slashc < 1:
        slashc = 200


    if colt() == False and col() == False:
        if ymom < 1:
            ymom += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if key[pygame.K_SPACE] == True and (colt() == True or col() == True) and jcool < 1:
        ymom = -10
        jumps = 1
        jcool = 250
    elif key[pygame.K_SPACE] == True and soul > 30 and jumps >0 and jcool < 1:
        ymom = -10
        jumps = 0
        soul-=30


    if key[pygame.K_q] == True and soul > 40 and dcool < 1:
        if facing == 0:
            xmom = 12
        if facing == 1:
            xmom = -12
        soul -= 40
        dcool = 100
    if not xmom == 0:
        moveObjsX(objects + tobjects + enemies + noncols,xmom)
        if xmom > 0:
            xmom-=0.2
        else:
            xmom+=0.2
        if xmom > -1 and xmom < 1:
            xmom = 0
    else:
        if col() == False and colt() == False:
            for thobject in objects+tobjects+enemies+noncols:
                thobject.move_ip(0,ymom * -1)
        else:
            if colt() == True:
                if ymom < 0:
                    for thobject in objects+tobjects+enemies+noncols:
                        thobject.move_ip(0,ymom * -1)
            elif bcol() == True:
                print("bottom col")
                for thobject in objects+tobjects+enemies+noncols:
                    thobject.move_ip(0,-1)

    for anEnemy in enemies:
        if anEnemy.health > 0:
            pygame.draw.rect(screen,(255,0,0),anEnemy)
            if xposition > anEnemy.centerx - 400 and xposition < anEnemy.centerx + 500 and not anEnemy.colliderect(player):
                if anEnemy.centerx<player.left:
                    anEnemy.move_ip(.5,0)
                else:
                    anEnemy.move_ip(-.5,0)
            cold = 0
            for atobject in tobjects:
                if not anEnemy.colliderect(atobject):
                    cold += 1
                else:
                    anEnemy.move_ip(0,-1)
                if anEnemy.colliderect(player) and soul > -100 and invulnrability < 1:
                    soul-=1
                    invulnrability = 7
            if cold == len(tobjects):
                anEnemy.move_ip(0,1)
                print(str(anEnemy)+" is falling.")
            if anEnemy.colliderect(slash) and anEnemy.invulnrabilityc < 1 and slash.hidden == False:
                anEnemy.health-=sldammage
                anEnemy.invulnrabilityc=50
                if xposition < anEnemy.centerx:
                    anEnemy.move_ip(8,0)
                else:
                    anEnemy.move_ip(-8,0)
            anEnemy.invulnrabilityc-=1
        else:
            enemies.remove(anEnemy)

    
    if player.colliderect(secret):
        if secret in noncols:
            noncols.remove(secret)
            max_soul+=20
            soul_gain+=1
            s1f = False
    
    
    jcool-=1
    soulc-=1
    slashc-=1
    invulnrability-=1
    dcool-=1
    if soulc < 1 and soul < max_soul:
        soul+=soul_gain
        soulc = 10
    soulbar.width = soul

    pygame.display.update()

pygame.quit()