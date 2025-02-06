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
poisonc = 300
max_soul = 100
soul_gain = 1
cash = 0
apsh = 0
apss = 0
invulnrability = 0
harvestg = False
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
ml2bwall1 = movable(0,0,50,1000)
ml2floort1 = movable(0,1000,1500,50)
ml2ceiling1 = movable(0,0,2300,50)
ml2floort2 = movable(1500,1500,3000,50)
ml2bwall2 = movable(2300,-2000,50,2500)
ml2fwall1 = movable(4500,-1000,50,2500)
ml2ceil2 = movable(2300,-2000,6000,50)
ml2floort3 =  movable(4500,-1000,2000,50)
ml2floort4 = movable(6000,1000,5000,50)
ml2fwall2 = movable(6000,-1000,50,2000)
ml2bwall3 = movable(7500,-1000,50,1500)
ml2ceil3 = movable(7500,500,3500,50)
ml2bwall4 = movable(11000,500,50,500)
ml2secretar1 = movable(1000,1000,500,500)
ml2secret1 = movable(1200,1400,50,50)
ml2secretfloort1 = movable(1000,1500,500,50)
ml2secretar2 = movable(4500,-1000,500,500)
ml2secret2 = movable(4700,-600,50,50)
ml2secretfloort2 = movable(4500,-500,500,50)
ml2secretar3 = movable(1800,0,500,500)
ml2secret3 = movable(2000,400,50,50)
ml2secretfloort3 = movable(1800,500,500,50)
ml2secretar4 = movable(5300,-2000,500,500)
ml2secret4 = movable(5500,-1600,50,50)
ml2secretfloort4 = movable(5300,-1500,500,50)
ml2secretar5 = movable(7000,500,500,500)
ml2secret5 = movable(7200,900,50,50)
ml2secretfloort5 = movable(7000,1000,500,50)
ml2secretar6 = movable(8300,-2000,500,500)
ml2secret6 = movable(6000,-1600,50,50)
ml2secretfloort6 = movable(8300,-1500,500,50)
ml2plat1 = movable(4200,500,150,50)
ml2plat2 = movable(3900,100,150,50)
ml2plat3 = movable(4200,-300,150,50)
ml2plat4 = movable(3900,-700,150,50)
ml2plat5 = movable(3900,900,150,50)
ml2enemy1 = movable(400,800,50,100)
ml2enemy2 = movable(900,800,50,100)
ml2enemy3 = movable(1800,1300,50,100)
ml2enemy4 = movable(2300,1300,50,100)
ml2penemy1 = movable(2500,1300,50,100)
ml2enemy5 = movable(4900,-1100,50,100)
ml2enemy6 = movable(5200,-1100,50,100)
ml2penemy2 = movable(5500,-1100,50,100)
ml2enemy7 = movable(7500,900,50,100)
ml2enemy8 = movable(7800,900,50,100)
ml2enemy9 = movable(8100,900,50,100)
ml2enemy10 = movable(8400,900,50,100)
ml2enemy11 = movable(8700,900,50,100)
ml2penemy3 = movable(8900,900,50,100)
ml2penemy4 = movable(9200,900,50,100)
ml2penemy5 = movable(9500,900,50,100)

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
    for anmobject in objects:
        pygame.draw.rect(screen,(0,0,0),anmobject)
    for aproj in projectiles:
        pygame.draw.rect(screen,(0,0,255),aproj)
    for anmtobject in tobjects:
        pygame.draw.rect(screen,(0,0,80),anmtobject)
    for anmenemy in enemies:
        pygame.draw.rect(screen,(200,0,0),anmenemy)
    for anmnoncol in noncols:
        pygame.draw.rect(screen,(30,30,30),anmnoncol)
    for anmpenemy in projectileenemies:
        pygame.draw.rect(screen,(0,200,0),anmpenemy)
    for anmaps in aps:
        pygame.draw.rect(screen,(0,0,0),anmaps)

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
        if backboard.centerx < -4500:
            text = tutorialfont.render('w to travel to the next level',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True:
                level = 3
        
    

    elif level == 0:
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
        aps = []
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
            invulnrability = 300
            poisonc = 300
            deadbwall.left = 0
            objects.clear()
    
    elif level == 3:
        if not bossfloort in tobjects:    
            objects = [bossbwall,bossfwall,bossceiling]
            tobjects = [bossfloort]
            enemies = []
            noncols = [bosspoisonfloort,beelzlbub]
            projectiles = []
            projectileenemies = []
        boss = 1
        pygame.draw.rect(screen,(200,0,0),bhealthbar,beelzlbub.health)
        bhealthbar.width = beelzlbub.health * 10
        if beelzlbub.health > 50:
            pygame.draw.rect(screen,(255,0,0),beelzlbub)
            if xposition > beelzlbub.centerx - 600 and xposition < beelzlbub.centerx + 600 and not beelzlbub.colliderect(player):
                if beelzlbub.ensxm == 0:
                    if beelzlbub.centerx<player.left:
                        beelzlbub.move_ip(.4,0)
                        for awall in objects:
                            if beelzlbub.colliderect(awall):
                                beelzlbub.move_ip(-1,0)
                    else:
                        beelzlbub.move_ip(-.4,0)
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
#                    soul-=100
                    invulnrability = 300
            if cold == len(tobjects):
                beelzlbub.move_ip(0,1)
                print(str(beelzlbub)+" is falling.")
            if beelzlbub.colliderect(slash) and beelzlbub.invulnrabilityc < 1 and slash.hidden == False:
                beelzlbub.health-=sldammage
                beelzlbub.invulnrabilityc=sli
            beelzlbub.invulnrabilityc-=1
        elif beelzlbub.health > 0:
            if platpc < 1:
                beelzplat = movable(bossbwall.x + 500,bossceiling.y,150,50)
                aps.append(beelzplat)
                platchoice = random.randint(1,2)
                if platchoice == 1:
                    tobjects.append(beelzplat)
                else:
                    noncols.append(beelzplat)
                beelzplatp2 = movable(bossbwall.x + 1200,bossceiling.y,150,50)
                aps.append(beelzplatp2)
                if platchoice == 2:
                    tobjects.append(beelzplatp2)
                else:
                    noncols.append(beelzplatp2)
                platpc = 1000
            else:
                platpc-=1
            for abplat in aps:
                abplat.move_ip(0,0.3)
                if abplat.y > bossfloort.y:
                    aps.remove(abplat)
                    if abplat in tobjects:
                        tobjects.remove(abplat)
                    else:
                        noncols.remove(abplat)
            if ascrollc < 1:
                beelzlbub.health-=1
                ascrollc = 150
            else:
                ascrollc-=1
            if player.colliderect(bosspoisonfloort):
                if poisonc < 1:
                    soul-=2
                else:
                    poisonc-=1
        else:
            harvestg = True
            level = 4
    elif level == 4:
        if not ml2bwall1 in objects:
            objects = [ml2bwall1,ml2bwall2,ml2bwall3,ml2bwall4,ml2ceiling1,ml2ceil2,ml2ceil3,ml2fwall1,ml2fwall2]
            tobjects = [ml2floort1,ml2floort2,ml2floort3,ml2floort4,ml2secretfloort1,ml2secretfloort2,ml2secretfloort3,ml2secretfloort4,ml2secretfloort5,ml2secretfloort6,ml2plat1,ml2plat2,ml2plat3,ml2plat4,ml2plat5]
            enemies = [ml2enemy1,ml2enemy2,ml2enemy3,ml2enemy4,ml2enemy5,ml2enemy6,ml2enemy7,ml2enemy8,ml2enemy9,ml2enemy10,ml2enemy11]
            projectileenemies = [ml2penemy1,ml2penemy2,ml2penemy3,ml2penemy4,ml2penemy5]
            noncols = [ml2secretar1,ml2secret1,ml2secretar2,ml2secret2,ml2secretar3,ml2secret3,ml2secretar4,ml2secret4,ml2secretar5,ml2secret5,ml2secretar6,ml2secret6]
            aps = [ml2plat1,ml2plat2,ml2plat3,ml2plat4,ml2plat5]
        if apss == 0:
            
        



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
                objectsList[l].move_ip(-1.4*x,0)
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
    elif key[pygame.K_SPACE] == True and soul > 40 and jumps >0 and jcool < 1:
        ymom = -10
        jumps = 0
        soul-=40


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
                    ymom = 0

    for anEnemy in enemies:
        if anEnemy.health > 0:
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
        aproj.move_ip(aproj.ensxm,0)
        if player.colliderect(aproj) and xmom == 0:
            soul-=30
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
        soulc = 15
    soulbar.width = soul
    #timekeep.sleep(0.005)


    pygame.display.update()

pygame.quit()