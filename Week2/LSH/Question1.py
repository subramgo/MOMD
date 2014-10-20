# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:54:54 2014

@author: gsubramanian

The edit distance is the minimum number of character insertions and character deletions 
required to turn one string into another. Compute the edit distance between each pair of the strings he,
she, his, and hers. Then, identify which of the following is a true statement about the number of 
pairs at a certain edit distance.


"""
from collections import defaultdict

def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

from itertools import combinations
strings = ["he","she","his","hers"]
pairs =  list(combinations(strings,2))


length = defaultdict(list)
for pair in pairs:
    x = pair[0]
    y = pair[1]
    dist = len(x) + len(y) - 2 * (len(lcs(x,y)))
    length[dist].append((x,y))


for k,v in length.items():
    print k,v
    
    
