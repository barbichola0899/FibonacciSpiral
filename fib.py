import pyautogui as p
import numpy as np
import math

class Spiral():
    def __init__(self,width, height, coord):
        self.width = width
        self.height = height
        self.coord = coord


    def DrawRectangle(self):
        iw_max = GetIndex(self.width,self.height)[0]
        ih_max = GetIndex(self.width,self.height)[1]
        w_max = fib(iw_max)
        h_max = fib(ih_max)
        #set perimeter
        p.click(coord[0],coord[1])
        p.dragRel(w,0,duration= 0.5)#right
        p.dragRel(0,h,duration = 0.5)#down
        p.dragRel(-w,0, duration= 0.5)#left
        p.dragRel(0,-h,duration = 0.5)#up
        i = iw_max -1
        coord_inicial = np.array([self.coord[0] + fib(i), self.coord[1]])
        p.click(coord_inicial[0],coord_inicial[1])
        while i > 0:
            dir_drag = np.array(dirDrag(i))
            print(dir_drag)
            vet_drag = np.array([fib(i), fib(i)])
            print(vet_drag)
            vet_drag = vet_drag * dir_drag
            print(vet_drag)
            p.dragRel(vet_drag[0],vet_drag[1],duration = 0.5)
            i = i - 1
            vet_rot = np.array(vetRot(i))
            print(vet_rot)
            vet_click = np.array([fib(i),fib(i)])
            print(vet_click)
            vet_click =  vet_click * vet_rot
            print(vet_click)
            coord_inicial = coord_inicial + vet_click
            print(coord_inicial)
            p.click(coord_inicial[0],coord_inicial[1])

    def DrawSpiral(self):
        i_max = GetIndex(self.width,self.height)[0]
        i = i_max - 1
        coord_inicial = np.array([self.coord[0] + fib(i), self.coord[1]+fib(i)])
        theta = math.pi
        cont = 1 #1 = n para caso dot[0] == center[0] ou dot[1] == center[1]
        center = np.array([coord_inicial[0],coord_inicial[1]])
        while i > 0: #iterar os diferenes quartos de circulis
            r = fib(i)
            print(r)
            #loops para cada quarto de circulo
            while not(math.fabs(round(math.sin(theta),4)) == 1 or math.fabs(round(math.cos(theta),4)) == 1)or cont == 1: 
                cont = 0
                dot = np.array([r*math.cos(theta), (-1)*r*math.sin(theta)])        
                print(dot)
                dot += center
                p.click(dot[0],dot[1],clicks = 2)
                theta -= 0.02
            cont = 1
            vet_center = np.array(dirDrag(i))#vetor para mover o centro 
            print(vet_center)
            vet_center *= -1
            print(vet_center)
            i -= 1
            vet_mod = np.array([fib(i-1),fib(i-1)])
            vet_mod *= vet_center
            center += vet_mod
            print(center)            
            

def fib(i):#i é o i-ésimo numero, e fib(i) é o valor deste número 
    if i == 1:
        return 1
    if i == 2:
        return 1
    else:
        return fib(i-1) + fib(i-2)
        
def GetIndex(width,height):
    iwidth = iheight = 0
    x = 1
    while x < 100:
        print(x,fib(x))
        if fib(x) == width:
            iwidth = x
        if fib(x) == height:
            iheight = x
        
        if iwidth != 0 and iheight != 0:
            break

        x += 1
    
    return(iwidth, iheight)

def vetRot(i):#vet q determinará para onde o proximo click irá
    if i % 4 == 0:
        vet = (-1,1)
    if i % 4 == 1:
        vet = (1,1)

    if i % 4 == 2:
        vet = (1,-1)
    
    if i % 4 == 3:
        vet = (-1,-1)

    return(vet)

def dirDrag(i):
    vet = (0,0)
    if i % 4 == 0:
        vet = (0,-1)

    if i % 4 == 1:
        vet = (-1,0)

    if i % 4 == 2:
        vet = (0,1)
    
    if i % 4 == 3:
        vet = (1,0)

    return(vet)


w= 610
h = 377
coord = (10,205)
espiral = Spiral(w,h,coord)
espiral.DrawSpiral()