#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:56:08 2019

@author: amit.panda03
"""

import numpy as np
x,y,z = np.random.rand(3,50)
print(x)
print(y)
print(z)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(121,projection='3d')

ax.scatter(x,y,z)
plt.show()

