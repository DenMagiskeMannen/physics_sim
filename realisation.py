# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 18:58:10 2023

@author: teodo
"""

#Physics 2

#Format
totalTime=2 #SEc
timestep=0.01 #Also sec
ratio=1/timestep # If something does something by the second then it does it.. something
times=[]
for i in range(int(totalTime/timestep)):
    times.append(i)
print(times)

#Boundry box
xlim=0, 100
ylim=0, 100



#Object permeability
elasticity=0
ground_friction_coof=0
air_friction_coof=0

m=20 #Kg
YPos=0   #StartHeigh
XPos=0   #StartDirection

#Reality stuff
g=-9.81

StartForward=1 #NOT NEWTIOn, Speed

ForceForward=0 #N
ForceBackward=0 #N


#Convesion STuff/ MATH TIME
#In this case, speed is constant therefore a=0
speed = StartForward#...
#FUUUCK NEWTONS ARE BARELY RELATED TO SPPED ITS ALL ACELATRTUAIUh


#Simulation
sec=0
count=0
while sec<totalTime:
    #Do math
    
    
    #Check object
    
    
    #Plot Object
    
    #Plot S,V,A grafs
    
    count+=1
    sec+=timestep
print(count)

