#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:42:15 2019

@author: amit.panda03
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
   
n = 30
x = np.arange(0,1,0.001)
y = np.ones( (1000,n) )
for i in range(0,n):
    y[:,i] = np.sin(2 * np.pi * x) * i+1
def func(arg):
     plt.cla()   #Clear axis
     plt.plot(y[:,arg])
     plt.ylim(-30,30)
fig = plt.figure(figsize=(5,4))
      
to_save = animation.FuncAnimation(fig, func, frames=30)