# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:49:24 2014

@author: gsubramanian
"""

import numpy as np
from collections import defaultdict

def col_wise_jaccard_sim(in_matrix):
    rows,cols = in_matrix.shape
    sim_list = defaultdict(float)
    for col in range(cols):
        for nxt_col in range(col+1,cols):
            a = in_matrix[:,col]
            b = in_matrix[:,nxt_col]
            equal_count = 0
            total = a.size + b.size
            for r in range(rows):
                if a[r,0] == b[r,0]:
                    equal_count+=1
            key = str(col) + "-" + str(nxt_col)
            sim_list[key] = equal_count/(1.0*total)
    return sim_list
                

def getSigMatrix(char_matrix,hash_funcs):
    """
    Returns a signature matrix
    Args:
        Input : char_matrix - characteristic matrix
                
    """
    rows,cols = char_matrix.shape
    no_hash = len(hash_funcs)
    sig_matrix =np.full((no_hash ,cols),np.inf).reshape(no_hash,cols)
    sig_matrix = np.matrix(sig_matrix) 
    for row in range(rows):
        row_value = char_matrix[row,:]
        h_value = []
        for h_func in hash_funcs:
            h_value.append(h_func(row))
        for col in range(row_value.size):
            if row_value[0,col] == 1:
                for j in range(no_hash):
                    if sig_matrix[j,col] > h_value[j]:
                        sig_matrix[j,col] = h_value[j]
    return sig_matrix


if __name__ == "__main__":
    """
    Example 3.8 : 
    (a) h3(x) = x+1 mod 5
    (b) h4(x) = 3x+1 mod 5
      Element S1 S2 S3 S4
            0  1 0  0  1
            1  0 0  1  0
            2  0 1  0  1
            3  1 0  1  1
            4  0 0  1  0
    """
    
    hash_functions = []
    hash_functions.append(lambda x:(x+1)%5)
    hash_functions.append(lambda x:(3*x+1)%5)
    
    
    char_matrix = np.matrix([
                        	[1,0,0,1],
                           [0,0,1,0],
                           [0,1,0,1],
                           [1,0,1,1],
                           [0,0,1,0]
                        ])
    
    print getSigMatrix(char_matrix,hash_functions)                    
    
    
    """
    Exercise 3.3.2 : Using the data from Fig. 3.4, add to the signatures of the
    columns the values of the following hash functions:
    (a) h3(x) = 2x + 4.
    (b) h4(x) = 3x − 1.
      Element S1 S2 S3 S4
            0  0 1  0  1
            1  0 1  0  0
            2  1 0  0  1
            3  0 0  1  0
            4  0 0  1  1
            5  1 0  0  0
    """
    
    hash_functions = []
    hash_functions.append(lambda x:2*x+4)
    hash_functions.append(lambda x:3*x-1)
    
    
    char_matrix = np.matrix([
                        	[1,0,0,1],
                           [0,0,1,0],
                           [0,1,0,1],
                           [1,0,1,1],
                           [0,0,1,0]
                        ])
    
    print getSigMatrix(char_matrix,hash_functions)                    
    
    """
    Exercise 3.3.3 : In Fig. 3.5 is a matrix with six rows.
    
    (a) Compute the minhash signature for each column if we use the following
    three hash functions: h1(x) = 2x + 1 mod 6; h2(x) = 3x + 2 mod 6;
    h3(x) = 5x + 2 mod 6.
    (b) Which of these hash functions are true permutations?
    (c) How close are the estimated Jaccard similarities for the six pairs of columns
    to the true Jaccard similarities?
    """
    
    char_matrix = np.matrix([
                        	[0,1,0,1],
                           [0,1,0,0],
                           [1,0,0,1],
                           [0,0,1,0],
                           [0,0,1,1],
                           [1,0,0,0]     
                        ])
    hash_functions = []
    
    hash_functions.append(lambda x:(2*x+1)%6)
    hash_functions.append(lambda x:(3*x+2)%6)
    hash_functions.append(lambda x:(5*x+2)%6)
    hash_functions.append(lambda x:(6*x+2)%6)
    
    sig_matrix = getSigMatrix(char_matrix,hash_functions)                    
    
    # Min hash signatures
    print sig_matrix
    
    print
    print "Jaccard similarity of characteristic matrix"
    js_dict_char_matrix = col_wise_jaccard_sim(char_matrix)
    for k,v in  js_dict_char_matrix.items():
        print k,v
    
    print
    
    print "Jaccard similarity of signature matrix"
    js_dict_sig_matrix = col_wise_jaccard_sim(sig_matrix)
    for k,v in  js_dict_sig_matrix.items():
        print k,v
