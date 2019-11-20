#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:47:55 2019

@author: amit.panda03
"""

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Creating 18 random colors range (0 - 1)
clrs = np.linspace( 0, 1, 18 )
print(clrs)

random.shuffle(clrs)
print(clrs)
# Creating final list of 18 random colors
colors = []
for i in range(0, 72, 4):
    idx = np.arange( 0, 18, 1 )
    random.shuffle(idx)
    r = clrs[idx[0]]
    g = clrs[idx[1]]
    b = clrs[idx[2]]
    a = clrs[idx[3]]
    colors.append([r, g, b, a])
    
    
df = pd.read_csv('/users/amit.panda03/Desktop/pokemon_alopez247.csv') 


from scipy.stats import itemfreq
# Retrieve a list of group types against the
# number of pokemon(s) belonging to that group
type_1 = itemfreq(df.iloc[:,2])
print('type_1= ',type_1)
# Total number of distinct groups
type_1_grps = len(type_1)
print('type_1_grps= ',type_1_grps)
# Names of group
type_1_names = type_1[:,0]
print('type_1_names= ',type_1_names)
# Pokemon count particular to each group
type_1_count = type_1[:,1]
print('type_1_count= ',type_1_count)

type_1_grps = np.arange(type_1_grps)
print('type_1_grps= ',type_1_grps)

bar_width = 0.25
    
bar_graph = plt.bar(type_1_grps, type_1_count, bar_width,
                 alpha = 0.5,   # tranparency factor
                 color = colors)   # color factor


plt.legend(bar_graph, 
           type_1_names,                    # List of group names
           bbox_to_anchor=(1.128, 1.015))   # Position of legend

plt.xticks(type_1_grps + bar_width/2, type_1_names)
plt.xlabel('Type')
plt.ylabel('Pokemon count')
plt.title('Number of Pokemon per Type_1')
plt.grid()
plt.ylim(0,10)