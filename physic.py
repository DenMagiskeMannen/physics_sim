# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:52:58 2023

@author: teodo
"""
import time
import random
import matplotlib.pyplot as plt

#Vo
startUp=5
startRight=0

#So
startX=0
startY=10

#A
g=-9.81
m=10
G=m*g

Xconstant=0

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

for frame in times:
    print(frame,currentY)
    #Ratio
    ratio=1/timestep
    
    #MovementX
    Xvector=Xvector+(Xconstant/ratio)
    currentX=currentX+(Xvector)
    #Movement Y
    Yvector=Yvector+(g/ratio)
    currentY=currentY+Yvector
    
    if currentY <=0:
        #currentY=currentY-Yvector
        currentY=0
    
    Distances.append(currentX)
    Heights.append(currentY)
    
    
    
    """
    #Every SECOND
    print(currentX,currentY)
    #MovementX
    Xvector=Xvector+Xconstant
    currentX=currentX+(Xvector)
    #Movement Y
    Yvector=Yvector+g
    currentY=currentY+Yvector
    """
    #time.sleep(1)
    
    
plt.plot(times,Heights)

