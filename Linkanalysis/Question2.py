# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 23:48:24 2014

@author: gsubramanian
"""


#   a   b   c
#a  0   0   1
#b  0.5 0   0
#c  0.5 1   0
import numpy as np

M = np.matrix(([0,0,1],[0.5,0,0],[0.5,1,0]),dtype=float)
beta =0.85
const =np.matrix( (1-beta) * 1/3 * np.ones(3) )
const = const.transpose()
 
r = np.matrix([1/3,1/3,1/3])
r = r.transpose()
itr=0

while (True):
    r_old = r
    r = beta* M * r + const
    itr+=1

    if (r - r_old).sum() < 0.000001:
        break
print itr
print r


#print 0.475 * r[0] + 0.05 * r[2] ,0.95 * r[1]
#print r[2] ,.9*r[1] + .475*r[0]
#print r[1],.475*r[0] + .05*r[2]    
#print r[0],.9*r[2] + .05*r[1]    

# Attempt 2
print 0.95*r[0],"=",.9*r[2] + .05*r[1]
print r[1],"=",.575*r[0] + .15*r[2]
print .85*r[2],"=",r[1] + .575*r[0]
print 85*r[2],"=",.575*r[0] + .15*r[2]