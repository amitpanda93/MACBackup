#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 19:23:00 2019

@author: amit.panda03
"""

import pandas as pd
import numpy as np
df = pd.DataFrame([
            ['IND', 'Gold', 'Game1', '9.9'],
            ['IND', 'Bronze', 'Game2', '8'],
            ['USA', 'Silver', 'Game1', '9.5'],
            ['USA', 'Gold', 'Game2', '8.6'],
            ], columns = ['Country', 'Medal', 
                'Game', 'Score'],
                index = ['Year1', 'Year2','Year1', 'Year2'])
                  
print(df)  

# Listing all the features
print(df.pivot(index = 'Country', columns = 'Medal'))
#           Game                Score            
# Medal   Bronze   Gold Silver Bronze Gold Silver
# Country                                        
# IND      Game2  Game1   None      8  9.9   None
# USA       None  Game2  Game1   None  8.6    9.5
# Listing only Score feature
print(df.pivot(index = 'Country', columns = 'Medal',
               values = 'Score')) 

print(df.pivot_table(index = 'Country', 
                     columns = 'Game',
                     values = 'Score',
                     aggfunc = np.max))  