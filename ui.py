import cv2
import pandas as pd
import numpy as np
import io
from plotly import tools
from math import *
import pandas as pd
import os


img_filpath = './db_pics/'
img_filename = os.listdir(img_filpath)

ui = np.zeros((600,750,3), np.uint8)
name_filename = input("Please enter user's name: ")

file = open(name_filename+'.csv','w')
file.write("img_file, score\n")

# for filename in img_filename:
for i in range(len(img_filename)):
    filename = img_filename[i]
    img = cv2.resize(cv2.imread(img_filpath+filename), (750,500))
    border = cv2.copyMakeBorder(img,0,100,0,0,cv2.BORDER_CONSTANT,value=[0,0,0])
    cv2.putText(border, "Press rate from 1(unattractive) to 5(attractive)", (10, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
    cv2.putText(border, "Number images left: " + str(len(img_filename) - i), (10, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

    cv2.addWeighted(ui, 0, border, 1, 0, ui)

    cv2.imshow('image',ui)
    res = cv2.waitKey(0)

    if res == ord('1'):
        file.write(filename[:-3]+", "+str(1)+"\n")
    elif res == ord('2'):
        file.write(filename[:-3]+", "+str(2)+"\n")
    elif res == ord('3'):
        file.write(filename[:-3]+", "+str(3)+"\n")
    elif res == ord('4'):
        file.write(filename[:-3]+", "+str(4)+"\n")
    elif res == ord('5'):
        file.write(filename[:-3]+", "+str(5)+"\n")


cv2.destroyAllWindows()
