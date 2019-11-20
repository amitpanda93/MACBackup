# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lst = [5,10,0,100]
import numpy as np
arr = np.array(lst)
print(arr+5)
print(arr-3)

print(np.arange(0,10,2,dtype=np.float64))

arr1 = [25, 56, 12, 85, 34, 75]
arr2 = [42, 3, 86, 32, 856, 46]

Narr = np.random.rand(1,6)
print(Narr)


#a = np.ndarray.astype(np.ndarray(arr1),dtype = np.complex128)
print(np.array(arr1).reshape(2,3).astype(complex) + np.array(arr2).reshape(2,3).astype(complex))


S_X = np.array([[2, 5, 6, 5],
               [4, 8, 6, 5]])
print(S_X)
# [[2 5 6 5]
#  [4 8 6 5]]
S_Y = np.array([[6, 7, 5, 9],
               [7, 5, 6, 4]])
print(S_Y)
# [[6 7 5 9]
#  [7 5 6 4]] 

x_cumsum = np.cumsum(S_X,axis=0)
print(x_cumsum)

arr = np.diag(np.arange(4,7),k=1)
print(arr)

arr= np.arange(11)
arr[(arr>5)&(arr<10)]*=-1
print(arr)

print(np.diagflat([4,5,6],1))

mat = np.array([['abc','A'],['def','B'],['ghi','C'],['jkl','D']])
arr = np.array(['abc','dfe','ghi','kjl']) 


mat = np.array([[1,21,3],[5,4,2],[56,12,4]])
print(mat)
print(np.argsort(mat,axis=0))
