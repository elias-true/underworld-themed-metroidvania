import pygame
pygame.init()
import time as timekeep
import random
import math


Screen_Hight = 1200
Screen_width = 2000
run = True
screen = pygame.display.set_mode((Screen_width,Screen_Hight))
foraging_guidebook = pygame.surface.Surface((1400,800))
tutorialfont = pygame.font.SysFont(None,40)
bossfont = pygame.font.SysFont(None,70)
titlefont = pygame.font.SysFont(None,150)

class movable(pygame.Rect):
    "these are objects that can be moved and destroyed"
    def __init__(self,back,top,width,height):
        self.inittop = top
        self.initback = back
        super().__init__(back,top,width,height)
        self.tx = back
        self.ty = top

    thing_type = 0
    
    def move_ip(self,deltaX:float,deltaY:float):
        self.tx = self.tx+deltaX
        self.ty = self.ty+deltaY
        selfAsRect = super()
        selfAsRect.move_ip(round(self.tx)-selfAsRect.x,round(self.ty)-selfAsRect.y)

    def move(self,X:float,Y:float):
        self.tx = X
        self.ty = Y
        selfAsRect = super()
        selfAsRect.move(round(X),round(Y))

    def resetInitialPosition(self):
        self.tx = self.initback
        self.ty = self.inittop
        self.move(self.tx,self.ty)

area = 1
level_indicator = 0
manual_open = False
selecting = 1
dp = 0
totalpoints = 0
currentpoints = 0

player = movable(975,550,50,100)

visible_things = []



def move_stuff(x,y):
    res = False
    for athing in visible_things:
        athing.move_ip(x,y)
        if athing.thing_type < 3 and athing.colliderect(player) and not athing.thing_type == 0:
            athing.move_ip(-1.5*x,-1.5*y)
            x/=2
            y/=2
            athing.move_ip(x,y)
        if athing.thing_type == 0 and athing.colliderect(player):
            res = True
            
    if res == True:
        for athing in visible_things:
            athing.move_ip(-2*x,-2*y)



