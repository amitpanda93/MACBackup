#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:19:10 2019

@author: amit.panda03
"""

import os.path
from skimage.io import imread
from skimage import data_dir
import matplotlib.pyplot as plt
import numpy as np
# Original Image
img = imread(os.path.join(data_dir, 'ihc.png'))
plt.imshow(img)

h_slice = img.copy()
v_slice = img.copy()
h_slice = np.hsplit(h_slice,2)
v_slice = np.vsplit(v_slice,4)
''' Horizontal Split '''
plt.figure()
plt.imshow(h_slice[1])
''' Vertical Split '''
plt.figure()
plt.imshow(v_slice[1])