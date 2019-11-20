#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:46:05 2019

@author: amit.panda03
"""

import numpy as np

a = np.array([[2,3,2],[1,0,3],[2,2,3]])
b = np.array([1,2,3])

print(np.linalg.solve(a,b))

a = np.array([[1,3,-1],[2,5,4],[2,3,-1]])

#print(scipy.linalg.lu(a,False,False))

a = np.array([[56,18.2,-1],[2.3,5,4],[55,37.1,69]])

print(np.linalg.qr(a))
