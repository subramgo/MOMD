# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 20:00:02 2014

@author: gsubramanian
"""
import math

def norm((x1,y1),(x2,y2),degree):
    degree = degree * 1.0
    temp = math.fabs ( math.pow((x2-x1),degree) + math.pow((y2-y1),degree))
    return math.pow(temp,1/degree)
    
    
point1 = (0,0)
point2 = (100,40)

entrants = [(63,8),(53,18),(56,13),(58,13)]


for ent in entrants:
    print "Distance under L1 = ",ent,point1,norm(ent,point1,1)
    print "Distance under L1 = ",ent,point2,norm(ent,point2,1)
    if norm(ent,point1,1) < norm(ent,point2,1):
        print "Point ",ent," Assigned to ", point1
    else:
        print "Point ",ent," Assigned to ", point2
    print "###################################################"
        
    
for ent in entrants:
    print "Distance under L2 = ",ent,point1,norm(ent,point1,2)
    print "Distance under L2 = ",ent,point2,norm(ent,point2,2)
    if norm(ent,point1,2) < norm(ent,point2,2):
        print "Point ",ent," Assigned to ", point1
    else:
        print "Point ",ent," Assigned to ", point2
    print "###################################################"
    
    