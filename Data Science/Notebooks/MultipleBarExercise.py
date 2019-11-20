#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:33:08 2019

@author: amit.panda03
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n_grps = np.arange(5)
print(n_grps)

bar_width = 0.4
men_sc = [20, 30, 10, 50, 90]
err_men_sc = [2, 3, 4, 5, 4]
women = [10, 123, 19, 60, 40]
err_women_sc = [1, 6, 2, 8, 7]

fig,ax = plt.subplots()

p1 = ax.bar(n_grps,men_sc,bar_width,color='r',bottom = 0, yerr=err_men_sc)
p2 = ax.bar(n_grps+bar_width,women,bar_width,color='g',bottom = 0,yerr=err_women_sc)

ax.set_xticks(n_grps+bar_width/2)
ax.set_xticklabels(('A','B','C','D','E'))

ax.legend((p1[0], p2[0]), ('Men', 'Women'))

ax.autoscale_view()

plt.show()
