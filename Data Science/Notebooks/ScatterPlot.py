#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:07:53 2019

@author: amit.panda03
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms


df = pd.read_csv('/users/amit.panda03/Desktop/pokemon_alopez247.csv') 
tot_power = df.iloc[:,4]
print(tot_power.head(4))

catch_rate = df.iloc[:,21]
print(catch_rate.head(4))

fig, ax = plt.subplots()
p = ax.scatter(catch_rate, tot_power, c = 'g')
ax.grid()
ax.set_xlabel('Catch Rate')
ax.set_ylabel('Total Power')
ax.set_title('Pokemon Catch Rate vs their Power')
plt.legend([p],['Pokemons'])


trans = transforms.blended_transform_factory(
    ax.transData,ax.transAxes)
rect = patches.Rectangle((44,0), width=2, height=5,
                         transform=trans, color='red',
                         alpha=0.4)
ax.add_patch(rect)

catch_rate_45 = df[df.loc[:,'Catch_Rate'] == 45]
pow_330 = catch_rate_45[catch_rate_45.loc[:,'Total'] <= 1000]
print("Number of such Pokemons:", len(pow_330))
# Top 10 adamant Pokets
print(pow_330.loc[:,'Name'].head(10))
