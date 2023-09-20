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


#Vo
startUp=5
startRight=5

#So
startX=0
startY=10

#A
g=-9.81
m=10
G=m*g

Xresistence=0

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
    #print(frame,currentY)
    #Ratio
    ratio=1/timestep
    
    #MovementX
    Xvector=Xvector+(Xresistence/ratio)
    currentX=currentX+(Xvector)
    #Movement Y
    Yvector=Yvector+(g/ratio)
    currentY=currentY+Yvector
    
    if currentY <=0:
        #currentY=currentY-Yvector
        currentY=0
    
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

dist=5
for i in times:
    #print(i,Distances[i],Heights[i])
    
    
    establish_para()
    
    if i % dist == 0:
        plt.scatter(Distances[i],Heights[i])
        plt.plot(Distances[:i],Heights[:i])
        plt.show()
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



