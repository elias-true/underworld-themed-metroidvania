#import pprint
import pygame
pygame.init()
import time as timekeep
import random
import math

Screen_Hight = 1000
Screen_width = 1800
screen = pygame.display.set_mode((Screen_width,Screen_Hight))
soultotem_menu = pygame.surface.Surface((1400,800))

class movable(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height):
        self.inittop = top
        self.initback = back
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    health = 250
    invulnrabilityc = 0
    srinvulnrabilityc = 0
    hidden = False
    ensxm = 0
    wbreak = 0
    ensym = 0
    alr = 0
    coriographs = 0
    ppt = False
    cooldown = 0
    ymom = 0 
    slashlife = 40
    pdammage = 30
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
sladd = 0
difficuty = 0
b2b = False
oneteract = 0
triggert1 = 1
stunint = False
knockback = 5
timec = 0
sli = 30
lost_fight = False
soulrec = 1
blinkt = 0
time = 0
blinktc = 600
triggert2 = 1
triggert3 = 1
triggert4 = 1
mjs = 1
souldammage = 1
triggert5 = 1
lostsoul_beaten = False
dashblock = False
slashc = 0
bsldammage = 2
bsoul_gain = 1
dash = 12
b2b = 0
platpc = 0
ftc = 0
level = -4
lives = 10
sgadd = 0
levsave = 0
ascrollc = 0
partam = 0
interact2ing = False
eq6f = False
eq5f = False
eq4f = False
eq3f = False
intcool = 0
rncad = 0
ft = 1
sch1eqa = 0
projss = 0
eqmo = False
ft0 = 1
ft1 = 1
dp = 0
eq1a = 0
eq2a = 0
eq3a = 0
eq4a = 0
eq5a = 0
eq6a = 0
b2b1 = False
b2b2 = False
b2b3 = False
sch1coled = False
ft2 = 1
ft3 = 1
ft4 = 1
selecting = 1
interacting = False
bcount = 0
ft5 = 1
ft6 = 1
ft7 = 1
ft8 = 1
bdc = 0
pdmadd = 0
souladd = 0
lost_attack = 0
intc=0
poisonc = 300
bmax_soul = 100
soul_gain = 1
cash = 0
apsh = 0
apss = 0
introt = 0
invulnrability = 0
projcost = 50
projdam = 4
projcool = 0
mprojcool = 1000
run = True

b1b = False
tutorialfont = pygame.font.SysFont(None,40)
bossfont = pygame.font.SysFont(None,70)
titlefont = pygame.font.SysFont(None,150)

def resetlevel(objects):
    for anobject in objects:
        anobject.resetInitialPosition()

soul = 130
jumps = 0
s1f = True
soulc = 0
xposition = 900
yposition = 500

def colap(cthing):
    apcol = False
    for d in aps:
        if apcol == False:
            if cthing.colliderect(d):
                apcol = True
    return apcol

