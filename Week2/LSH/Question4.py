# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 19:17:23 2014

@author: gsubramanian
"""

doc_1 = "ABRACADABRA"
doc_2 = "BRICABRAC"


def getShingles(doc,no_shingles):
    doc_shingles = []
    for i in range(len(doc)-1):
        doc_shingles.append(doc_1[i]+doc_1[i+(no_shingles-1)])
    return set(doc_shingles)
        
def getCommon(list1,list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2))

print getShingles(doc_1,2)
print getShingles(doc_2,2)

print "Doc 1, No 2 Shingles=%d"%(len(getShingles(doc_1,2)))       
print "Doc 2, No 2 Shingles=%d"%(len(getShingles(doc_2,2)))      
print "Common Shingles=%d"%(getCommon(getShingles(doc_1,2),getShingles(doc_2,2)))