while run:
    key = pygame.key.get_pressed()
    screen.fill((200,200,200))
    pygame.draw.rect(screen,(80,10,0),player)
    for athing in visible_things:
        if athing.thing_type < 2:
            pygame.draw.rect(screen,(100,80,100),athing)
        else:
            if athing.thing_type == 3:
                pygame.draw.polygon(screen,(40,200,70),[(athing.x+20,athing.y),(athing.x+16,athing.y+5),(athing.x+16,athing.y+22),(athing.x+8,athing.y+18),(athing.x,athing.y+22),(athing.x+8,athing.y+26),(athing.x+16,athing.y+22),(athing.x+16,athing.y+60),(athing.x+24,athing.y+60),(athing.x+24,athing.y+42),(athing.x+32,athing.y+46),(athing.x+40,athing.y+42),(athing.x+32,athing.y+38),(athing.x+24,athing.y+42),(athing.x+24,athing.y+5)])
                athing.width = 35
                athing.height = 60
            elif athing.thing_type == 4:
                pygame.draw.rect(screen,(40,200,70),athing)
                pygame.draw.polygon(screen,(40,200,70),[(athing.x+20,athing.y),(athing.x+16,athing.y+5),(athing.x+16,athing.y+22),(athing.x+8,athing.y+18),(athing.x,athing.y+22),(athing.x+8,athing.y+26),(athing.x+16,athing.y+22),(athing.x+16,athing.y+60),(athing.x+24,athing.y+60),(athing.x+24,athing.y+42),(athing.x+32,athing.y+46),(athing.x+40,athing.y+42),(athing.x+32,athing.y+38),(athing.x+24,athing.y+42),(athing.x+24,athing.y+5)])
                athing.width = 35
                athing.height = 40
            elif athing.thing_type == 5:
                pygame.draw.rect(screen,(130,150,0),athing)
                athing.width = 35
                athing.height = 60
            elif athing.thing_type == 6:
                pygame.draw.rect(screen,(130,150,0),athing)
                athing.width = 35
                athing.height = 40
            elif athing.thing_type == 7:
                pygame.draw.rect(screen,(40,200,70),athing)
                athing.width = 60
                athing.height = 50
            elif athing.thing_type == 8:
                pygame.draw.rect(screen,(0,150,150),athing)
                athing.width = 35
                athing.height = 40
            if key[pygame.K_e] == True and player.colliderect(athing):
                if athing.thing_type == 3 or athing.thing_type == 4 or athing.thing_type == 5:
                    currentpoints+=1
                else:
                    currentpoints-=2
                visible_things.remove(athing)

    if area == 1:
        if not level_indicator == 1:
            levelbackwall = movable(-500,-500,50,2200)
            levelfrontwall = movable(2500,-500,50,2200)
            leveltopwall = movable(-500,-500,3000,50)
            levelbottomwall = movable(-500,1700,3000,50)
            test_rock = movable(78,800,60,60)
            visible_things = [test_rock,levelbackwall,levelbottomwall,levelfrontwall,leveltopwall]
            test_rock.thing_type = 1
            new_plant = movable(random.randint(-500,3000),random.randint(-400,1600),1,1)
            visible_things.append(new_plant)
            new_plant.thing_type = random.randint(3,8)
            new_plant = movable(random.randint(-500,3000),random.randint(-400,1600),1,1)
            visible_things.append(new_plant)
            new_plant.thing_type = random.randint(3,8)
            new_plant = movable(random.randint(-500,3000),random.randint(-400,1600),1,1)
            visible_things.append(new_plant)
            new_plant.thing_type = random.randint(3,8)
            new_plant = movable(random.randint(-500,3000),random.randint(-400,1600),1,1)
            visible_things.append(new_plant)
            new_plant.thing_type = random.randint(3,8)
            new_plant = movable(random.randint(-500,3000),random.randint(-400,1600),1,1)
            visible_things.append(new_plant)
            new_plant.thing_type = random.randint(3,8)
            new_plant = movable(random.randint(-500,3000),random.randint(-400,1600),1,1)
            visible_things.append(new_plant)
            new_plant.thing_type = random.randint(3,8)
            level_indicator = 1
    
    if manual_open == False:
        if key[pygame.K_w] == True:
            move_stuff(0,1)
        if key[pygame.K_s] == True:
            move_stuff(0,-1)
        if key[pygame.K_a] == True:
            move_stuff(1,0)
        if key[pygame.K_d] == True:
            move_stuff(-1,0)
    
    if key[pygame.K_i] == True:
        if area == 1:
            area = 2
            totalpoints+=currentpoints
            currentpoints = 0
            timekeep.sleep(0.2)
        elif area == 2:
            area = 1
            level_indicator = 0
            timekeep.sleep(0.2)
    if area == 2:
        screen.blit(foraging_guidebook,(300,150))
        foraging_guidebook.fill((250,250,200))
        text = bossfont.render('foraging',True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(50,0))
        text = bossfont.render('points' + str(totalpoints),True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(500,0))
        text = bossfont.render('1',True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(100,300))
        text = bossfont.render('2',True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(300,300))
        text = bossfont.render('3',True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(500,300))
        text = bossfont.render('4',True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(700,300))
        text = bossfont.render('5',True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(900,300))
        text = bossfont.render('6',True,(0,0,0),(200,200,200))
        foraging_guidebook.blit(text,(1100,300))
        if selecting == 1:
            text = tutorialfont.render('light green, somewhat tall, alternate leaves, edble',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(50,500))
            text = bossfont.render('<1>',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(60,300))
        elif selecting == 2:
            text = tutorialfont.render('light green, short, edble',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(50,500))
            text = bossfont.render('<2>',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(260,300))
        elif selecting == 3:
            text = tutorialfont.render('brownish green, somewhat tall, edble',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(50,500))
            text = bossfont.render('<3>',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(460,300))
        elif selecting == 4:
            text = tutorialfont.render('brownish green, short, poison',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(50,500))
            text = bossfont.render('<4>',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(660,300))
        elif selecting == 5:
            text = tutorialfont.render('light green, wide, poison',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(50,500))
            text = bossfont.render('<5>',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(860,300))
        elif selecting == 6:
            text = tutorialfont.render('blue green, short, poison',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(50,500))
            text = bossfont.render('<6>',True,(0,0,0),(200,200,200))
            foraging_guidebook.blit(text,(1060,300))
        if key[pygame.K_RIGHT] == True and dp < 1:
            selecting+=1
            if selecting>6:
                selecting = 1
            dp = 100
        elif key[pygame.K_LEFT] == True and dp < 1:
            selecting-=1
            if selecting<1:
                selecting = 6
            dp = 100
        else:
            dp-=1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()