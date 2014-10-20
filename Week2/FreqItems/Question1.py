# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 22:55:36 2014

@author: gsubramanian
"""

def triangularMethod(N):
    return (2*N *N) + 4*N
    
def tripleMethod(N,M):
    return 4*N + 12*M
    
    
# N = 30,000; M = 100,000,000; S = 500,000,000
N = 30000
M = 100000000
S = 500000000

val = 0
if triangularMethod(N) < tripleMethod(N,M):
    val = triangularMethod(N)
else:
    val = tripleMethod(N,M)

print "option a) Lowest Value =%f, 10percent of S=%f, Is less than 10percent=%s"%(val,S*10/100,str(val < (S*1/10)))        
print "if val < s",val < S
a = S -val

#N = 10,000; M = 50,000,000; S = 600,000,000
N = 10000
M = 50000000
S = 600000000

val = 0

if triangularMethod(N) < tripleMethod(N,M):
    val = triangularMethod(N)
else:
    val = tripleMethod(N,M)

print "option a) Lowest Value =%f, 10percent of S=%f, Is less than 10percent=%s"%(val,S*10/100,str(val < (S*1/10)))        
print "if val < s",val < S
b = S- val
#N = 100,000; M = 100,000,000; S = 1,200,000,000
N = 100000
M = 100000000
S = 1200000000

val = 0

if triangularMethod(N) < tripleMethod(N,M):
    val = triangularMethod(N)
else:
    val = tripleMethod(N,M)

print "option a) Lowest Value =%f, 10percent of S=%f, Is less than 10percent=%s"%(val,S*10/100,str(val < (S*1/10)))        
print "if val < s",val < S
c = S - val

#N = 20,000; M = 80,000,000; S = 1,100,000,000
N = 20000
M = 80000000
S = 1100000000
val = 0

if triangularMethod(N) < tripleMethod(N,M):
    val = triangularMethod(N)
else:
    val = tripleMethod(N,M)

print "option a) Lowest Value =%f, 10percent of S=%f, Is less than 10percent=%s"%(val,S*10/100,str(val < (S*1/10)))        
print "if val < s",val < S

if a > b and a > c:
    print "a"
if b > a and b > c:
    print "b"
if c > a  and c > b:
    print "c"
