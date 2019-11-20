#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:35:02 2019

@author: amit.panda03
"""

import numpy as np
mat1 = np.arange(4).reshape(2,2)
mat2 = (np.arange(4)*2).reshape(2,2)
mat3 = (np.arange(4)*3).reshape(2,2)

print(mat1)
print(mat2)
print(mat3)

print(np.linalg.multi_dot( [mat1, mat2, mat3] ))


a = np.array([[3, 1],[1, 2]])
b = np.array([9, 8])
''' Checking if system of equation has unique solution '''
print(np.linalg.det(a)) 
# 5.0
''' Since det = 5 which is non-zero. Hence, we have unique solutions
 Finding unique solution '''
print(np.linalg.solve(a, b))
# [ 2.  3.]
''' Calculating Inverse: Since, determinant is non-zero 
 hence, matrix is invertible '''
print(np.linalg.inv(a))
# [[ 0.4 -0.2]
#  [-0.2  0.6]]
''' Calculating Rank of the matrix '''
print(np.linalg.matrix_rank(a))