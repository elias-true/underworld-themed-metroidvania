#import pprint
import pygame
pygame.init()
import time as timekeep
import random

Screen_Hight = 1000
Screen_width = 1800
screen = pygame.display.set_mode((Screen_width,Screen_Hight))

class movable(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height):
        self.inittop = top
        self.initback = back
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    health = 4
    invulnrabilityc = 0
    hidden = False
    ensxm = 0
    cooldown = 0
    initback = None
    inittop = None
    
    def move_ip(self,deltaX:float,deltaY:float):
        self.tx = self.tx+deltaX
        self.ty = self.ty+deltaY
        selfAsRect = super()
        selfAsRect.move_ip(round(self.tx)-selfAsRect.x,round(self.ty)-selfAsRect.y)
#d        print("moved to "+str(self.tx)+","+str(self.ty))

    def move(self,X:float,Y:float):
        self.tx = X
        self.ty = Y
        selfAsRect = super()
        selfAsRect.move(round(X),round(Y))

    def resetInitialPosition(self):
        self.tx = self.initback
        self.ty = self.inittop
        self.move(self.tx,self.ty)

jcool = 0
boss = 0
ymom = 0
dcool = 0
xmom = 0
triggert1 = 1
knockback = 5
timec = 0
sli = 50
time = 0
triggert2 = 1
triggert3 = 1
dashblock = False
slashc = 0
sldammage = 1
dash = 12
platpc = 0
ftc = 0
level = 0
levsave = 0
ascrollc = 0
ft1 = 1
ft2 = 1
ft3 = 1
ft4 = 1
ft5 = 1
poisonc = 0
max_soul = 100
soul_gain = 1
cash = 0
invulnrability = 0
tutorialfont = pygame.font.SysFont(None,40)

def resetlevel(objects,tobjects):
    for anobject in tobjects + objects:
        anobject.resetInitialPosition()

soul = 100
jumps = 0
s1f = True
soulc = 0
xposition = 900
yposition = 500
player = movable(xposition,yposition - 20,30,60)
enemy1 = movable(1300,800,50,100)
enemy2 = movable(2500,100,50,100)
enemy3 = movable(3400,-400,50,100)
enemyprojectile = movable(1500,900,50,100)
enemyprojectile2 = movable(3700,-400,50,100)
#map instanciacion
floort = movable(-500,980,3500,20)
sbackboard = movable(-500,0,500,1100)
backboard = movable(-500,0,50,1100)
roof = movable(0,0,2000,50)
fwall = movable(3000,200,50,1400)
invis_secret = movable(3000,-300,500,600)
invis_sfloort = movable(3000,200,500,50)
bwall = movable(2000,-600,50,800)
plat1 = movable(2000,800,150,50)
tplat1 = movable(2000,795,150,5)
plat2 = movable(2200,500,150,50)
tplat2 = movable(2200,495,150,5)
plat3 = movable(2400,200,150,50)
tplat3 = movable(2400,195,150,5)
plat4 = movable(2600,-100,150,50)
tplat4 = movable(2600,-105,150,5)
floort2 = movable(3000,-300,3000,50)
fiwall = movable(6000,-1400,50,1100)
soulbar = movable(30,50,100,20)
timebar = movable(30,100,100,20)
secret = movable(3200,130,50,50)
slashup = movable(2900,900,50,50)
dashup = movable(-200,900,50,50)
slash = movable(0,0,60,40)
ifloort = movable(0,1000,3000,50)
ibackwall = movable(0,400,50,600)
iceiling = movable(0,400,2000,50)
ifrontwall = movable(3000,700,50,400)
ifloort2 = movable(3000,700,1000,50)
ibackwall2 = movable(2000,0,50,600)
idjtest = movable(4000,100,50,600)
idjwalk = movable(4000,100,1000,50)
idjwalkceiling = movable(4000,-100,2000,50)
idashtest = movable(5300,100,1500,50)
deadfloort = movable(0,1000,2000,50)
deadbwall = movable(0,0,50,1000)
deadceil = movable(0,0,3050,50)
deadfwall1 = movable(2000,600,50,400)
deadfloort2 = movable(2050,600,1000,50)
deadfwall2 = movable(3050,0,50,600)
bossfloort = movable(0,1000,1800,50)
bossfwall = movable(1800,0,50,1000)
bossbwall = movable(0,0,50,1000)
bossceiling = movable(0,0,1800,50)
bosspoisonfloort = movable(50,950,1800,50)
beelzlbub = movable(900,600,130,150)
bhealthbar = movable(400,100,100,30)
objects = [ibackwall,iceiling,ifrontwall,ibackwall2,idjtest,idjwalkceiling]
tobjects = [ifloort,ifloort2,idjwalk,idashtest]
enemies = []
noncols = []
projectiles = []
projectileenemies = []
aps = []

