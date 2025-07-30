import pygame
pygame.init()
import time as timekeep
import random
import math
import copy

Screen_Hight = 800
Screen_width = 1500
playgame = False
run = True
facing = 0
playerpoints = 0
playercooldown = 0
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
    biasknowledge = None

    def __init__(self,initial_knowledge:list,initial_biasknowledge):
        self._knowledge = copy.deepcopy(initial_knowledge)
        self.biasknowledge = copy.deepcopy(initial_biasknowledge)
    
    def evaluate(self,external_info:list):
        total = 0
        for index in range(len(external_info)):
            if index > len(self._knowledge):
                break
            total += external_info[index]*self._knowledge[index]
        total+=self.biasknowledge
        if total > 0:
            out = 1
        else:
            out = 0
        return out
    
    def mutate(self):
        for nmbdr in range(len(self._knowledge)):
            self._knowledge[nmbdr] += random.uniform(-.7,.7)
        self.biasknowledge += random.uniform(-.3,.3)

    def copy(self,other_neuron):
        self._knowledge = copy.deepcopy(other_neuron._knowledge)
class projectile(movable):
    shooter = None
    xmomentum = 0
    life = 200

class movable_ai(movable):
    def __init__(self,back,top,width,height):
        super().__init__(back,top,width,height)
        self.jump = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.jump2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.jump3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.dontjump = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.dontjump2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.dontjump3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.go_left = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.go_left2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.go_left3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.go_right = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.go_right2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.go_right3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.shoot_left = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.shoot_left2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.shoot_left3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.shoot_right = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.shoot_right2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.shoot_right3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.attack_right = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.attack_right2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.attack_right3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.attack_left = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.attack_left2 = neuron([random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
        self.attack_left3 = neuron([random.uniform(-3,3),random.uniform(-3,3)],random.uniform(-3,3))
    shootcooldown = 0
    timebetweenhit = 0
    exp = 0
    health = 50
    ymomentum = 0
    jumps = 0


    def copy_neurons(self,other_movable_ai):
        self.go_right.copy(other_movable_ai.go_right)
        self.go_right2.copy(other_movable_ai.go_right2)
        self.go_right3.copy(other_movable_ai.go_right3)
        self.go_left.copy(other_movable_ai.go_left)
        self.go_left2.copy(other_movable_ai.go_left2)
        self.go_left3.copy(other_movable_ai.go_left3)
        self.jump.copy(other_movable_ai.jump)
        self.jump2.copy(other_movable_ai.jump2)
        self.jump3.copy(other_movable_ai.jump3)
        self.dontjump.copy(other_movable_ai.dontjump)
        self.dontjump2.copy(other_movable_ai.dontjump2)
        self.dontjump3.copy(other_movable_ai.dontjump3)
        self.shoot_left.copy(other_movable_ai.shoot_left)
        self.shoot_left2.copy(other_movable_ai.shoot_left2)
        self.shoot_left3.copy(other_movable_ai.shoot_left3)
        self.shoot_right.copy(other_movable_ai.shoot_right)
        self.shoot_right2.copy(other_movable_ai.shoot_right2)
        self.shoot_right3.copy(other_movable_ai.shoot_right3)
        self.attack_left.copy(other_movable_ai.attack_left)
        self.attack_left2.copy(other_movable_ai.attack_left2)
        self.attack_left3.copy(other_movable_ai.attack_left3)
        self.attack_right.copy(other_movable_ai.attack_right)
        self.attack_right2.copy(other_movable_ai.attack_right2)
        self.attack_right3.copy(other_movable_ai.attack_right3)
    
    def mutate_neurons(self):
        self.go_right.mutate()
        self.go_right2.mutate()
        self.go_right3.mutate()
        self.go_left.mutate()
        self.go_left2.mutate()
        self.go_left3.mutate()
        self.jump.mutate()
        self.jump2.mutate()
        self.jump3.mutate()
        self.dontjump.mutate()
        self.dontjump2.mutate()
        self.dontjump3.mutate()
        self.shoot_left.mutate()
        self.shoot_left2.mutate()
        self.shoot_left3.mutate()
        self.shoot_right.mutate()
        self.shoot_right2.mutate()
        self.shoot_right3.mutate()
        self.attack_left.mutate()
        self.attack_left2.mutate()
        self.attack_left3.mutate()
        self.attack_right.mutate()
        self.attack_right2.mutate()
        self.attack_right3.mutate()
        

    def deltafind(self,tgoal:movable):
        ai_deltax = (self.tx-tgoal.tx)
        ai_deltay = (self.ty-tgoal.ty)
        return [ai_deltax,ai_deltay]

    def move_toward_goal(self,goals):
        move_x = 0
        move_y = 0
        for goal in goals:
            move_x += self.go_left3.evaluate([self.go_left2.evaluate(self.deltafind(goal)),self.go_left.evaluate(self.deltafind(goal))]) - self.go_right3.evaluate([self.go_right2.evaluate(self.deltafind(goal)),self.go_right.evaluate(self.deltafind(goal))])
            move_y += self.jump3.evaluate([self.jump2.evaluate(self.deltafind(goal)),self.jump.evaluate(self.deltafind(goal))]) - self.dontjump3.evaluate([self.dontjump2.evaluate(self.deltafind(goal)),self.dontjump.evaluate(self.deltafind(goal))])
        if move_x>0:
            self.move_ip(1,0)
        elif move_x<0:
            self.move_ip(-1,0)
        if move_y<0 and self.jumps == 1:
            self.ymomentum = -10
            self.move_ip(0,-200)
            self.jumps = 0
    def shoot_toward(self,goals:list):
        shootx = 0
        for goal in goals:
            shootx += self.shoot_left3.evaluate([self.shoot_left2.evaluate(self.deltafind(goal)),self.shoot_left.evaluate(self.deltafind(goal))]) - self.shoot_right3.evaluate([self.shoot_right2.evaluate(self.deltafind(goal)),self.shoot_right.evaluate(self.deltafind(goal))])
        if shootx > 0:
            newproj = projectile(self.x,self.y,30,10)
            newproj.shooter = self
            newproj.xmomentum = 5
            projectiles.append(newproj)
            if self.upgrade == True:
                newproj.life = 100
        elif shootx < 0:
            newproj = projectile(self.x,self.y,30,10)
            newproj.shooter = self
            newproj.xmomentum = -5
            projectiles.append(newproj)
            if self.upgrade == True:
                newproj.life = 100
    def attack_toward(self,goals:list):
        shootx = 0
        for goal in goals:
            shootx += self.attack_left3.evaluate([self.attack_left2.evaluate(self.deltafind(goal)),self.attack_left.evaluate(self.deltafind(goal))]) - self.attack_right3.evaluate([self.attack_right2.evaluate(self.deltafind(goal)),self.attack_right.evaluate(self.deltafind(goal))])
        if shootx > 0:
            newproj = projectile(self.x-30,self.y,30,10)
            newproj.shooter = self
            attacks.append(newproj)
            if self.upgrade == True:
                newproj.life = 50
        elif shootx < 0:
            newproj = projectile(self.x+50,self.y,30,10)
            newproj.shooter = self
            attacks.append(newproj)
            if self.upgrade == True:
                newproj.life = 50

    points = 0

def reset_points(moveable_ai_list:list):
    for a_moveable_ai in moveable_ai_list:
        a_moveable_ai.points=0


aiformebest = movable_ai(750,400,50,100)
aichalenger = movable_ai(750,400,50,100)


the_ai_list = [aiformebest,aichalenger]
projectiles = []
attacks = []
rems = []



tickcount = 0
generations = 0


while run:
    if aiformebest.health < 1 or aichalenger.health < 1 or tickcount<1:
        generations+=1
        tickcount = 8000
        projectiles.clear()

        the_ai_list.sort( key=(lambda some_ai : some_ai.health), reverse=True )

        for index in range(1,len(the_ai_list)):
            the_ai_list[index].copy_neurons(the_ai_list[0])
            the_ai_list[index].mutate_neurons()


        for anai in the_ai_list:
            anai.exp = 0
            anai.health=50
            anai.upgrade = False
            anai.move(0,0)
            anai.move_ip(random.randint(0,1500),700)

        reset_points(the_ai_list) # after learning happens, reset the AIs to learn again
    

    screen.fill((200,200,200))
    #key = pygame.key.get_pressed()
    pygame.draw.rect(screen,(0,100,0),aiformebest)
    pygame.draw.rect(screen,(100,0,0),aichalenger)
    for aproj in projectiles:
        if aproj.life > 0:
            pygame.draw.rect(screen,(0,0,100),aproj)
            aproj.move_ip(aproj.xmomentum,0)
            aproj.life-=1
            for anai in the_ai_list:
                if aproj.colliderect(anai) and not anai == aproj.shooter:
                    anai.move_ip(aproj.xmomentum*50,0)
                    anai.health -= 20
                    rems.append(aproj)
        else:
            rems.append(aproj)
    for arem in rems:
        if arem in projectiles:
            projectiles.remove(arem)
    rems = []
    for aproj in attacks:
        if aproj.life > 0:
            pygame.draw.rect(screen,(0,0,100),aproj)
            aproj.life-=1
            for anai in the_ai_list:
                if aproj.colliderect(anai) and not anai == aproj.shooter:
                    anai.move_ip(aproj.xmomentum*50,0)
                    anai.health -= 20
                    rems.append(aproj)
        else:
            rems.append(aproj)
    for arem in rems:
        if arem in attacks:
            attacks.remove(arem)
    rems = []
    text = bossfont.render('generations ' + str(generations),True,(0,0,0),(255,255,255))
    screen.blit(text,(150,200))



    

    
    
    for anai in the_ai_list:
        #TODO:  Create a list of "relative positions" for the current AI and pass that in as the "goals"
        #TODO:  Maybe add an attribute to the movables class to say whether they are "good" or "bad".  Then the AI could learn to go toward good things and avoid bad ones.
        anai.move_toward_goal(the_ai_list + projectiles)
        if anai.shootcooldown < 1:
            anai.shoot_toward(the_ai_list)
            anai.shootcooldown = 200


   
    for anai in the_ai_list:
        anai.shootcooldown -= 1
        anai.move_ip(0,anai.ymomentum)
        if anai.x<0 or anai.x>1500 or anai.y<0 or anai.y>800:
            anai.health-=50
            anai.move(0,0)
            anai.move_ip(random.randint(0,1500),700)
        elif anai.ymomentum<1 and anai.y<700:
            anai.ymomentum+=0.3
        elif anai.y>700 or anai.y == 700:
            anai.move(anai.x,700)
            anai.ymomentum = 0
            anai.jumps = 1

            
    
    tickcount-=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()