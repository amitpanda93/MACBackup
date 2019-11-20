#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:35:26 2019

@author: amit.panda03
"""

import pandas as pd
import numpy as np

df = pd.DataFrame([[11, 202],
                    [33, 44]],
                    index = list('AB'),
                    columns = list('CD'))
''' Writing to excel file '''
df.to_excel('test_file.xlsx', sheet_name = 'Sheet1')
''' Reading from excel file '''
print(pd.read_excel('test_file.xlsx', 'Sheet1')) 

