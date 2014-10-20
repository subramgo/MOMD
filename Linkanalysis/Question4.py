# -*- coding: utf-8 -*-
"""
Created on Sat Oct 04 13:34:09 2014

@author: gsubramanian
"""
from collections import defaultdict

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# Get the prime divisors of a given number
# Prime divisors of 12 are 2,3
out = defaultdict(list)

def getPrimeDivisors(number):
    ret = []
    for i in range(2,number):
        if isprime(i):
            if number%i == 0:
                ret.append(i)
    return ret
    

numbers = [15,21,24,30,49]

for n in numbers:
    print n
    l = getPrimeDivisors(n)
    print l
    for k in l:
        out[k].append(n)
        
for k,v in out.items():
    print k,sum(v)
    
    

            
        