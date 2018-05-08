import pandas as pd

import numpy as np

import statsmodels.api as sm
df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
X = df_adv[['TV', 'radio']]
y = df_adv['sales']


df_adv.head()

X = df_adv[['TV', 'radio']]

y = df_adv['sales']

import sys
import os
df = pd.read_csv("subject_data.csv")
df = df[(df.color_1 != 0) | (df.color_2 != 0) | (df.color_3 != 0)]

target = pd.read_csv("Catherine.csv")
target = target.sort_values(["img_file"])

target.index = range(147)

X = df.iloc[:,4:]
y = target.iloc[:,1]
y = list(y)

## fit a OLS model with intercept on TV and Radio

est = sm.OLS(y, X).fit()

est.summary()
