# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 13:28:16 2014

@author: gsubramanian
"""

#   a   b   c
#a  0   0   1
#b  0.5 0   0
#c  0.5 1   0
import numpy as np

M = np.matrix(([0,0,1],[0.5,0,0],[0.5,1,0]),dtype=float)
r = np.matrix([1,1,1])
r = r.transpose()

for i in range(6):
    r = M.dot(r)
    print i+1
    print r
    
