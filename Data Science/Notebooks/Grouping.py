#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:45:43 2019

@author: amit.panda03
"""

import pandas as pd
df = pd.DataFrame([["Laptop", 1000],
                   ["Laptop", 2520],
                   ["Desktop", 3000],
                   ["Desktop", 400]], columns = ['Category','Sales'])
print(df)
#   Category  Sales
# 0   Laptop   1000
# 1   Laptop   2520
# 2  Desktop   3000
# 3  Desktop    400
print(df.groupby(['Category'], sort = False).sum())
#           Sales
# Category       
# Laptop     3520
# Desktop    3400 