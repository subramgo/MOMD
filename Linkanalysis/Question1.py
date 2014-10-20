# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 12:28:46 2014

@author: gsubramanian
"""

import numpy as np

M = np.matrix(([0,0,0],[0.5,0,0],[0.5,1,1]),dtype=float)
beta =0.7
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
print r*3
r = r*3
print 'b+c',r[1]+r[2]
print 'a+c',r[0]+r[2]
print 'a+b',r[0]+r[1]
print 'b+c',r[1]+r[2]