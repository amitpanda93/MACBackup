#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:41:22 2019

@author: amit.panda03
"""

import pandas as pd
import numpy as np

df = pd.DataFrame([[18,10,5,11,-2],
                    [2,-2,9,-11,3],
                    [-4,6,-19,2,1],
                    [3,-14,1,-2,8],
                    [-2,2,4,6,13]],
                  index = list('pqrst'),
                    columns = list('abcde'))

print(df)