while level < -1 and run == True:
    key = pygame.key.get_pressed()
    screen.fill((255,255,255))
    if level == -4:
        text = titlefont.render('Reapers Quest',True,(0,0,0),(255,255,255))
        screen.blit(text,(150,200))
        if selecting == 1:
            if blinkt == True:
                text = bossfont.render('<play>',True,(0,0,0),(255,255,255))
                screen.blit(text,(1472,400))
            else:
                text = bossfont.render('play',True,(0,0,0),(255,255,255))
                screen.blit(text,(1500,400))
            text = bossfont.render('options',True,(0,0,0),(255,255,255))
            screen.blit(text,(1500,600))
            if key[pygame.K_KP_ENTER] == True and dp < 1:
                level = -3
                dp = 200
        else:
            if blinkt == True:
                text = bossfont.render('<options>',True,(0,0,0),(255,255,255))
                screen.blit(text,(1472,600))
            else:
                text = bossfont.render('options',True,(0,0,0),(255,255,255))
                screen.blit(text,(1500,600))
            text = bossfont.render('play',True,(0,0,0),(255,255,255))
            screen.blit(text,(1500,400))
            if key[pygame.K_KP_ENTER] == True and dp < 1:
                level = -2
                selecting = 1
                dp = 200
    elif level == -3:
        text = titlefont.render('difficulty',True,(0,0,0),(255,255,255))
        screen.blit(text,(150,200))
        if selecting == 1:
            if blinkt == True:
                text = bossfont.render('<easy>',True,(0,0,0),(255,255,255))
                screen.blit(text,(1472,400))
            else:
                text = bossfont.render('easy',True,(0,0,0),(255,255,255))
                screen.blit(text,(1500,400))
            text = bossfont.render('hard',True,(0,0,0),(255,255,255))
            screen.blit(text,(1500,600))
            if key[pygame.K_KP_ENTER] == True and dp < 1:
                level = -1
                difficulty = 1
                dp = 200
        else:
            if blinkt == True:
                text = bossfont.render('<hard>',True,(0,0,0),(255,255,255))
                screen.blit(text,(1472,600))
            else:
                text = bossfont.render('hard',True,(0,0,0),(255,255,255))
                screen.blit(text,(1500,600))
            text = bossfont.render('easy',True,(0,0,0),(255,255,255))
            screen.blit(text,(1500,400))
            if key[pygame.K_KP_ENTER] == True and dp < 1:
                level = -1
                difficulty = 2
                dp = 200
    if blinktc < 1:
        if blinkt == True:
            blinkt = False
        else:
            blinkt = True
        blinktc = 450
    blinktc-=1
    dp-=1
    if key[pygame.K_DOWN] == True and dp < 1:
        if selecting == 1:
            selecting = 2
        else:
            selecting = 1
        dp = 160
    elif key[pygame.K_UP] == True and dp < 1:
        if selecting == 1:
            selecting = 2
        else:
            selecting = 1
        dp = 160
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
class movable(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height):
        self.inittop = top
        self.initback = back
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top
    health = 250
    invulnrabilityc = 0
    srinvulnrabilityc = 0
    hidden = False
    ensxm = 0
    wbreak = 0
    ensym = 0
    alr = 0
    coriographs = 0
    ppt = False
    cooldown = 0
    ymom = 0 
    slashlife = 40
    pdammage = 30
    initback = None
    inittop = None
    animate_step = 0
    animate_iterator = 0
    
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
player = movable(xposition,yposition - 20,30,60)
enemy1 = movable(1300,800,50,100)
spenemy1 = movable(1300,800,50,100)
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
slash = movable(0,0,60,50)
soulreap = movable(0,0,120,70)
ifloort = movable(0,1000,3000,50)
ibackwall = movable(0,400,50,600)
iceiling = movable(0,400,2000,50)
ifrontwall = movable(3000,700,50,400)
ifloort2 = movable(3000,700,1000,50)
ibackwall2 = movable(2000,0,50,600)
idjtest = movable(4000,100,50,600)
idjwalk = movable(4000,100,1000,50)
idjwalkceiling = movable(4000,-100,4500,50)
idashtest = movable(5300,100,3200,50)
istot = movable(8300,-20,40,120)
iflyingentest = movable(600,700,64,64)
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
ml3floort1 = movable(0,1000,3000,50)
ml3floort2 = movable(3050,-700,2000,50)
ml3floort3 = movable(4000,1000,2000,50)
ml3floort4 = movable(-900,-800,3000,50)
ml3floort5 = movable(0,-2000,2500,50)
ml3bwall1 = movable(0,0,50,1000)
ml3bwall2 = movable(2100,-800,50,800)
ml3bwall3 = movable(-900,-2800,50,2000)
ml3bwall4 = movable(5000,-700,50,700)
ml3bwall5 = movable(4000,0,50,1000)
ml3fwall1 = movable(3000,-700,50,1700)
ml3fwall2 = movable(6000,-1500,50,2500)
ml3fwall3 = movable(0,-2000,50,500)
ml3fwall4 = movable(2500,-2800,50,800)
ml3ceil1 = movable(0,0,2100,50)
ml3ceil2 = movable(0,-1500,6000,50)
ml3ceil3 = movable(4000,0,1000,50)
ml3ceil4 = movable(-900,-2800,3400,50)
ml3plat1 = movable(2150,600,200,50)
ml3plat2 = movable(2400,200,200,50)
ml3plat3 = movable(2150,-200,200,50)
ml3plat4 = movable(5100,-600,200,50)
ml3plat5 = movable(5400,-200,200,50)
ml3plat6 = movable(5100,200,200,50)
ml3plat7 = movable(5400,600,200,50)
ml3plat8 = movable(-300,-1000,200,50)
ml3plat9 = movable(-600,-1400,200,50)
ml3plat10 = movable(-300,-1800,200,50)
ml3enemy1 = movable(2000,800,50,100)
ml3enemy2 = movable(2250,800,50,100)
ml3enemy3 = movable(2500,800,50,100)
ml3enemy4 = movable(3100,-800,50,100)
ml3enemy5 = movable(3400,-800,50,100)
ml3enemy6 = movable(3700,-800,50,100)
ml3enemy7 = movable(3850,-800,50,100)
ml3stenemy1 = movable(1900,800,50,100)
ml3stenemy2 = movable(3250,-800,50,100)
ml3stenemy3 = movable(3550,-800,50,100)
ml3penemy1 = movable(2700,800,50,100)
ml3penemy2 = movable(2900,800,50,100)
ml3senemy1 = movable(2800,800,50,100)
ml3senemy2 = movable(4000,-800,50,100)
ml3senemy3 = movable(4150,-800,50,100)
lostsoul = movable(4200,880,60,100)
blockwall = movable(5000,-1500,50,800)
eqm = movable(200,100,1400,800)
ml2_eqar = movable(2300,-100,300,50)
ml2_eqarp = movable(3000,-350,200,50)
ml2_eq3 = movable(2450,-200,50,50)
chl_floort = movable(0,1000,1800,50)
chl_bwall = movable(0,0,50,1000)
chl_fwall = movable(1800,0,50,1000)
chl_ceil = movable(0,0,1800,50)
chl_ptarget1 = movable(0,400,100,150)
chl_ptarget2 = movable(0,700,100,150)
chl_ptarget3 = movable(1700,400,100,150)
ml2_soultotem = movable(10800,950,50,100)
soultotem = movable(5800,-400,50,100)
bsoultotem = movable(1000,950,50,100)
ml3soultotem = movable(2300,-2000,50,100)
b3floort = movable(0,1000,10000,50)
b3bwall = movable(0,0,50,1000)
b3ceil = movable(0,0,50,10000)
b3fwall1 = movable(1800,0,50,1000)
b3fwall2 = movable(10000,0,50,1000)
death = movable(100,850,40,150)
b3soultotem = movable(200,950,50,100)
b2soultotem = movable(200,950,50,100)

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
plprojectiles = []
stenemies = []
invisis = []
soultotems = []
prsponds = []
flyingens = []
bosses = [lostsoul, clotho, lachesis, atropos, beelzlbub, death]
player_front_image = pygame.image.load("player_front.gif")
player_right_image = pygame.image.load("player_right.gif")
player_left_image = pygame.transform.flip(player_right_image,True,False)
fen_1_1 = pygame.image.load("ghost_bat_thing1.png")
fen_2_1 = pygame.image.load("ghost_bat_thing2.png")
fen_3_1 = pygame.image.load("ghost_bat_thing3.png")
fen_1 = pygame.transform.scale(fen_1_1,(64,64))
fen_2 = pygame.transform.scale(fen_2_1,(64,64))
fen_3 = pygame.transform.scale(fen_3_1,(64,64))

if difficulty == 1:
    beelzlbub.health = 1000
    bbh = 1000
    clotho.health = 1700
    atropos.health = 1700
    lachesis.health = 1700
    lostsoul.health = 3000
    death.health = 5000
    bbenemdm = 1
else:
    beelzlbub.health = 1500
    bbh = 1500
    clotho.health = 2000
    atropos.health = 2000
    lachesis.health = 2000
    lostsoul.health = 4000
    death.health = 6000
    bbenemdm = 1.3


while run:
    if soul<1:
        levsave = level
        soul = max_soul
        lives-=1
        level = 2
        if difficulty == 1:
            time = 220
        else:
            time = 170
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

    dmable = spenemies + senemies + projectileenemies + enemies + stenemies + bosses + flyingens
    mable = objects+enemies+noncols+projectileenemies+projectiles+enatcks+fatcks+senemies+spenemies+stenemies+invisis+soultotems+flyingens 
