# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 21:23:38 2014

@author: gsubramanian
"""

baskets = range(1,101)
items = range(1,101)

# Create transactions
transactions = []

for i in baskets:
    basket = []
    for item in items:
        if i % item == 0:
            basket.append(item)
    transactions.append(basket)
    


def find_count(transactions,query):
    count=0
    for t in transactions:
        query_in = True
        for q in query:
            if q not in t:
                query_in = False
        if query_in:
            count+=1
    return count
            
def confidence(num,denom):
    count_denom = find_count(transactions,denom)
    count_num = find_count(transactions,num)
    confidence = count_num /(1.0* count_denom ) * 100
    return confidence            

    
print "{1,2}-> 4,Condidence = %d"%(confidence([1,2,4],[1,2]))   
print "{1}-> 2,Condidence = %d"%(confidence([1,2],[1]))   
print "{1,4,7}-> 14,Condidence = %d"%(confidence([1,4,7,14],[1,4,7]))   
print "{1,3,6}-> 12,Condidence = %d"%(confidence([1,3,6,12],[1,3,6]))   
     
print "{4,6}-> 12,Condidence = %d"%(confidence([4,6,12],[4,6]))   
print "{8,12}-> 96,Condidence = %d"%(confidence([8,12,96],[8,12]))   
print "{4,6}-> 24,Condidence = %d"%(confidence([4,6,24],[4,6]))   
print "{1,3,6}-> 12,Condidence = %d"%(confidence([1,3,6,12],[1,3,6]))   
     