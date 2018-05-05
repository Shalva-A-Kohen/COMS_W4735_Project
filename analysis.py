import cv2
import pandas as pd
import numpy as np
import io
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
from math import *
import pandas as pd
import os

df = pd.read_table('./subject_data.txt', sep = ',', header = 0)

df.dtypes
df  = df[(df.color_1+df.color_2+df.color_3 > 0.0)]

img_filpath = './db_pics/'
img_filename = os.listdir(img_filpath)

ui = np.zeros((600,750,3), np.uint8)
name_filename = input("Please enter user's name: ")

file = open(name_filename+'.txt','w')

for filename in img_filename:
    img = cv2.resize(cv2.imread(img_filpath+filename), (750,500))
    border = cv2.copyMakeBorder(img,0,100,0,0,cv2.BORDER_CONSTANT,value=[0,0,0])
    cv2.putText(border, "Press 'z' for attractive and 'm' for unattractive", (10, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

    cv2.addWeighted(ui, 0, border, 1, 0, ui)

    cv2.imshow('image',ui)
    res = cv2.waitKey(0)

    if res == ord('m'):
        file.write(filename+", "+str(0)+"\n")
        print("u ugly")
        continue
    elif res == ord('z'):
        file.write(filename+", "+str(1)+"\n")
        print("look kinda like a human")
        continue


cv2.destroyAllWindows()
