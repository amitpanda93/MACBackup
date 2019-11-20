#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:04:45 2019

@author: amit.panda03
"""

import pandas as pd
import numpy as np
df = pd.DataFrame([[0.23,'f1'],[5.36,'f2']],
                  index = list('pq'),
                    columns = list('ab'))

print(df)

#change the column name from a to A
df.columns = list('Ab')
print(df)


#To add a new column with random values
print(df.assign(c=np.random.randn(2)))

#to change type of column to complex
print(df.astype({"A": complex}))


#to filter rows based on values
lst = ['f30','f50','f2','f0']
print(df[df['b'].isin(lst) | df['A'].isin(lst)])


