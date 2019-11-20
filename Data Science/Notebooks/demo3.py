#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:01:51 2019

@author: amit.panda03
"""

import os.path
from skimage.io import imread
from skimage import data_dir
img = imread(os.path.join(data_dir, 'Phantom.png')) 

import matplotlib.pyplot as plt
plt.imshow(img)

