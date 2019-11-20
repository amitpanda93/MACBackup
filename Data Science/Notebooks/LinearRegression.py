#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:20:54 2019

@author: amit.panda03
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston

boston = load_boston()
#print(boston.data.shape)       # (506, 13)
#print(boston.feature_names)  # Column names
#print(boston.DESCR)        # brief desc.
df = pd.DataFrame(boston.data)
#print(df.head(5))

df.columns = boston.feature_names
#print(df.head(5))

df['PRICE'] = boston.target
#print(df.head(5))

X = df.drop('PRICE', axis = 1)
print(df)
              
## (use sklearn.model_selection in case sklearn.cross_validation results into error)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X, df.PRICE, test_size = 0.33, # Test data (33%)
        random_state = 42) # assign random_state to any value, to get same samples on each fresh run

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
pred_test = lm.predict(X_test)

plt.scatter(y_test,pred_test)
plt.plot(np.unique(y_test), 
      np.poly1d(np.polyfit(y_test, pred_test, 1))(np.unique(y_test)),
      linewidth = 3)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')

coeff_df = pd.DataFrame(X_train.columns, lm.coef_)
print(coeff_df)
mse = sklearn.metrics.mean_squared_error(y_test, pred_test)
print(mse)