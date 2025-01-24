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
    ensxm = 0
    cooldown = 0
    
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
triggert1 = 1
triggert2 = 1
triggert3 = 1
dashblock = False
slashc = 0
sldammage = 1
dash = 12
ftc = 0
level = 0
ft1 = 1
ft2 = 1
ft3 = 1
ft4 = 1
ft5 = 1
max_soul = 100
soul_gain = 1
cash = 0
invulnrability = 0
tutorialfont = pygame.font.SysFont(None,40)

soul = 100
jumps = 0
s1f = True
soulc = 0
xposition = 900
yposition = 500
player = pygame.Rect(xposition,yposition - 20,30,60)
enemy1 = movable(800,1300,50,100)
enemy2 = movable(100,2500,50,100)
enemyprojectile = movable(900,1500,50,100)
#map instanciacion
floort = pygame.Rect(-500,980,3500,20)
sbackboard = pygame.Rect(-500,0,500,1100)
backboard = pygame.Rect(-500,0,50,1100)
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
secret = pygame.Rect(3200,130,50,50)
dashup = pygame.Rect(-200,900,50,50)
slash = movable(0,0,60,40)
ifloort = pygame.Rect(0,1000,3000,50)
ibackwall = pygame.Rect(0,400,50,600)
iceiling = pygame.Rect(0,400,2000,50)
ifrontwall = pygame.Rect(3000,700,50,400)
ifloort2 = pygame.Rect(3000,700,1000,50)
ibackwall2 = pygame.Rect(2000,0,50,600)
idjtest = pygame.Rect(4000,100,50,600)
idjwalk = pygame.Rect(4000,100,1000,50)
idjwalkceiling = pygame.Rect(4000,-100,2000,50)
idashtest = pygame.Rect(5300,100,1500,50)
objects = [ibackwall,iceiling,ifrontwall,ibackwall2,idjtest,idjwalkceiling]
tobjects = [ifloort,ifloort2,idjwalk,idashtest]
enemies = []
noncols = []
projectiles = []
projectileenemies = []

player_front_image = pygame.image.load("player_front.gif")
player_right_image = pygame.image.load("player_right.gif")
player_left_image = pygame.transform.flip(player_right_image,True,False)

run = True



while run:
    if soul<1:
        run = False
    

    screen.fill((255,255,255))

    #pygame.draw.circle(screen,(255,0,0),player.center,40)
    

    pygame.draw.rect(screen,(200,200,200),soulbar,soul)
    text0 = tutorialfont.render(str(cash),True,(0,0,0),(255,255,255))
    screen.blit(text0,(100,100))
    if slashc > 150:
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
            enemies = [enemy1,enemy2]
            projectileenemies = [enemyprojectile]
            noncols = [sbackboard,invis_secret,secret,dashup]
        
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
        
    
#        objects.clear
#        tobjects.clear
#        enemies.clear
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
                    if ibackwall.centerx < -5800:
                        objects.clear()
                        tobjects.clear()
                        level = 1




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
                anEnemy.invulnrabilityc=50
                if xposition < anEnemy.centerx:
                    anEnemy.ensxm += 11
                else:
                    anEnemy.ensxm -= 11
            anEnemy.invulnrabilityc-=1
            if anEnemy.ensxm>0:
                anEnemy.ensxm-=1
            elif anEnemy.ensxm<0:
                anEnemy.ensxm+=1
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
                    projectile = movable(apEnemy.y + 50,apEnemy.x,10,10)
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
                apEnemy.invulnrabilityc=50
                if xposition < apEnemy.centerx:
                    apEnemy.ensxm += 11
                else:
                    apEnemy.ensxm -= 11
            apEnemy.invulnrabilityc-=1
            if apEnemy.ensxm>0:
                apEnemy.ensxm-=1
            elif apEnemy.ensxm<0:
                apEnemy.ensxm+=1
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

    pygame.display.update()

pygame.quit()