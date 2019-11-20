#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:49:43 2019

@author: amit.panda03
"""
import pandas as pd

sys = ['s1','s1','s1','s1',
        's2','s2','s2','s2']
net_day = ['d1','d1','d2','d2',
        'd1','d1','d2','d2']
spd = [1.3, 11.4, 5.6, 12.3, 
        6.2, 1.1, 20.0, 8.8]
df = pd.DataFrame({'set_name':sys,
                    'spd_per_day':net_day,
                    'speed':spd})

print(df)

new_df = df.groupby(['set_name','spd_per_day']).median()
print(new_df)

new_df.sort_values(by=['Median'])
print(new_df)