from pygame.locals import*
import sys
import pygame

class Player:
    def __init__(self,size,pos):
        self.width=size[0]
        self.height=size[1]
        self.x=grid(pos[0])
        self.y=grid(pos[1])
        self.arr=[]
        self.land=[]
        for ar1 in range(grid(w//2-50),grid(w//2+50),d):
            for ar2 in range(grid(h//2-50),grid(h//2+50),d):
                self.land.append((ar1,ar2))

    def draw(self,win):
        self.arr.append((self.x,self.y))
        if not((self.x,self.y) in self.land):
            for ar in range(len(self.arr)):
                pygame.draw.rect(win,LBLUE,(self.arr[ar][0],self.arr[ar][1],self.height,self.width))
        else:
            self.land=self.land+self.arr
            self.arr=[]
            self.land+=givepoints(self.land)
        for la in range(len(self.land)):
            pygame.draw.rect(win,LDBLUE,(self.land[la][0],self.land[la][1],self.height,self.width))
        pygame.draw.rect(win,BLUE,(self.x,self.y,self.height,self.width))

def givepoints(area):
    s=[]
    time=0
    for y in range(0,h,d):
        time=0
        for x in range(0,w,d):
            if (x,y) in area:
                time+=1
            if time==1:
                xi=x
            if time==2:
                time=0
                if ((x-xi)==d):
                    for ax in range(xi,x,d):
                        s.append((ax,y))
    return s
                


def redrawwin(win):
    win.fill(WHITE)

    for x in range (0,w+2*d,2*d):
        for y in range(0,h+2*d,2*d):
            pygame.draw.rect(win,GRAY,(x,y,d,d))
    for x in range (d,w+2*d,2*d):
        for y in range(d,h+2*d,2*d):
            pygame.draw.rect(win,GRAY,(x,y,d,d))
    player.draw(win)
    rect1=pygame.Rect(0,0,grid(w/2),grid(h/2))
    rect1.center=((w/2),(h/2))
    pygame.draw.rect(win, (255, 128, 0), rect1, 2)
    pygame.display.update()

def grid(x):
    x=(x//d)*d
    return x

pygame.init()
w,h=(1000,500)
win=pygame.display.set_mode((w,h))
global d
d=12
dir=0
WHITE=(255,255,255)
GRAY=(55,55,55)
BLUE=(0,0,255)
LDBLUE=(0,128,128)
LBLUE=(0,255,255)
RED=(255,0,0)
player=Player((2*d,2*d),(w/2,h/2))
clock = pygame.time.Clock() 
while True:
    redrawwin(win)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                dir=1
            if event.key==K_DOWN:
                dir=-1
            if event.key==K_LEFT:
                dir=-2
            if event.key==K_RIGHT:
                dir=2
            if event.key==K_SPACE:
                dir=0
    if dir==1:
        player.y-=d
    if dir==-1:
        player.y+=d
    if dir==2:
        player.x+=d
    if dir==-2:
        player.x-=d
    clock.tick(40)
