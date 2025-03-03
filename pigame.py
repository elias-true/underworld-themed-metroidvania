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
    srinvulnrabilityc = 0
    hidden = False
    ensxm = 0
    ensym = 0
    alr = 0
    cooldown = 0
    slashlife = 40
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
platmooveam = 0
md = 1
JH = -10
jable = 0
boss = 0
ymom = 0
dcool = 0
xmom = 0
oneteract = 0
triggert1 = 1
knockback = 5
timec = 0
sli = 50
soulrec = 1
mjs = 1
time = 0
triggert2 = 1
triggert3 = 1
triggert4 = 1
souldammage = 10
triggert5 = 1
dashblock = False
slashc = 0
sldammage = 1
dash = 12
b2d = 0
platpc = 0
ftc = 0
level = -1
levsave = 0
ascrollc = 0
intcool = 0
rncad = 0
ft = 1
ft0 = 1
ft1 = 1
b2b = False
ft2 = 1
ft3 = 1
ft4 = 1
interacting = False
bcount = 0
ft5 = 1
ft6 = 1
ft7 = 1
bdc = 0
intc=0
poisonc = 300
max_soul = 100
soul_gain = 1
cash = 0
apsh = 0
apss = 0
introt = 0
invulnrability = 0

b1b = False
tutorialfont = pygame.font.SysFont(None,40)

def resetlevel(objects):
    for anobject in objects:
        anobject.resetInitialPosition()

soul = 130
jumps = 0
s1f = True
soulc = 0
xposition = 900
yposition = 500
player = movable(xposition,yposition - 20,30,60)
enemy1 = movable(1300,800,50,100)
enemy2 = movable(2500,100,50,100)
enemy3 = movable(3400,-400,50,100)
enemyprojectile = movable(1500,800,50,100)
enemyprojectile2 = movable(3700,-500,50,100)
#map instanciacion
floort = movable(-500,980,3500,20)
sbackboard = movable(-500,0,500,1100)
backboard = movable(-500,0,50,1100)
roof = movable(0,0,2000,50)
fwall = movable(3000,200,50,1400)
invis_secret = movable(3000,-300,500,600)
invis_sfloort = movable(3000,200,500,50)
invis_sbwall = movable(3500,-300,50,600)
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
soulreap = movable(0,0,120,100)
ifloort = movable(0,1000,3000,50)
ibackwall = movable(0,400,50,600)
iceiling = movable(0,400,2000,50)
ifrontwall = movable(3000,700,50,400)
ifloort2 = movable(3000,700,1000,50)
ibackwall2 = movable(2000,0,50,600)
idjtest = movable(4000,100,50,600)
idjwalk = movable(4000,100,1000,50)
idjwalkceiling = movable(4000,-100,2000,50)
idashtest = movable(5300,100,2500,50)
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
ml2fwall1 = movable(4500,-500,50,2500)
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
ml2plat1 = movable(4200,700,150,50)
ml2plat2 = movable(3900,300,150,50)
ml2plat3 = movable(4200,-100,150,50)
ml2plat4 = movable(3900,-500,150,50)
ml2plat5 = movable(3900,1100,150,50)
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
ml2senemy = movable(9600,900,50,100)
lostsoul1 = movable(2000,900,60,110)
l2bfloort = movable(0,1000,2000,50)
l2bbwall = movable(0,0,50,1000)
l2bfwall = movable(2000,0,50,1000)
l2bceil = movable(0,0,2000,50)
clotho = movable(500,500,30,110)
lachesis = movable(300,500,50,80)
atropos = movable(150,500,50,100)

objects = []
enemies = []
senemies = []
noncols = []
projectiles = []
projectileenemies = []
spenemies = []
aps = []
enatcks = []
battacks = []
rems = []
slashups = []
dashups = []
soulups = []
reapups = []
jumpups = []
fatcks = []
statcks = []
player_front_image = pygame.image.load("player_front.gif")
player_right_image = pygame.image.load("player_right.gif")
player_left_image = pygame.transform.flip(player_right_image,True,False)

run = True
beelzlbub.health = 90
clotho.health = 40
atropos.health = 40
lachesis.health = 40

def colap(cthing):
    apcol = False
    for d in aps:
        if apcol == False:
            if cthing.colliderect(d):
                apcol = True
    return apcol

