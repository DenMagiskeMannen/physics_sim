# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:52:58 2023

@author: teodo
"""
import time
import random
import matplotlib.pyplot as plt



def limfind(list):
    smallest=0
    biggest=0
    for number in list:
        if number < smallest:
            smallest=number
        elif number > biggest:
            biggest= number
    return(smallest,biggest)

def establish_para():
    plt.xlim(xlim0,xlim1)
    plt.ylim(ylim0,ylim1+10)

def check_on_ground(y_value,floor_value):
    On_ground=False
    if y_value<=floor_value:
        On_ground=True
    else:
        On_ground=False
    return(On_ground)

def do_friction(vector,coof,ratio):
    friction=(vector*coof)/ratio
    print(friction)
    if vector > 0: #
        vector=vector-friction
        if vector < 0:
            vector=0
        print("Big;",vector)
    elif vector < 0:
        vector=vector+friction
        if vector > 0:
            vector=0
        print("small;",vector)
        
    return(vector)

#Material
elasticity=0.9


#Vo
startUp=0
startRight=3

#So
startX=2
startY=100

#A
g=-9.81
m=10
G=m*g


air_friction=0
ground_friction=1
Xresistence=0 #Wind or smt


#T
timestep=0.01
totaltime=2.0
times=[]
for i in range(int(totaltime/timestep)):
    times.append(i)

print(times)

currentX=startX
currentY=startY

Yvector=startUp
Xvector=startRight

Distances=[]
Heights=[]


#physics
for frame in times:
    #print(frame,currentY)
    #Ratio
    ratio=1/timestep
    
    #MovementX
    #XForce
    Xvector=Xvector+(Xresistence/ratio)
    currentX=currentX+(Xvector)
    #Movement Y
    Yvector=Yvector+(g/ratio)
    currentY=currentY+Yvector
    
    if currentY <=0:
        #print(Yvector)
        #currentY=currentY-Yvector
        currentY=0
        Yvector=Yvector*(-1)*elasticity
        #print(Yvector)
        #print()
    In_contact=check_on_ground(currentY,0)
    if In_contact==True and Xvector != 0:
        Friction_affected_Xvector=do_friction(Xvector,ground_friction,ratio)
        print(Friction_affected_Xvector)
        Xvector=Friction_affected_Xvector
        print(Xvector)
        
   #is_on_grond=check_on_ground(currentY, 0)
        
    Distances.append(currentX)
    Heights.append(currentY)

    
xlim0,xlim1 =limfind(Distances)
if xlim0 == xlim1:
    xlim0-=1
    xlim1+=1
ylim0,ylim1 =limfind(Heights)
if ylim0 == ylim1:
    ylim0-=1
    ylim1+=1
#print(xlim0,xlim1,"\n",ylim0,ylim1)

dist=50
for i in times:
    #print(i,Distances[i],Heights[i])
    
    
    establish_para()
    
    if i % dist == 0:
        plt.scatter(Distances[i],Heights[i])
        plt.plot(Distances[:i],Heights[:i])
        plt.show()
        #print(On_ground)
        time.sleep(0.1)
        

"""
if frame % fta ==0:
    plt.scatter(Distances[-1],Heights[-1])
    plt.show()
    time.sleep(0.5)
"""
establish_para()
plt.plot(Distances,Heights)
#plt.subplot(2,1,1)
#plt.plot(times,Heights)



