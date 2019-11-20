#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:27:55 2019

@author: amit.panda03
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
plt.bar(type_1_grps, type_1_count, bar_width,
                 alpha = 0.5,   # tranparency factor
                 color = 'g',   # color factor
                 label='Pokemon count respective to their Type_1')
plt.legend(loc='best')
plt.xticks(type_1_grps + bar_width/2, type_1_names)