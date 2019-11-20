#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:15:19 2019

@author: amit.panda03
"""

import os.path
from skimage.io import imread
from skimage import data_dir
img = imread(os.path.join(data_dir, 'checker_bilevel.png'))
 
import matplotlib.pyplot as plt
plt.imshow(img, cmap = 'Greys')

print(type(img))