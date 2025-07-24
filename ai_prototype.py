import pygame
pygame.init()
import time as timekeep
import random
import math

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

def evaluate_neuron(inputs:list,knowledge:list):
    total = 0
    for index in range(len(inputs)):
        if index > len(knowledge):
            break
        total+=inputs[index]*knowledge[index]
    if total > 0:
        out = 1
    else:
        out = 0
    return out

class movable_ai(movable):
    ai_hidden_layer_1_1 = 0
    ai_hidden_layer_1_2 = 0
    ai_hidden_layer_1_3 = 0
    ai_hidden_layer_2_1 = 0
    ai_hidden_layer_2_2 = 0
    ai_hidden_layer_2_3 = 0
    ai_hidden_layer_2_4 = 0
    ai_hidden_layer_1_1_signal = 0
    ai_hidden_layer_1_2_signal = 0
    ai_hidden_layer_1_3_signal = 0
    ai_hidden_layer_2_1_signal = 0
    ai_hidden_layer_2_2_signal = 0
    ai_hidden_layer_2_3_signal = 0
    ai_hidden_layer_2_4_signal = 0
    points = 0

    def __init__(self,back,top,width,height):
        super().__init__(back,top,width,height)


aiformebest = movable_ai(750,400,50,100)
aichalenger = movable_ai(750,400,50,100)
goal = movable(random.randint(0,1500),random.randint(0,800),50,50)
tickcount = 0
generations = 0
aiformebestpoints = 0
aichalengerpoints = 0
aiformebest_deltax = 0
aiformebest_deltay = 0
aiformebest_hidden_layer_1_1 = random.uniform(-3,3)
aiformebest_hidden_layer_1_2 = random.uniform(-3,3)
aiformebest_hidden_layer_1_3 = random.uniform(-3,3)
aiformebest_hidden_layer_2_1 = random.uniform(-3,3)
aiformebest_hidden_layer_2_2 = random.uniform(-3,3)
aiformebest_hidden_layer_2_3 = random.uniform(-3,3)
aiformebest_hidden_layer_2_4 = random.uniform(-3,3)
aiformebest_hidden_layer_1_1_signal = 0
aiformebest_hidden_layer_1_2_signal = 0
aiformebest_hidden_layer_1_3_signal = 0
aiformebest_hidden_layer_2_1_signal = 0
aiformebest_hidden_layer_2_2_signal = 0
aiformebest_hidden_layer_2_3_signal = 0
aichalenger_hidden_layer_2_4_signal = 0
aichalenger_hidden_layer_1_1_signal = 0
aichalenger_hidden_layer_1_2_signal = 0
aichalenger_hidden_layer_1_3_signal = 0
aichalenger_hidden_layer_2_1_signal = 0
aichalenger_hidden_layer_2_2_signal = 0
aichalenger_hidden_layer_2_3_signal = 0
aichalenger_hidden_layer_2_4_signal = 0
aiformebest_output_up = 0
aiformebest_output_down = 0
aiformebest_output_left = 0
aiformebest_output_right = 0

aichalenger_deltax = 0
aichalenger_deltay = 0
aichalenger_hidden_layer_1_1 = random.uniform(-3,3)
aichalenger_hidden_layer_1_2 = random.uniform(-3,3)
aichalenger_hidden_layer_1_3 = random.uniform(-3,3)
aichalenger_hidden_layer_2_1 = random.uniform(-3,3)
aichalenger_hidden_layer_2_2 = random.uniform(-3,3)
aichalenger_hidden_layer_2_3 = random.uniform(-3,3)
aichalenger_hidden_layer_2_4 = random.uniform(-3,3)
aichalenger_output_up = 0
aichalenger_output_down = 0
aichalenger_output_left = 0
aichalenger_output_right = 0