while run:
    if soul<1:
        levsave = level
        soul = max_soul
        level = 2
        time = 200
        ft7 = 1
        rncad = 0
        objects = [deadfwall1,deadbwall,deadceil,deadfwall2,deadfloort,deadfloort2]
        enemies = []
        senemies = []
        noncols = []
        projectiles = []
        projectileenemies = []
        spenemies = []
        aps = []
        enatcks = []
        battacks = []
        resetlevel(objects)

    
    key = pygame.key.get_pressed()
    screen.fill((150,150,150))
    for anmobject in objects:
        pygame.draw.rect(screen,(0,0,0),anmobject)
    for aproj in projectiles:
        pygame.draw.rect(screen,(0,0,255),aproj)
    for anmenemy in enemies:
        pygame.draw.rect(screen,(200,0,0),anmenemy)
    for anmnoncol in noncols:
        pygame.draw.rect(screen,(50,0,0),anmnoncol)
    for anmpenemy in projectileenemies:
        pygame.draw.rect(screen,(0,200,0),anmpenemy)
    for anmaps in aps:
        pygame.draw.rect(screen,(0,0,0),anmaps)
    for senemyn in senemies:
        pygame.draw.rect(screen,(150,150,0),senemyn)
    for spawneden in spenemies:
        pygame.draw.rect(screen,(150,0,0),spawneden)
    for antack in enatcks:
        pygame.draw.rect(screen,(100,0,150),antack)
    for antack in statcks:
        pygame.draw.rect(screen,(100,0,150),antack)
    for antack in fatcks:
        pygame.draw.rect(screen,(100,0,150),antack)

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
    if key[pygame.K_r] == True and b1b == True:
        if soulrec > 1:
            if soulrec > 4900:
                soulreap.hidden = False
                if facing == 1:
                    soulreap.x=player.right
                else:
                    soulreap.x=player.left-100
                soulreap.y = yposition - 50
                pygame.draw.rect(screen,(205,200,0),soulreap)
                print("reapshow")
            elif soulrec < 4900:
                soulreap.hidden = True
        else:    
            soulrec = 5000
            print("reapcool")
    if soulrec < 4900:
        soulreap.hidden = True

    if level == -1:
        if ft0 < 255:    
            text = tutorialfont.render("life's shadow must have been terified of of what I fortold for it to have banished your soul here here",True,(ft0,ft0,ft0),(255,255,255))
            screen.blit(text,(400,200))
            if ftc < 1:
                ft0 += 1
                ftc = 11
        else:
            if ft < 255:    
                text = tutorialfont.render('luckily for you, however, my power is such that I may let you out, in extchange for some help down the road of course',True,(ft,ft,ft),(255,255,255))
                screen.blit(text,(100,200))
                if ftc < 1:
                    ft += 1
                    ftc = 14
            else:
                text = tutorialfont.render('w to accept help',True,(0,0,0),(255,255,255))
                screen.blit(text,(800,200))
                if key[pygame.K_w] == True:
                    level = 0
            

    if level == 1:
        if len(objects) == 0:
            objects = [roof,fwall,bwall,plat1,plat2,plat3,plat4,fiwall,backboard,floort,tplat1,tplat2,tplat3,tplat4,floort2,invis_sfloort,invis_sbwall]
            enemies = [enemy1,enemy2,enemy3]
            projectileenemies = [enemyprojectile,enemyprojectile2]
            noncols = [sbackboard,invis_secret,secret,dashup,slashup,lostsoul1]
            soulups = [secret]
            slashups = [slashup]
            dashups = [dashup]
        if backboard.centerx < -4500:
            text = tutorialfont.render('w to travel to the next level',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True:
                level = 3
        
    

    elif level == 0:
        objects = [ibackwall,iceiling,ifrontwall,ibackwall2,idjtest,idjwalkceiling,ifloort,ifloort2,idjwalk,idashtest]
        enemies = []
        senemies = []
        noncols = []
        projectiles = []
        projectileenemies = []
        spenemies = []
        aps = []
        enatcks = []
        battacks = []
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
                        ftc = 4
                if ibackwall.centerx < -5500:
                    if triggert4 > 0:
                        triggert4 = 0
                    if ft5 < 255:   
                        text = tutorialfont.render('s to regenerate soul',True,(ft5,ft5,ft5),(255,255,255))
                        screen.blit(text,(900,200))
                        if ftc < 1:
                            ft5 += 1
                            ftc = 3
                    if ibackwall.centerx < -6500:
                        if triggert5 > 0:
                            triggert5 = 0
                        if ft6 < 255:   
                            text = tutorialfont.render('e to hit',True,(ft6,ft6,ft6),(255,255,255))
                            screen.blit(text,(900,200))
                            if ftc < 1:
                                ft6 += 1
                                ftc = 4
                        if ibackwall.centerx < -6500 and key[pygame.K_e] == True:
                            objects.clear()
                            level = 1
    elif level == 2:
        objects = [deadfwall1,deadbwall,deadceil,deadfwall2,deadfloort,deadfloort2]
        enemies = []
        noncols = []
        projectiles = []
        projectileenemies = []
        aps = []
        text = tutorialfont.render('escape',True,(255,0,0),(255,255,255))
        screen.blit(text,(900,200))
        pygame.draw.rect(screen,(200,0,0),timebar,time)
        if timec < 1 and rncad == 0:
            time-=1
            timec = 15
        elif rncad == 0:
            timec-=1
        timebar.width = time
        if time < 1:
            run = False
        if deadbwall.left < -1800:
            rncad = 1
            text = tutorialfont.render("don't fail me again",True,(ft7,ft7,ft7),(255,255,255))
            screen.blit(text,(900,200))
            if ftc < 1:
                ft7 += 1
                ftc = 4
            if ft7 > 250:
                level = levsave
                resetlevel(objects)
                invulnrability = 300
                poisonc = 300
                deadbwall.left = 0
                objects.clear()
    
    elif level == 3:
        if not bossfloort in objects:    
            objects = [bossbwall,bossfwall,bossceiling,bossfloort]
            enemies = []
            noncols = [bosspoisonfloort,beelzlbub]
            projectiles = []
            projectileenemies = []
        boss = 1
        pygame.draw.rect(screen,(200,0,0),bhealthbar,beelzlbub.health)
        bhealthbar.width = beelzlbub.health * 10
        if beelzlbub.health > 50:
            pygame.draw.rect(screen,(255,0,0),beelzlbub)
            if xposition > beelzlbub.centerx - 800 and xposition < beelzlbub.centerx + 800 and not beelzlbub.colliderect(player):
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
            if colt(beelzlbub) == False:
                beelzlbub.move_ip(0,1)
            else:
                beelzlbub.move_ip(0,-2)
            if xposition > beelzlbub.centerx - 120 and xposition < beelzlbub.centerx + 120 and xmom == 0 and beelzlbub.cooldown < 1 and invulnrability < 1:
                if beelzlbub.centerx>player.left:
                    attack = movable(beelzlbub.x - 150,beelzlbub.y + 40,150,5)
                    enatcks.append(attack)
                else:
                    attack = movable(beelzlbub.x + 150,beelzlbub.y + 40,150,5)
                    enatcks.append(attack)
                beelzlbub.cooldown = 800
                enatcks[len(enatcks) - 1].slashlife = 150
            elif beelzlbub.ensxm < 1 and beelzlbub.ensxm > -1 and beelzlbub.cooldown < 1:
                beelzlbub.y=500
                if beelzlbub.x < 300 and bdc < 1:
                    beelzlbub.ensxm = -5
                elif beelzlbub.x > 1700 and bdc < 1:
                    beelzlbub.ensxm = 5
                bdc = 1
                beelzlbub.cooldown = 1500
            elif not beelzlbub.cooldown < 1:
                bdc-=1
            bcount = 0
            for anobject in objects:
                if not beelzlbub.colliderect(anobject):
                    bcount+=1
            if not bcount == len(objects):
                beelzlbub.ensxm*=-1
                beelzlbub.move_ip(beelzlbub.ensxm,0)
            beelzlbub.move_ip(beelzlbub.ensxm,0)
            if beelzlbub.colliderect(player) and not beelzlbub.ensxm == 0:
                soul-=2
            if beelzlbub.ensxm < -1.1: 
                beelzlbub.ensxm+=0.1
            if beelzlbub.ensxm > 1.1: 
                beelzlbub.ensxm-=0.1
            if beelzlbub.colliderect(slash) and beelzlbub.invulnrabilityc < 1 and slash.hidden == False:
                beelzlbub.health-=sldammage
                beelzlbub.invulnrabilityc=sli
            beelzlbub.invulnrabilityc-=1
            beelzlbub.cooldown-=1
        elif beelzlbub.health > 0:
            if platpc < 1:
                beelzplat = movable(bossbwall.x + 500,bossceiling.y,150,50)
                aps.append(beelzplat)
                platchoice = random.randint(1,2)
                if platchoice == 1:
                    objects.append(beelzplat)
                else:
                    noncols.append(beelzplat)
                beelzplatp2 = movable(bossbwall.x + 1200,bossceiling.y,150,50)
                aps.append(beelzplatp2)
                if platchoice == 2:
                    objects.append(beelzplatp2)
                else:
                    noncols.append(beelzplatp2)
                platpc = 1000
            else:
                platpc-=1
            for abplat in aps:
                abplat.move_ip(0,0.3)
                if abplat.y > bossfloort.y:
                    aps.remove(abplat)
                    if abplat in objects:
                        objects.remove(abplat)
                    else:
                        noncols.remove(abplat)
            if ascrollc < 1:
                beelzlbub.health-=1
                ascrollc = 150
            else:
                ascrollc-=1
            if player.colliderect(bosspoisonfloort):
                if poisonc < 1:
#                    soul-=1
                    print("m")
                else:
                    poisonc-=1
        else:
            b1b = True
            level = 4
    elif level == 4:
        if not ml2bwall1 in objects:
            objects = [ml2bwall1,ml2bwall2,ml2bwall3,ml2bwall4,ml2ceiling1,ml2ceil2,ml2ceil3,ml2fwall1,ml2fwall2,ml2floort1,ml2floort2,ml2floort3,ml2floort4,ml2secretfloort1,ml2secretfloort2,ml2secretfloort3,ml2secretfloort4,ml2secretfloort5,ml2secretfloort6,ml2plat1,ml2plat2,ml2plat3,ml2plat4,ml2plat5]
            enemies = [ml2enemy1,ml2enemy2,ml2enemy3,ml2enemy4,ml2enemy5,ml2enemy6,ml2enemy7,ml2enemy8,ml2enemy9,ml2enemy10,ml2enemy11]
            projectileenemies = [ml2penemy1,ml2penemy2,ml2penemy3,ml2penemy4,ml2penemy5]
            senemies = [ml2senemy]
            noncols = [ml2secretar1,ml2secret1,ml2secretar2,ml2secret2,ml2secretar3,ml2secret3,ml2secretar4,ml2secret4,ml2secretar5,ml2secret5,ml2secretar6,ml2secret6]
            aps = [ml2plat1,ml2plat2,ml2plat3,ml2plat4,ml2plat5]
            soulups = [ml2secret1,ml2secret6]
            slashups = [ml2secret2]
            dashups = [ml2secret3]
            reapups = [ml2secret4]
            jumpups = [ml2secret5]
        if md == 1:
            for amoplat in aps:
                amoplat.move_ip(0,-0.5)
            platmooveam+=1
        elif md == 0:
            for amoplat in aps:
                amoplat.move_ip(0,0.5)
            platmooveam+=1
        if platmooveam > 499:
            if md == 1:
                md = 0
            elif md == 0:
                md = 1
            platmooveam = platmooveam-500
        if ml2bwall1.centerx < -9600:
            text = tutorialfont.render('w to travel to the next level',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True:
                level = 5
    elif level == 5:
        objects = [l2bfloort,l2bbwall,l2bfwall,l2bceil]
        noncols = [atropos,lachesis,clotho]
        if clotho.health > 0:
            pygame.draw.rect(screen,(255,0,0),clotho)
            if xposition > clotho.centerx - 800 and xposition < clotho.centerx + 800 and not clotho.colliderect(player):
                if clotho.ensxm == 0:
                    if clotho.centerx<player.left:
                        clotho.move_ip(.7,0)
                        for awall in objects:
                            if clotho.colliderect(awall):
                                clotho.move_ip(-1,0)
                    else:
                        clotho.move_ip(-.7,0)
                        for awall in objects:
                            if clotho.colliderect(awall):
                                clotho.move_ip(1,0)
            if colt(clotho) == False:
                clotho.move_ip(0,1)
            else:
                clotho.move_ip(0,-2)
            if xposition > clotho.centerx - 70 and xposition < clotho.centerx + 70 and xmom == 0 and clotho.cooldown < 1 and invulnrability < 1:
                if clotho.centerx>player.left:
                    attack = movable(clotho.x - 70,clotho.y + 40,5,50)
                    fatcks.append(attack)
                    fatcks[len(fatcks) - 1].alr = -1
                else:
                    attack = movable(clotho.x + 70,clotho.y + 40,5,50)
                    fatcks.append(attack)
                clotho.cooldown = 300
                fatcks[len(fatcks) - 1].slashlife = 90
            elif clotho.centerx>player.left and not clotho.cooldown < 1:
                clotho.move_ip(0.8,0)
                for awall in objects:
                    if clotho.colliderect(awall):
                        clotho.move_ip(-1,0)
            elif clotho.centerx<player.left and not clotho.cooldown < 1:
                clotho.move_ip(-0.8,0)
                for awall in objects:
                    if clotho.colliderect(awall):
                        clotho.move_ip(1,0)
            if clotho.colliderect(player):
                soul-=1
            if clotho.colliderect(slash) and clotho.invulnrabilityc < 1 and slash.hidden == False:
                clotho.health-=sldammage
                clotho.invulnrabilityc=sli
            if clotho.colliderect(soulreap) and clotho.srinvulnrabilityc < 1 and soulreap.hidden == False:
                clotho.health-=souldammage
                soul+=souldammage*2
                clotho.srinvulnrabilityc=5000
            clotho.invulnrabilityc-=1
            clotho.srinvulnrabilityc -= 1
            clotho.cooldown-=1
        else:
            b2d += 1
        if lachesis.health > 0:
            pygame.draw.rect(screen,(0,255,0),lachesis)
            if xposition > lachesis.centerx - 800 and xposition < lachesis.centerx + 800 and not lachesis.colliderect(player):
                if lachesis.ensxm == 0:
                    if lachesis.centerx<player.left:
                        lachesis.move_ip(.5,0)
                        for awall in objects:
                            if lachesis.colliderect(awall):
                                lachesis.move_ip(-1,0)
                    else:
                        lachesis.move_ip(-.5,0)
                        for awall in objects:
                            if lachesis.colliderect(awall):
                                lachesis.move_ip(1,0)
            if colt(lachesis) == False:
                lachesis.move_ip(0,1)
            else:
                lachesis.move_ip(0,-2)
            if xposition > lachesis.centerx - 150 and xposition < lachesis.centerx + 150 and xmom == 0 and lachesis.cooldown < 1 and invulnrability < 1:
                if lachesis.centerx>player.left:
                    attack = movable(lachesis.x - 150,lachesis.y + 40,5,50)
                    fatcks.append(attack)
                    fatcks[len(fatcks) - 1].alr = -1
                else:
                    attack = movable(lachesis.x + 150,lachesis.y + 40,5,50)
                    fatcks.append(attack)
                lachesis.cooldown = 1500
                fatcks[len(fatcks) - 1].slashlife = 300
            elif lachesis.centerx>player.left and not lachesis.cooldown < 1:
                lachesis.move_ip(0.6,0)
                for awall in objects:
                    if lachesis.colliderect(awall):
                        lachesis.move_ip(-1,0)
            elif lachesis.centerx<player.left and not lachesis.cooldown < 1:
                lachesis.move_ip(-0.6,0)
                for awall in objects:
                    if lachesis.colliderect(awall):
                        lachesis.move_ip(1,0)
            if lachesis.colliderect(player):
                soul-=1
            if lachesis.colliderect(slash) and lachesis.invulnrabilityc < 1 and slash.hidden == False:
                lachesis.health-=sldammage
                lachesis.invulnrabilityc=sli
            if lachesis.colliderect(soulreap) and lachesis.srinvulnrabilityc < 1 and soulreap.hidden == False:
                lachesis.health-=souldammage
                soul+=souldammage*2
                lachesis.srinvulnrabilityc=5000
            lachesis.invulnrabilityc-=1
            lachesis.srinvulnrabilityc -= 1
            lachesis.cooldown-=1
        else:
            b2d += 1
        if atropos.health > 0:
            pygame.draw.rect(screen,(0,0,255),atropos)
            if xposition > atropos.centerx - 800 and xposition < atropos.centerx + 800 and not atropos.colliderect(player):
                if atropos.ensxm == 0:
                    if atropos.centerx<player.left:
                        atropos.move_ip(.3,0)
                        for awall in objects:
                            if atropos.colliderect(awall):
                                atropos.move_ip(-1,0)
                    else:
                        atropos.move_ip(-.3,0)
                        for awall in objects:
                            if atropos.colliderect(awall):
                                atropos.move_ip(1,0)
            if colt(atropos) == False:
                atropos.move_ip(0,1)
            else:
                atropos.move_ip(0,-2)
            if xposition > atropos.centerx - 150 and xposition < atropos.centerx + 150 and xmom == 0 and atropos.cooldown < 1 and invulnrability < 1:
                if atropos.centerx>player.left:
                    attack = movable(atropos.x - 150,atropos.y + 40,5,50)
                    statcks.append(attack)
                else:
                    attack = movable(atropos.x + 150,atropos.y + 40,5,50)
                    statcks.append(attack)
                atropos.cooldown = 1500
                statcks[len(statcks) - 1].slashlife = 100
            elif atropos.centerx>player.left and not atropos.cooldown < 1:
                atropos.move_ip(0.5,0)
                for awall in objects:
                    if atropos.colliderect(awall):
                        atropos.move_ip(-1,0)
            elif atropos.centerx<player.left and not atropos.cooldown < 1:
                atropos.move_ip(-0.5,0)
                for awall in objects:
                    if atropos.colliderect(awall):
                        atropos.move_ip(1,0)
            if atropos.colliderect(player):
                soul-=1
            if atropos.colliderect(slash) and atropos.invulnrabilityc < 1 and slash.hidden == False:
                atropos.health-=sldammage
                atropos.invulnrabilityc=sli
            if atropos.colliderect(soulreap) and atropos.srinvulnrabilityc < 1 and soulreap.hidden == False:
                atropos.health-=souldammage
                soul+=souldammage*2
                atropos.srinvulnrabilityc=5000
            atropos.invulnrabilityc-=1
            atropos.srinvulnrabilityc-=1
            atropos.cooldown-=1
        else:
            b2d += 1
        if b2d == 3:
            b2b = True
            level = 6

    
        
    


    # Check if we're on the screen
    if player.x<0:
        player.x = Screen_width - 10
    if player.x>Screen_width:
        player.x = 10
    if player.y>Screen_Hight:
        player.y = 10
    if player.y<0:
        player.y = Screen_Hight - 10
    
    
    def col(athing):
        colliding = False
        for d in objects:
            if not colliding:
                if athing.colliderect(d):
                    colliding = True
        return colliding
    
    
    def bcol(bthing):
        bottomcol = False
        for d in objects:
            if bottomcol == False:
                if bthing.top > d.bottom - 2 and bthing.top < d.bottom + 3 and bthing.tx < d.tx + d.width and bthing.tx + bthing.width > d.tx:
                    bottomcol = True
        return bottomcol
        

    
    def colt(thing):
        collided = False
        for d in objects:
            if collided == False:
                if thing.bottom < d.top + 2 and thing.bottom > d.top - 3 and thing.tx < d.tx + d.width and thing.tx + thing.width > d.tx:
                    collided = True

        return collided

    def moveObjsX(objectsList,x):
        l=0
        while l < len(objectsList):
            objectsList[l].move_ip(x,0)
            l+=1
        if col(player) == True:
            l = 0
            while l < len(objectsList):
                objectsList[l].move_ip(-1.4*x,0)
                l+=1

    if interacting == False:
        if key[pygame.K_a] == True and not key[pygame.K_s] == True:
            screen.blit(player_left_image,(885,480))
            moveObjsX(objects + enemies + noncols + projectileenemies + projectiles,1)
            facing = 0
        elif key[pygame.K_d] == True and not key[pygame.K_s] == True:
            screen.blit(player_right_image,(885,480))
            moveObjsX(objects + enemies + noncols + projectileenemies + projectiles,-1)
            facing = 1
        else:
            screen.blit(player_front_image,(885,480))
        if key[pygame.K_e] == True and slashc < 1:
            slashc = sli * 4
        if colt(player) == False and col(player) == False and jable < 1:
            if ymom < 1:
                ymom += 0.1

        if key[pygame.K_SPACE] == True and (colt(player) == True or col(player) == True or jable>0) and jcool < 1 and not key[pygame.K_s] == True:
            ymom = JH
            jumps = mjs
            jcool = 250
        elif key[pygame.K_SPACE] == True and soul > 40 and jumps >0 and jcool < 1 and not key[pygame.K_s] == True:
            ymom = JH+1
            jumps -= 1
            jcool = 250
            soul-=40
        if key[pygame.K_q] == True and soul > 40 and dcool < 1 and not key[pygame.K_s] == True:
            if facing == 0:
                xmom = dash
            if facing == 1:
                xmom = dash*-1
            soul -= 40
            dcool = 100
    else:
        screen.blit(player_front_image,(885,480))
    if not xmom == 0:
        moveObjsX(objects + enemies + noncols + projectileenemies + projectiles + enatcks + fatcks,xmom)
        if xmom > 0:
            xmom-=0.2
        else:
            xmom+=0.2
        if xmom > -1 and xmom < 1:
            xmom = 0
    else:
        if col(player) == False and colt(player) == False:
            for thobject in objects+enemies+noncols+projectileenemies+projectiles+enatcks+fatcks:
                thobject.move_ip(0,ymom * -1)
            for thproj in projectiles:
                thproj.move_ip(0,ymom * 0.1)
        else:
            if colt(player) == True:
                if ymom < 0:
                    jable = 2
                    for thobject in objects+enemies+noncols+projectileenemies+projectiles+aps+enatcks+fatcks:
                        thobject.move_ip(0,ymom * -1)
                else:
                    jable = 2
                    if colap(player):
                        for thobject in objects+enemies+noncols+projectileenemies+projectiles+enatcks+fatcks:
                            thobject.move_ip(0,0.6)
                            print("apcol")
            else:
                for thobject in objects+enemies+noncols+projectileenemies+projectiles+enatcks+fatcks:
                    thobject.move_ip(0,-1)
                    ymom = 0
                    print("napcol")
                    jable = 2



    for anEnemy in enemies:
        if anEnemy.health > 0:
            if xposition > anEnemy.centerx - 600 and xposition < anEnemy.centerx + 600 and not anEnemy.colliderect(player) and anEnemy.cooldown<1:
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
            elif xposition < anEnemy.centerx and xposition > anEnemy.centerx - 600 and xposition < anEnemy.centerx + 600:
                    anEnemy.move_ip(.5,0)
                    for awall in objects:
                        if anEnemy.colliderect(awall):
                            anEnemy.move_ip(-1,0)
            elif xposition > anEnemy.centerx - 600 and xposition < anEnemy.centerx + 600:
                anEnemy.move_ip(-.5,0)
                for awall in objects:
                    if anEnemy.colliderect(awall):
                        anEnemy.move_ip(1,0)
            if colt(anEnemy) == False:
                anEnemy.move_ip(0,1)
            else:
                anEnemy.move_ip(0,-2)
                if xposition > anEnemy.centerx - 70 and xposition < anEnemy.centerx + 70 and xmom == 0 and anEnemy.cooldown < 1 and not anEnemy.colliderect(player) and invulnrability < 1:
                    if anEnemy.centerx>player.left:
                        attack = movable(anEnemy.x - 50,anEnemy.y + 30,80,5)
                        enatcks.append(attack)
                    else:
                        attack = movable(anEnemy.x + 80,anEnemy.y + 30,80,5)
                        enatcks.append(attack)
                    anEnemy.cooldown = 500
            if anEnemy.colliderect(slash) and anEnemy.invulnrabilityc < 1 and slash.hidden == False:
                anEnemy.health-=sldammage
                anEnemy.invulnrabilityc=sli
                if xposition < anEnemy.centerx:
                    anEnemy.ensxm += knockback
                else:
                    anEnemy.ensxm -= knockback
            if anEnemy.colliderect(soulreap) and anEnemy.srinvulnrabilityc < 1 and soulreap.hidden == False:
                anEnemy.health-=souldammage
                soul+=souldammage*2
                anEnemy.srinvulnrabilityc=5000
            anEnemy.cooldown-=1
            anEnemy.invulnrabilityc-=1
            anEnemy.srinvulnrabilityc-=1
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
            if colt(apEnemy) == False:
                apEnemy.move_ip(0,1)
            else:
                apEnemy.move_ip(0,-2)


            if apEnemy.cooldown < 1:
                projectile = movable(apEnemy.x,apEnemy.y + 50,10,10)
                projectiles.append(projectile)
                if apEnemy.x < 900:
                    projectiles[len(projectiles) - 1].ensxm = 1
                else:
                    projectiles[len(projectiles) - 1].ensxm = -1
                apEnemy.cooldown = 1000
            else:
                apEnemy.cooldown -= 1

                print(str(apEnemy)+" is falling.")
            if apEnemy.colliderect(slash) and apEnemy.invulnrabilityc < 1 and slash.hidden == False:
                apEnemy.health-=sldammage
                apEnemy.invulnrabilityc=sli
                if xposition < apEnemy.centerx:
                    apEnemy.ensxm += knockback
                else:
                    apEnemy.ensxm -= knockback
            if apEnemy.colliderect(soulreap) and apEnemy.srinvulnrabilityc < 1 and soulreap.hidden == False:
                apEnemy.health-=souldammage
                soul+=souldammage*2
                apEnemy.srinvulnrabilityc=5000
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
    for apEnemy in senemies:
        if apEnemy.health > 0:
            if colt(apEnemy) == False:
                apEnemy.move_ip(0,1)
            else:
                apEnemy.move_ip(0,-2)


            if apEnemy.cooldown < 1:
                spnden = movable(apEnemy.x,apEnemy.y,10,20)
                spenemies.append(spnden)
                spenemies[len(spenemies) - 1].health = 2
                apEnemy.cooldown = 5000
            else:
                apEnemy.cooldown -= 1

                print(str(apEnemy)+" is falling.")
            if apEnemy.colliderect(slash) and apEnemy.invulnrabilityc < 1 and slash.hidden == False:
                apEnemy.health-=sldammage
                apEnemy.invulnrabilityc=sli
                if xposition < apEnemy.centerx:
                    apEnemy.ensxm += knockback
                else:
                    apEnemy.ensxm -= knockback
            if apEnemy.colliderect(soulreap) and apEnemy.srinvulnrabilityc < 1 and soulreap.hidden == False:
                apEnemy.health-=souldammage
                soul+=souldammage*2
                apEnemy.srinvulnrabilityc=5000
            apEnemy.invulnrabilityc-=1
            apEnemy.srinvulnrabilityc-=1
            if apEnemy.ensxm>0:
                apEnemy.ensxm-=0.1
            elif apEnemy.ensxm<0:
                apEnemy.ensxm+=0.1
            if apEnemy.ensxm < 0.1 and apEnemy.ensxm > -0.1:
                apEnemy.ensxm = 0
            apEnemy.move_ip(apEnemy.ensxm,0)
        else:
            senemies.remove(apEnemy)
            cash+=5


    if player.colliderect(lostsoul1):
        if oneteract == 0:
            text = tutorialfont.render('w to interact',True,(0,0,0),(255,255,255))
            if key[pygame.K_w] == True and intcool < 1:
                oneteract = 1
                intcool = 100
                interacting = False
        elif oneteract == 1:    
            text = tutorialfont.render("hello there traveler, i've been exploring these depths for... a long time, my memory is hazy but I remember one vile figure",True,(0,0,0),(255,255,255))
            interacting = True
            if key[pygame.K_w] == True and intcool < 1:
                oneteract = 0
                intcool = 100
                interacting = False
        screen.blit(text,(0,200))
    elif interacting == True:
        oneteract = 0
        interacting = False

        
    for asoul in soulups:
        if player.colliderect(asoul):
            if asoul in noncols:
                text = tutorialfont.render('w to pick up for 3 cash',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
                if key[pygame.K_w] == True and cash > 2:
                    max_soul+=50
                    soul_gain+=1
                    cash-=3
                    noncols.remove(asoul)
    for adsh in dashups:
        if player.colliderect(adsh):
            if adsh in noncols:
                text = tutorialfont.render('w to pick up for 3 cash',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
                if key[pygame.K_w] == True and cash > 2:
                    dash+=3
                    dashblock = True
                    cash-=3
                    noncols.remove(adsh)
    for aslsh in slashups:
        if player.colliderect(aslsh):
            if aslsh in noncols:
                text = tutorialfont.render('w to pick up for 6 cash',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
                if key[pygame.K_w] == True and cash > 5:
                    sldammage+=1
                    sli-=10
                    knockback+=1
                    cash-=6
                    noncols.remove(aslsh)
    for asreap in reapups:
        if player.colliderect(asreap):
            if asreap in noncols:
                text = tutorialfont.render('w to pick up for 6 cash',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
                if key[pygame.K_w] == True and cash > 5:
                    cash-=6
                    noncols.remove(asreap)
    for ajump in jumpups:
        if player.colliderect(ajump):
            if ajump in noncols:
                text = tutorialfont.render('w to pick up for 9 cash',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
                if key[pygame.K_w] == True and cash > 8:
                    sldammage+=1
                    JH-=1
                    mjs += 1
                    cash-=9
                    noncols.remove(ajump)
    
    for aproj in projectiles:
        aproj.move_ip(aproj.ensxm,0)
        if player.colliderect(aproj) and xmom == 0:
            soul-=30
            projectiles.remove(aproj)
        elif aproj in projectiles:
            for awall in objects:
                if aproj.colliderect(awall):
                    rems.append(aproj)
    for arem in rems:
        if arem in projectiles:
            projectiles.remove(arem)
    rems = []
    for anattack in enatcks:
        if anattack.slashlife > 0:
            anattack.height+=1
            anattack.slashlife-=1
            if anattack.colliderect(player) and xmom == 0:
                soul-=1
        else:
            enatcks.remove(anattack)
    for anfattack in fatcks:
        if anfattack.slashlife > 0:
            anfattack.width+=1
            if anfattack.alr == -1:
                anfattack.move_ip(-1,0)
            anfattack.slashlife-=1
            if anfattack.colliderect(player) and xmom == 0:
                soul-=1
        else:
            fatcks.remove(anfattack)
    intc = 0
    for anstattack in statcks:
        if anstattack.slashlife > 0:
            anstattack.slashlife-=1
            if anstattack.colliderect(player) and xmom == 0:
                interacting = True
            else:
                intc += 1
        else:
            statcks.remove(anstattack)
    if intc == len(statcks):
        interacting = False
    for anEnemy in spenemies:
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
            if colt(anEnemy) == False:
                anEnemy.move_ip(0,1)
            else:
                anEnemy.move_ip(0,-2)
                if anEnemy.colliderect(player) and invulnrability < 1 and xmom == 0:
                    soul-=1
                    invulnrability = 3
            if anEnemy.colliderect(slash) and anEnemy.invulnrabilityc < 1 and slash.hidden == False:
                anEnemy.health-=sldammage
                anEnemy.invulnrabilityc=sli
                if xposition < anEnemy.centerx:
                    anEnemy.ensxm += knockback * 2
                else:
                    anEnemy.ensxm -= knockback * 2
            if anEnemy.colliderect(soulreap) and anEnemy.srinvulnrabilityc < 1 and soulreap.hidden == False:
                anEnemy.health-=souldammage
                soul+=souldammage*2
                anEnemy.srinvulnrabilityc=5000
            anEnemy.invulnrabilityc-=1
            anEnemy.srinvulnrabilityc-=1
            if anEnemy.ensxm>0:
                anEnemy.ensxm-=0.1
            elif anEnemy.ensxm<0:
                anEnemy.ensxm+=0.1
            if anEnemy.ensxm < 0.1 and anEnemy.ensxm > -0.1:
                anEnemy.ensxm = 0
            anEnemy.move_ip(anEnemy.ensxm,0)
        else:
            rems.append(anEnemy)
    for arem in rems:
        spenemies.remove(arem)
    rems = []
        
    
    ftc-=1
    jcool-=1
    soulc-=1
    jable-=1
    slashc-=1
    intcool-=1
    invulnrability-=1
    dcool-=1
    soulrec-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if soulc < 1 and soul < max_soul:
        if key[pygame.K_s] == True:
            soul+=soul_gain
            soulc = 16
    soulbar.width = soul
    #timekeep.sleep(0.005)


    pygame.display.update()

pygame.quit()