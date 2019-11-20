#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:14:49 2019

@author: amit.panda03
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/users/amit.panda03/Desktop/pokemon_alopez247.csv') 

df_pie = df[['Type_1', 'Attack', 'Defense', 'Speed', 'HP']].copy()
print(df_pie.head())

from scipy.stats import itemfreq
frequent_grp = itemfreq(df_pie.iloc[:,0])
print(frequent_grp)
frequent_grp = np.array(sorted(frequent_grp, key=lambda x: x[1]))[::-1][0:4,:]
print(frequent_grp)

df_pie = df_pie.loc[df_pie.loc[:,'Type_1'].str.contains(r'(Water|Normal|Grass|Bug)')]
print(df_pie)

# Names of the group
type_1_names = frequent_grp[:,0]
print(type_1_names)
# Mean of samples for each feature corresponding to all 4 group 
df_grp = df_pie.groupby('Type_1').mean()
print(df_grp)

names = df_grp.columns
colors = ['gold', 'lightcoral', 
              'yellowgreen', 'lightskyblue']
explode = (0, 0, 0, 0.1)  # takes out only the 4th slice 
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)
ax = [ax1, ax2, ax3, ax4]

for i in range(0,4):
    percent = df_grp.iloc[i,:]
    ax[i].pie(percent, explode = explode,
            labels = names, colors = colors,
            autopct='%.2f%%',   # display value
            shadow=True,
            startangle=90)
    ax[i].set_aspect('equal')
    ax[i].set_title(type_1_names[i])


plt.suptitle('Comparing major features of 4 most frequent Pokemon Group',
             fontsize = 14,
             fontweight = 'bold')