#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:35:23 2019

@author: amit.panda03
"""

import os.path
from skimage.io import imread
from skimage import data_dir
img = imread(os.path.join(data_dir, 'astronaut.png')) 

import matplotlib.pyplot as plt
plt.imshow(img)

img_slice = img.copy()
img_slice = img_slice[0:300,360:480]
plt.figure()
plt.imshow(img_slice)

import numpy as np

img_slice[np.greater_equal(img_slice[:,:,0],100) & np.less_equal(img_slice[:,:,0],150)] = 0
plt.figure()
plt.imshow(img_slice)