#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:30:56 2022

@author: Andrea Grianti
Published on: Medium.com

This code helps understanding the usage of the Munkres algorithm, but
it transform the problem from minimize the costs to maximize the profits.
Also note that matrix could also be rectangular
"""

from munkres import Munkres
import numpy as np

cols=['c0','c1','c2','c3','c4','c5']
rows=['p0','p1','p2','p3','p4']

#create a toy matrix of integers based on length of cols and rows
matrix=[list(np.random.randint(1,9,size=len(cols))) for i in range(len(rows))]

#matrix transformation to a profit matrix
#the following two lines can be deleted to try minimization costs
max_value=np.max(matrix)+1 #this value gets the max+1 to be subtracted from the matrix
p_matrix=[[max_value-num for num in row] for row in matrix]  #in order to have a profit matrix
    
m = Munkres() #initialize the algorithm
indexes = m.compute(p_matrix) #indexes will contain the tuples with assignmts

#this part below calculates the total profit of the matrix
total = 0
print('Optimal assignments to maximize the profit:')
for row_idx, col_idx in indexes:
    value = matrix[row_idx][col_idx]
    total += value
    print(f'Assign {rows[row_idx]} to {cols[col_idx]} -> profit:{value}')
print(f'Total profit: {total}')

    