player_front_image = pygame.image.load("player_front.gif")
player_right_image = pygame.image.load("player_right.gif")
player_left_image = pygame.transform.flip(player_right_image,True,False)

run = True
beelzlbub.health = 90


while run:
    if soul<1:
        levsave = level
        soul = 1
        level = 2
        time = 150
        objects = [deadfwall1,deadbwall,deadceil,deadfwall2]
        tobjects = [deadfloort,deadfloort2]
        resetlevel(objects,tobjects)

    

    screen.fill((255,255,255))

    #pygame.draw.circle(screen,(255,0,0),player.center,40)
    

    pygame.draw.rect(screen,(200,200,200),soulbar,soul)
    text0 = tutorialfont.render(str(cash),True,(0,0,0),(255,255,255))
    screen.blit(text0,(100,100))
    if slashc > sli * 3:
        slash.hidden = False
        if facing == 1:
            slash.x=player.right
        else:
            slash.x=player.left-60
        slash.y = yposition
        pygame.draw.rect(screen,(0,0,0),slash)
    else:
        slash.hidden = True
    if level == 1:
        if len(objects) == 0:
            objects = [roof,fwall,bwall,plat1,plat2,plat3,plat4,fiwall,backboard]
            tobjects = [floort,tplat1,tplat2,tplat3,tplat4,floort2,invis_sfloort]
            enemies = [enemy1,enemy2,enemy3]
            projectileenemies = [enemyprojectile,enemyprojectile2]
            noncols = [sbackboard,invis_secret,secret,dashup,slashup]
        
        pygame.draw.rect(screen,(0,0,0),floort)
        pygame.draw.rect(screen,(0,0,0),sbackboard)
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
        pygame.draw.rect(screen,(20,20,20),invis_secret)
        pygame.draw.rect(screen,(20,20,20),invis_sfloort)
        if secret in noncols:
            pygame.draw.rect(screen,(20,20,20),secret)
        if dashup in noncols:
            pygame.draw.rect(screen,(20,20,20),dashup)
        if slashup in noncols:
            pygame.draw.rect(screen,(20,20,20),slashup)
        if backboard.centerx < -4500:
            text = tutorialfont.render('w to travel to the next level',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True:
                level = 3
        
    

    elif level == 0:
        pygame.draw.rect(screen,(0,0,0),ifloort)
        pygame.draw.rect(screen,(0,0,0),ibackwall)
        pygame.draw.rect(screen,(0,0,0),iceiling)
        pygame.draw.rect(screen,(0,0,0),ifrontwall)
        pygame.draw.rect(screen,(0,0,0),ifloort2)
        pygame.draw.rect(screen,(0,0,0),ibackwall2)
        pygame.draw.rect(screen,(0,0,0),idjtest)
        pygame.draw.rect(screen,(0,0,0),idjwalk)
        pygame.draw.rect(screen,(0,0,0),idjwalkceiling)
        pygame.draw.rect(screen,(0,0,0),idashtest)
        if ft1 < 255 and not ibackwall.centerx < -1000:    
            text = tutorialfont.render('A and D to move',True,(ft1,ft1,ft1),(255,255,255))
            screen.blit(text,(900,200))
            if ftc < 1:
                ft1 += 1
                ftc = 6
        if ibackwall.centerx < -1000:
            if triggert1 > 0:
                triggert1 = 0
            if ft2 < 255:    
                text = tutorialfont.render('space to jump',True,(ft2,ft2,ft2),(255,255,255))
                screen.blit(text,(900,200))
                if ftc < 1:
                    ft2 += 1
                    ftc = 6
            if ibackwall.centerx < -2500:
                if triggert2 > 0:
                    triggert2 = 0
                if ft3 < 255:    
                    text = tutorialfont.render('you can preform a double jump at the cost of soul(the grey bar)',True,(ft3,ft3,ft3),(255,255,255))
                    screen.blit(text,(900,200))
                    if ftc < 1:
                        ft3 += 1
                        ftc = 6
            if ibackwall.centerx < -3000:
                if triggert3 > 0:
                    triggert3 = 0
                if ft4 < 255:   
                    text = tutorialfont.render('q to dash(costs soul)',True,(ft4,ft4,ft4),(255,255,255))
                    screen.blit(text,(900,200))
                    if ftc < 1:
                        ft4 += 1
                        ftc = 6
                if ibackwall.centerx < -5500:
                    if triggert3 > 0:
                        triggert3 = 0
                    if ft5 < 255:   
                        text = tutorialfont.render('e to hit',True,(ft5,ft5,ft5),(255,255,255))
                        screen.blit(text,(900,200))
                        if ftc < 1:
                            ft5 += 1
                            ftc = 4
                    if ibackwall.centerx < -5600 and key[pygame.K_e] == True:
                        objects.clear()
                        tobjects.clear()
                        level = 1
    elif level == 2:
        objects = [deadfwall1,deadbwall,deadceil,deadfwall2]
        tobjects = [deadfloort,deadfloort2]
        enemies = []
        noncols = []
        projectiles = []
        projectileenemies = []
        pygame.draw.rect(screen,(0,0,0),deadfloort2)
        pygame.draw.rect(screen,(0,0,0),deadfloort)
        pygame.draw.rect(screen,(0,0,0),deadbwall)
        pygame.draw.rect(screen,(0,0,0),deadceil)
        pygame.draw.rect(screen,(0,0,0),deadfwall1)
        pygame.draw.rect(screen,(0,0,0),deadfwall2)
        pygame.draw.rect(screen,(200,0,0),timebar,time)
        if timec < 1:
            time-=1
            timec = 15
        else:
            timec-=1
        timebar.width = time
        if time < 1:
            run = False
        if deadbwall.left < -2000:
            level = levsave
            resetlevel(objects,tobjects)
            deadbwall.left = 0
            objects.clear()
    
    elif level == 3:
        objects = [bossbwall,bossfwall,bossceiling]
        tobjects = [bossfloort]
        enemies = []
        noncols = [bosspoisonfloort,beelzlbub]
        projectiles = []
        projectileenemies = []
        boss = 1
        pygame.draw.rect(screen,(0,0,0),bossfloort)
        pygame.draw.rect(screen,(0,0,0),bossfwall)
        pygame.draw.rect(screen,(0,0,0),bossbwall)
        pygame.draw.rect(screen,(0,0,0),bossceiling)
        pygame.draw.rect(screen,(200,0,0),bhealthbar,beelzlbub.health)
        bhealthbar.width = beelzlbub.health
        if beelzlbub.health > 50:
            pygame.draw.rect(screen,(255,0,0),beelzlbub)
            if xposition > beelzlbub.centerx - 600 and xposition < beelzlbub.centerx + 600 and not beelzlbub.colliderect(player):
                if beelzlbub.ensxm == 0:
                    if beelzlbub.centerx<player.left:
                        beelzlbub.move_ip(.7,0)
                        for awall in objects:
                            if beelzlbub.colliderect(awall):
                                beelzlbub.move_ip(-1,0)
                    else:
                        beelzlbub.move_ip(-.7,0)
                        for awall in objects:
                            if beelzlbub.colliderect(awall):
                                beelzlbub.move_ip(1,0)
            cold = 0
            for atobject in tobjects:
                if not beelzlbub.colliderect(atobject):
                    cold += 1
                else:
                    beelzlbub.move_ip(0,-1)
                if beelzlbub.colliderect(player) and invulnrability < 1 and xmom == 0:
                    soul-=40
                    invulnrability = 200
            if cold == len(tobjects):
                beelzlbub.move_ip(0,1)
                print(str(beelzlbub)+" is falling.")
            if beelzlbub.colliderect(slash) and beelzlbub.invulnrabilityc < 1 and slash.hidden == False:
                beelzlbub.health-=sldammage
                beelzlbub.invulnrabilityc=sli
            beelzlbub.invulnrabilityc-=1
        elif beelzlbub.health > 0:
            if platpc < 1:
                beelzplat = movable(500,0,100,50)
                aps.append(beelzplat)
                platchoice = random.randint(1,2)
                if platchoice == 1:
                    tobjects.append(beelzplat)
                else:
                    noncols.append(beelzplat)
                beelzplat = movable(1200,0,100,50)
                aps.append(beelzplat)
                if platchoice == 2:
                    tobjects.append(beelzplat)
                else:
                    noncols.append(beelzplat)
                platpc = 10000
            else:
                platpc-=1
            for abplat in aps:
                pygame.draw.rect(screen,(0,0,0),abplat)
                abplat.move_ip(0,0.5)
                if abplat.y > 1000:
                    aps.remove(abplat)
                    if abplat in tobjects:
                        tobjects.remove(abplat)
                    else:
                        noncols.remove(abplat)
            pygame.draw.rect(screen,(0,0,0),bosspoisonfloort)
            if ascrollc < 1:
                beelzlbub.health-=1
                ascrollc = 60
            else:
                ascrollc-=1
            if player.colliderect(bosspoisonfloort):
                if poisonc < 1:
                    soul-=1
                    poisonc = 10
                else:
                    poisonc-=1

            


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
        while l < len(objectsList):
            objectsList[l].move_ip(x,0)
            l+=1
        if col() == True:
            l = 0
            while l < len(objectsList):
                objectsList[l].move_ip(-2*x,0)
                l+=1

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        screen.blit(player_left_image,(900,480))
        moveObjsX(objects + tobjects + enemies + noncols + projectileenemies + projectiles,1)
        facing = 0

    elif key[pygame.K_d] == True:
        screen.blit(player_right_image,(900,480))
        moveObjsX(objects + tobjects + enemies + noncols + projectileenemies + projectiles,-1)
        facing = 1
    else:
        screen.blit(player_front_image,(885,480))
    if key[pygame.K_e] == True and slashc < 1:
        slashc = sli * 4


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
            xmom = dash
        if facing == 1:
            xmom = dash*-1
        soul -= 40
        dcool = 100
    if not xmom == 0:
        moveObjsX(objects + tobjects + enemies + noncols + projectileenemies + projectiles,xmom)
        if xmom > 0:
            xmom-=0.2
        else:
            xmom+=0.2
        if xmom > -1 and xmom < 1:
            xmom = 0
    else:
        if col() == False and colt() == False:
            for thobject in objects+tobjects+enemies+noncols+projectileenemies+projectiles:
                thobject.move_ip(0,ymom * -1)
            for thproj in projectiles:
                thobject.move_ip(0,ymom * 0.1)
        else:
            if colt() == True:
                if ymom < 0:
                    for thobject in objects+tobjects+enemies+noncols+projectileenemies+projectiles:
                        thobject.move_ip(0,ymom * -1)
            elif bcol() == True:
                print("bottom col")
                for thobject in objects+tobjects+enemies+noncols+projectileenemies+projectiles:
                    thobject.move_ip(0,-1)

    for anEnemy in enemies:
        if anEnemy.health > 0:
            pygame.draw.rect(screen,(255,0,0),anEnemy)
            if xposition > anEnemy.centerx - 600 and xposition < anEnemy.centerx + 600 and not anEnemy.colliderect(player):
                if anEnemy.ensxm == 0:
                    if anEnemy.centerx<player.left:
                        anEnemy.move_ip(.5,0)
                        for awall in objects:
                            if anEnemy.colliderect(awall):
                                anEnemy.move_ip(-1,0)
                    else:
                        anEnemy.move_ip(-.5,0)
                        for awall in objects:
                            if anEnemy.colliderect(awall):
                                anEnemy.move_ip(1,0)
            cold = 0
            for atobject in tobjects:
                if not anEnemy.colliderect(atobject):
                    cold += 1
                else:
                    anEnemy.move_ip(0,-1)
                if anEnemy.colliderect(player) and invulnrability < 1 and xmom == 0:
                    soul-=1
                    invulnrability = 3
            if cold == len(tobjects):
                anEnemy.move_ip(0,1)
                print(str(anEnemy)+" is falling.")
            if anEnemy.colliderect(slash) and anEnemy.invulnrabilityc < 1 and slash.hidden == False:
                anEnemy.health-=sldammage
                anEnemy.invulnrabilityc=sli
                if xposition < anEnemy.centerx:
                    anEnemy.ensxm += knockback
                else:
                    anEnemy.ensxm -= knockback
            anEnemy.invulnrabilityc-=1
            if anEnemy.ensxm>0:
                anEnemy.ensxm-=0.1
            elif anEnemy.ensxm<0:
                anEnemy.ensxm+=0.1
            if anEnemy.ensxm < 0.1 and anEnemy.ensxm > -0.1:
                anEnemy.ensxm = 0
            anEnemy.move_ip(anEnemy.ensxm,0)
        else:
            enemies.remove(anEnemy)
            cash+=3
            
    for apEnemy in projectileenemies:
        if apEnemy.health > 0:
            pygame.draw.rect(screen,(0,255,0),apEnemy)
            cold = 0
            for atobject in tobjects:
                if not apEnemy.colliderect(atobject):
                    cold += 1
                else:
                    apEnemy.move_ip(0,-1)

                if apEnemy.cooldown < 1:
                    projectile = movable(apEnemy.x,apEnemy.y + 50,10,10)
                    projectiles.append(projectile)
                    if apEnemy.x < 900:
                        projectiles[len(projectiles) - 1].ensxm = 1
                    else:
                        projectiles[len(projectiles) - 1].ensxm = -1
                    apEnemy.cooldown = 10000
                else:
                    apEnemy.cooldown -= 1

            if cold == len(tobjects):
                apEnemy.move_ip(0,1)
                print(str(apEnemy)+" is falling.")
            if apEnemy.colliderect(slash) and apEnemy.invulnrabilityc < 1 and slash.hidden == False:
                apEnemy.health-=sldammage
                apEnemy.invulnrabilityc=sli
                if xposition < apEnemy.centerx:
                    apEnemy.ensxm += knockback
                else:
                    apEnemy.ensxm -= knockback
            apEnemy.invulnrabilityc-=1
            if apEnemy.ensxm>0:
                apEnemy.ensxm-=0.1
            elif apEnemy.ensxm<0:
                apEnemy.ensxm+=0.1
            if apEnemy.ensxm < 0.1 and apEnemy.ensxm > -0.1:
                apEnemy.ensxm = 0
            apEnemy.move_ip(apEnemy.ensxm,0)
        else:
            projectileenemies.remove(apEnemy)
            cash+=3

    
    if player.colliderect(secret):
        if secret in noncols:
            text = tutorialfont.render('w to pick up for 3 cash',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True and cash > 2:
                max_soul+=20
                soul_gain+=1
                cash-=3
                noncols.remove(secret)
    if player.colliderect(dashup):
        if dashup in noncols:
            text = tutorialfont.render('w to pick up for 3 cash',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True and cash > 2:
                dash+=3
                dashblock = True
                cash-=3
                noncols.remove(dashup)
    if player.colliderect(slashup):
        if slashup in noncols:
            text = tutorialfont.render('w to pick up for 3 cash',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True and cash > 2:
                sldammage+=1
                sli-=10
                knockback+=1
                cash-=3
                noncols.remove(slashup)
    
    for aproj in projectiles:
        pygame.draw.rect(screen,(0,0,255),aproj)
        aproj.move_ip(aproj.ensxm,0)
        if player.colliderect(aproj) and xmom == 0:
            soul-=20
            projectiles.remove(aproj)
        for awall in objects:
            if aproj.colliderect(awall):
                projectiles.remove(aproj)
        
    
    ftc-=1
    jcool-=1
    soulc-=1
    slashc-=1
    invulnrability-=1
    dcool-=1
    if soulc < 1 and soul < max_soul:
        soul+=soul_gain
        soulc = 10
    soulbar.width = soul
    #timekeep.sleep(0.005)
    pygame.display.update()

pygame.quit()