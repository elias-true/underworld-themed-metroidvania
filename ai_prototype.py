import pygame
pygame.init()
import time as timekeep
import random
import math
import copy

Screen_Hight = 800
Screen_width = 1500
run = True
screen = pygame.display.set_mode((Screen_width,Screen_Hight))
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

    def move_ip(self,deltaX:float,deltaY:float):
        self.tx = self.tx+deltaX
        self.ty = self.ty+deltaY
        selfAsRect = super()
        selfAsRect.move_ip(round(self.tx)-selfAsRect.x,round(self.ty)-selfAsRect.y)

    def move(self,X:float,Y:float):
        "Move the moveable to a new location."
        self.tx = X
        self.ty = Y
        selfAsRect = super()
        selfAsRect.move(round(X),round(Y))

    def resetInitialPosition(self):
        self.tx = self.initback
        self.ty = self.inittop
        self.move(self.tx,self.ty)



class neuron:
    _knowledge:list = []

    def __init__(self,initial_knowledge:list):
        self._knowledge = copy.deepcopy(initial_knowledge)
    
    def evaluate(self,external_info:list):
        total = 0
        for index in range(len(external_info)):
            if index > len(self._knowledge):
                break
            total += external_info[index]*self._knowledge[index]
        if total > 0:
            out = 1
        else:
            out = 0
        return out
    
    def mutate(self):
        for nmbdr in range(len(self._knowledge)):
            self._knowledge[nmbdr] += random.uniform(-.5,.5)

    def copy(self,other_neuron):
        self._knowledge = copy.deepcopy(other_neuron._knowledge)
class projectile(movable):
    shooter = None
    xmomentum = 0
    life = 400

class movable_ai(movable):
    def __init__(self,back,top,width,height):
        super().__init__(back,top,width,height)
        self.go_up = neuron([random.uniform(-3,3),random.uniform(-3,3)])
        self.go_down = neuron([random.uniform(-3,3),random.uniform(-3,3)])
        self.go_left = neuron([random.uniform(-3,3),random.uniform(-3,3)])
        self.go_right = neuron([random.uniform(-3,3),random.uniform(-3,3)])
        self.shoot_left = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)])
        self.shoot_right = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)])
    shootcooldown = 0

    def copy_neurons(self,other_movable_ai):
        self.go_right.copy(other_movable_ai.go_right)
        self.go_left.copy(other_movable_ai.go_left)
        self.go_up.copy(other_movable_ai.go_up)
        self.go_down.copy(other_movable_ai.go_down)
        self.shoot_right.copy(other_movable_ai.shoot_right)
        self.shoot_left.copy(other_movable_ai.shoot_left)
    
    def mutate_neurons(self):
        self.go_right.mutate()
        self.go_left.mutate()
        self.go_up.mutate()
        self.go_down.mutate()
        self.shoot_right.mutate()
        self.shoot_left.mutate()
        

    def deltafind(self,tgoal:movable):
        ai_deltax = (self.tx-tgoal.tx)
        ai_deltay = (self.ty-tgoal.ty)
        return [ai_deltax,ai_deltay]

    def move_toward_goal(self,goal):
        move_x = self.go_left.evaluate(self.deltafind(goal)) - self.go_right.evaluate(self.deltafind(goal))
        move_y = self.go_up.evaluate(self.deltafind(goal)) - self.go_down.evaluate(self.deltafind(goal))
        self.move_ip(move_x,move_y)
    def shoot_toward(self,goals:list):
        shootx = 0
        for goal in goals:
            shootx += self.shoot_left.evaluate(self.deltafind(goal)) - self.shoot_right.evaluate(self.deltafind(goal))
        if shootx > 0:
            newproj = projectile(self.x,self.y,30,10)
            newproj.shooter = self
            newproj.xmomentum = 3
            projectiles.append(newproj)
        elif shootx < 0:
            newproj = projectile(self.x,self.y,30,10)
            newproj.shooter = self
            newproj.xmomentum = -3
            projectiles.append(newproj)
        shootcooldown = 500

    points = 0

def reset_points(moveable_ai_list:list):
    for a_moveable_ai in moveable_ai_list:
        a_moveable_ai.points=0


aiformebest = movable_ai(750,400,50,100)
aichalenger = movable_ai(750,400,50,100)
aiformebest2 = movable_ai(750,400,50,100)
aichalenger2 = movable_ai(750,400,50,100)
aiformebest3 = movable_ai(750,400,50,100)
aichalenger3 = movable_ai(750,400,50,100)

the_ai_list = [aiformebest,aichalenger,aiformebest2,aichalenger2,aiformebest3,aichalenger3]
projectiles = []
rems = []

goal = movable(random.randint(0,1500),random.randint(0,800),50,50)
tickcount = 0
generations = 0


while run:
    if tickcount < 1:
        tickcount = 2000
        generations+=1
        for anai in the_ai_list:
            anai.points-=math.sqrt(((anai.y-goal.y)**2)+((anai.x-goal.x)**2))/1000

        the_ai_list.sort( key=(lambda some_ai : some_ai.points) , reverse=True )

        for index in range(1,len(the_ai_list)):
            the_ai_list[index].copy_neurons(the_ai_list[0])
            the_ai_list[index].mutate_neurons()

        goal.move(0,0)
        goal.move_ip(random.randint(0,1500),random.randint(0,800))

        for anai in the_ai_list:
            anai.move(750,400)

        reset_points(the_ai_list) # after learning happens, reset the AIs to learn again
    

    screen.fill((200,200,200))
    pygame.draw.rect(screen,(0,100,0),aiformebest)
    pygame.draw.rect(screen,(100,0,0),aichalenger)
    pygame.draw.rect(screen,(0,100,0),aiformebest2)
    pygame.draw.rect(screen,(100,0,0),aichalenger2)
    pygame.draw.rect(screen,(0,100,0),aiformebest3)
    pygame.draw.rect(screen,(100,0,0),aichalenger3)
    pygame.draw.rect(screen,(0,100,0),goal)
    for aproj in projectiles:
        if aproj.life > 0:
            pygame.draw.rect(screen,(0,0,100),aproj)
            aproj.move_ip(aproj.xmomentum,0)
            for anai in the_ai_list:
                if aproj.colliderect(anai) and not anai == aproj.shooter:
                    anai.move_ip(aproj.xmomentum*50,0)
                    aproj.shooter.points +=0.1
                    anai.points -= 0.1
                    rems.append(aproj)
        else:
            rems.append(aproj)
    for arem in rems:
        if arem in projectiles:
            projectiles.remove(arem)
    rems = []
    text = bossfont.render(str(generations),True,(0,0,0),(255,255,255))
    screen.blit(text,(150,200))

    

    
    
    for anai in the_ai_list:
        anai.move_toward_goal(goal)
        if anai.shootcooldown < 1:
            anai.shoot_toward(the_ai_list)
            anai.shootcooldown = 500
        else:
            anai.shootcooldown -= 1
   
    for anai in the_ai_list:
        if anai.x<0 or anai.x>1500 or anai.y<0 or anai.y>800:
            anai.points-=0.01
        if anai.colliderect(goal):
            anai.points+=10
            goal.move(0,0)
            goal.move_ip(random.randint(0,1500),random.randint(0,800))
    

    tickcount-=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()