while run:
    if tickcount < 1:
        tickcount = 900
        aichalengerpoints = 0
        aiformebestpoints = 0
        generations+=1
        aiformebestpoints -= math.sqrt(((aiformebest.y-goal.y)**2)+((aiformebest.x-goal.x)**2))/1000
        aichalengerpoints -= math.sqrt(((aichalenger.y-goal.y)**2)+((aichalenger.x-goal.x)**2))/1000
        if aichalengerpoints > aiformebestpoints:
            aiformebest_hidden_layer_1_1 = aichalenger_hidden_layer_1_1
            aiformebest_hidden_layer_1_2 = aichalenger_hidden_layer_1_2
            aiformebest_hidden_layer_1_3 = aichalenger_hidden_layer_1_3
            aiformebest_hidden_layer_2_1 = aichalenger_hidden_layer_2_1
            aiformebest_hidden_layer_2_2 = aichalenger_hidden_layer_2_2
            aiformebest_hidden_layer_2_3 = aichalenger_hidden_layer_2_3
            aiformebest_hidden_layer_2_4 = aichalenger_hidden_layer_2_4
            aichalenger_hidden_layer_1_1 = aiformebest_hidden_layer_1_1 + random.uniform(-2,2)
            aichalenger_hidden_layer_1_2 = aiformebest_hidden_layer_1_2 + random.uniform(-2,2)
            aichalenger_hidden_layer_1_3 = aiformebest_hidden_layer_1_3 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_1 = aiformebest_hidden_layer_2_1 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_2 = aiformebest_hidden_layer_2_2 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_3 = aiformebest_hidden_layer_2_3 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_4 = aiformebest_hidden_layer_2_4 + random.uniform(-2,2)
        else:
            aichalenger_hidden_layer_1_1 = aiformebest_hidden_layer_1_1 + random.uniform(-2,2)
            aichalenger_hidden_layer_1_2 = aiformebest_hidden_layer_1_2 + random.uniform(-2,2)
            aichalenger_hidden_layer_1_3 = aiformebest_hidden_layer_1_3 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_1 = aiformebest_hidden_layer_2_1 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_2 = aiformebest_hidden_layer_2_2 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_3 = aiformebest_hidden_layer_2_3 + random.uniform(-2,2)
            aichalenger_hidden_layer_2_4 = aiformebest_hidden_layer_2_4 + random.uniform(-2,2)
        goal.move(0,0)
        goal.move_ip(random.randint(0,1500),random.randint(0,800))
        aichalenger.move(750,400)
        aiformebest.move(750,400)
    
    key = pygame.key.get_pressed()
    screen.fill((200,200,200))
    pygame.draw.rect(screen,(0,100,0),aiformebest)
    pygame.draw.rect(screen,(100,0,0),aichalenger)
    pygame.draw.rect(screen,(0,100,0),goal)
    text = bossfont.render(str(generations),True,(0,0,0),(255,255,255))
    screen.blit(text,(150,200))
    text = bossfont.render(str(aichalengerpoints) + 'chalenger',True,(0,0,0),(255,255,255))
    screen.blit(text,(150,500))
    text = bossfont.render(str(aiformebestpoints) + 'formerbest',True,(0,0,0),(255,255,255))
    screen.blit(text,(150,700))
    
    aichalenger_deltay = (aichalenger.y-goal.y)
    aichalenger_deltax = (aichalenger.x-goal.x)
    aiformerbest_deltay = (aiformebest.y-goal.y)
    aiformebest_deltax = (aiformebest.x-goal.x)
    
    aichalenger_hidden_layer_1_1_signal = aichalenger_hidden_layer_1_1 * ((aichalenger_deltax**2) + (aichalenger_deltay**2))
    aichalenger_hidden_layer_1_2_signal = aichalenger_hidden_layer_1_2 * ((aichalenger_deltax**2) + (aichalenger_deltay**2))
    aichalenger_hidden_layer_1_3_signal = aichalenger_hidden_layer_1_3 * ((aichalenger_deltax**2) + (aichalenger_deltay**2))
    aichalenger_hidden_layer_2_1_signal = aichalenger_hidden_layer_2_1 * aichalenger_hidden_layer_1_1_signal
    aichalenger_hidden_layer_2_2_signal = aichalenger_hidden_layer_2_2 * aichalenger_hidden_layer_1_1_signal + aichalenger_hidden_layer_1_2_signal
    aichalenger_hidden_layer_2_3_signal = aichalenger_hidden_layer_2_3 * aichalenger_hidden_layer_1_3_signal + aichalenger_hidden_layer_1_2_signal
    aichalenger_hidden_layer_2_4_signal = aichalenger_hidden_layer_2_4 * aichalenger_hidden_layer_1_3_signal
    aichalenger_output_up = aichalenger_hidden_layer_2_1_signal + aichalenger_hidden_layer_2_2_signal
    aichalenger_output_down = aichalenger_hidden_layer_2_2_signal + aichalenger_hidden_layer_2_3_signal
    aichalenger_output_left = aichalenger_hidden_layer_2_3_signal + aichalenger_hidden_layer_2_4_signal
    aichalenger_output_right = aichalenger_hidden_layer_2_4_signal + aichalenger_hidden_layer_2_1_signal
    
    aiformerbest_hidden_layer_1_1_signal = aiformebest_hidden_layer_1_1 * ((aiformebest_deltax**2) + (aiformebest_deltay**2))
    aiformerbest_hidden_layer_1_2_signal = aiformebest_hidden_layer_1_2 * ((aiformebest_deltax**2) + (aiformebest_deltay**2))
    aiformerbest_hidden_layer_1_3_signal = aiformebest_hidden_layer_1_3 * ((aiformebest_deltax**2) + (aiformebest_deltay**2))
    aiformerbest_hidden_layer_2_1_signal = aiformebest_hidden_layer_2_1 * aiformerbest_hidden_layer_1_1_signal
    aiformerbest_hidden_layer_2_2_signal = aiformebest_hidden_layer_2_2 * aiformerbest_hidden_layer_1_1_signal + aiformerbest_hidden_layer_1_2_signal
    aiformerbest_hidden_layer_2_3_signal = aiformebest_hidden_layer_2_3 * aiformerbest_hidden_layer_1_3_signal + aiformerbest_hidden_layer_1_2_signal
    aiformerbest_hidden_layer_2_4_signal = aiformebest_hidden_layer_2_4 * aiformerbest_hidden_layer_1_3_signal
    aichalenger_output_up = aichalenger_hidden_layer_2_1_signal + aichalenger_hidden_layer_2_2_signal
    aiformerbest_output_down = aiformerbest_hidden_layer_2_2_signal + aiformerbest_hidden_layer_2_3_signal
    aiformerbest_output_left = aiformerbest_hidden_layer_2_3_signal + aiformerbest_hidden_layer_2_4_signal
    aiformerbest_output_right = aiformerbest_hidden_layer_2_4_signal + aiformerbest_hidden_layer_2_1_signal
    if aichalenger_output_down > aichalenger_output_up:
        aichalenger.move_ip(0,1)
    else:
        aichalenger.move_ip(0,-1)
    if aichalenger_output_left > aichalenger_output_right:
        aichalenger.move_ip(-1,0)
    else:
        aichalenger.move_ip(1,0)
    if aichalenger.colliderect(goal):
        aichalengerpoints+=5
        goal.move(0,0)
        goal.move_ip(random.randint(0,1500),random.randint(0,800))
    
    if aiformerbest_output_down > aiformebest_output_up:
        aiformebest.move_ip(0,1)
    else:
        aiformebest.move_ip(0,-1)
    if aiformerbest_output_left > aiformerbest_output_right:
        aiformebest.move_ip(-1,0)
    else:
        aiformebest.move_ip(1,0)
    if aiformebest.colliderect(goal):
        aiformebestpoints+=5
        goal.move(0,0)
        goal.move_ip(random.randint(0,1500),random.randint(0,800))
    tickcount-=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()