#    if eq5a == 1 and not projectiles in dmable:
#        dmable.append(projectiles)
#    elif projectiles in dmable:
#        dmable.remove(projectiles)
    sldammage = bsldammage + sladd
    max_soul = bmax_soul + souladd
    soul_gain = bsoul_gain + sgadd
    benemdm = bbenemdm + pdmadd

    key = pygame.key.get_pressed()
    screen.fill((255,255,255))
    for anmobject in objects:
        pygame.draw.rect(screen,(0,0,0),anmobject)
    for aproj in projectiles:
        pygame.draw.rect(screen,(0,0,255),aproj)
    for anmenemy in enemies:
        pygame.draw.rect(screen,(200,0,0),anmenemy)
    for anmpenemy in projectileenemies:
        pygame.draw.rect(screen,(0,200,0),anmpenemy)
    for anmaps in aps:
        pygame.draw.rect(screen,(0,0,0),anmaps)
    for anmnoncol in noncols:
        pygame.draw.rect(screen,(50,0,0),anmnoncol)
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
    for anproj in plprojectiles:
        pygame.draw.rect(screen,(200,0,0),anproj)
    for astenemy in stenemies:
        pygame.draw.rect(screen,(250,0,250),astenemy)
    for asoultot in soultotems:
        pygame.draw.rect(screen,(0,0,250),asoultot)
    for aprsponds in prsponds:
        pygame.draw.rect(screen,(255,0,0),aprsponds)

    #pygame.draw.circle(screen,(255,0,0),player.center,40)
    

    pygame.draw.rect(screen,(200,200,200),soulbar,round(soul))
    text0 = tutorialfont.render(str(cash),True,(0,0,0),(255,255,255))
    screen.blit(text0,(100,100))
    text0 = tutorialfont.render("lives" + str(lives),True,(0,0,0),(255,255,255))
    screen.blit(text0,(100,150))
    if slashc > sli * 4:
        slash.hidden = False
        if facing == 1:
            slash.x=player.right
        else:
            slash.x=player.left-60
        slash.y = yposition - 10
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
            stunint = False
            objects = [roof,fwall,bwall,plat1,plat2,plat3,plat4,fiwall,backboard,floort,tplat1,tplat2,tplat3,tplat4,floort2,invis_sfloort,invis_sbwall]
            enemies = [enemy1,enemy2,enemy3]
            projectileenemies = [enemyprojectile,enemyprojectile2]
            noncols = [sbackboard,invis_secret,secret,dashup,slashup,lostsoul1]
            soulups = [secret]
            slashups = [slashup]
            dashups = [dashup]
            senemies = [spenemy1]
            stenemies = []
            invisis = []
            soultotems = [soultotem]
        if backboard.centerx < -4500:
            if stunint == True:
                level = 3
                stunint == False
        
    

    elif level == 0:
        objects = [ibackwall,iceiling,ifrontwall,ibackwall2,idjtest,idjwalkceiling,ifloort,ifloort2,idjwalk,idashtest]
        soultotems = [istot]
        enemies = []
        senemies = []
        noncols = []
        projectiles = []
        projectileenemies = []
        spenemies = []
        aps = []
        enatcks = []
        battacks = []
        flyingens = [iflyingentest]
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
                            text = tutorialfont.render('e to attack',True,(ft6,ft6,ft6),(255,255,255))
                            screen.blit(text,(900,200))
                            if ftc < 1:
                                ft6 += 1
                                ftc = 4
                        if ibackwall.centerx < -7200:
                            if triggert5 > 0:
                                triggert5 = 0
                            if ft8 < 255:   
                                text = tutorialfont.render('this is a soul totem, press w while overlapping with it to refil your soul, edit your equipables, and move to the next level',True,(ft8,ft8,ft8),(255,255,255))
                                screen.blit(text,(100,200))
                                if ftc < 1:
                                    ft8 += 1
                                    ftc = 15
                        
                        if stunint:
                            objects.clear()
                            level = 1
                            stunint = False
    elif level == 2:
        objects = [deadfwall1,deadbwall,deadceil,deadfwall2,deadfloort,deadfloort2]
        enemies = []
        noncols = []
        projectiles = []
        projectileenemies = []
        aps = []
        stenemies = []
        invisis = []
        soultotems = []
        text = tutorialfont.render('escape',True,(255,0,0),(255,255,255))
        screen.blit(text,(900,200))
        pygame.draw.rect(screen,(200,0,0),timebar,time)
        if timec < 1 and rncad == 0:
            time-=1
            timec = 15
        elif rncad == 0:
            timec-=1
        timebar.width = time
        if time < 1 or lives < 1:
            run = False
        if deadbwall.left < -1800:
            rncad = 1
            if lives > 5:
                text = tutorialfont.render("get back up and fight in my name",True,(ft7,ft7,ft7),(255,255,255))
                screen.blit(text,(900,200))
            elif lives < 6:
                text = tutorialfont.render("I cant give You many more of these",True,(ft7,ft7,ft7),(255,255,255))
                screen.blit(text,(900,200))
            elif lives < 2:
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
            stunint = False
            objects = [bossbwall,bossfwall,bossceiling,bossfloort]
            enemies = []
            noncols = [bosspoisonfloort,beelzlbub]
            projectiles = []
            projectileenemies = []
            invisis = [bsoultotem]
        boss = 1
        pygame.draw.rect(screen,(200,0,0),bhealthbar,round(beelzlbub.health))
        bhealthbar.width = round(beelzlbub.health)
        text = bossfont.render("beelzlbub, lord of flies",True,(255,100,100),(255,255,255))
        screen.blit(text,(400,0))
        if beelzlbub.health > bbh/2:
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
                soul-= 1.5 * benemdm
            if beelzlbub.ensxm < 0: 
                beelzlbub.ensxm+=0.02
            if beelzlbub.ensxm > 0: 
                beelzlbub.ensxm-=0.02
            if beelzlbub.ensxm > -0.1 and beelzlbub.ensxm < 0.1:
                beelzlbub.ensxm = 0
            if beelzlbub.colliderect(slash) and beelzlbub.invulnrabilityc < 1 and slash.hidden == False:
                beelzlbub.health-=sldammage
                beelzlbub.invulnrabilityc=sli
            beelzlbub.invulnrabilityc-=1
            beelzlbub.cooldown-=1
        elif beelzlbub.health > 0:
            if len(aps) == 0:
                poisonc = 100
                ymom = -13
            if platpc < 1:
                beelzplat = movable(bossbwall.x + 500,bossceiling.y + 100,150,50)
                aps.append(beelzplat)
                platchoice = random.randint(1,2)
                if platchoice == 1:
                    objects.append(beelzplat)
                else:
                    noncols.append(beelzplat)
                beelzplatp2 = movable(bossbwall.x + 1200,bossceiling.y + 100,150,50)
                aps.append(beelzplatp2)
                if platchoice == 2:
                    objects.append(beelzplatp2)
                else:
                    noncols.append(beelzplatp2)
                platpc = 1300
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
                ascrollc = 50
            else:
                ascrollc-=1
            if player.colliderect(bosspoisonfloort):
                if poisonc < 1:
                    soul-=40
                    ymom = -13
                    poisonc = 50
                else:
                    poisonc-=1
        else:
            b1b = True
            soultotems = [bsoultotem]
            invisis = []
            text = tutorialfont.render('soulreap unlocked, press R',True,(ft8,ft8,ft8),(255,255,255))
            screen.blit(text,(100,200))
            if stunint:
                level = 4
                stunint = False
    elif level == 4:
        if not ml2bwall1 in objects:
            stunint = False
            objects = [ml2bwall1,ml2bwall2,ml2bwall3,ml2bwall4,ml2ceiling1,ml2ceil2,ml2ceil3,ml2fwall1,ml2fwall2,ml2floort1,ml2floort2,ml2floort3,ml2floort4,ml2secretfloort1,ml2secretfloort2,ml2secretfloort3,ml2secretfloort4,ml2secretfloort5,ml2secretfloort6,ml2plat1,ml2plat2,ml2plat3,ml2plat4,ml2plat5,ml2_eqar,ml2_eqarp]
            enemies = [ml2enemy1,ml2enemy2,ml2enemy3,ml2enemy4,ml2enemy5,ml2enemy6,ml2enemy7,ml2enemy8,ml2enemy9,ml2enemy10,ml2enemy11]
            projectileenemies = [ml2penemy1,ml2penemy2,ml2penemy3,ml2penemy4,ml2penemy5]
            senemies = [ml2senemy]
            noncols = [ml2secretar1,ml2secret1,ml2secretar2,ml2secret2,ml2secretar3,ml2secret3,ml2secretar4,ml2secret4,ml2secretar5,ml2secret5,ml2secretar6,ml2secret6,ml2_eq3]
            aps = [ml2plat1,ml2plat2,ml2plat3,ml2plat4,ml2plat5,ml2_eqarp,ml2_eqar]
            soulups = [ml2secret1,ml2secret6]
            slashups = [ml2secret2]
            dashups = [ml2secret3]
            reapups = [ml2secret4]
            jumpups = [ml2secret5]
            soultotems = [ml2_soultotem]
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
            if stunint == True:
                level = 5
                stunint == False
    elif level == 5:
        if not l2bfloort in objects:
            objects = [l2bfloort,l2bbwall,l2bfwall,l2bceil]
            noncols = [atropos,lachesis,clotho]
            invisis = [b2soultotem]
            stunint == False
        pygame.draw.rect(screen,(200,0,0),bhealthbar)
        bhealthbar.width = (clotho.health + lachesis.health + atropos.health)
        text = bossfont.render("the fates",True,(255,100,100),(255,255,255))
        screen.blit(text,(400,0))
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
                soul-=0.3
                clotho.srinvulnrabilityc=5000
            clotho.invulnrabilityc-=1
            clotho.srinvulnrabilityc -= 1
            clotho.cooldown-=1
        else:
            b2b1 = True
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
                soul-=0.3
                lachesis.srinvulnrabilityc=5000
            lachesis.invulnrabilityc-=1
            lachesis.srinvulnrabilityc -= 1
            lachesis.cooldown-=1
        else:
            b2b2 = True
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
            if xposition > atropos.centerx - 120 and xposition < atropos.centerx + 120 and xmom == 0 and atropos.cooldown < 1 and invulnrability < 1:
                if atropos.centerx>player.left:
                    attack = movable(atropos.x - 150,atropos.y + 40,150,70)
                    statcks.append(attack)
                else:
                    attack = movable(atropos.x,atropos.y + 40,150,70)
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
                soul-=0.3
                atropos.srinvulnrabilityc=5000
            atropos.invulnrabilityc-=1
            atropos.srinvulnrabilityc-=1
            atropos.cooldown-=1
        else:
            b2b3 = True
        if b2b1 == True and b2b2 == True and b2b3 == True:
            b2b = True
            soultotems = [b2soultotem]
            invisis = []
            text = tutorialfont.render('projectile unlocked, press F',True,(ft8,ft8,ft8),(255,255,255))
            screen.blit(text,(100,200))
            if stunint:
                bosses.remove(atropos)
                bosses.remove(lachesis)
                bosses.remove(clotho)
                level = 6
                stunint = False
    elif level == 6:
        if not ml3floort1 in objects:
            stunint = False
            objects = [ml3floort1,ml3floort2,ml3floort3,ml3floort4,ml3floort5,ml3bwall1,ml3bwall2,ml3bwall3,ml3bwall4,ml3bwall5,ml3fwall1,ml3fwall2,ml3fwall3,ml3fwall4,ml3ceil1,ml3ceil2,ml3ceil3,ml3ceil4,ml3plat1,ml3plat2,ml3plat3,ml3plat4,ml3plat5,ml3plat6,ml3plat7,ml3plat8,ml3plat9,ml3plat10]
            enemies = [ml3enemy1,ml3enemy2,ml3enemy3,ml3enemy4,ml3enemy5,ml3enemy6,ml3enemy7]
            projectileenemies = [ml3penemy1,ml3penemy2]
            senemies = [ml3senemy1,ml3senemy2,ml3senemy3]
            stenemies = [ml3stenemy1,ml3stenemy2,ml3stenemy3]
            noncols = [lostsoul]
            aps = [ml3plat1,ml3plat2,ml3plat3,ml3plat4,ml3plat5,ml3plat6,ml3plat7,ml3plat8,ml3plat9,ml3plat10]
            soulups = []
            slashups = []
            dashups = []
            reapups = []
            jumpups = []
            prsponds = []
            invisis = [blockwall]
            soultotems = [ml3soultotem]
        if (player.x > ml3floort3.x and player.y > ml3floort3.y - 100 and player.x < ml3floort3.x + 1000 and lostsoul_beaten == False) or lost_fight == True:
            if not blockwall in objects:
                objects.append(blockwall)
                invisis.remove(blockwall)
                print("lsfv")
            if lostsoul.health > 0:
                pygame.draw.rect(screen,(0,0,150),lostsoul)
                lost_fight = True
                if lostsoul.health < 1700 and lostsoul.cooldown < 1:
                    atchoice = random.randint(1,6)
                else:
                    atchoice = random.randint(1,3)
                if atchoice == 1 and lostsoul.cooldown < 1 and lost_attack == 0 and projss < 1:
                    lostsoul.move(200,500)
                    if lostsoul.health < 1700:
                        lostsoul.wbreak = 250
                    else:
                        lostsoul.wbreak = 400
                    lost_attack = 1
                elif lost_attack == 1 and lostsoul.cooldown < 1 and lostsoul.wbreak < 1:
                    lostsoul.ensxm = 12
                    if lostsoul.health < 1700:
                        lostsoul.cooldown = 1500
                    else:
                        lostsoul.cooldown = 2500
                elif atchoice == 2 and lostsoul.cooldown < 1 and lost_attack == 0 and projss < 1:
                    lostsoul.move(1600,500)
                    if lostsoul.health < 1700:
                        lostsoul.wbreak = 250
                    else:
                        lostsoul.wbreak = 400
                    lost_attack = 2
                elif lost_attack == 2 and lostsoul.cooldown < 1 and lostsoul.wbreak < 1:
                    lostsoul.ensxm = -12
                    if lostsoul.health < 1700:
                        lostsoul.cooldown = 1500
                    else:
                        lostsoul.cooldown = 2500
                elif atchoice == 3 and lostsoul.cooldown < 1 and lost_attack == 0 and projss < 1:
                    lostsoul.move(900,0)
                    lostsoul.wbreak = 200
                    lost_attack = 3
                    
                elif lost_attack == 3 and lostsoul.cooldown < 1 and lostsoul.wbreak < 1:
                    lostsoul.ymom = 8
                    if lostsoul.health < 1700:
                        lostsoul.cooldown = 2000
                    else:
                        lostsoul.cooldown = 3000
                elif atchoice == 4 and lostsoul.cooldown < 1 and lost_attack == 0 and projss < 1:
                    lost_attack = 4
                    lostsoul.move(200,450)
                    projss = 6
                elif atchoice == 5 and lostsoul.cooldown < 1 and lost_attack == 0 and projss < 1:
                    lost_attack = 5
                    projss = 6
                    lostsoul.move(1600,450)
                elif (atchoice == 6) and lostsoul.cooldown < 1 and lost_attack == 0 and projss < 1 and player.x < lostsoul.x + 600 and player.x > lostsoul.x - 600:
                    lost_attack = 6
                    lostsoul.coriographs = 100
                elif lost_attack == 6 and lostsoul.cooldown < 1:
                    if lostsoul.coriographs < 1:
                        lostsoul.coooldown = 1000
                        if player.x < lostsoul.x + 700 and player.x > lostsoul.x - 700 + player.y < lostsoul.y + 700 and player.y > lostsoul.y - 700:
                            soul-=150 * benemdm
                            lost_attack = 0
                        else:
                            lost_attack = 0
                    elif lostsoul.cooldown < 1:
                        sigpart = movable(lostsoul.x + random.randint(-300,300), lostsoul.y + random.randint(-300,300), 5, 5)
                        projectiles.append(sigpart)
                        projectiles[len(projectiles) - 1].pdammage = 0
                        projectiles[len(projectiles) - 1].ppt = True
                        if projectiles[len(projectiles) - 1].x > lostsoul.x:
                            projectiles[len(projectiles) - 1].ensxm = -1
                        else:
                            projectiles[len(projectiles) - 1].ensxm = 1
                        if projectiles[len(projectiles) - 1].y > lostsoul.y:
                            projectiles[len(projectiles) - 1].ymom = -1
                        else:
                            projectiles[len(projectiles) - 1].ymom = 1
                        lostsoul.coriographs-=1
                        lostsoul.cooldown = 10

                else:
                    lostsoul.move_ip(lostsoul.ensxm,0)
                    if lost_attack == 1 or lost_attack == 2:
                        if lostsoul.colliderect(player):
                            soul-=0.8*abs(lostsoul.ensxm)*benemdm
                    elif lost_attack == 3:
                        lostsoul.move_ip(0,lostsoul.ymom)
                        if lostsoul.colliderect(player):
                            soul-=1*abs(lostsoul.ymom)*benemdm
                if lostsoul.ensxm > 0:
                    lostsoul.ensxm-=0.05
                elif lostsoul.ensxm < 0:
                    lostsoul.ensxm+=0.05
                elif lostsoul.ymom < 0:
                    lostsoul.ymom+=0.05
                elif lostsoul.ymom > 0:
                    lostsoul.ymom-=0.05
                if lostsoul.ensxm > -0.1 and lostsoul.ensxm < 0.1:
                    lostsoul.ensxm = 0
                    if (lost_attack == 1 or lost_attack == 2) and lostsoul.wbreak < 1:
                        lost_attack = 0
                if lostsoul.ymom > -0.1 and lostsoul.ymom < 0.1:
                    lostsoul.ymom = 0
                    if lost_attack == 3 and lostsoul.wbreak < 1:
                        lost_attack = 0
                lostsoul.cooldown-=1
                lostsoul.wbreak-=1

                if projss > 0 and lostsoul.cooldown<1:
                    if player.x < lostsoul.x:
                        lostproj = movable(lostsoul.x - 40,lostsoul.y+(projss-1)*10,20,10)
                        projectiles.append(lostproj)
                    else:
                        lostproj = movable(lostsoul.x + 70,lostsoul.y + 40,20,10)
                        projectiles.append(lostproj)
                    projectiles[len(projectiles) - 1].pdammage = 40
                    projectiles[len(projectiles) - 1].ppt = True
                    if player.x < lostsoul.x:
                        projectiles[len(projectiles) - 1].ensxm = -2
                    else:
                        projectiles[len(projectiles) - 1].ensxm = 2
                    projss-=1
                    lostsoul.cooldown = 500
                elif lost_attack == 4 or lost_attack == 5:
                    lost_attack = 0
            else:
                eq6f = True
                lostsoul_beaten = True
                lost_fight = False
                if blockwall in objects:
                    objects.remove(blockwall)
                text = tutorialfont.render('equipable aquired',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
        elif ml3bwall1.x > 300 and ml3bwall1.y < 1000:
            text = tutorialfont.render('w to travel the rift to a challenge level',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True:
                prhits = 0
                level = 7
        elif stunint:
            objects.clear()
            level = 8
            stunint = False
    elif level == 7:
        if not chl_floort in objects:
            time = 600
            objects = [chl_floort,chl_bwall,chl_fwall,chl_ceil]
            enemies = []
            projectileenemies = []
            senemies = []
            stenemies = []
            noncols = [chl_ptarget1,chl_ptarget2,chl_ptarget3]
            aps = []
            soulups = []
            slashups = []
            dashups = []
            reapups = []
            jumpups = []
            invisis = []
            prsponds = [chl_ptarget1,chl_ptarget2,chl_ptarget3]
        text = tutorialfont.render('shoot the red targets',True,(0,0,0),(255,255,255))
        screen.blit(text,(900,200))
        pygame.draw.rect(screen,(200,0,0),timebar,time)
        if timec < 1:
            time-=1
            timec = 30
        else:
            timec-=1
        if time < 1:
            level = 6
        timebar.width = time
        for prs in prsponds:
            for aplproj in plprojectiles:
                if prs.colliderect(aplproj):
                    prsponds.remove(prs)
                    prhits+=1
        if len(prsponds)<1:
            eq4f = True
            eq5f = True
            level = 6
    elif level == 8:
        level = 9
        if not b3floort in objects:
            objects = [b3floort,b3bwall,b3ceil,b3fwall1,b3fwall2]
            enemies = []
            senemies = []
            noncols = [death]
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
            plprojectiles = []
            stenemies = []
            invisis = [b3soultotem]
            soultotems = []
            prsponds = []
            atchoice = 0
        if death.health > 3000:
            pygame.draw.rect(screen,(200,0,100),death)
            if death.centerx>player.left and atchoice == 0:
                death.move_ip(-0.5,0)
                for awall in objects:
                    if death.colliderect(awall):
                        death.move_ip(1,0)
            elif death.centerx<player.left and atchoice == 0:
                death.move_ip(0.5,0)
                for awall in objects:
                    if death.colliderect(awall):
                        death.move_ip(-1,0)
            if player.centerx > death.centerx -200 and player.centerx < death.centerx + 200 and death.cooldown < 1 and atchoice == 0:
                death.ymom = -10
                death.cooldoown = 2500
                atchoice = 1
            elif atchoice == 1:
                death.move_ip(0,death.ymom)
                if death.ymom>0:
                    death.ymom-=0.05
                else:
                    death.ymom+=0.05
                if death.colliderect(player):
                    soul-=1
                if death.ymom > -0.1 and death.ymom < 0.1:
                    death.ymom = 0
                if death.ymom == 0:
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -2
                        projectiles[len(projectiles) - 1].ymom = 0
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -1.8
                        projectiles[len(projectiles) - 1].ymom = 0.2
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -1.6
                        projectiles[len(projectiles) - 1].ymom = 0.4
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -1.4
                        projectiles[len(projectiles) - 1].ymom = 0.6
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -1.2
                        projectiles[len(projectiles) - 1].ymom = 0.8
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -1
                        projectiles[len(projectiles) - 1].ymom = 1
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -0.8
                        projectiles[len(projectiles) - 1].ymom = 1.2
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -0.6
                        projectiles[len(projectiles) - 1].ymom = 1.4
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -0.4
                        projectiles[len(projectiles) - 1].ymom = 1.6
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = -0.2
                        projectiles[len(projectiles) - 1].ymom = 1.8
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 0
                        projectiles[len(projectiles) - 1].ymom = 2
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 0.2
                        projectiles[len(projectiles) - 1].ymom = 1.8
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 0.4
                        projectiles[len(projectiles) - 1].ymom = 1.6
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 0.6
                        projectiles[len(projectiles) - 1].ymom = 1.4
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 0.8
                        projectiles[len(projectiles) - 1].ymom = 1.2
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 1
                        projectiles[len(projectiles) - 1].ymom = 1
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 1.2
                        projectiles[len(projectiles) - 1].ymom = 0.8
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 1.4
                        projectiles[len(projectiles) - 1].ymom = 0.6
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 1.6
                        projectiles[len(projectiles) - 1].ymom = 0.4
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 1.8
                        projectiles[len(projectiles) - 1].ymom = 0.2
                        deathproj = movable(death.centerx,death.centery+70,10,10)
                        projectiles.append(deathproj)
                        projectiles[len(projectiles) - 1].pdammage = 50
                        projectiles[len(projectiles) - 1].ensxm = 2
                        projectiles[len(projectiles) - 1].ymom = 0
    elif level == 9:
        screen.fill((0,0,0))
        text = bossfont.render('a game by elias true schoenfelder watson',True,(255,255,255),(0,0,0))
        screen.blit(text,(200,200))
        text = tutorialfont.render('enemy and wall art by reuben haugen',True,(255,255,255),(0,0,0))
        screen.blit(text,(200,450))
        text = tutorialfont.render('player art by illiana',True,(255,255,255),(0,0,0))
        screen.blit(text,(200,700))
        text = tutorialfont.render('notable story assistance provided by colin bannen and will severtson',True,(255,255,255),(0,0,0))
        screen.blit(text,(200,800))




            

        
        





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

    if interacting == False and interact2ing == False:
        if key[pygame.K_a] == True and not key[pygame.K_s] == True:
            screen.blit(player_left_image,(885,480))
            moveObjsX(mable,1)
            facing = 0
        elif key[pygame.K_d] == True and not key[pygame.K_s] == True:
            screen.blit(player_right_image,(885,480))
            moveObjsX(mable,-1)
            facing = 1
        else:
            screen.blit(player_front_image,(885,480))
        if key[pygame.K_e] == True and slashc < 1:
            slashc = sli * 5
        if colt(player) == False and col(player) == False and jable < 1:
            if ymom < 1:
                ymom += 0.1
        if key[pygame.K_f] == True and projcool < 1 and soul > projcost and b2b == True:
            player_proj = movable(900,500,30,20)
            plprojectiles.append(player_proj)
            if facing == 1:
                plprojectiles[len(plprojectiles)-1].ensxm = 3
            else:
                plprojectiles[len(plprojectiles)-1].ensxm = -3
            soul-=projcost
            projcool = mprojcool - (eq4a/3)*mprojcool

        if key[pygame.K_SPACE] == True and (colt(player) == True or col(player) == True or jable>0) and jcool < 1 and not key[pygame.K_s] == True:
            ymom = JH
            jumps = mjs
            jcool = 250
        elif key[pygame.K_SPACE] == True and soul > 40 and jumps >0 and jcool < 1 and not key[pygame.K_s] == True:
            ymom = JH+1
            jumps -= 1
            jcool = 250
            soul-=40
        if key[pygame.K_q] == True and soul > 20 and dcool < 1 and not key[pygame.K_s] == True:
            if facing == 0:
                xmom = dash
            if facing == 1:
                xmom = dash*-1
            soul -= 20
            dcool = 500
    else:
        screen.blit(player_front_image,(885,480))
    if not xmom == 0:
        moveObjsX(mable,xmom)
        if xmom > 0:
            xmom-=0.2
        else:
            xmom+=0.2
        if xmom > -1 and xmom < 1:
            xmom = 0
    else:
        if col(player) == False and colt(player) == False:
            for thobject in mable:
                thobject.move_ip(0,ymom * -1)
        else:
            if colt(player) == True:
                if ymom < 0:
                    jable = 2
                    for thobject in mable:
                        thobject.move_ip(0,ymom * -1)
                else:
                    jable = 2
                    if colap(player):
                        for thobject in mable:
                            thobject.move_ip(0,0.6)
                            print("apcol")
            else:
                for thobject in mable:
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
            anEnemy.cooldown-=1
            if not (anEnemy.colliderect(slash) and slash.hidden == False):
                if anEnemy.ensxm>0:
                    anEnemy.ensxm-=0.1
                elif anEnemy.ensxm<0:
                    anEnemy.ensxm+=0.1
                if anEnemy.ensxm < 0.1 and anEnemy.ensxm > -0.1:
                    anEnemy.ensxm = 0
                anEnemy.move_ip(anEnemy.ensxm,0)
                if col(anEnemy):
                    anEnemy.move_ip(anEnemy.ensxm * -2,0)
        else:
            enemies.remove(anEnemy)
            if anEnemy in dmable:
                dmable.remove(anEnemy)
            eq3a * 15
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

#                print(str(apEnemy)+" is falling.")
            if not (apEnemy.colliderect(slash) and slash.hidden == False):
                if apEnemy.ensxm>0:
                    apEnemy.ensxm-=0.1
                elif apEnemy.ensxm<0:
                    apEnemy.ensxm+=0.1
                if apEnemy.ensxm < 0.1 and apEnemy.ensxm > -0.1:
                    apEnemy.ensxm = 0
                apEnemy.move_ip(apEnemy.ensxm,0)
                if col(apEnemy):
                    apEnemy.move_ip(apEnemy.ensxm * -2,0)
        else:
            projectileenemies.remove(apEnemy)
            if apEnemy in dmable:
                dmable.remove(apEnemy)
            soul+=eq3a * 15
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
                spenemies[len(spenemies) - 1].health = 1
                apEnemy.cooldown = 3000
            else:
                apEnemy.cooldown -= 1

#                print(str(apEnemy)+" is falling.")
            if not (apEnemy.colliderect(slash) and slash.hidden == False):
                if apEnemy.ensxm>0:
                    apEnemy.ensxm-=0.1
                elif apEnemy.ensxm<0:
                    apEnemy.ensxm+=0.1
                if apEnemy.ensxm < 0.1 and apEnemy.ensxm > -0.1:
                    apEnemy.ensxm = 0
                apEnemy.move_ip(apEnemy.ensxm,0)
                if col(apEnemy):
                    apEnemy.move_ip(apEnemy.ensxm * -2,0)
        else:
            senemies.remove(apEnemy)
            if apEnemy in dmable:
                dmable.remove(apEnemy)
            soul+=eq3a * 15
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
#    elif interacting == True:
#        oneteract = 0
#        interacting = False

        
    for asoul in soulups:
        if player.colliderect(asoul):
            if asoul in noncols:
                text = tutorialfont.render('w to pick up for 3 cash',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
                if key[pygame.K_w] == True and cash > 2:
                    bmax_soul+=15
                    bsoul_gain+=0.2
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
                    bsldammage+=1
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
                    JH-=1
                    mjs += 1
                    cash-=9
                    noncols.remove(ajump)
    if player.colliderect(ml2_eq3):
        if ml2_eq3 in noncols:
            text = tutorialfont.render('w to pick up equipable',True,(0,0,0),(255,255,255))
            screen.blit(text,(900,200))
            if key[pygame.K_w] == True and cash > 2:
                noncols.remove(ml2_eq3)
                eq3f = True
    
    for aproj in projectiles:
        aproj.move_ip(aproj.ensxm,0)
        aproj.move_ip(0,aproj.ymom)
        if player.colliderect(aproj) and xmom == 0:
            soul-=aproj.pdammage*benemdm
            projectiles.remove(aproj)
        elif aproj in projectiles:
            for aboss in bosses:
                if aproj.colliderect(aboss):
                    rems.append(aproj)
            for awall in objects:
                if aproj.colliderect(awall) and aproj.ppt == False:
                    rems.append(aproj)
            if aproj.x < player.x -2000:
                rems.append(aproj)
            elif aproj.x > player.x + 2000:
                rems.append(aproj)
            elif aproj.x < player.y -2000:
                rems.append(aproj)
            elif aproj.y > player.y + 2000:
                rems.append(aproj)
    for arem in rems:
        if arem in projectiles:
            projectiles.remove(arem)
        if arem in dmable:
            dmable.remove(arem)
    rems = []
    for anattack in enatcks:
        if anattack.slashlife > 0:
            anattack.height+=1
            anattack.slashlife-=1
            if anattack.colliderect(player) and xmom == 0:
                soul-=1*benemdm
        else:
            enatcks.remove(anattack)
    for anfattack in fatcks:
        if anfattack.slashlife > 0:
            anfattack.width+=1
            if anfattack.alr == -1:
                anfattack.move_ip(-1,0)
            anfattack.slashlife-=1
            if anfattack.colliderect(player) and xmom == 0:
                soul-=1*benemdm
        else:
            fatcks.remove(anfattack)
    intc = 0
    for anstattack in statcks:
        if anstattack.slashlife > 0:
            anstattack.slashlife-=1
            if anstattack.colliderect(player) and xmom == 0:
                interact2ing = True
            else:
                intc += 1
        else:
            statcks.remove(anstattack)
    if intc == len(statcks):
        interact2ing = False
    for anEnemy in spenemies:
        if anEnemy.health > 0:
            if xposition > anEnemy.centerx - 800 and xposition < anEnemy.centerx + 800 and not anEnemy.colliderect(player):
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
                    soul-=1*benemdm
                    invulnrability = 3
            if not (anEnemy.colliderect(slash) and slash.hidden == False):
                if anEnemy.ensxm>0:
                    anEnemy.ensxm-=0.1
                elif anEnemy.ensxm<0:
                    anEnemy.ensxm+=0.1
                if anEnemy.ensxm < 0.1 and anEnemy.ensxm > -0.1:
                    anEnemy.ensxm = 0
                anEnemy.move_ip(anEnemy.ensxm,0)
                if col(anEnemy):
                    anEnemy.move_ip(anEnemy.ensxm * -2,0)
        else:
            rems.append(anEnemy)
            soul+=eq3a * 15
    for arem in rems:
        spenemies.remove(arem)
        if anEnemy in dmable:
            dmable.remove(arem)
    rems = []

    for atot in soultotems:
        if player.colliderect(atot):
            if interacting == False:
                text = tutorialfont.render('w to use totem',True,(0,0,0),(255,255,255))
                screen.blit(text,(900,200))
            if key[pygame.K_w]:
                if interacting == True and atot.cooldown < 1:
                    interacting = False
                    stunint = True
                    soul = max_soul
                    atot.cooldown = 250
                elif atot.cooldown < 1 and interacting == False:
                    interacting = True
                    selecting = 1
                    atot.cooldown = 250
            atot.cooldown-=1
            if interacting == True:
                soultotem_menu.fill((250,250,250))
                text = bossfont.render('equipables',True,(0,0,0),(200,200,200))
                soultotem_menu.blit(text,(50,0))
                if selecting == 1:
                    text = bossfont.render('<1>',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(100,300))
                    text = bossfont.render('2',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(300,300))
                    if eq3f:
                        text = bossfont.render('3',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(500,300))
                    if eq4f == True:
                        text = bossfont.render('4',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(700,300))
                    if eq5f == True:
                        text = bossfont.render('5',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(900,300))
                    if eq6f == True:
                        text = bossfont.render('6',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(1100,300))
                    text = tutorialfont.render('take more dammage deal more dammage',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(50,500))
                    text = bossfont.render(str(eq1a),True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(1100,50))
                    if key[pygame.K_UP] == True and dp < 1 and interacting == True:
                        eq1a+=1
                        if eq1a>3:
                            eq1a = 0
                        dp = 160
                    elif key[pygame.K_UP] == True and dp < 1 and interacting == True:
                        eq1a-=1
                        if eq1a<0:
                            eq1a = 3
                        dp = 160
                    else:
                        dp-=1
                elif selecting == 2:
                    text = bossfont.render('1',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(100,300))
                    if eq3f:
                        text = bossfont.render('3',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(500,300))
                    if eq4f == True:
                        text = bossfont.render('4',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(700,300))
                    if eq5f == True:
                        text = bossfont.render('5',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(900,300))
                    if eq6f == True:
                        text = bossfont.render('6',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(1100,300))
                    text = bossfont.render('<2>',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(300,300))
                    text = tutorialfont.render('more max soul, less soul regen',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(50,500))
                    text = bossfont.render(str(eq2a),True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(1100,50))
                    if key[pygame.K_UP] == True and dp < 1 and interacting == True:
                        eq2a+=1
                        if eq2a>3:
                            eq2a = 0
                        dp = 160
                    elif key[pygame.K_UP] == True and dp < 1 and interacting == True:
                        eq2a-=1
                        if eq2a<0:
                            eq2a = 3
                        dp = 160
                    else:
                        dp-=1
                elif selecting == 3:
                    if eq3f:
                        text = bossfont.render('<3>',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(500,300))
                    text = bossfont.render('2',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(300,300))
                    text = bossfont.render('1',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(100,300))
                    if eq4f == True:
                        text = bossfont.render('4',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(700,300))
                    if eq5f == True:
                        text = bossfont.render('5',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(900,300))
                    if eq6f == True:
                        text = bossfont.render('6',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(1100,300))
                    text = tutorialfont.render('lose soulreap effectiveness but gain some  soul each kill',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(50,500))
                    text = bossfont.render(str(eq3a),True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(1100,50))
                    if key[pygame.K_UP] == True and dp < 1 and interacting == True and eq3f:
                        eq3a+=1
                        if eq3a>3:
                            eq3a = 0
                        dp = 160
                    else:
                        dp-=1
                elif selecting == 4:
                    if eq4f == True:
                        text = bossfont.render('<4>',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(700,300))
                    text = bossfont.render('1',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(100,300))
                    text = bossfont.render('2',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(300,300))
                    if eq3f:
                        text = bossfont.render('3',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(500,300))
                    if eq5f == True:
                        text = bossfont.render('5',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(900,300))
                    if eq6f == True:
                        text = bossfont.render('6',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(1100,300))
                    text = tutorialfont.render('fire projectiles faster but deal less slash dammage',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(50,500))
                    text = bossfont.render(str(eq4a),True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(1100,50))
                    if key[pygame.K_UP] == True and dp < 1 and interacting == True and eq4f:
                        eq4a+=1
                        if eq4a>3:
                            eq4a = 0
                        dp = 160
                    else:
                        dp-=1
                elif selecting == 5:
                    if eq5f == True:
                        text = bossfont.render('<5>',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(900,300))
                    text = bossfont.render('1',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(100,300))
                    text = bossfont.render('2',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(300,300))
                    if eq3f:
                        text = bossfont.render('3',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(500,300))
                    if eq4f == True:
                        text = bossfont.render('4',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(700,300))
                    if eq6f == True:
                        text = bossfont.render('6',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(1100,300))
                    text = tutorialfont.render('slash projectiles to deflect them',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(50,500))
                    text = bossfont.render(str(eq5a),True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(1100,50))
                    if key[pygame.K_UP] == True and dp < 1 and interacting == True and eq5f == True:
                        eq5a+=1
                        if eq5a>1:
                            eq5a = 0
                        dp = 160
                    else:
                        dp-=1
                elif selecting == 6:
                    if eq6f == True:
                        text = bossfont.render('<6>',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(1100,300))
                    text = bossfont.render('1',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(100,300))
                    text = bossfont.render('2',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(300,300))
                    if eq3f:
                        text = bossfont.render('3',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(500,300))
                    if eq4f == True:
                        text = bossfont.render('4',True,(0,0,0),(200,200,200))
                        soultotem_menu.blit(text,(700,300))
                    text = bossfont.render('5',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(900,300))
                    text = tutorialfont.render('small dammage increase',True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(50,500))
                    text = bossfont.render(str(eq6a),True,(0,0,0),(200,200,200))
                    soultotem_menu.blit(text,(1100,50))
                    if key[pygame.K_UP] == True and dp < 1 and interacting == True and eq6f:
                        eq6a+=1
                        if eq6a>1:
                            eq6a = 0
                        dp = 160
                    elif not eq6f:
                        eq6a = 0
                    else:
                        dp-=1
                sladd = (eq1a * 0.3 * bsldammage) + (eq6a * 0.05 * bsldammage) - (eq4a * 0.1 * bsldammage)
                souladd = 2/3 * eq2a * bmax_soul
                sgadd = -1/4 * eq2a * bsoul_gain
                pdmadd = eq1a * 0.2 * bbenemdm
                                        
                screen.blit(soultotem_menu,(200,100))



            if key[pygame.K_RIGHT] == True and dp < 1 and interacting == True:
                selecting+=1
                if selecting>6:
                    selecting = 1
                dp = 160
            elif key[pygame.K_LEFT] == True and dp < 1 and interacting == True:
                selecting-=1
                if selecting<1:
                    selecting = 6
                dp = 160
            else:
                dp-=1
            
    
    for anEnemy in stenemies:
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
                            attack = movable(anEnemy.x - 50,anEnemy.y + 30,80,50)
                            statcks.append(attack)
                        else:
                            attack = movable(anEnemy.x + 80,anEnemy.y + 30,80,50)
                            statcks.append(attack)
                        statcks[len(statcks) - 1].slashlife = 120
                        anEnemy.cooldown = 500
                anEnemy.cooldown-=1
                if not (anEnemy.colliderect(slash) and slash.hidden == False):
                    if anEnemy.ensxm>0:
                        anEnemy.ensxm-=0.1
                    elif anEnemy.ensxm<0:
                        anEnemy.ensxm+=0.1
                    if anEnemy.ensxm < 0.1 and anEnemy.ensxm > -0.1:
                        anEnemy.ensxm = 0
                    anEnemy.move_ip(anEnemy.ensxm,0)
                    if col(anEnemy):
                        anEnemy.move_ip(anEnemy.ensxm * -2,0)
            else:
                rems.append(anEnemy)
                soul+=eq3a * 15
                cash+=3
    for arem in rems:
        stenemies.remove(arem)
        if anEnemy in dmable:
            dmable.remove(arem)
    rems = []

    for afen in flyingens:
        if afen.health > 0:
            if afen.animate_step == 0:
                screen.blit(fen_1,(afen.x,afen.y))
            elif afen.animate_step == 1:
                screen.blit(fen_2,(afen.x,afen.y))
            elif afen.animate_step == 2:
                screen.blit(fen_3,(afen.x,afen.y))
            else:
                afen.animate_step = 0
            if xposition > afen.centerx - 600 and xposition < afen.centerx + 600 and yposition > afen.centery - 600 and yposition < afen.centery + 600 and not afen.colliderect(player):
                afen.move_ip(((xposition-afen.centerx)/math.sqrt((xposition-afen.centerx)**2+(yposition-afen.centery)**2)) * 0.6,((yposition-afen.centery)/math.sqrt((xposition-afen.centerx)**2+(yposition-afen.centery)**2)) * 0.6)
                for anob in objects:
                    if afen.colliderect(anob):
                        afen.move_ip(((xposition-afen.centerx)/math.sqrt((xposition-afen.centerx)**2+(yposition-afen.centery)**2)) * -1,((yposition-afen.centery)/math.sqrt((xposition-afen.centerx)**2+(yposition-afen.centery)**2)) * -1)
            afen.animate_iterator += 1
            if afen.animate_iterator > 60:
                afen.animate_iterator = 0
                afen.animate_step += 1
            if afen.colliderect(player):
                soul-=0.3
            
                

    for adma in dmable:
        if adma.colliderect(slash) and slash.hidden == False:
            adma.health-=sldammage
            if facing == 1:
                adma.ensxm = 5
            else:
                adma.ensxm = -5
        if adma.colliderect(soulreap) and soulreap.hidden == False and (adma in spenemies or adma in senemies or adma in projectileenemies or adma in enemies or adma in stenemies or adma in bosses):
            adma.health-=souldammage
            soul+=souldammage-(souldammage/3)*eq3a
        for aplproj in plprojectiles:
            if adma.colliderect(aplproj):
                adma.health-=projdam
    
    for aplproj in plprojectiles:
        aplproj.move_ip(aplproj.ensxm,0)
        aplproj.move_ip(0,aplproj.ymom)
        for awall in objects:
            if aplproj.colliderect(awall):
                rems.append(aplproj)
    while len(rems) > 0:
        plprojectiles.remove(rems[0])
        rems.remove(rems[0])
        
    
    ftc-=1
    jcool-=1
    soulc-=1
    jable-=1
    slashc-=1
    intcool-=1
    invulnrability-=1
    dcool-=1
    soulrec-=1
    projcool-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if soulc < 1 and soul < max_soul:
        if key[pygame.K_s] == True:
            soul+=soul_gain
            soulc = 20
    soulbar.width = soul
    #timekeep.sleep(0.005)


    pygame.display.update()

pygame.quit()