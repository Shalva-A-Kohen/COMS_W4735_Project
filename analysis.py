import cv2
import pandas as pd
import numpy as np
import io
from plotly import tools
from math import *
import pandas as pd
import os
import sys
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

import statsmodels.api as sm

def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

df = pd.read_csv("subject_data.csv")
df = df[(df.color_1 != 0) | (df.color_2 != 0) | (df.color_3 != 0)]

target = pd.read_csv(sys.argv[1])
target = target.sort_values(["img_file"], ascending=[1])
print(target.dtypes, df.shape)

X = df
y = target.iloc[:,1]


print(reg_m(y,X))
